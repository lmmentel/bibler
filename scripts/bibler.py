#!/usr/bin/env python

'''
Module that provides some utilities for handling bibtex bibliography files.
Intended to handle file produced by MedeleyDesktop but should work with any
regular bibtex file.

Basis capabilities are summarized by the script options:
    Options:
        -a, --abbreviate    abbreviate full journal names,
        -d, --discard       remove selected fileds,
        -e, --expand        expand abbreviated journal names,
        -l, --links         convert journal names to links (hyperrefs),
        -o <outfile>, --output <outfile>    output file name,
        -v, --version       version
'''

__version__ = "0.1.0"

from pybtex.database.input import bibtex
import datetime
import docopt
import os
import re

AbbrevDict = {
"Advances in Quantum Chemistry"               : "Adv.~Quantum Chem.",
"Annals of Physics"                           : "Ann.~Phys.",
"Annalen der Physik"                          : "Ann.~Phys.",
"Annual Review of Physical Chemistry"         : "Annu.~Rev.~Phys.~Chem.",
"Chemical Physics"                            : "Chem.~Phys",
"Chemical Physics Letters"                    : "Chem.~Phys.~Lett.",
"Chemical Reviews"                            : "Chem.~Rev.",
"Chemical Society Reviews"                    : "Chem.~Soc.~Rev.",
"Chemphyschem: A European journal of chemical physics and physical chemistry" : "ChemPhysChem",
"Collection of Czechoslovak Chemical Communications" : "Collect.~Czech.~Chem.~Commun.",
"Combinatorial Chemistry \& High Throughput Screening" : "Comb.~Chem.~High Throughput Screening",
"Computer Physics Communications"             : "Comput.~Phys.~Commun.",
"International Journal of Quantum CHemistry"  : "Int.~J.~Quantum Chem.",
"International Reviews in Physical Chemistry" : "Int.~Rev.~Phys.~Chem",
"Journal of Chemical Education"               : "J.~Chem.~Educ.",
"Journal of Chemical Physics"                 : "J.~Chem.~Phys.",
"Journal of Chemical Theory and Computation"  : "J.~Chem.~Theory Comput.",
"Journal of Computational Chemistry"          : "J.~Comput.~Chem.",
"Journal of Computational Physics"            : "J.~Comput.~Phys",
"Journal of Molecular Graphics and Modelling" : "J.~Mol.~Graphics Modell.",
"Journal of Molecular Graphics \& Modelling"  : "J.~Mol.~Graphics Modell.",
"Journal of Molecular Structure: THEOCHEM"    : "J.~Mol.~Struct. THEOCHEM",
"Journal of Physical Chemistry"               : "J.~Phys.~Chem.",
"Journal of Physical Chemistry A"             : "J.~Phys.~Chem.~A",
"Journal of Physical Chemistry B"             : "J.~Phys.~Chem.~B",
"Journal of Physics A: General Physics"       : "J.~Phys.~A: Gen.~Phys.",
"Journal of Physics A: Mathematical and General" : "J.~Phys.~A: Math.~Gen.",
"Journal of Physics A: Mathematical and Theoretical" : "J.~Phys.~A: Math.~Theor.",
"Journal of Physics B: Atomic and Molecular Physics" :
"J.~Phys.~B: At.~Mol.~Phys.",
"Journal of Physics B: Atomic, Molecular and Optical Physics" :
"J.~Phys.~B: At.~Mol.~Opt.~Phys.",
"Journal of the Chemical Society, Faraday Transactions 2: Molecular and Chemical Physics" :
"J.~Chem.~Soc.,~Faraday Trans. 2",
"Molecular Physics"                           : "Mol.~Phys.",
"Philosophical Magazine"                      : "Philos.~Mag.",
"Philosophical Transactions of the Royal Society of London" : "Philos.~Trans.~R.~Soc.~London",
"Physical Chemistry Chemical Physics"         : "Phys.~Chem.~Chem.~Phys.",
"Physical Chemistry Chemical Physics : PCCP"  : "Phys.~Chem.~Chem.~Phys.",
"Physical Review"                             : "Phys.~Rev.",
"Physical Review A"                           : "Phys.~Rev.~A",
"Physical Review B"                           : "Phys.~Rev.~B",
"Physical Review C"                           : "Phys.~Rev.~C",
"Physical Review Letters"                     : "Phys.~Rev.~Lett.",
"Physikalische Zeitschrift"                   : "Phys.~Zs.",
"Physics Letters"                             : "Phys.~Lett.",
"Proceedings of the Royal Society of London. Series A" : "Proc.~R.~Soc.~London, Ser.~A",
"Proceedings of the National Academy of Sciences of the United States of America" : "PNAS",
"Quarterly Reviews, Chemical Society"         : "Q.~Rev.~Chem.~Soc.",
"Reviews of Modern Physics"                   : "Rev.~Mod.~Phys.",
"Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy" : "Spectrochim.~Acta, Part A",
"Structural Chemistry"                        : "Struct.~Chem.",
"The Journal of Physical Chemistry"           : "J.~Phys.~Chem.",
"The Journal of Physical Chemistry A"         : "J.~Phys.~Chem.~A",
"The Journal of Physical Chemistry B"         : "J.~Phys.~Chem.~B",
"The Journal of Chemical Physics"             : "J.~Chem.~Phys.",
"Theoretica Chimica Acta"                     : "Theor.~Chim.~Acta",
"Theoretical Chemistry Accounts"              : "Theor.~Chem.~Acc.",
"Transactions of The Faraday Society"         : "Trans.~Faraday Soc.",
"Wiley Interdisciplinary Reviews Computational Molecular Science" : "WIREs~Comput.~Mol.~Sci.",
"Wiley Interdisciplinary Reviews: Computational Molecular Science" : "WIREs~Comput.~Mol.~Sci.",
'Zeitschrift f\"{u}r Physik'                  : "Z.~Phys.",
'Zeitschrift f\"{u}r Physik D Atoms, Molecules and Clusters' : "Z.~Phys.~D: At.~Mol.~Clusters",
"Zeitschrift fur Physik D: Atoms, Molecules and Clusters" : "Z.~Phys.~D: At.~Mol.~Clusters"
}

def abbreviate_journalname(journal):
    '''
    Abbreviate the journal name based on the entry in the AbbrevsDict.
    '''

    p = re.compile(r'[~\.:\s+]')

    for key in AbbrevDict.keys():
        if p.sub('', journal.lower()) == p.sub('', key.lower()):
            return AbbrevDict[key]
    else:
        return journal

def expand_journalname(journal):
    '''
    Expand the abbreviated journal name based on the entry in the AbbrevsDict.
    '''

    p = re.compile(r'[~\.]')

    for key, value in AbbrevDict.items():
        if p.sub('', journal.lower()) == p.sub('', value.lower()):
            return key
    else:
        return journal

def print_entries(entries, discard):
    '''
    Print all bibtex entries.
    '''

    for item in entries:
        authors = []
        print "@{0:<s}{{{1:s},".format(entries[item].type, item)
        if "author" in entries[item].persons.keys():
            for author in entries[item].persons["author"]:
                authors.append(author.get_part_as_text("last") +", "+ " ".join(author.bibtex_first()))
            print "\t{0:s} = {{{1:s}}},".format("author", " and ".join(authors))
        b = entries[item].fields
        for key in sorted(b.keys()):
            if key not in discard:
                print "\t{0:s} = {{{1:s}}},".format(key, b[key])
        print "}"

def write_entries(entries, discard, args, output):
    '''
    Write all bibtex entries to a file.
    '''

    out = file(output, 'w')

    for item in entries:
        authors = []
        out.write("@{0:<s}{{{1:s},\n".format(entries[item].type, item))
        if "author" in entries[item].persons.keys():
            for author in entries[item].persons["author"]:
                authors.append(author.get_part_as_text("last") +", "+ " ".join(author.bibtex_first()))
            out.write("\t{0:s} = {{{1:s}}},\n".format("author", " and ".join(authors)))
        b = entries[item].fields
        for key in sorted(b.keys()):
            if key not in discard:
                out.write("\t{0:s} = {{{1:s}}},\n".format(key, b[key]))
        out.write("}\n")
    out.close()

def insert_link(fields, entry, linkcolor=None):
    '''
    Create a link to the article from the doi or url fields and place it on:
    journal name for @article, booktitle for @incollection.
    '''

    if linkcolor:
        if "doi" in fields:
            return "\href{{http://dx.doi.org/{0:s}}}{{{{\\color{{{1:s}}}{2:s}}}}}".format(fields["doi"], linkcolor, fields[entry])
        elif "url" in fields:
            return "\href{{{0:s}}}{{{{\\color{{{1:s}}}{2:s}}}}}".format(fields["url"], linkcolor, fields[entry])
        else:
            return fields[entry]
    else:
        if "doi" in fields:
            return "\href{{http://dx.doi.org/{0:s}}}{{{{{1:s}}}}}".format(fields["doi"], fields[entry])
        elif "url" in fields:
            return "\href{{{0:s}}}{{{{{1:s}}}}}".format(fields["url"], fields[entry])
        else:
            return fields[entry]


def main():

    """
    Usage:
        abbrlibrary.py (<bibfile>) [-a | -e] [-l] [-d <entries>...] [-o <outfile>]
        abbrlibrary.py --version

    Options:
        -a, --abbreviate    abbreviate full journal names,
        -d, --discard       remove selected fields,
        -e, --expand        expand abbreviated journal names,
        -l, --links         convert journal names to links (hyperrefs),
        -o <outfile>, --output <outfile>    output file name,
        -v, --version       version
    """

    args = docopt.docopt(main.__doc__, help=True, version=__version__)

    print "File created by '{0:s}' at {1} with options:".format(os.path.basename(__file__), datetime.datetime.today())

    # if no entries are given substitute the default ones
    if args["--discard"] and len(args["<entries>"]) == 0:
        args["<entries>"] = ["abstract", "doi", "file", "isbn", "issn",
                             "keywords", "month", "pmid", "url"]

    for key, value in args.items():
        print "{0:<15s} : {1}".format(key, value)

    bibparser = bibtex.Parser()
    bibdata   = bibparser.parse_file(args["<bibfile>"])

    args["--color"] = False
    linkcolor= "RoyalBlue"

    for item in bibdata.entries:

        b = bibdata.entries[item].fields

        if bibdata.entries[item].type == "article":
            if args["--abbreviate"]:
                b["journal"] = "{0:s}".format(abbreviate_journalname(b["journal"]))
            elif args["--expand"]:
                b["journal"] = "{0:s}".format(expand_journalname(b["journal"]))
            else:
                pass
            if args["--links"]:
                if args["--color"]:
                    b["journal"] = insert_link(b, "journal", args["<color>"])
                else:
                    b["journal"] = insert_link(b, "journal")

        elif bibdata.entries[item].type == "incollection":
            if args["--links"]:
                if args["--color"]:
                    b["booktitle"] = insert_link(b, "booktitle", args["<color>"])
                else:
                    b["booktitle"] = insert_link(b, "booktitle")
        elif bibdata.entries[item].type == "book" or bibdata.entries[item].type == "misc":
            if args["--links"]:
                if args["--color"]:
                    b["title"] = insert_link(b, "title", args["<color>"])
                else:
                    b["title"] = insert_link(b, "title")

    if args["--output"]:
        write_entries(bibdata.entries, args["<entries>"], args, args["--output"])
    else:
        print_entries(bibdata.entries, args["<entries>"])

if __name__ == "__main__":
    main()
