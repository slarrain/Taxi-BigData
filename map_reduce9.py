from mrjob.job import MRJob
import simplejson as sj
from datetime import datetime
import numpy as np
from mrjob.step import MRStep

def compare(datetime1,datetime2):
    hour1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S").hour
    hour2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S").hour
    day1 = datetime.strptime(datetime1, "%Y-%m-%d %H:%M:%S").weekday()
    day2 = datetime.strptime(datetime2, "%Y-%m-%d %H:%M:%S").weekday()
    if hour1 >=5 and hour1 < 11:
        period1 = 0
    elif hour1>=11 and hour1 <16:
        period1 =1
    elif hour1>=16 and hour1 <20:
        period1 = 2
    else:
        period1 = 3

    if hour2 >=5 and hour2 < 11:
        period2 = 0
    elif hour2>=11 and hour2 <16:
        period2 =1
    elif hour2>=16 and hour2 <20:
        period2 = 2
    else:
        period2 = 3

    if (day1>=4) and (day2>=4):
        if period1 == period2:
            return True
    elif (day1>=0) and (day1<4) and (day2>=0) and (day2<4):
        if period1 == period2:
            return True
    return False



class MRSimilarRides(MRJob):

    def mapper_init(self):
        with open ('all_coord.txt', 'r') as g:
            self.all_coord = sj.load(g)
        with open ('all_time.txt', 'r') as g:
            self.all_time = sj.load(g)

    def mapper(self, _, line):
        c = line.strip().split(',')
        if c[2]!='medallion':    # So its not the first line
            coord_list = [float(c[12]), float(c[13]), float(c[14]), float(c[15])]
            dt = c[7]
            name = c[3]
            if coord_list in self.all_coord:
                n_times = self.all_coord.count(coord_list)
                curr_index = 0
                for n in range(n_times-1):
                    curr_index = self.all_coord.index(coord_list, curr_index)
                    if (compare(dt, self.all_time[curr_index])):
                        yield curr_index, float(c[17])
                        break

    def combiner(self, index, fare):
        yield index, list(fare)

    def reducer_init(self):
        with open ('all_fares.txt', 'r') as g:
            self.all_fares = sj.load(g)
        with open ('all_hack_l.txt', 'r') as g:
            self.all_hack_l = sj.load(g)

    def reducer(self, index, fares):
        fare_list = []
        for comb in fares:
            for elem in comb:
                fare_list.append(elem)
        mu = np.mean(fare_list)
        sd = np.std(fare_list)
        val = mu+(3*sd)
        if self.all_fares[index] > val:
            yield self.all_hack_l[index], 1

    def reducer2 (self, hack_l, n_fraud):
        yield hack_l, sum(n_fraud)

    def steps(self):
        return [
          MRStep(mapper_init=self.mapper_init,
                mapper=self.mapper,
                 combiner=self.combiner,
                 reducer_init=self.reducer_init,
                 reducer=self.reducer),
          MRStep(reducer=self.reducer2)
        ]

if __name__ == '__main__':
    MRSimilarRides.run()
