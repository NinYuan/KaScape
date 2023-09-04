#coding:UTF-8

import os,math
import numpy as np
from tool.readBase import readData
import matplotlib.pyplot as plt
import pandas as pd

def writeKmer(subkmer,outfilepath):
    fw = open(outfilepath, 'w')
    for i in range(len(subkmer)):
        for j in range(len(subkmer)):

            fw.write(str(subkmer[i][j]) + "\t")

        fw.write('\n')

    fw.close()
def getdivExceptzero(inPathText,outPathText,outfile):
    inMat = readData(inPathText) #in
    outMat = readData(outPathText) #out
    inex = np.array(inMat) #in
    outcon = np.array(outMat) #out
    sm = -np.log2(np.divide(outcon, inex, out=np.zeros_like(outcon), where=inex != 0)) #
    writeKmer(sm,outfile)



def printPic(fMatrixpath,outpath,labeltxt,figsize):
    fMatrix=np.loadtxt(fMatrixpath)
    plt.clf()
    nparrayf=np.array(fMatrix)
    Nsize=int(math.log2(nparrayf.shape[0]))
    lable1=int(math.sqrt(4**Nsize))-1

    fig, ax = plt.subplots(figsize=(figsize / 2.54, figsize / 2.54))

    data=ax.imshow(fMatrix)
    print(np.max(fMatrix))
    plt.xticks([])
    plt.yticks([])

    cb=fig.colorbar(data ,label=labeltxt)

    colornm='r'

    text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif'}

    plt.text(-0, -0, 'G' * Nsize, color=colornm, **text_params)
    plt.text(lable1, -0, 'C' * Nsize, color=colornm, **text_params)
    plt.text(-0, lable1 , 'A' * Nsize, color=colornm, **text_params)
    plt.text(lable1, lable1 , 'T' * Nsize, color=colornm, **text_params)

    plt.tight_layout()
    plt.savefig(outpath,dpi=400)


    plt.close()








def osmakedir(outdir):
    try:
        os.mkdir(outdir)
    except:
        pass





def inputoutputDivBU(outdir,seqName,inputfilepath,outputfilepath,columnlabel,figsize,cmatrix,randomK):
    outfilepath1 = outdir + seqName + 'ddG.txt'
    outfigurepath1 = outdir + seqName + 'ddG.pdf'
    Orderpath=outdir + seqName + 'ddGsort.txt'
    getdivExceptzero(inputfilepath, outputfilepath, outfilepath1)
    printPic(outfilepath1, outfigurepath1, columnlabel,figsize)

    energydict = getSignalDict(cmatrix, randomK, outfilepath1)
    orderdict = sorted(energydict.items(), key=lambda kv: kv[1], reverse=True)

    writeOrderDict(orderdict, Orderpath)




def getOutDivInDate20230510(basedir,outdir,figsize,cmatrix):
    datadir=basedir+'NPortionKmer/'


    for file in os.listdir(datadir):
        filename=file[:-4]
        if filename.endswith('b'):
            filenamelist=filename.split('_')
            randomN=filenamelist[0][1]
            unboundname='_'.join(filenamelist[0:3])+'_un_'+filenamelist[-1][:-1]+'u.pkl'
            inputname='f'+randomN+'N_input_'+randomN+'NIshort.pkl'


            elutionpath0 = datadir + file
            unboundflowpath0 = datadir + unboundname
            seqName=filename+'BU'
            columnlabel='bound div unbound'
            inputoutputDivBU(outdir,seqName, unboundflowpath0, elutionpath0, columnlabel,figsize,cmatrix,randomN)

            inputpath = datadir + inputname
            columnlabel = 'output div input'
            seqName = filename  + 'IO'
            inputoutputDivBU(outdir, seqName, inputpath, elutionpath0, columnlabel,figsize,cmatrix,randomN)






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


    plt.rcParams['font.sans-serif'] = ['Simhei', 'Arial']  # 用来正常显示中文标签
    plt.rcParams['font.size'] = 9

    figsize=9
    rootdir = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'

    cmatrix = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/cMatrix/'
    datet = '20230510'
    outdirRoot = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/OutDivInResult/'+datet+'/'

    osmakedir(outdirRoot)

    basedir = rootdir + datet + 'BarcodeUnionUnique/'
    outdir = outdirRoot + datet + 'BarcodeUnionUnique/'
    osmakedir(outdir)
    getOutDivInDate20230510(basedir, outdir,figsize,cmatrix)

