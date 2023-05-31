#coding:UTF-8
import re
from tool.transComplementaryRead import transComplementaryRead
from tool.toolclass.alignmentClass import alignment
def getfix2starts(seq1,seq2,randN,ref):
    rp = seq1 + '\w{'+str(randN)+'}' + seq2
    #rp = seq1 + '\w{4}' + seq2

    pattern = re.compile(rp)

    m = pattern.finditer(ref)
    rfix2starts=[]
    for m1 in m:
        fix1start=m1.start()
        fix2start=fix1start+len(seq1)+randN

        rfix2starts.append(fix2start)
    return rfix2starts



def gAlignment(lst,rname,orient,e):
    lenlst=len(lst)
    alignments=[]
    if lenlst>0:
        for pos in lst:

            align = alignment(rname, orient, pos,e.sequence,e.quality)
            alignments.append(align)
    return alignments

def getAlignment60Mseq12(seq1,seq2,randN,e):
    rname=e.rname
    ref=e.sequence

    lst=getfix2starts(seq1,seq2,randN,ref)

    alignments=gAlignment(lst,rname,'+',e)

    transref=transComplementaryRead(ref)

    lst = getfix2starts(seq1, seq2, randN, transref)
    alignments0=gAlignment(lst,rname,'-',e)
    ralignment=alignments+alignments0
    return ralignment







def getfix2startsBarcode(seq1,seq2,randN,ref,barcode,barcodeLeftRange,barcodeRightRange):
    rp = seq1 + '\w{'+str(randN)+'}' + seq2
    #rp = seq1 + '\w{4}' + seq2

    pattern = re.compile(rp)

    m = pattern.finditer(ref)
    rfix2starts=[]
    hasbarcode=False
    for m1 in m:
        fix1start=m1.start()
        fix2start=fix1start+len(seq1)+randN
        remainseq=ref[fix2start:]
        barcodeIndex=remainseq.find(barcode)
        if barcodeIndex!=-1:
            if barcodeIndex>=int(barcodeLeftRange) and barcodeIndex<=int(barcodeRightRange):
                hasbarcode=True
                rfix2starts.append(fix2start)
    if hasbarcode:
        return rfix2starts
    else:
        return []


def getAlignment60Mseq12Barcode(seq1,seq2,randN,e,barcode,barcodeLeftRange,barcodeRightRange):
    rname=e.rname
    ref=e.sequence
    transref = transComplementaryRead(ref)


    lst=getfix2startsBarcode(seq1,seq2,randN,ref,barcode,barcodeLeftRange,barcodeRightRange)

    alignments=gAlignment(lst,rname,'+',e)


    lst = getfix2startsBarcode(seq1, seq2, randN, transref,barcode,barcodeLeftRange,barcodeRightRange)
    alignments0=gAlignment(lst,rname,'-',e)
    ralignment=alignments+alignments0
    return ralignment
