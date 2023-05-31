#coding:UTF-8

from xlwt import *

def writeToExcel(excelpath,dataname,ldata):
    file = Workbook(encoding='utf-8')
    table = file.add_sheet(dataname)

    for i, p in enumerate(ldata):
        # 将数据写入文件,i是enumerate()函数返回的序号数
        for j, q in enumerate(p):
            # print i,j,q
            table.write(i, j, q)
    file.save(excelpath)
