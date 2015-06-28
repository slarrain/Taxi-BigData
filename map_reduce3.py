from mrjob.job import MRJob
import simplejson as sj
import requests
import os

coord = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']

coordinat = 'http://m.uploadedit.com/ba3d/1432615166424.txt'
#index = 'http://m.uploadedit.com/ba3d/1432505827401.txt'

def get_request(url):
    '''
    Open a connection to the specified URL and if successful
    read the data.

    Inputs:
        url: must be an absolute URL

    Outputs:
        request object or None

    Examples:
        get_request("http://www.cs.uchicago.edu")
    '''

    try:
        html = requests.get(url)
        return html
    except:
        # fail on any kind of error
        return None

def read_request(request):
    '''
    Return data from request object.  Returns result or "" if the read
    fails..
    '''

    try:
        return request.text.encode('iso-8859-1')
    except:
        print "read failed: " + request.url
        return ""


class MRSimilarRides(MRJob):

    def mapper_init(self):

        #indexes = sj.loads(read_request(get_request(index)))
        coordinates = sj.loads(read_request(get_request(coordinat)))
        #self.indexes = indexes
        self.coordinates = coordinates
        #self.lista = []


    def mapper(self, _, line):

        c = line.strip().split(',')
        if c[2]!='medallion':    # So its not the first line
            coord_list = [float(c[12]), float(c[13]), float(c[14]), float(c[15])]
            if coord_list in self.coordinates:
                yield coord_list, (c[7], int(c[0]))
    '''
    def combiner_init(self):
        self.lista = []

    '''
    def combiner(self, random_coord, match_index):
        yield random_coord, list(match_index)

    def reducer(self, random_coord, match_index):
        yield None, list(match_index)


if __name__ == '__main__':
    MRSimilarRides.run()
