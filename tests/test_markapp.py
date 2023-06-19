from markapp import markapp
import shutil
import os

def test_sample():
    output_dir = 'tests'

    markapp.compile('tests/sample.md', output_dir)

    expected = os.path.join(output_dir, 'sample')

    assert os.path.exists(os.path.join(expected, 'index.html'))

    assert 'inner html' == open(os.path.join(expected, 'index.html')).read().strip()

    assert 'inner css' == open(os.path.join(expected, 'style.css')).read().strip()

    assert 'inner javascript' == open(os.path.join(expected, 'script.js')).read().strip()

    shutil.rmtree(expected)

def test_append():
    output_dir = 'tests'

    markapp.compile('tests/sample-append.md', output_dir)

    expected = os.path.join(output_dir, 'sample-append')

    assert os.path.exists(os.path.join(expected, 'foo.html')), 'foo.html should exist'

    content = """first html
second html
"""
    assert content == open(os.path.join(expected, 'foo.html')).read()

    shutil.rmtree(expected)

def test_parser():

    blocks = markapp.extract_code_blocks('tests/sample-3.md')

    assert len(blocks) == 3
    assert blocks[0]['file_type'] == 'html'
    assert blocks[0]['operation'] == '>'
    assert blocks[0]['file_path'] == 'index.html'

    assert blocks[1]['file_type'] == 'javascript'
    assert blocks[1]['operation'] == '>'
    assert blocks[1]['file_path'] == 'src/game.js'

    assert blocks[2]['file_type'] == 'javascript'
    assert blocks[2]['operation'] == '>'
    assert blocks[2]['file_path'] == 'src/game.js'

