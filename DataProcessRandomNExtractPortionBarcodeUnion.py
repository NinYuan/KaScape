#coding:UTF-8
#1.数据下载
# 2.文件名修改
# 3.数据提取，利用率计算。
# 给每个文件提取序列，并求其分布图


import sys,os

from ExtractPattern.ExtractEachExpDataBarcodeUnion import extractNNNN
if __name__ == '__main__':

    base_path = sys.argv[1]  # /PROJ3/chenhong/flank_N/wrky/
    date_name = sys.argv[2]  # 20190719

    Nsize = int(sys.argv[3])  # 4

    seq1 = sys.argv[4]  # ACTCAGTG
    seq2 = sys.argv[5]  # CTAGTACGAGGAGATCTGCATCTCCGTGAT

    fileIndex=sys.argv[6]
    samplename=sys.argv[7]
    barcode = sys.argv[8]
    barcodeLeftRange = sys.argv[9]
    barcodeRightRange= sys.argv[10]

    data_name=date_name+'BarcodeUnionUnique'
    datapath=base_path+data_name+'/' #/PROJ3/chenhong/flank_N/wrky/20190521/

    excelpath=datapath+'result/' #/PROJ3/chenhong/flank_N/result/utilize20190521B1.xls
    excelfilepathN=excelpath+'utilize'+'N' + str(Nsize)+'_'+data_name+samplename+'.xls'




    if not os.path.exists(excelpath):
        os.makedirs(excelpath)
    print('makedir '+excelpath)


    date_path=base_path+date_name+'/'
    rawdataPath = date_path+'/'+'rawdata/'


    extractNNNN(rawdataPath,fileIndex, datapath, seq1, seq2, Nsize,excelfilepathN,samplename,barcode,barcodeLeftRange,barcodeRightRange)

    print('extractNNNN ok!')


