from  tool.toolclass.rnmSeqQClass import rnmSeqQClass
#get rnmSeqQClass list from fq and dump
def getRnmSeqQ(f):

    with open(f) as file_object:
        contents = file_object.read()
    cntlist=contents.split('\n')
    iterate=int(len(cntlist)/4)
    rnmSeqQs=[]
    j=0
    for i in range(iterate):

        rnm=cntlist[j].split(' ')[0]
        seq=cntlist[j+1]
        quality=cntlist[j+3]
        j=j+4
        rsq = rnmSeqQClass(rnm,seq,quality)

        rnmSeqQs.append(rsq)
    print("total rnmSeqQs=")
    print(len(rnmSeqQs))
    totalseqs=len(rnmSeqQs)
    print("rnameSeqQuality Done!")
    return rnmSeqQs,totalseqs

