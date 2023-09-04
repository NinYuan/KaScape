#coding:UTF-8


from traits.api import  Str,  Button, File
import numpy as np

from traits.api import HasTraits, Instance, Array, \
    on_trait_change
from traitsui.api import View, Item, HGroup, Group



from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, \
    MlabSceneModel

from tools.readData import readData
from tools.getGenePosition import getGeneData
import pickle

import configparser


class Gene(HasTraits):
    cp = configparser.ConfigParser()

    cp.read('./KGViewerMain.conf')
    cop = cp.get('kmer','kmerpath')
    print(cop)
    fix1=cp.get('fixsequence','leftfix')
    fix2 = cp.get('fixsequence', 'rightfix')
    print(fix1)
    print(fix2)
    data = Array()

    scene_n = Instance(MlabSceneModel, ())

    kmerNoBackground = Button
    kmer2d = Button
    ipw_3d_z = Instance(PipelineBase)

    GeneN = Str
    NumberOrPortion=Str
    Search = Str
    searchButton = Button

    #experimentPathText=File(exists=True)
    experimentPathText=Str
    #experimentPathText = File()
    #experimentPathText='/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/all/20220715/NPortionKmer/ON4.txt'

    #controlPathText =File(exists=True)
    controlPathText=Str
    #controlPathText = '/Users/chenhong/Documents/pkucode/workStudio/G1/data/test/kmer/wrky/all/20220715/NPortionKmer/IN4.txt'

    gnum = "4"
    saclefactor = "10"
    ATGCPosition = '1'
    ATGCScale = '1'
    potionSub = Button
    pcdiv = Button
    portion_click_yes = 0
    div_click_yes = 0
    noback_click_yes = 0
    search_click_yes = 0


    def __init__(self, **traits):
        super(Gene, self).__init__(**traits)


    def clear_figure(self):
        for child in self.scene_n.mayavi_scene.children:
            child.remove()

    @on_trait_change('kmerNoBackground.activated')
    def display_kmerNoBackground_n(self):

        if self.noback_click_yes >= 1:
            self.clear_figure()
        mlab.clf(mlab.colorbar)
        print ('raw data without backgroud process or to see backgroud')
        print (self.experimentPathText)

        cpath = self.cop +'/'+ str(self.gnum) + '.txt'
        sf = float(self.saclefactor)

        fMatrix1 = readData(self.controlPathText)

        cMatrix = pickle.load(open(cpath, "rb"))
        rCm = np.rot90(cMatrix, -1)
        self.cMatrix = rCm
        rFm1 = np.rot90(fMatrix1, -1)

        self.data = rFm1
        snum = 2 ** int(self.gnum)


        def picker_callback(picker_obj):
            picked = picker_obj.actors

            x_, y_, z_ = picker_obj.pick_position
            x = int(round(x_))
            y = int(round(y_))
            #print x, y
            self.GeneN = self.cMatrix[x][y]
            self.NumberOrPortion = str(self.data[x][y])

        if self.noback_click_yes == 0:
            self.noback_click_yes += 1
        self.scene_n.mayavi_scene.on_mouse_pick(picker_callback, type="cell")
        outline = mlab.barchart(self.data, figure=self.scene_n.mayavi_scene, scale_factor=sf)
        mlab.text3d(-float(self.ATGCPosition), snum, 0, 'G', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(snum, snum, 0, 'C', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(-float(self.ATGCPosition), -float(self.ATGCPosition), 0, 'A',
                    scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(snum, -float(self.ATGCPosition), 0, 'T', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))


        cb=mlab.colorbar(orientation='vertical')
        cb.label_text_property.font_family = 'arial'
        cb.label_text_property.bold = 0
        cb.label_text_property.font_size = 20

        self.scene_n.mlab.view(0, 0)

    @on_trait_change('pcdiv.activated')
    def display_potionDiv_n(self):

        if self.div_click_yes >= 1:
            self.clear_figure()
        mlab.clf(mlab.colorbar)


        cpath = self.cop + '/' + str(self.gnum) + '.txt'
        sf = float(self.saclefactor)
        snum = 2 ** int(self.gnum)

        fMatrix1 = readData(self.controlPathText)
        fMatrix2 = readData(self.experimentPathText)

        cMatrix = pickle.load(open(cpath, "rb"))
        rFm1 = np.rot90(fMatrix1, -1)
        rFm2 = np.rot90(fMatrix2, -1)

        if len(rFm1) == len(rFm2):

            #sm = rFm2 / rFm1
            sm = np.log2(rFm2 / rFm1)
            self.data = sm

            rCm = np.rot90(cMatrix, -1)
            self.cMatrix = rCm

            outline = mlab.barchart(self.data, figure=self.scene_n.mayavi_scene, scale_factor=sf, line_width=5.0)

            mlab.text3d(-float(self.ATGCPosition), snum, 0, 'G', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
            mlab.text3d(snum, snum, 0, 'C', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))

            mlab.text3d(-float(self.ATGCPosition), -float(self.ATGCPosition), 0, 'A',
                        scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
            mlab.text3d(snum, -float(self.ATGCPosition), 0, 'T', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))

        def picker_callback0(picker_obj):
            picked = picker_obj.actors

            x_, y_, z_ = picker_obj.pick_position
            x = int(round(x_))
            y = int(round(y_))
            print (x, y)
            self.GeneN = self.cMatrix[x][y]
            self.NumberOrPortion = str(self.data[x][y])

        if self.div_click_yes == 0:
            self.div_click_yes += 1
        isadd = len(self.scene_n.mayavi_scene._mouse_pick_dispatcher._mouse_press_callback_nbs)

        self.scene_n.mayavi_scene.on_mouse_pick(picker_callback0, type="cell")


        cb = mlab.colorbar(orientation='vertical')
        cb.label_text_property.font_family = 'arial'
        cb.label_text_property.bold = 0
        cb.label_text_property.font_size = 20

        self.scene_n.mlab.view(0, 0)



    @on_trait_change('searchButton.activated')
    def search(self):
        if self.search_click_yes >= 1:
            self.clear_figure()
        mlab.clf(mlab.colorbar)
        sf = float(self.saclefactor)

        searchstr = self.Search.upper()
        snum = 2 ** int(self.gnum)

        ngene1, ndata1 = getGeneData(self.cMatrix, searchstr)

        bar = mlab.barchart(self.data, figure=self.scene_n.mayavi_scene, scale_factor=sf)

        indexRange = len(ndata1[0])

        mlab.text3d(-float(self.ATGCPosition), snum, 0, 'G', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(snum, snum, 0, 'C', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(-float(self.ATGCPosition), -float(self.ATGCPosition), 0, 'A',
                    scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        mlab.text3d(snum, -float(self.ATGCPosition), 0, 'T', scale=(self.ATGCScale, self.ATGCScale, self.ATGCScale))
        for i in range(indexRange):
            for j in range(indexRange):
                if ndata1[i][j] == 5.0:
                    # bar = mlab.barchart(i, j, self.data[i][j], figure=self.scene_n.mayavi_scene, color=(1, 1, 1),
                    #                     #                     scale_factor=sf)

                    bar = mlab.barchart(i, j, self.data[i][j], figure=self.scene_n.mayavi_scene,color=(1,1,1),lateral_scale=0.8,
                                        scale_factor=sf)




        def picker_callback1(picker_obj):
            picked = picker_obj.actors

            x_, y_, z_ = picker_obj.pick_position
            x = int(round(x_))
            y = int(round(y_))

            self.GeneN = self.cMatrix[x][y]
            self.NumberOrPortion = str(self.data[x][y])
        if self.search_click_yes == 0:
            self.search_click_yes += 1
        self.scene_n.mayavi_scene.on_mouse_pick(picker_callback1, type="cell")
        cb = mlab.colorbar(orientation='vertical')
        cb.label_text_property.font_family = 'arial'
        cb.label_text_property.bold = 0
        cb.label_text_property.font_size = 20

        self.scene_n.mlab.view(0, 0)



    view = View(HGroup(
        Group(

            Item('scene_n',
                 editor=SceneEditor(scene_class=MayaviScene),
                 height=500, width=500),

            show_labels=False,
        ),
        Group(
            Group(Item(label='KaScape Analysis',height=100),show_border=False, style_sheet='*{font-size: 20px; font-family: arial}'),
            Group(
                Item(name='gnum', label='Random DNA Base Number',resizable=True,height=15, width=10),
                Group(
                Item(name='fix1', label='Left Fix Sequence'),
            Item(name='fix2', label='Right Fix Sequence'),orientation='horizontal'),show_border=True, style_sheet='*{font-size: 18px; font-family: arial}'),

            Group(Item(name='controlPathText', label='Input Raw Data Path', resizable=True),style_sheet='*{font-size: 18px; font-family: arial}'),

            Group(

                Item(name='kmerNoBackground', label='Raw Data Scape'),show_labels=False, style_sheet='*{font-size: 18px; font-family: arial}'),

            Group(Item(name='experimentPathText', label='Output Raw Data Path', resizable=True), style_sheet='*{font-size: 18px; font-family: arial}'),
            Group(

                Item(name='pcdiv', label='KaScape ( - relative binding energy)'),show_labels=False, style_sheet='*{font-size: 18px; font-family: arial}'
            ),

            Group(

                Group(
                    Item(name='GeneN', label='Point Sequence'),
                    Item(name='NumberOrPortion', label='Relative Signal'),orientation='horizontal'
                ),
                Group(Item(name='Search', label='Core Sequence'),
                      Item(name='searchButton', label='Search'), orientation='horizontal'),
                show_border=True, style_sheet='*{font-size: 18px; font-family: arial}'
            ),

            Group(
                Item(name='saclefactor', label='Zoom Scale'),
                Item(name='ATGCScale', label='ATGC Label Scale'),
                Item(name='ATGCPosition', label='ATGC Label Position'),
                orientation='horizontal', style_sheet='*{font-size: 18px; font-family: arial}'
            ),




            show_labels=True,
            show_border=True

        ),

    ),
        resizable=True,width=20,
        title='KGViewer'

    )




m1 = Gene()

m1.configure_traits()

