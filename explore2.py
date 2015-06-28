import simplejson as sj

def read_out (filename):
    with open(filename, 'r') as f:
        lista = sj.load(f)
    return lista

def analyze():
    prefix = 'trip_data_'
    folder = '/media/santiago/2816D26916D23790/Users/Santiago/Documents/taxi/'
    file = open('List_count5k.txt', 'w')
    for n in range(1, 2):
        outname = 'out5k_clean_taxi_'+str(n)+'.txt'
        print >> file, outname
        lista = read_out(outname)
        for item in lista:
            if len(item)>1:
                print >> file, len(item)
        print >> file, ''
        print 'File '+str(n)
    file.close()

if __name__ == "__main__":
    analyze()
