#coding: UTF-8

import pickle
import  datetime
from collections import defaultdict
def getNlist(NSeqlist,ofle):
    outfile = open(ofle, 'w')
    Ncountdic = {}
    total = 0

    Ncountdic = defaultdict(lambda: 0)
    for Nseq in NSeqlist:
        if Nseq==-1:
            continue
        Ncountdic[Nseq] += 1

    sortNlist = sorted(Ncountdic, key=lambda x: Ncountdic[x])
    sortNlist.reverse()  # reverse

    for key in sortNlist:
        total = total + Ncountdic[key]
    for key in sortNlist:
        rate = float(Ncountdic[key]) / total
        line = "%s\t%d\t%f\n" % (key, Ncountdic[key], rate)
        outfile.write(line)
    print(ofle)
    print(total)
    outfile.close()
    return total




def countNSeqWithoutGTC(content,fname,o,coreseq):
    st=datetime.datetime.now()
    print("start countN")
    total=0

    NSeqlist=[]
    for e in content:
        if 'N' not in e.Nseq:
            ns=e.Nseq
            seqindex = ns.find(coreseq)
            if seqindex==3:
                nseq=ns[:3]+ns[6:]
                NSeqlist.append(nseq)

    ofile=o +fname+'.pkl'
    rt=getNlist(NSeqlist, ofile)
    total+=rt
    print("total sequence for each file=")
    print(total)

    et = datetime.datetime.now()

    print("count Nseq data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))


def gcountNSeq(content,fname,o,coreseq,Nsize):
    st=datetime.datetime.now()
    print("start countN")
    total=0

    NSeqlist=[]
    coreseqindex=(Nsize-len(coreseq))/2

    for e in content:
        if 'N' not in e.Nseq:
            ns=e.Nseq
            seqindex = ns.find(coreseq)
            if seqindex == coreseqindex:

                NSeqlist.append(ns)

    ofile=o +fname+'.pkl'
    rt=getNlist(NSeqlist, ofile)
    total+=rt
    print("total sequence for each file=")
    print(total)

    et = datetime.datetime.now()

    print("count Nseq data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))

def gcountNSeqNNN(content,fname,o):
    st=datetime.datetime.now()
    print("start countN")
    total=0

    NSeqlist=[]
    for e in content:
        if 'N' not in e.Nseq:

            NSeqlist.append(e.Nseq)

    ofile=o +fname+'.pkl'
    rt=getNlist(NSeqlist, ofile)
    total+=rt
    print("total sequence for each file=")
    print(total)

    et = datetime.datetime.now()

    print("count Nseq data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))


def countNSeqWithoutBarcode(path,fname,o):
    st=datetime.datetime.now()
    print("start countN")
    total=0

    f=path+fname+'.pkl'
    fr = open(f, 'rb')
    content = pickle.load(fr)
    NSeqlist=[]
    for e in content:
        if 'N' not in e.Nseq:
            NSeqlist.append(e.Nseq)

    ofile=o +fname+'.pkl'
    rt=getNlist(NSeqlist, ofile)
    total+=rt
    print("total sequence for each file=")
    print(total)

    et = datetime.datetime.now()

    print("count Nseq data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))





