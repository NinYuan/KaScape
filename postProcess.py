#coding:UTF-8

import os,math
import numpy as np
from PreProcess.tool.readBase import *
import matplotlib.pyplot as plt
import seaborn, pickle
import pandas as pd


# out div in log2
def writeKmer(subkmer,outfilepath):
    fw = open(outfilepath, 'w')
    for i in range(len(subkmer)):
        for j in range(len(subkmer)):
            # SeqMatrixfile.write(str(SeqMatrix[i][j])+"\t")
            fw.write(str(subkmer[i][j]) + "\t")
        # SeqMatrixfile.write('\n')
        fw.write('\n')

    fw.close()
def getdivExceptzero(inPathText,outPathText,outfile):
    inMat = readData(inPathText) #in
    outMat = readData(outPathText) #out
    inex = np.array(inMat) #in
    outcon = np.array(outMat) #out
    sm = np.divide(outcon, inex, out=np.zeros_like(outcon), where=inex != 0) #
    writeKmer(sm,outfile)

def getdivExceptzeroE(inPathText,outPathText,outfile):
    inMat = readData(inPathText) #in
    outMat = readData(outPathText) #out
    inex = np.array(inMat) #in
    outcon = np.array(outMat) #out
    sm = np.divide(outcon, inex, out=np.zeros_like(outcon), where=inex != 0) #
    e=-np.log2(sm)
    writeKmer(e,outfile)


def printPic(fMatrixpath,outpath,labeltxt,figsize,title):
    fMatrix=np.loadtxt(fMatrixpath)
    plt.clf()
    nparrayf=np.array(fMatrix)
    Nsize=int(math.log2(nparrayf.shape[0]))
    #print(Nsize)
    lable1=int(math.sqrt(4**Nsize))-1

    fig, ax = plt.subplots(figsize=(figsize / 2.54, figsize / 2.54))

    data=ax.imshow(fMatrix)
    print(np.max(fMatrix))
    #data = ax.imshow(fMatrix,vmax=vmax,vmin=vmin)
    plt.xticks([])
    plt.yticks([])
    #plt.colorbar( format='%.2e',label='Output Div Input signal')
    #cb = fig.colorbar(data,format='%.1f', label=labeltxt)
    cb=fig.colorbar(data ,label=labeltxt)
    #cb.ax.tick_params(labelsize=4)
    #cb.set_ticks([0,1])
    colornm='r'

    text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif'}
    # plt.text(-1, -1, 'G' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, -1, 'C' * Nsize, color=colornm, **text_params)
    # plt.text(-1, lable1+1, 'A' * Nsize, color=colornm, **text_params)
    # plt.text(lable1 ,lable1+1, 'T' * Nsize, color=colornm, **text_params)
    # plt.text(-0.5, -0.5, 'G' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, -0.5, 'C' * Nsize, color=colornm, **text_params)
    # plt.text(-0.5, lable1 + 0.5, 'A' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, lable1 + 0.5, 'T' * Nsize, color=colornm, **text_params)
    plt.text(-0, -0, 'G' * Nsize, color=colornm, **text_params)
    plt.text(lable1, -0, 'C' * Nsize, color=colornm, **text_params)
    plt.text(-0, lable1 , 'A' * Nsize, color=colornm, **text_params)
    plt.text(lable1, lable1 , 'T' * Nsize, color=colornm, **text_params)
    plt.title(title)

    #plt.xlim((0, 14000))
    plt.tight_layout()
    plt.savefig(outpath,dpi=400)

    #plt.savefig(outpath,dpi=400,figsize=(9 / 2.54, 9 / 2.54))
    plt.close()








def osmakedir(outdir):
    try:
        os.mkdir(outdir)
    except:
        pass



def inputoutputDivBUE(cmatrix,outdir,seqName,inputfilepath,outputfilepath,columnlabel,figsize):
    outfilepath1 = outdir + seqName + 'divE.txt'
    outfigurepath1 = outdir + seqName + 'divE.png'

    inputname=inputfilepath.split('/')[-1][:-3]+'png'
    outputname=outputfilepath.split('/')[-1][:-3]+'png'
    inputfigurepath=outdir+inputname
    outputfigurepath=outdir+outputname

    getdivExceptzeroE(inputfilepath, outputfilepath, outfilepath1)
    printPicE(outfilepath1, outfigurepath1, '-log2(bound/'+columnlabel+')',figsize,seqName+'divE')
    energydict = getSignalDict(cmatrix, outfilepath1)
    # orderdict = sorted(energydict.items(), key=lambda kv: kv[1], reverse=True)
    orderdict = sorted(energydict.items(), key=lambda kv: kv[1])
    Orderpath=outdir + seqName + 'Eorder.txt'
    writeOrderDict(orderdict, Orderpath)

    #printPicE(inputfilepath, inputfigurepath, columnlabel, figsize,inputname)
    outi=outdir+inputname[:-4]+'counts.png'
    countinput=basedir + 'NCountKmer/'+inputfilepath.split('/')[-1]
    readsCountDis(countinput, outi, inputname[:-4], figsize)

    #printPicE(outputfilepath, outputfigurepath, 'bound', figsize,outputname)
    outi=outdir+outputname[:-4]+'counts.png'
    countoutput = basedir + 'NCountKmer/' + outputfilepath.split('/')[-1]
    readsCountDis(countoutput, outi, outputname[:-4], figsize)

def inputoutputDivBU(outdir,seqName,inputfilepath,outputfilepath,columnlabel,figsize):
    outfilepath1 = outdir + seqName + 'div.txt'
    outfigurepath1 = outdir + seqName + 'div.png'

    inputname=inputfilepath.split('/')[-1][:-3]+'png'
    outputname=outputfilepath.split('/')[-1][:-3]+'png'
    inputfigurepath=outdir+inputname
    outputfigurepath=outdir+outputname

    getdivExceptzero(inputfilepath, outputfilepath, outfilepath1)
    printPic(outfilepath1, outfigurepath1, 'bound/'+columnlabel,figsize,seqName+'div')
    energydict = getSignalDict(cmatrix, outfilepath1)
    orderdict = sorted(energydict.items(), key=lambda kv: kv[1], reverse=True)
    Orderpath=outdir + seqName + 'order.txt'
    writeOrderDict(orderdict, Orderpath)


    printPic(inputfilepath, inputfigurepath, columnlabel, figsize,inputname)
    printPic(outputfilepath, outputfigurepath, 'bound', figsize,outputname)


def printPicE(fMatrixpath,outpath,labeltxt,figsize,title):
    print(fMatrixpath)
    #fMatrix=-np.log2(np.loadtxt(fMatrixpath))
    fMatrix=np.loadtxt(fMatrixpath)

    plt.clf()
    nparrayf=np.array(fMatrix)
    Nsize=int(math.log2(nparrayf.shape[0]))
    #print(Nsize)
    lable1=int(math.sqrt(4**Nsize))-1

    fig, ax = plt.subplots(figsize=(figsize / 2.54*1.2, figsize / 2.54))

    #data=ax.imshow(fMatrix)
    #print(np.max(fMatrix))
    #print(np.min(fMatrix))
    nparrayf[np.isinf(nparrayf)]=0
    #data = ax.imshow(fMatrix,vmax=vmax,vmin=vmin)
    #seaborn.heatmap(fMatrix, ax=ax, cmap="rainbow")
    #ax=seaborn.heatmap(fMatrix,  ax=ax,cmap="viridis_r")
    vmax=np.max(nparrayf)
    vmin=np.min(nparrayf)
    print(vmax)
    print(vmin)
    ax = seaborn.heatmap(fMatrix, ax=ax,vmax=vmax,vmin=vmin, cmap="viridis_r")
    #ax = seaborn.heatmap(fMatrix, ax=ax,vmax=0, cmap="viridis_r")
    #seaborn.heatmap(fMatrix, ax=ax,vmax=vmax,vmin=vmin, cmap="viridis_r")
    #seaborn.heatmap(fMatrix, ax=ax,vmax=vmax, cmap="viridis_r")

    #seaborn.heatmap(fMatrix,vmax=vmax,vmin=vmin,ax=ax,cmap="rainbow")

    plt.xticks([])
    plt.yticks([])
    #plt.colorbar(label=labeltxt)
    #plt.colorbar( format='%.2e',label='Output Div Input signal')
    #cb = fig.colorbar(data,format='%.1f', label=labeltxt)
    #cb=fig.colorbar(fMatrix ,label=labeltxt)
    #cb=fig.colorbar(data ,label=labeltxt)
    cbar = ax.collections[0].colorbar
    cbar.set_label(labeltxt)
    #cb.ax.tick_params(labelsize=4)
    #cb.set_ticks([0,1])
    colornm='red'

    text_params = {'ha': 'center', 'va': 'center', 'family': 'sans-serif'}
    # plt.text(-1, -1, 'G' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, -1, 'C' * Nsize, color=colornm, **text_params)
    # plt.text(-1, lable1+1, 'A' * Nsize, color=colornm, **text_params)
    # plt.text(lable1 ,lable1+1, 'T' * Nsize, color=colornm, **text_params)
    # plt.text(-0.5, -0.5, 'G' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, -0.5, 'C' * Nsize, color=colornm, **text_params)
    # plt.text(-0.5, lable1 + 0.5, 'A' * Nsize, color=colornm, **text_params)
    # plt.text(lable1, lable1 + 0.5, 'T' * Nsize, color=colornm, **text_params)

    if Nsize<6:
        plt.text(-0 + 0.5, -0 + 0.5, 'G' * Nsize, color=colornm, **text_params)
        plt.text(lable1 + 0.5, -0 + 0.5, 'C' * Nsize, color=colornm, **text_params)
        plt.text(-0 + 0.5, lable1 + 0.5, 'A' * Nsize, color=colornm, **text_params)
        plt.text(lable1 + 0.5, lable1 + 0.5, 'T' * Nsize, color=colornm, **text_params)
    else:
        plt.text(-0, -0, 'G' * Nsize, color=colornm, **text_params)
        plt.text(lable1-1, -0, 'C' * Nsize, color=colornm, **text_params)
        plt.text(-0, lable1 , 'A' * Nsize, color=colornm, **text_params)
        plt.text(lable1-1, lable1 , 'T' * Nsize, color=colornm, **text_params)

    plt.title(title)

    #plt.xlim((0, 14000))
    plt.tight_layout()
    plt.savefig(outpath,dpi=400)

    #plt.savefig(outpath,dpi=400,figsize=(9 / 2.54, 9 / 2.54))
    plt.close()



def calcDivE(datadir,filename,ufilename,infilename,outname,outdir,figsize,cmatrix):
    elutionpath0 = datadir + filename + '.pkl'
    unboundpath = datadir + ufilename + '.pkl'
    columnlabel = 'unbound'
    seqName = outname + 'bu'
    inputoutputDivBUE(cmatrix,outdir, seqName, unboundpath, elutionpath0, columnlabel, figsize)
    inputoutputDivBU(outdir, seqName, unboundpath, elutionpath0, columnlabel, figsize)

    inputpath = datadir + infilename
    columnlabel = 'input'
    seqName = outname + 'bi'
    inputoutputDivBUE(cmatrix,outdir, seqName, inputpath, elutionpath0, columnlabel, figsize)
    inputoutputDivBU(outdir, seqName, inputpath, elutionpath0, columnlabel, figsize)







# kmer order
def getSignalDict(cmatrix,energypath):

    energyMatrix = readData(energypath)
    energyFlatten = np.array(energyMatrix).flatten()
    randomK=int(np.log2(np.sqrt(len(energyFlatten))))
    cpath = cmatrix + str(randomK) + '.txt'
    cMatrix = np.array(pickle.load(open(cpath, "rb"))).flatten()
    kmerdict={}
    i=0
    for c in cMatrix:
        kmerdict[c]=energyFlatten[i]
        i+=1

    return kmerdict

def writeOrderDict(orderdict,coresignalOrderpath):
    s=''
    for each in orderdict:
        #normalizesignal=each[1]/allsignal
        #s+=each[0]+'\t'+'%.4f'%normalizesignal+'\n'
        s += each[0] + '\t' + '%.4f' % each[1] + '\n'
    fw=open(coresignalOrderpath,'w')
    fw.write(s)
    fw.close()


# reads count

def readsCountDis(filepath,outpath1,title1,figsize):
    #cMatrix = pickle.load(open(cpath, "rb"))
    #cMatrixflatten = np.array(cMatrix).flatten()
    xlabel='reads species'
    ylabel='reads count'
    data_histogram(filepath, outpath1, title1, xlabel, ylabel,figsize)


def data_histogram(filepath,outfilepath,title,xlabel,ylabel,figsize):
    fMatrix = readData(filepath)

    plt.clf()


    signalFlatten = np.array(fMatrix).flatten()
    # print(filepath)
    # print('total counts')
    # print(np.sum(signalFlatten))
    # counts=sum(signalFlatten)
    # numbers=np.sum(signalFlatten>0)
    # labelnum='non zero number '+str(numbers)+'\ntotal reads %d'%counts
    #histres = plt.hist(signalFlatten, bins=len(signalFlatten), label=labelnum)
    #histres = plt.hist(signalFlatten, bins=len(signalFlatten))
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
    if minv==0:
        #print('ok')
        minv=sorted(signalFlatten)[zeros]
        #print(sorted(signalFlatten))
        #print(minv)
    maxminratio=maxv/minv

    meanstr='totalreads:%.2f'%sumall+'\n'+'max:%.2f'%maxv+'\n'+'min:%.2f'%minv+'\n'+'zeronumber:%d'%zeros+'\n'+'median:%.2f'%median+'\n'+'mean:%.2f'%mean+'\n'+'max/min:%.2f'%maxminratio

    fig, ax = plt.subplots(figsize=(figsize / 2.54, figsize / 2.54))

    histres = ax.plot(signalFlatten,label=meanstr)

    #histres = plt.hist(signalFlatten, label=labelnum)
    # meanx=getMean(histres[1])
    # print('min')
    # print(signalFlatten.min())
    # print('max')
    # print(signalFlatten.max())
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    #plt.ylim((0,10))
    plt.title(title)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.savefig(outfilepath,dpi=400)
    #print(numbers)
    #plt.show()
   # return counts

# combine result extraction rate
def get_total(filepath):
    fpd=pd.read_excel(filepath)
    newfpd=fpd.query('seqName!="total"')
    #print(newfpd)
    #selectfpd=newfpd.loc[:,['seqName','seqNum','extractNum','utilizeRate']]
    selectfpd = newfpd.iloc[:, newfpd.columns.get_indexer(['seqName','seqNum','extractNum','utilizeRate'])]
    data=selectfpd.values.tolist()
    return data

def get_Main(filedir):
    items=[]
    for filename in os.listdir(filedir):
        if filename.endswith('xls'):
            filepath=filedir+filename
            item=get_total(filepath)
            items.extend(item)
    fpd=pd.DataFrame(items,columns=['seqName','seqNum','extractNum','utilizeRate'])
    return fpd

def mergeColumn(fpd1,fpd2):
    seqNameUnion=fpd2['seqName'].values.tolist()
    seqNumUnion=fpd2['seqNum'].values.tolist()
    i=0
    items=[]
    for seqNameU in seqNameUnion:
        seqNumU=seqNumUnion[i]
        querystr='seqName=='+'"'+seqNameU+'"'
        newfpd1 = fpd1.query(querystr).values.tolist()
        seqnumfpd1=newfpd1[0][1]
        unionrate=seqNumU/seqnumfpd1
        item=newfpd1[0]+[seqNumU]+[unionrate]
        items.append(item)
        i+=1
    fpd = pd.DataFrame(items, columns=['seqName', 'seqNum', 'extractNum', 'utilizeRate','unionExtractNum','unionExtractRate'])
    return fpd

def combineExtractionRate(rootdir,date):
    filedir1 = rootdir + date + '/' + 'result/'

    outfilepath = rootdir + date + '/result' + date + '.xlsx'
    sheetname1 = date

    fpd1 = get_Main(filedir1)

    fpd1.to_excel(outfilepath)



def getOutDivInDate20231201(basedir, outdir, figsize,cmatrix):
    datadir = basedir + 'NPortionKmer/'


    for i in range(5):
        N = i + 4
        filename = 'f'+ str(N) + 'N' + '_b_H1N'+ str(N)+'b'
        ufilename = 'f'+ str(N) + 'N' + '_unb_H1N'+ str(N)+'u'
        infilename = 'f'+ str(N) + 'N' + '_i_R1N'+ str(N)+'.pkl'
        calcDivE(datadir, filename, ufilename, infilename, 'H1N' + str(N), outdir, figsize,cmatrix)

if __name__ == '__main__':


    plt.rcParams['font.sans-serif'] = ['Simhei', 'Arial']  # 用来正常显示中文标签
    #plt.rcParams['font.sans-serif'] = ['Simhei']  # 用来正常显示中文标签
    plt.rcParams['font.size'] = 9

    figsize=9
    #rootdir='/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/'
    rootdir = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'
    cmatrix = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/cMatrix/'
    #rootdir='/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/allProtein/'

    #datet = '20220519'
    #datet = '20220608'
    #datet = '20220807'
    #datet = '20230510'
    #datet = '20230809'
    #datet = '20230713'
    #datet = '20231116'
    #datet = '20231123'
    #date = '20231127'
    date='20231201'
    outdirRoot = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/OutDivInResult/'+date+'/'

    osmakedir(outdirRoot)

    basedir = rootdir + date + '/'
    outdir = outdirRoot + date + '/'
    osmakedir(outdir)

    getOutDivInDate20231201(basedir, outdir, figsize,cmatrix)

    combineExtractionRate(rootdir, date)


