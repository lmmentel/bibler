bibler.py
=========

A small utility python script to perform some basis operations on bibtex_
bibliography files. The options include:

* abbreviate the journal name,
* discard selected fields on each bibtex entry,
* expand abbreviated journal name into full form,
* turn journal names into hypertext (links) based on the doi or url entries,

Dependencies
============

The script depends on pybtex_ for parsing the bibliography file available from
PyPI::

    $ [sudo] pip install pybtex

.. _bibtex: http://www.bibtex.org
.. _pybtex: http://pybtex.sourceforge.net/
