#coding:UTF-8
import os
import datetime
from tool.getAlignment import getAlignment60Mseq12
import pickle
from tool.extractN import merge2RandNBarcode,extractNRnameWithoutBarcode60M
from tool.countNSeq import gcountNSeqNNN
from tool.portionNseq import CountPotionMapWithoutBarcode
from tool.CreateKmerMat import getCountPotionKmerMatrixWithoutBarcode
from tool.getRnmSeq import getRnmSeqQ
from tool.extractUtilize import extractUtilizationExcel
import gc

def Alignment60Mseq12(filepathlist,seq1,seq2,randN,outfile):

    print('start align')
    st = datetime.datetime.now()
    # use seq + to search in the refer dna record + and the first pos
    # get the complement dna and use the seq to match get the pos at the first pos
    # instore the reference name

    alignments60Ms = []
    print(len(filepathlist))
    for e in filepathlist:
        alignments60M = getAlignment60Mseq12(seq1,seq2,randN, e)
        if len(alignments60M) > 0:
            alignments60Ms.append(alignments60M)
    print("total alignments=")
    print(len(alignments60Ms))

    openfile = open(outfile, 'wb')
    pickle.dump(alignments60Ms, openfile)
    et = datetime.datetime.now()
    print("alignment end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("start time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))
    return alignments60Ms



def extractNWithoutBarcode(align60MContent,randNum):
    print("start get random N")
    st = datetime.datetime.now()

    print(len(align60MContent))

    alignNbList = []
    for align in align60MContent:
        alignNb = extractNRnameWithoutBarcode60M(align, randNum)
        if len(alignNb) != 0:
            alignNbList+=alignNb
    print("total extract N without barcode =")
    print(len(alignNbList))

    et = datetime.datetime.now()
    print("get random N Barcode end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))
    return alignNbList


def mergeData(extractedContent1,extractedContent2):
    st = datetime.datetime.now()
    print("start merge data")

    print("extractedContent1 len=")
    print(len(extractedContent1))

    print("extractedContent2 len=")
    print(len(extractedContent2))
    extractall = merge2RandNBarcode(extractedContent1, extractedContent2)
    print("extractall len=")
    print(len(extractall))

    et = datetime.datetime.now()

    print("merge data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))
    return extractall


#

def dumpFile(getNout,fname,extractall):

    epath=getNout+fname+'.pkl'
    epathfile = open(epath, 'wb')
    pickle.dump(extractall, epathfile)


def getRawDataseqs(f):

    with open(f) as file_object:
        contents = file_object.read()
    cntlist=contents.split('\n')
    iterate=int(len(cntlist)/4)

    totalseqs=iterate

    print("total totalseqs=")
    print(totalseqs)

    return totalseqs




def extractNNNN(rawdataPath,fileIndex,base_dir,seq1,seq2,Nsize,excelpath,samplename):



    tseqlist = []
    extractlist = []
    seqnamelist = []


    f1name = 'f'+fileIndex+'_1'
    f2name = 'f'+fileIndex+'_2'

    fname='f'+fileIndex+ '_' + samplename

    rawdata1=rawdataPath+f1name+'.fq'

    rawdata2 = rawdataPath+ f2name+'.fq'

    AlignOut = base_dir + "NAlignment/"
    if not os.path.exists(AlignOut):
        os.makedirs(AlignOut)

    NseqOut = base_dir + "NCountRate/"
    if not os.path.exists(NseqOut):
        os.makedirs(NseqOut)

    cf = base_dir + "NCount/"
    if not os.path.exists(cf):
        os.makedirs(cf)

    pf = base_dir + "NPortion/"
    if not os.path.exists(pf):
        os.makedirs(pf)

    oCountfile = base_dir + "NCountKmer/"
    if not os.path.exists(oCountfile):
        os.makedirs(oCountfile)


    oPortionfile = base_dir + "NPortionKmer/"
    if not os.path.exists(oPortionfile):
        os.makedirs(oPortionfile)

    print("start to work")

    outfile1 = AlignOut + fname + '_1.pkl'
    if os.path.exists(outfile1):
        alignments60Ms1 = pickle.load(open(outfile1, 'rb'))
        totalseqs1 = getRawDataseqs(rawdata1)
        del rawdata1
        gc.collect()
        print('alignment 1 ok')
    else:

        rnmSeqQfile1, totalseqs1 = getRnmSeqQ(rawdata1)
        del rawdata1
        gc.collect()

        alignments60Ms1 = Alignment60Mseq12(rnmSeqQfile1, seq1, seq2, Nsize,outfile1)
        del rnmSeqQfile1
        gc.collect()

    extractFile1 = extractNWithoutBarcode(alignments60Ms1, Nsize)

    del alignments60Ms1
    gc.collect()

    outfile2 = AlignOut + fname + '_2.pkl'
    if os.path.exists(outfile2):
        alignments60Ms2 = pickle.load(open(outfile2, 'rb'))

        print('alignment 2 ok')
    else:

        rnmSeqQfile2, totalseqs2 = getRnmSeqQ(rawdata2)
        del rawdata2
        gc.collect()
        alignments60Ms2 = Alignment60Mseq12(rnmSeqQfile2, seq1, seq2, Nsize,outfile2)
        del rnmSeqQfile2
        gc.collect()


    extractFile2 = extractNWithoutBarcode(alignments60Ms2, Nsize)
    del alignments60Ms2
    gc.collect()

    getNout = mergeData(extractFile1, extractFile2)
    del extractFile1
    gc.collect()
    del extractFile2
    gc.collect()

    gcountNSeqNNN(getNout, fname, NseqOut)

    extractlen = len(getNout)
    del getNout
    gc.collect()

    CountPotionMapWithoutBarcode(NseqOut, fname, cf, pf)

    getCountPotionKmerMatrixWithoutBarcode(cf, pf, oCountfile, oPortionfile, Nsize, fname)
    dataname = fname
    tseqlist.append(totalseqs1)
    extractlist.append(extractlen)
    seqnamelist.append(dataname)



    excelname = 'sequtilize'
    extractUtilizationExcel(tseqlist, extractlist, seqnamelist, excelname, excelpath)


    print("process done!")
