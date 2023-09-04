#coding:UTF-8

import pandas as pd
import os




def barcodeUtilize(barcodepath):
    barcodedict={}
    for file in os.listdir(barcodepath):
        filepath=barcodepath+file
        fpd = pd.read_excel(filepath)

        newfpd = fpd.query('seqName!="total"')

        selectfpd = newfpd.iloc[:, newfpd.columns.get_indexer(['seqName', 'seqNum', 'extractNum', 'utilizeRate'])].values[0]

        barcodedict[selectfpd[0]]=selectfpd

    return barcodedict


def combinefpd(filepath1,barcodedict,filepathout):
    fpd = pd.read_excel(filepath1)

    itemlist=[]
    for idx, row in fpd.iterrows():

        rowlist=row.values.tolist()

        seqname=rowlist[2]
        if seqname in barcodedict.keys():
            barcode=barcodedict[seqname]
        else:
            barcode=[None,None,None,None]
        rowlist.extend(barcode)
        itemlist.append(rowlist)

    ncolumn=list(fpd.keys())
    ncolumn.extend(['barcodeSeqName', 'barcodeSeqNum', 'barcodeExtractNum', 'barcodeUtilizeRate'])
    npd=pd.DataFrame(itemlist,columns=ncolumn)
    npd.to_excel(filepathout)

if __name__ == '__main__':


    # rootdir = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'
    # date = '20230510'
    #
    # filepath1 = rootdir + date + '/result' + date + '.xlsx'
    # filepathout=rootdir + date + '/resultCombine' + date + '.xlsx'
    # barcodepath=rootdir + date + 'BarcodeUnion/result/'
    # barcodedict=barcodeUtilize(barcodepath)
    # combinefpd(filepath1, barcodedict,filepathout)


    rootdir = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/'
    date = '20230510'

    filepath1 = rootdir + date + '/resultCombine' + date + '.xlsx'
    filepathout=rootdir + date + '/resultAll' + date + '.xlsx'
    barcodepath=rootdir + date + 'BarcodeUnionUnique/result/'
    barcodedict=barcodeUtilize(barcodepath)
    combinefpd(filepath1, barcodedict,filepathout)