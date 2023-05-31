#form alignment class
class alignment:
    # recode randomN sequence, quality
    def __init__(self, rname, orient,pos,seq,quality):
        self.rname=rname
        self.orient=orient
        self.pos=pos
        self.seq = seq
        self.quality=quality
        self.Nseq=""
        self.NseqQuality=""
        self.Nbarcode=""
        self.NBarcodeQuality=""
        self.barcodeClass=""




