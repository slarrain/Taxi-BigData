from mrjob.job import MRJob
import simplejson as sj

coordinat = 'coord_all_year_4kx12.txt'

class MRSimilarRides(MRJob):

    def mapper_init(self):
        with open (coordinat, 'r') as g:
            coordinates = sj.load(g)
        self.coordinates = coordinates

    def mapper(self, _, line):
        c = line.strip().split(',')
        if c[2]!='medallion':    # So its not the first line
            coord_list = [float(c[12]), float(c[13]), float(c[14]), float(c[15])]
            if coord_list in self.coordinates:
                yield coord_list, (int(c[0]), c[3], c[7], int(c[9]), int(c[10]), float(c[11]),
                        float(c[12]), float(c[13]), float(c[14]), float(c[15]), float(c[17]))

    def combiner(self, random_coord, match_index):
        yield random_coord, list(match_index)

    def reducer(self, random_coord, match_index):
        yield None, list(match_index)

if __name__ == '__main__':
    MRSimilarRides.run()
