KaScape data analysis


Usage

1. download Next-Generation Sequencing (NGS) data: 
    linuxnd ./downloadNGSData.sh
2. unzip and copy data: 
    python cpgunzip.py.    
    The code need to be modified according to the sample name used for NGS. 
3. obtain distribution for the random dsDNA pool P(Si) and the bound DNA P(Si|bound):
    3.1 python DataProcessRandomNExtractPortion.py /PROJ4/chenhong/kscape/kascapeProcessData/ 20230510 4 GCT AGGAGTGGGATCCGGGGGGGGGCCTAA 4N_out_4N_un six5N4u
    the extracted random base type from reads R1 and R2 must be same.
    3.2 python DataProcessRandomNExtractPortionUnion.py /PROJ4/chenhong/kscape/kascapeProcessData/ 20230510 4 GCT AGGAGTGGGATCCGGGGGGGGGCCTAA 4N_out_4N_un six5N4u 
    the extracted random base type from reads R1 and R2 do not need to be same.
    3.3 python DataProcessRandomNExtractPortionBarcodeUnion.py /PROJ4/chenhong/kscape/kascapeProcessData/ 20230510 4 GCT AGGAGTGGGA 4N_out_4N_b six3N4b CGTGAT 21 21
    the extracted random base type from reads R1 and R2 do not need to be same 
    if the barcode is used to specify different proteins studied.
    The code can generate NAlignment, NCount, NCountKmer, NCountRate, NPortion, NPortionKmer and result folders.
    NAlignment records the alignment between the sequencing reads and the regular expression. It is the intermediate information which can be deleted.
    NCount records the count number for each random sequence type, Bsi or Rsi.
    NCountKmer is the count number represented on the K-mer graph, Bsi or Rsi.
    NCountRate is the sorted count number and proportion, Bsi, Rsi, P(Si), or P(Si|bound).
    NPortion is the proportion of each random DNA type, P(Si), or P(Si|bound)
    NPortionKmer is the proportion represented on the K-mer graph, P(Si), or P(Si|bound).
    result is the utilization rate evaluation for each sequencing sample.
    
4. Combine the utilization rate excels of each sequencing sample from 3.1 and 3.2. 
    python FormTotalXlsx.py 
5. Combine the utilization rate excels of each sequencing sample from 3.1, 3.2, and 3.3
    python combineMergeUnionBarcode.py
6. Calculate relative binding energy and sort DDG order
    python calcDDG.py
7. Calculate rawdataDistribution
    python rawdataDistribution.py
    
  
8. use 3d software KGViewer to explore the data 
python KGViewer/KGViewerMain.py  


The user need to specify their own sample index and the directory.  






Getting started/ installation

Please install the required packages before start.
