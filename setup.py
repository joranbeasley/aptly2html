from distutils.core import setup
import os
print os.name
scripts = ['bin/aptly2html','bin/aptly2json'] if os.name != "nt" else ['bin/aptly2html.cmd','bin/aptly2json.cmd']
print scripts
setup(
    name='aptly2html',
    version='0.1',
    packages=['aptly2html_data'],
    py_modules=['aptly2html','aptly2json'],
    scripts=scripts,
    url='',
    license='MIT',
    author='Joran Beasley',
    author_email='',
    package_data={
   'aptly2html_data': ["templates/*.html",'templates/**/*.html'],     # All files from templates folder
   },
    description='convert aptly package list into a static single html webpage'
)
