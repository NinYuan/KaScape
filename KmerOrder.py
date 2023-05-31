#coding:UTF-8
import numpy as np
import pickle,os
from tool.readBase import *

def getSignalDict(cmatrix,randomK,energypath):
    cpath = cmatrix + str(randomK) + '.txt'
    cMatrix = np.array(pickle.load(open(cpath, "rb"))).flatten()
    energyMatrix = readData(energypath)
    energyFlatten = np.array(energyMatrix).flatten()
    kmerdict={}
    i=0
    for c in cMatrix:
        kmerdict[c]=energyFlatten[i]
        i+=1

    return kmerdict

def writeOrderDict(orderdict,coresignalOrderpath):
    s=''
    for each in orderdict:

        s += each[0] + '\t' + '%.4f' % each[1] + '\n'
    fw=open(coresignalOrderpath,'w')
    fw.write(s)
    fw.close()

def mkdir(filepath):
    try:
        os.mkdir(filepath)
    except:
        pass



if __name__ == '__main__':
    cmatrix = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/cMatrix/'

    outdirRootpath = '/Users/chenhong/pkuWork/workStudio/G2_2/kscape/DATAanalysis/result/'
    mkdir(outdirRootpath)

    date = '20230510'

    energyRootpath = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/OutDivInResult/' + date + '/'

    dirnames = [date + 'BarcodeUnionUnique']

    for dirname in dirnames:

        energydirpath = energyRootpath + '/' + dirname+'/'


        outdirpath = outdirRootpath + '/' + dirname+'/'

        mkdir(outdirpath)

        for filename in os.listdir(energydirpath):

            if filename.endswith('.txt'):
                filepath = energydirpath + filename

                Orderpath = outdirpath + filename[:-4] + 'order.txt'

                print(filename)

                randomK=filename.split('_')[0][1]
                print(randomK)

                energydict = getSignalDict(cmatrix, randomK, filepath)
                orderdict = sorted(energydict.items(), key=lambda kv: kv[1], reverse=True)

                writeOrderDict(orderdict, Orderpath)





