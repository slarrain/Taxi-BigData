from mrjob.job import MRJob

names = 'flag_drivers.csv'

class MRSimilarRides(MRJob):

    def mapper_init(self):

        with open(names, 'r') as f:
            rf = f.readline().strip().split(',')
        self.names = rf


    def mapper(self, _, line):
        c = line.strip().split(',')
        if c[2]!='medallion':    # So its not the first line
            coord_list = [float(c[12]), float(c[13]), float(c[14]), float(c[15])]
            name = c[3]
            date = c[7]
            fare = float(c[17])
            if name in self.names:
                yield name, (date, coord_list, fare)

    def combiner(self, name, coord_list):
        yield name, list(coord_list)

    def reducer(self, name, coord_list):
        yield name, list(coord_list)

if __name__ == '__main__':
    MRSimilarRides.run()
