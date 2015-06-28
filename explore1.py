import numpy as np
import pandas as pd
import simplejson as sj
import gc

coord = [ 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude']

def explore(df, n):

    rv = []
    index_checked = []

    for i in range(5000):

        random = np.random.randint(len(df))
        while (random not in df.index):
            random = np.random.randint(len(df))

        random_drive = df.ix[random].copy()

        #random_drive = rand_drive(df)
        #print random_drive
        #Check if any of the coord is 0. Don't do anything in that case.
        notzero = True
        if random_drive[coord[0]]==0 or random_drive[coord[1]]==0 or random_drive[coord[2]]==0 or random_drive[coord[3]]==0:
            notzero = False

        if random not in index_checked and notzero:

            #index_checked.append(random)

            compare = random_drive[coord]==df[coord]

	        #print type(compare), type(df[coord]), type(random_drive[coord])
            lista = df[coord][compare[coord]].dropna().index.tolist()
            #lista = compare.loc[compare[coord[0]]==True].index.tolist()
            rv.append(lista)
            index_checked = sum(rv, [])
            print 'Month '+str(n)+' - Loop '+str(i)
    print rv
    return rv

def do():

    #filenames = []
    prefix = 'clean_taxi_'
    sufix = '.csv'
    #folder = '/media/santiago/2816D26916D23790/Users/Santiago/Documents/taxi/'

    for n in range(1, 2):
        name = prefix+str(n)+sufix
        outname = 'out5k_'+prefix+str(n)+'.txt'

        #filenames.append(name)
        #temp_name = '/media/santiago/2816D26916D23790/Users/Santiago/Documents/taxi/trip_data_10.csv'

        df = pd.read_csv(name, index_col=0)
        df.columns = [col.strip() for col in df.columns]
        print 'Calling Explore...'+ str(n)
        lista = explore(df, n)

        with open(outname, 'w') as f:
            sj.dump(lista, f)
        del df
        gc.collect()
        print 'Month '+str(n)+'... Done'

    #output_filename = 'trip_10_matches.csv'
    #df_list = pd.DataFrame(lista)
    #df_list.to_csv(output_filename, index=False, header=False)
    #return lista

if __name__ == "__main__":
    print 'In...'
    do()
