
def getGeneData(cM,s):
    x=[]
    y=[]
    rc=[]
    nd=[]
    for i in range(len(cM)):
        hang=[]
        drow=[]
        for j in range(len(cM[i])):

            if cM[i][j].find(s)!=-1:

                x.append(i)
                y.append(j)
                hang.append(cM[i][j])
                drow.append(5.0)
            else:
                hang.append('0')
                drow.append(-5.0)
        rc.append(hang)
        nd.append(drow)

    return rc,nd


