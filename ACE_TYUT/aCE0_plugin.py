from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class ACE0_plugin(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='ICE_Main',
            objectName='test_class', registerQuery=False)
        pickedDefault = ''
        self.modelNameKw = AFXStringKeyword(self.cmd, 'modelName', True)
        self.partNameKw = AFXStringKeyword(self.cmd, 'partName', True)

        if not self.radioButtonGroups.has_key('CreatPart'):
            self.CreatPartKw1 = AFXIntKeyword(None, 'CreatPartDummy', True)
            self.CreatPartKw2 = AFXStringKeyword(self.cmd, 'CreatPart', True)
            self.radioButtonGroups['CreatPart'] = (self.CreatPartKw1, self.CreatPartKw2, {})
        self.radioButtonGroups['CreatPart'][2][11] = 'no'
        self.CreatPartKw1.setValue(11)

        if not self.radioButtonGroups.has_key('CreatPart'):
            self.CreatPartKw1 = AFXIntKeyword(None, 'CreatPartDummy', True)
            self.CreatPartKw2 = AFXStringKeyword(self.cmd, 'CreatPart', True)
            self.radioButtonGroups['CreatPart'] = (self.CreatPartKw1, self.CreatPartKw2, {})
        self.radioButtonGroups['CreatPart'][2][12] = 'yes'
        self.NewPartNameKw = AFXStringKeyword(self.cmd, 'NewPartName', True, '')

        if not self.radioButtonGroups.has_key('Addtype'):
            self.AddtypeKw1 = AFXIntKeyword(None, 'AddtypeDummy', True)
            self.AddtypeKw2 = AFXStringKeyword(self.cmd, 'Addtype', True)
            self.radioButtonGroups['Addtype'] = (self.AddtypeKw1, self.AddtypeKw2, {})

        self.radioButtonGroups['Addtype'][2][13] = 'ALL EleFace'
        self.AddtypeKw1.setValue(13)

        if not self.radioButtonGroups.has_key('Addtype'):
            self.AddtypeKw1 = AFXIntKeyword(None, 'AddtypeDummy', True)
            self.AddtypeKw2 = AFXStringKeyword(self.cmd, 'Addtype', True)
            self.radioButtonGroups['Addtype'] = (self.AddtypeKw1, self.AddtypeKw2, {})
        self.radioButtonGroups['Addtype'][2][14] = 'select'
        self.PickEleFaceKw = AFXObjectKeyword(self.cmd, 'PickEleFace', TRUE, pickedDefault)

        if not self.radioButtonGroups.has_key('Addtype'):
            self.AddtypeKw1 = AFXIntKeyword(None, 'AddtypeDummy', True)
            self.AddtypeKw2 = AFXStringKeyword(self.cmd, 'Addtype', True)
            self.radioButtonGroups['Addtype'] = (self.AddtypeKw1, self.AddtypeKw2, {})
        self.radioButtonGroups['Addtype'][2][15] = 'all geo face, form inp:'
        self.fileNameKw = AFXStringKeyword(self.cmd, 'fileName', True, '')

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import aCE0DB
        return aCE0DB.ACE0DB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Register the plug-in
#
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='ACE_TYUT',
    object=ACE0_plugin(toolset),
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    kernelInitString='import test_class',
    applicableModules=ALL,
    version='1.0',
    author='Gao Bolong,Zhu Defu-lib',
    description='The two-dimensional cohesive element parametric modeling program ,ACE_TYUT , is an Abaqus plugin program that has the basic function of adding cohesive elements to the entire model or some model edges. Based on this, it provides a more convenient and effective solution for complex and variable situations that require parametric modeling, as well as special situations where the Abaqus mesh partitioning effect is not satisfied and the model is imported into Abaqus after external mesh.',
    helpUrl='N/A'
)
