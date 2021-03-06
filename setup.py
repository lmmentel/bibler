
''' bibler tools for handling bib files '''

from setuptools import setup

def readme():
    '''Return the contents of the README.rst file.'''
    with open('README.rst') as freadme:
        return freadme.read()


setup(
    author = "Lukasz Mentel",
    author_email = "lmmentel@gmail.com",
    scripts=[
        'scripts/bibler.py',
        'scripts/strnormalize.py'],
    description = "Script for manipulating bibtex bibliography",
    install_requires = [
        'pybtex >= 0.17',
    ],
    license = open('LICENSE.txt').read(),
    long_description = readme(),
    name = 'bibler.py',
    url = 'https://bitbucket.org/lukaszmentel/bibler/',
    version = '0.1.0',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
    ],
)
