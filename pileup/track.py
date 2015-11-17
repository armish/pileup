import urwid

class Track(object):
    width = 0
    height = 0
    name = ''
    palette = []

    def __init__(self, width=0, height=0, name=''):
        self.width = width
        self.height = height
        self.name = name

    def render(self, region):
        raise NotImplementedError()

    def setSize(self, width, height):
        self.width = width
        self.height = height

    def getSize(self):
        return width, height

    def getPalette(self):
        return self.palette

class TrackLabel(Track):
    label = None
    labelFormat = '%s | '

    def __init__(self, label, width=0, height=0, name=''):
        super(TrackLabel, self).__init__(width, height, name)
        self.label = label

    def render(self, region):
        labelTxt = self.labelFormat % self.label
        txt = urwid.Text(('bold', labelTxt), 'right', 'clip')
        return txt

class DivTrack(Track):
    divider = '-'

    def __init__(self, width=0, height=0, divider='-', name=''):
        super(DivTrack, self).__init__(width, height, name)
        self.divider = divider

    def render(self, region):
        div = urwid.Divider(self.divider)
        return div

class ReferenceTrack(Track):
    twoBitFile = None
    palette = [('base-a', 'white', 'dark green'),
               ('base-t', 'white', 'dark red'),
               ('base-g', 'white', 'light magenta'),
               ('base-c', 'white', 'light blue')]

    def __init__(self, twoBitFile, width=0, height=0, name=''):
        super(ReferenceTrack, self).__init__(width, height, name)
        self.twoBitFile = twoBitFile

    def render(self, region):
        chromosome, start, end = region.explode()
        regionSequence = self.twoBitFile[chromosome][start-1:end]
        visibleSequence = regionSequence[0:self.width]
        baseCols = []
        for base in visibleSequence:
            txt = urwid.Text(base.upper())
            base = urwid.AttrMap(txt, 'base-%s' % base.lower())
            baseCols.append(base)
        cols = urwid.Columns(baseCols)
        return cols