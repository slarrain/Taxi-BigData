import simplejson as sj
import pandas as pd

coord = [ 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']

def listas(outname):
    lista = []
    with open(outname, 'r') as f:
        lista = sj.load(f)
    lista = [z for z in lista if len(z)>1]
    return lista

def data(filename):
    print 'Reading ', filename
    df = pd.read_csv(filename, index_col=0)
    return df

def do():
    outname = 'out5k_clean_taxi_1.txt'
    filename = 'clean_taxi_1.csv'

    lista = listas(outname)
    df = data(filename)
    '''
    for x in lista:
        print len(x)
        print df.loc[x][coord]==df.loc[x][coord]
        raw_input("PRESS ENTER TO CONTINUE.")
    '''
    return df, lista

if __name__ == "__main__":
    do()
