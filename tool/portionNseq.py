
import datetime,os

def writeCountPortion(infile1,CFp,PFp):

    Countfile = open(CFp, 'w')
    Portionfile = open(PFp,'w')

    while 1:
        line1 = infile1.readline().rstrip()

        if not line1 :
            break
        rowElem=line1.split('\t')
        Countfile.write(rowElem[0]+'\t'+rowElem[1]+'\n')
        Portionfile.write(rowElem[0]+'\t'+rowElem[2]+'\n')
    Countfile.close()
    Portionfile.close()

def mkdir(filepath):
    try:
        os.mkdir(filepath)
    except:
        pass

def CountPotionMapWithoutBarcode(path,fname,CFp,PFp):
    st = datetime.datetime.now()
    f = path + fname+'.pkl'  # 打开文件
    fr = open(f, 'rt')
    mkdir(CFp)
    mkdir(PFp)
    Countfile=CFp+ fname+'.pkl'
    Portionfile=PFp+ fname+'.pkl'
    writeCountPortion(fr,Countfile,Portionfile)
    print('count portion map done !')
    et = datetime.datetime.now()

    print("merge data end!")
    print("start time       " + st.strftime('%Y.%m.%d-%H:%M:%S'))
    print("end time       " + et.strftime('%Y.%m.%d-%H:%M:%S'))