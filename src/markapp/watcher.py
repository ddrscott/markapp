import logging
import os
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DebouncedEventHandler(FileSystemEventHandler):
    def __init__(self, on_change, debounced_ms):
        super().__init__()
        self.on_change = on_change
        self.debounced_ms = debounced_ms
        self.last_call_time = 0

    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.md'):
            now = time.time()
            if now - self.last_call_time > self.debounced_ms / 1000:
                logger = logging.getLogger(__name__)
                if not os.path.isfile(event.src_path):
                    logger.info(f'File not found: {event.src_path}')
                    return

                logger.info(f'Change detected. Calling {self.on_change.__name__}')
                self.last_call_time = now
                self.on_change(event.src_path)

def watch(on_change, path, debounce_ms):
    event_handler = DebouncedEventHandler(on_change, debounced_ms=debounce_ms)
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(0.2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
