from distutils.core import setup

setup(
    name='aptly2html',
    version='0.1',
    packages=['aptly2html_data'],
    py_modules=['aptly2html','aptly2json'],
    url='',
    license='MIT',
    author='Joran Beasley',
    author_email='',
    description='convert aptly package list into a static single html webpage'
)
