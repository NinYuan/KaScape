#coding:UTF-8

import pandas as pd
import os

def get_total(filepath):
    fpd=pd.read_excel(filepath)
    newfpd=fpd.query('seqName!="total"')

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

if __name__ == '__main__':

    rootdir = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'
    date = '20230510'
    filedir1 = rootdir + date + '/' + 'result/'
    filedir2 = rootdir + date + 'Union' + '/' + 'result/'
    outfilepath = rootdir + date + '/result' + date + '.xlsx'
    sheetname1 = date
    sheetname2 = date + 'Union'
    fpd1 = get_Main(filedir1)
    fpd2 = get_Main(filedir2)
    fpd = mergeColumn(fpd1, fpd2)
    fpd.to_excel(outfilepath)







