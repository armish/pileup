# -*- coding: utf-8 -*-
import pileup
from optparse import OptionParser
from twobitreader import TwoBitFile
import urwid
import vcf

from .range import Range
from .pileup import Pileup
from .track import ReferenceTrack, DivTrack, VCFTrack, LocationTrack, ScaleTrack

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

    return Range(chromosome, int(start), int(end))

def main():
    (options, args) = _get_args()
    twoBitFile = TwoBitFile(options.twobit)

    pileup = Pileup(region=_parse_range(options.range))
    pileup.addTrack(ScaleTrack(name="Scale"))
    pileup.addTrack(LocationTrack(name="Location"))
    pileup.addTrack(ReferenceTrack(twoBitFile, name="Reference"))

    for filename in args:
        if filename.endswith('.vcf'):
            pileup.addTrack(DivTrack(divider='-', name="Div1"))
            vcf_reader = vcf.Reader(open(filename, 'r'))
            variants = list(vcf_reader)
            pileup.addTrack(VCFTrack(variants=variants, name="Variants"))

    pileup.addTrack(DivTrack(divider='~', name="Div2"))
    pileup.addTrack(DivTrack(divider='.', name="Div3"))

    pileup.render()

if __name__ == '__main__':
    main()
