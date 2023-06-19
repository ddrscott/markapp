from setuptools import setup

setup(
    name='markapp',
    version='0.3.1',
    author='Scott Pierce',
    author_email='ddrscott@gmail.com',
    description='A simple markdown to HTML compiler',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ddrscott/markapp',
    packages=['markapp'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'click',
        'watchdog',
    ],
    entry_points={
        'console_scripts':[
            "markapp = markapp.cli:cli",
        ],
    }
)
