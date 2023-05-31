#coding:UTF-8
from tool.writeToExcel import writeToExcel
def extractUtilizationExcel(totalseqs1, extractlen, dataname,excelname,excelpath):

    datafomat=[['seqName','seqNum','extractNum','origReads','extractReads','utilizeRate']]
    tseqnum=0
    eseqnum=0
    for i in range(len(totalseqs1)):
        tseq=totalseqs1[i]
        eseq=extractlen[i]
        seqname=dataname[i]

        origReads = tseq   # 条
        extractReads = eseq #条
        rate=eseq/tseq
        dlist=[seqname,tseq,eseq,origReads,extractReads,rate]
        tseqnum+=tseq
        eseqnum+=eseq
        datafomat.append(dlist)

    totalRate=eseqnum/tseqnum

    torigReads = tseqnum #条  # MB
    textractReads = eseqnum # 条
    lastline=['total',tseqnum,eseqnum,torigReads,textractReads,totalRate]
    datafomat.append(lastline)

    writeToExcel(excelpath, excelname, datafomat) #.xlsx



def extractUtilizationExcelEachFile( extractlen, dataname,excelname,excelpath):

    datafomat=[['seqName','extractNum']]

    for i in range(len(extractlen)):

        eseq=extractlen[i]
        seqname=dataname[i]

        dlist=[seqname,eseq]

        datafomat.append(dlist)


    writeToExcel(excelpath, excelname, datafomat) #.xlsx

