import subprocess

from setuptools import setup

import notedown


pandoc = subprocess.Popen(['pandoc', 'README.md', '--to', 'rst'],
                          stdout=subprocess.PIPE)

rst_readme = pandoc.communicate()[0]

setup(
    name="notedown",
    version=notedown.__version__,
    description="Convert markdown to IPython notebook.",
    long_description=rst_readme,
    packages=['notedown'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='BSD 2-Clause',
    url='http://github.com/aaren/notedown',
    install_requires=['ipython', 'jinja2', 'pandoc-attributes'],
    entry_points={'console_scripts': ['notedown = notedown:cli', ]},
    package_dir={'notedown': 'notedown'},
    package_data={'notedown': ['templates/markdown.tpl']},
    include_package_data=True,
)
