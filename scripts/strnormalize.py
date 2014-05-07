#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO
#
# integrate this with the abbrlibrary script and provide two kinds of
# substitutions:
# 1. substitution to ASCII fo bib keys 
# 2. substitution to special characters interpretable by bibtex

import codecs
import docopt

author_replacements = {
    u"ą" : r"\k{a}",
    u"Ą" : r"\k{A}",
    u"ć" : r"\'{c}",
    u"Ć" : r"\'{C}",
    u"ę" : r"\k{e}",
    u"Ę" : r"\k{E}",
    u"ł" : r"{\l}",
    u"Ł" : r"{\L}",
    u"ń" : r"\'{n}",
    u"Ń" : r"\'{N}",
    u"ó" : r"\'{o}",
    u"Ó" : r"\'{O}",
    u"ś" : r"\'{s}",
    u"Ś" : r"\'{S}",
    u"ź" : r"\'{z}",
    u"Ź" : r"\'{Z}",
    u"ż" : r"\.{z}",
    u"Ż" : r"\.{Z}",
    u"æ" : r"\ae",
    u"Æ" : r"\AE",
    u"œ" : r"\oe",
    u"Œ" : r"\OE",
    u"ø" : r"\o",
    u"Ø" : r"\O",
    u"å" : r"\aa",
    u"Å" : r"\AA",
    u"ß" : r"\ss",
    u"–" : r"-",
    u"–" : r"-",
    u"ň" : r"\u{n}",
    u"ñ" : r"\~{n}",
    u"ö" : r"\"{o}",
    }
citekey_replacements = {u"ą" : r"a",
                        u"Ą" : r"A",
                        u"ć" : r"c",
                        u"Ć" : r"C",
                        u"ę" : r"e",
                        u"Ę" : r"E",
                        u"ł" : r"l",
                        u"Ł" : r"L",
                        u"ń" : r"n",
                        u"Ń" : r"N",
                        u"ó" : r"o",
                        u"Ó" : r"O",
                        u"ś" : r"s",
                        u"Ś" : r"S",
                        u"ź" : r"z",
                        u"Ź" : r"Z",
                        u"ż" : r"z",
                        u"Ż" : r"Z",
                        u"æ" : r"ae",
                        u"Æ" : r"AE",
                        u"œ" : r"oe",
                        u"Œ" : r"OE",
                        u"ø" : r"o",
                        u"Ø" : r"O",
                        u"å" : r"aa",
                        u"Å" : r"AA",
                        u"ß" : r"ss",
                        }

def normalizebibfile(bibfile):

    f = codecs.open(bibfile, 'r', encoding="utf-8")
    contents = f.read()

    output = ""
    for x in contents:
        if x in author_replacements.keys():
            output += author_replacements[x]
        else:
            output += x
    f.close()
    return output

def main():

    """
    Usage:
        strnormalize.py <filename>

    """
    args = docopt.docopt(main.__doc__, help=True, version="strnormalize.py 0.1")

    out = normalizebibfile(args["<filename>"])

    print out

if __name__ == "__main__":
    main()
