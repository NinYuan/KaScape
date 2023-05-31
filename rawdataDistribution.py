#coding:UTF-8
import pickle
import numpy as np
from tool.readBase import readData

import matplotlib.pyplot as plt
import os

def data_histogram(filepath,outfilepath,title,xlabel,ylabel,figsize):
    fMatrix = readData(filepath)

    plt.clf()


    signalFlatten = np.array(fMatrix).flatten()

    calcStat=list(signalFlatten)
    maxv=np.max(signalFlatten)
    minv = np.min(signalFlatten)
    calcStat.remove(maxv)
    calcStat.remove(minv)
    median=np.median(calcStat)
    mean=np.mean(calcStat)
    std=np.std(calcStat)
    sumall=np.sum(signalFlatten)
    nonzero=np.count_nonzero(signalFlatten)
    zeros=len(signalFlatten)-nonzero
    meanstr='totalreads:%.2f'%sumall+'\n'+'max:%.2f'%maxv+'\n'+'min:%.2f'%minv+'\n'+'zeronumber:%d'%zeros+'\n'+'median:%.2f'%median+'\n'+'mean:%.2f'%mean+'\n'+'std:%.2f'%std

    fig, ax = plt.subplots(figsize=(figsize / 2.54, figsize / 2.54))

    histres = ax.plot(signalFlatten,label=meanstr)


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(outfilepath,dpi=400)


def data_sortplot(filepath,outfilepath,title,xlabel,ylabel):
    fMatrix = readData(filepath)

    plt.clf()
    signalFlatten = np.array(fMatrix).flatten()
    signalFlatten=np.sort(signalFlatten)

    histres = plt.plot(signalFlatten)


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)

    plt.savefig(outfilepath)

def readsCountDis(filepath,outpath1,outfilepath2,title1,title2,figsize):

    xlabel='reads species'
    ylabel='reads count'
    data_histogram(filepath, outpath1, title1, xlabel, ylabel,figsize)


def mkdir(filepath):
    try:
        os.mkdir(filepath)
    except:
        pass



def getInputdistributionMain(Riname,figsize):
    inputpath = rootpath + Riname + '.pkl'

    outi = outdir + Riname + '.png'
    outi2 = outdir + 'sort' + Riname + '.png'


    readsCountDis(inputpath, outi, outi2, Riname, Riname + '_sort',figsize)



if __name__ == '__main__':

    plt.rcParams['font.sans-serif'] = ['Simhei', 'Arial']  # 用来正常显示中文标签
    # plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
    plt.rcParams['font.size'] = 9

    figsize=9
    data = '20230510'
    outdir = '/Users/chenhong/pkuWork/workStudio/G2_2/kscape/kascapePaperFigures/outputfigure/countDistribution/'+data+'/'
    mkdir(outdir)


    dirnames = [data, data + 'Union', data + 'BarcodeUnion']

    for dirname in dirnames:
        rootpath = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'+dirname+'/NCountKmer/'
        for file in os.listdir(rootpath):
            Riname = file[:-4]
            print(Riname)

            getInputdistributionMain(Riname,figsize)

