#coding:UTF-8
from tool.transComplementaryRead import transComplementaryRead
from collections import defaultdict
from tool.gReverseQuality import gRQSeq
import re

def getRNQuality(e,randNum,read,quality):
    if e.orient=='-':
        read = transComplementaryRead(read)
        quality = gRQSeq(quality)
    prepos=e.pos-randNum
    if prepos<0:
        rn=-1
        qn=-1
    else:
        rn=read[prepos:e.pos]
        if 'N' in rn:
            rn = -1
            qn = -1
        else:
            qn=quality[prepos:e.pos]
    return rn,qn


def getRNQualityUMI(e,randNum,read,quality,rightSeq):
    #满足得到的随机碱基序列和UMI值一样就记录为1
    if e.orient=='-':
        read = transComplementaryRead(read)
        quality = gRQSeq(quality)
    prepos=e.pos-randNum
    #consider border
    if prepos<0:
        rn=-1
        qn=-1
        umin=-1
    else:
        rn=read[prepos:e.pos]
        if 'N' in rn:
            rn = -1
            qn = -1
            umin=-1
        else:

            rightseqlen=len(rightSeq)
            umistart = prepos + randNum +rightseqlen
            umiend=umistart+6
            qn=quality[prepos:e.pos]
            umin=read[umistart:umiend]
    return rn,qn,umin


def extractNAllFlank(alignmentContent,randNum,coreseq):
    ernb=[]
    for align in alignmentContent:
        rn, qn=getRNQuality(align,randNum,align.seq,align.quality)
        if rn == -1:
            continue
        corenum=rn.count(coreseq)
        seqindex = rn.find(coreseq)
        if corenum==1 and seqindex==3:
            align.Nseq=rn[:3]+rn[6:]
            align.NseqQuality=qn[:3]+qn[6:]

        if rn!=-1 :
            ernb.append(align)
    return ernb

def extractNLeftFlank(alignmentContent,randNum,coreseq):
    ernb=[]
    for align in alignmentContent:
        rn, qn=getRNQuality(align,randNum,align.seq,align.quality)
        if rn == -1:
            continue
        corenum=rn.count(coreseq)
        seqindex = rn.find(coreseq)
        if corenum==1 and seqindex==3:
            align.Nseq=rn[:3]
            align.NseqQuality=qn[:3]

        if rn!=-1 :
            ernb.append(align)
    return ernb


def extractNRightFlank(alignmentContent,randNum,coreseq):
    ernb=[]
    for align in alignmentContent:
        rn, qn=getRNQuality(align,randNum,align.seq,align.quality)
        if rn == -1:
            continue
        corenum=rn.count(coreseq)
        seqindex = rn.find(coreseq)
        if corenum==1 and seqindex==3:
            align.Nseq=rn[6:]
            align.NseqQuality=qn[6:]

        if rn!=-1 :
            ernb.append(align)
    return ernb




def extractNRnameWithoutBarcode60M(alignmentContent,randNum):
    ernb=[]
    for align in alignmentContent:
        rn, qn=getRNQuality(align,randNum,align.seq,align.quality)
        if rn == -1:
            continue
        align.Nseq=rn
        align.NseqQuality=qn

        if rn!=-1 :
            ernb.append(align)
    return ernb


def extractNRnameWithoutBarcode60MUMI(alignmentContent,randNum,rightSeq):
    ernb=[]
    umins=[]
    for align in alignmentContent:
        rn, qn,umin=getRNQualityUMI(align,randNum,align.seq,align.quality,rightSeq)
        if rn == -1:
            continue
        align.Nseq=rn
        align.NseqQuality=qn

        if rn!=-1 :
            umins.append(umin)
            ernb.append(align)
    return ernb,umins





def getCoreseqIndex(seq,coreseq):
    x = list(re.finditer(coreseq, seq))
    iters=[]
    for each in x:
        start=each.span()[0]
        iters.append(start)
    return iters


def extractNRnameGTC(alignmentContent,randNum,seqcore,Nsize):
    ernb=[]
    coreseqindex=(Nsize-len(seqcore))/2
    for align in alignmentContent:
        rn, qn=getRNQuality(align,randNum,align.seq,align.quality)
        if rn == -1:
            continue
        align.Nseq=rn

        seqindexes=getCoreseqIndex(rn,seqcore)

        if coreseqindex in seqindexes:
            align.Nseq = rn
            align.NseqQuality=qn
            ernb.append(align)
    return ernb

def merge2RandNBarcode(extractContent1,extractContent2):

    extractDict1 = defaultdict(list)


    for extract in extractContent1:
        extractDict1[extract.rname].append(extract.Nseq)

    extractAll=[]
    for extract in extractContent2:
        if extract.rname in extractDict1.keys():
            NseqList=extractDict1[extract.rname]
            if extract.Nseq in NseqList:
                extractAll.append(extract)
    print('merge ok!')
    return extractAll

def Union2RandNBarcode(extractContent1,extractContent2):

    extractDict1 = defaultdict(list)

    extractAll = []

    for extract in extractContent1:
        extractDict1[extract.rname].append(extract.Nseq)
        extractAll.append(extract)

    for extract in extractContent2:
        if extract.rname not in extractDict1.keys():

            extractAll.append(extract)
    print('Union ok!')
    return extractAll


#将两种reads的alignment结果合并，如果都有则只取reads1的
def Union2Data(extractContent1,extractContent2):

    extractDict1 = defaultdict(list)

    extractAll = []
    for extract in extractContent1:
        extractDict1[extract.rname].append(extract.Nseq)
        extractAll.append(extract)

    for extract in extractContent2:
        if extract.rname not in extractDict1.keys():

            extractAll.append(extract)
    print('Union ok!')
    return extractAll