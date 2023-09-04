KGViewer

Description
KGViewer is a 3d visualization software that can help visualize a value for all possible sequences 
by the height and color of the bars plotted on a K-mer-based graph. 

Things KGViewer can do
The KGViewer has the following features. The size of the K-mer-based graph (2, 3, 4, 5, 6, and 7 bases) 
can be adjusted by setting the “Random DNA Base Number” parameter. The random dsDNA pool distribution 
landscape can be conveniently visualized in a K-mer graph in the left panel by specifying the input 
raw data path (the path to the random dsDNA pool distribution landscape file) and clicking the 
"Raw Data Scape" button. After specifying the output raw data path (the path to the bound dsDNA 
distribution landscape file) and clicking the “KaScape (- relative binding energy )” button, 
the left panel will change to show the relative affinity landscape. To view the value and sequence 
information of a bar in the landscape, the user can click on the bar, which will display the relevant 
information in the "Point Sequence" and "Relative Signal" text boxes. For example, clicking on a bar 
may display information such as the sequence 'GACC' and a value of 2.58. To visualize all sequences 
that contain a core sequence (e.g. ‘GAC’) of interest, a search function has been provided to 
highlight them (e.g. ‘NGAC’ or ‘GACN’ that contain GAC has been highlighted, where. N represents 
one of four bases). The landscape size, the size of the G, C, A, and T labels and their position 
can be scaled in the last row of the right panel. 


Getting started/ installation
1.clone the repo:
git clone https://github.com/NinYuan/KaScape.git
2.Ensure that you have Anaconda installed and create the environment for KGViewer
conda create -n KGViewerEnv
conda install -n KGViewerEnv python=3.6
conda install -n KGViewerEnv -c conda-forge mayavi
conda install -n KGViewerEnv -c conda-forge pyface
the flanking fix sequence used in experiment can be changed in KGViewerMain.conf 

Usage
source activate KGViewerEnv
python KGViewerMain.py

