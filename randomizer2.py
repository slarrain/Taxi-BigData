import pandas as pd
import numpy as np
import simplejson as sj
import gc

coord = [ 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']


def randomness(taxi, coordinates):
    largo = len(taxi)
    for x in range(4000):
        rand_index = np.random.randint(0, largo)
        while (rand_index not in taxi.index) or (taxi.loc[rand_index][coord].tolist() in coordinates):
            rand_index = np.random.randint(0, largo)
        if rand_index in taxi.index:
            coordinates.append(taxi.loc[rand_index][coord].tolist())
    return coordinates


def read(month):
    name = 'clean_taxi_'+str(month)+'.csv'
    print 'Reading Data for Month ', month
    taxi = pd.read_csv(name, index_col=0)
    taxi.columns = [col.strip() for col in taxi.columns]
    print 'Reading ... Done'
    return taxi

def writer(lista, name):

    with open(name, 'w') as f:
        sj.dump(lista, f)

def do():
    coordinates = []
    for n in range(1, 13):
        print 'Randoms for Month ', n, '...'
        taxi = read(n)
        coordinates = randomness(taxi, coordinates)
        del taxi
        gc.collect()
    writer(coordinates, 'coord_all_year_4kx12.txt')
    print 'Done'

if __name__ == "__main__":
    print 'In...'
    do()
