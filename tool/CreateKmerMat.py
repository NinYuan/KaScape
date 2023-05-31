
import numpy as np
import os

def NMatrixCreat(infile,NMFpath,Nsize):
    NumMatrixfile=open(NMFpath, 'w')
    NumMatrix = np.zeros((2 ** Nsize, 2 ** Nsize))
    for line in infile:
        linelist = line.split()
        Nseq = linelist[0]
        if 'N' not in Nseq:
            x, y = 0, 0
            for n in range(0, Nsize):
                half = 2 ** (Nsize-1-n)
                if Nseq[n] == 'G':
                    ix = 0 * half
                    iy = 0 * half
                elif Nseq[n] == 'A':
                    ix = 1 * half
                    iy = 0 * half
                elif Nseq[n] == 'C':
                    ix = 0 * half
                    iy = 1 * half
                elif Nseq[n] == 'T':
                    ix = 1 * half
                    iy = 1 * half
                x += ix
                y += iy
            NumMatrix[x][y] = linelist[-1]
        else:
            pass
    for i in range(2**Nsize):
        for j in range(2**Nsize):
            NumMatrixfile.write(str(NumMatrix[i][j])+"\t")
        NumMatrixfile.write('\n')
    infile.close()
    NumMatrixfile.close()

def mkdir(filepath):
    try:
        os.mkdir(filepath)
    except:
        pass

def getCountPotionKmerMatrixWithoutBarcode(iCountfile,iPortionfile,oCountfile,oPortionfile,Nsize,fname):

    mkdir(oCountfile)
    mkdir(oPortionfile)
    f = iCountfile + fname+'.pkl'  # 打开文件
    fr = open(f, 'r')
    oCfile=oCountfile + fname+'.pkl'
    NMatrixCreat(fr,oCfile,Nsize)

    f = iPortionfile + fname+'.pkl'  # 打开文件
    fr = open(f, 'r')
    opfile = oPortionfile + fname+'.pkl'
    NMatrixCreat(fr, opfile, Nsize)
    print("create matrix kmer done!")