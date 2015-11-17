import urwid
from .range import Range
from .track import TrackLabel

class Pileup(object):
    tracks = []
    region = None
    loop = None
    labelWidth = 15
    palette = []

    def __init__(self, tracks=[], region=None):
        self.tracks = tracks
        self.region = region

    def addTrack(self, track):
        self.tracks.append(track)

    def sortTracks(self, compare=lambda x: x.__class__.__name__, reverse=False):
        self.tracks.sort(key=compare, reverse=reverse)

    def setRegion(self, region):
        self.region = region

    def adjustRegion(self, width):
        (chromosome, start, end) = self.region.explode()
        return Range(chromosome, start, start + width - 1)

    def exit_on_q(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def render(self):
        placeholder = urwid.SolidFill()  # For calculations
        loop = urwid.MainLoop(placeholder,
                              self.palette,
                              unhandled_input=self.exit_on_q)
        loop.screen.set_terminal_properties(colors=16)
        width, height = loop.screen.get_cols_rows()

        adjustedRegion = self.adjustRegion(width)
        lw = self.labelWidth  # label width
        tw = width - lw  # track width
        renderedTracks = []
        for track in self.tracks:
            label = TrackLabel(track.name)
            track.setSize(tw, height)
            cols = urwid.Columns([(lw, label.render(adjustedRegion)),
                                  (tw, track.render(adjustedRegion))])
            renderedTracks.append(cols)
            if track.palette:
                self.palette += track.palette

        pile = urwid.Pile(renderedTracks)
        fill = urwid.Filler(pile, 'top')
        loop.widget = fill
        loop.screen.register_palette(self.palette)
        loop.run()
