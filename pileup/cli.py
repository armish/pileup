# -*- coding: utf-8 -*-
import pileup
from optparse import OptionParser
from twobitreader import TwoBitFile
import urwid

def _get_args():
    parser = OptionParser()
    parser.add_option("-t", "--twobit", dest="twobit",
                      action="store", type="string",
                      help="enables reference sequence track",
                      metavar="twoBitFile.2bit")
    parser.add_option("-r", "--range", dest="range",
                      action="store", type="string",
                      help="focuses on the given range (e.g. chr1:1-100)",
                      metavar="chrX:start-end")
    return parser.parse_args()

def _parse_range(rangeStr):
    (chromosome, location) = rangeStr.split(":")
    (start, end) = location.split("-")

    return chromosome, int(start), int(end)

def main():
    (options, args) = _get_args()
    reference = TwoBitFile(options.twobit)
    (chromosome, start, end) = _parse_range(options.range)

    txt = urwid.Text(reference[chromosome][start-1:end])
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()

if __name__ == '__main__':
    main()
