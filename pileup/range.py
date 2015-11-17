class Range(object):
    chromosome = 'chrNone'
    start = 0
    stop = 0

    def __init__(self, chromosome, start, end):
        self.chromosome = chromosome
        self.start = start
        self.end = end

    def explode(self):
        return self.chromosome, self.start, self.end
