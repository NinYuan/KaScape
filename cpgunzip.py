#coding:UTF-8
import os,re




def getList(a):
    b = re.split('[.]', a)
    return b




a='4N_input_1.fq.gz'
b=getList(a)
print(b)
indexloc=0
r1r2loc=-3
expindex = b[indexloc]
rindex = b[r1r2loc]
print(expindex)
print(rindex)

#确定文件名，有两种情况：文库，index,r1orr2;index,r1orr2
#numloc指文库的index号的位置
def cpgunzipdata(f,o,libloc,numloc,indexloc,r1r2loc):
    osmkdir(o)
    for root, dirs, files in os.walk(f, topdown=False):
        for name in files:
            if name.endswith('fq.gz'):
                b = getList(name)

                expindex = b[indexloc]
                rindex = b[r1r2loc]
                if libloc!=-1:
                    lindex = b[libloc][numloc]
                    fname='f'+lindex+'_'+expindex+'_'+rindex+'.fq.gz'
                else:
                    fname = 'f' + expindex  + '.fq.gz'


                print(fname)
                inputfile=os.path.join(root, name)
                outputfile=o+fname
                cmd = 'cp ' + inputfile + " " + outputfile
                print(cmd)
                os.system(cmd)

                cmd1 = 'gunzip ' + outputfile
                print(cmd1)
                os.system(cmd1)



def osmkdir(dirpath):
    try:
        cmd='mkdir -p '+dirpath
        os.system(cmd)
    except:
        pass


# f='/PROJ4/chenhong/KascapeData/20230510/X101SC23030069-Z01-J082/01.RawData/'
# o='/PROJ4/chenhong/kscape/kascapeProcessData/20230510/rawdata/'
# osmkdir(o)
# libloc=-1
# numloc=0
# indexloc=0
# r1r2loc=-3
# cpgunzipdata(f,o,libloc,numloc,indexloc,r1r2loc)



