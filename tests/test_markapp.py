from markapp import markapp
import shutil
import os

def test_sample():
    output_dir = 'tests'

    markapp.compile('tests/sample.md', 'tests')

    expected = os.path.join(output_dir, 'sample')

    assert os.path.exists(os.path.join(expected, 'index.html'))

    assert 'inner html' == open(os.path.join(expected, 'index.html')).read().strip()

    assert 'inner css' == open(os.path.join(expected, 'style.css')).read().strip()

    assert 'inner javascript' == open(os.path.join(expected, 'script.js')).read().strip()

    shutil.rmtree(expected)
