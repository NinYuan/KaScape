def transComplementaryRead(read):
    dnaDict={'A':'T','T':'A','C':'G','G':'C'}
    cread=''
    for c in read:
        if c=='N':
            cread+='N'
        else:
            cread+=dnaDict[c]
    tcread=cread[::-1]
    return tcread



# if __name__=='__main__':
#     read='ATAGATTGGCGCATCAACGTGGCACTTGAGCATGCCTAACGTAGGAGATGCAGATCTCCTCGTACTAGCGCGCACTGAGTAGCTTGCGCATCAACGTGGCACTTGAGCATGCCTAACGTAGGAGATGCAGATCTCCTCGTACTAGTAAAT'
#     tcread=transComplementaryRead(read)
#     print(tcread)