from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class ACE0DB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'ACE_TYUT',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        GroupBox_2 = FXGroupBox(p=self, text='object', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        frame = AFXVerticalAligner(GroupBox_2, 0, 0,0,0,0, 0,0,0,0)

        # Model combo
        # Since all forms will be canceled if the  model changes,
        # we do not need to register a query on the model.
        #
        self.RootComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Model:', tgt=form.modelNameKw, sel=0)
        self.RootComboBox_1.setMaxVisible(10)

        names = mdb.models.keys()
        names.sort()
        for name in names:
            self.RootComboBox_1.appendItem(name)
        if not form.modelNameKw.getValue() in names:
            form.modelNameKw.setValue( names[0] )

        msgCount = 4
        form.modelNameKw.setTarget(self)
        form.modelNameKw.setSelector(AFXDataDialog.ID_LAST+msgCount)
        msgHandler = str(self.__class__).split('.')[-1] + '.onComboBox_1PartsChanged'
        exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)' % (msgCount, msgHandler) )

        # Parts combo
        #
        self.ComboBox_1 = AFXComboBox(p=frame, ncols=0, nvis=1, text='Part:', tgt=form.partNameKw, sel=0)
        self.ComboBox_1.setMaxVisible(10)

        self.form = form
        #self.regModelName = None
        msgCount4 = 45
        form.partNameKw.setTarget(self)
        form.partNameKw.setSelector(AFXDataDialog.ID_LAST + msgCount4)
        #msgHandler4 = str(self.__class__).split('.')[-1] + '.onComboBox_2elesetChanged'
        #exec('FXMAPFUNC(self, SEL_COMMAND, AFXDataDialog.ID_LAST+%d, %s)'
             #% (msgCount4, msgHandler4))
        GroupBox_3 = FXGroupBox(p=self, text='create a new part?', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        FXRadioButton(p=GroupBox_3, text='no', tgt=form.CreatPartKw1, sel=11)
        HFrame_2 = FXHorizontalFrame(p=GroupBox_3, opts=0, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=HFrame_2, text='yes', tgt=form.CreatPartKw1, sel=12)
        self.TextField1 = AFXTextField(p=HFrame_2, ncols=12, labelText='new part name:', tgt=form.NewPartNameKw, sel=0)

        GroupBox_4 = FXGroupBox(p=self, text='add to...', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        FXRadioButton(p=GroupBox_4, text='ALL EleFace', tgt=form.AddtypeKw1, sel=13)
        HFrame_1 = FXHorizontalFrame(p=GroupBox_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=HFrame_1, text='select', tgt=form.AddtypeKw1, sel=14)
        pickHf = FXHorizontalFrame(p=HFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        pickHf.setSelector(99)
        label = FXLabel(p=pickHf, text='EleFaces' + ' (None)', ic=None, opts=LAYOUT_CENTER_Y|JUSTIFY_LEFT)
        pickHandler = ACE0DBPickHandler(form, form.PickEleFaceKw, 'Pick an entity', ELEMENT_EDGES, MANY, label)
        icon = afxGetIcon('select', AFX_ICON_SMALL )
        self.pickButton1 = FXButton(p=pickHf, text='\tPick Items in Viewport', ic=icon, tgt=pickHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=2, pr=2, pt=1, pb=1)
        VFrame_1 = FXVerticalFrame(p=GroupBox_4, opts=LAYOUT_FILL_X, x=0, y=0, w=0, h=0, pl=0, pr=0, pt=0, pb=0)
        FXRadioButton(p=VFrame_1, text='all geo face, form inp:', tgt=form.AddtypeKw1, sel=15)
        fileHandler = ACE0DBFileHandler(form, 'fileName', 'Abaqus Input File(*.inp)')
        fileTextHf = FXHorizontalFrame(p=VFrame_1, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        # Note: Set the selector to indicate that this widget should not be
        #       colored differently from its parent when the 'Color layout managers'
        #       button is checked in the RSG Dialog Builder dialog.
        fileTextHf.setSelector(99)
        self.TextField2 = AFXTextField(p=fileTextHf, ncols=12, labelText='File name:', tgt=form.fileNameKw, sel=0,
            opts=AFXTEXTFIELD_STRING|LAYOUT_CENTER_Y)
        icon = afxGetIcon('fileOpen', AFX_ICON_SMALL )
        self.pickButton2 = FXButton(p=fileTextHf, text='	Select File\nFrom Dialog', ic=icon, tgt=fileHandler, sel=AFXMode.ID_ACTIVATE,
            opts=BUTTON_NORMAL|LAYOUT_CENTER_Y, x=0, y=0, w=0, h=0, pl=1, pr=1, pt=1, pb=1)
        self.oldAddtype = 0
        self.oldCreatPart = 0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def show(self):

        AFXDataDialog.show(self)

        # Register a query on parts
        #
        self.currentModelName = getCurrentContext()['modelName']
        self.form.modelNameKw.setValue(self.currentModelName)
        #mdb.models[self.currentModelName].registerQuery(self.updateComboBox_1Models, False)
        #self.registerComboBox_1PartQuery(currentModelName)
        mdb.models[self.currentModelName].parts.registerQuery(self.updateComboBox_1Parts)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def hide(self):

        AFXDataDialog.hide(self)

        #self.registerComboBox_1PartQuery(None)
        #mdb.models.unregisterQuery(self.updateComboBox_1Models)
        mdb.models[self.currentModelName].parts.unregisterQuery(self.updateComboBox_1Parts)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def registerComboBox_1PartQuery(self, modelName):

        #if modelName == self.regModelName:
           #return

        #cbFunc = self.updateComboBox_1Parts
        #modelKeys = mdb.models.keys()
        #if self.regModelName in modelKeys:
           #mdb.models[self.regModelName].unregisterQuery(cbFunc)
        #self.regModelName = None

        #if modelName in modelKeys:
           #mdb.models[modelName].registerQuery(cbFunc, False)
           #self.regModelName = modelName
        modelName = self.form.modelNameKw.getValue()
        self.ComboBox_1.clearItems()
        names = mdb.models[modelName].parts.keys()
        names.sort()
        for name in names:
            self.ComboBox_1.appendItem(name)
        if names:
            if not self.form.partNameKw.getValue() in names:
                self.form.partNameKw.setValue(names[0])
        else:
            self.form.partNameKw.setValue('')

        self.resize(self.getDefaultWidth(), self.getDefaultHeight())

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def processUpdates(self):
        if self.oldCreatPart != self.form.CreatPartKw1.getValue():
            self.oldCreatPart = self.form.CreatPartKw1.getValue()
            if self.oldCreatPart == 12:
                self.TextField1.enable()
            else:
                self.TextField1.disable()
        if self.oldAddtype != self.form.AddtypeKw1.getValue():
            self.oldAddtype = self.form.AddtypeKw1.getValue()
            if self.oldAddtype == 14:
                self.pickButton1.enable()
                sendCommand('session.viewports[session.currentViewportName].partDisplay.setValues(mesh=ON)', False)
            else:
                self.pickButton1.disable()
            if self.oldAddtype == 15:
                self.TextField2.enable()
                self.pickButton2.enable()
                sendCommand('session.viewports[session.currentViewportName].partDisplay.setValues(mesh=OFF)', False)
            else:
                self.TextField2.disable()
                self.pickButton2.disable()

    def updateComboBox_1Models(self):

        # Update the names in the Models combo
        #
        self.RootComboBox_1.clearItems()
        names = mdb.models.keys()
        names.sort()
        for name in names:
           self.RootComboBox_1.appendItem(name)

        modelName = self.form.modelNameKw.getValue()
        if not modelName in names:
           modelName = names[0]
        self.form.modelNameKw.setValue(modelName) # Triggers parts combo update

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def onComboBox_1PartsChanged(self, sender, sel, ptr):

        self.updateComboBox_1Parts()
        return 1

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def updateComboBox_1Parts(self):

        # This is needed to handle lost registrations caused by model rename
        #if not self.regModelName:
           #return 1

        # Update the names in the Parts combo
        # 
        modelName = self.form.modelNameKw.getValue()

        self.ComboBox_1.clearItems()
        names = mdb.models[modelName].parts.keys()
        names.sort()
        for name in names:
            self.ComboBox_1.appendItem(name)
        if names:
            if not self.form.partNameKw.getValue() in names:
                self.form.partNameKw.setValue( names[0] )
        else:
            self.form.partNameKw.setValue('')

        self.resize( self.getDefaultWidth(), self.getDefaultHeight() )

        # Change parts container registration if the model has changed
        self.registerComboBox_1PartQuery(modelName)



###########################################################################
# Class definition
###########################################################################

class ACE0DBPickHandler(AFXProcedure):

        count = 0

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def __init__(self, form, keyword, prompt, entitiesToPick, numberToPick, label):

                self.form = form
                self.keyword = keyword
                self.prompt = prompt
                self.entitiesToPick = entitiesToPick # Enum value
                self.numberToPick = numberToPick # Enum value
                self.label = label
                self.labelText = label.getText()

                AFXProcedure.__init__(self, form.getOwner())

                ACE0DBPickHandler.count += 1
                self.setModeName('ACE0DBPickHandler%d' % (ACE0DBPickHandler.count) )

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getFirstStep(self):

                return  AFXPickStep(self, self.keyword, self.prompt, 
                    self.entitiesToPick, self.numberToPick, sequenceStyle=TUPLE)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def getNextStep(self, previousStep):

                self.label.setText( self.labelText.replace('None', 'Picked') )
                return None

        def deactivate(self):

            AFXProcedure.deactivate(self)
            if  self.numberToPick == ONE and self.keyword.getValue() and self.keyword.getValue()[0]!='<':
                sendCommand(self.keyword.getSetupCommands() + '\nhighlight(%s)' % self.keyword.getValue() )



###########################################################################
# Class definition
###########################################################################

class ACE0DBFileHandler(FXObject):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form, keyword, patterns='*'):

        self.form = form
        self.patterns = patterns
        self.patternTgt = AFXIntTarget(0)
        exec('self.fileNameKw = form.%sKw' % keyword)
        self.readOnlyKw = AFXBoolKeyword(None, 'readOnly', AFXBoolKeyword.TRUE_FALSE)
        FXObject.__init__(self)
        FXMAPFUNC(self, SEL_COMMAND, AFXMode.ID_ACTIVATE, ACE0DBFileHandler.activate)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def activate(self, sender, sel, ptr):

       fileDb = AFXFileSelectorDialog(getAFXApp().getAFXMainWindow(), 'Select a File',
           self.fileNameKw, self.readOnlyKw,
           AFXSELECTFILE_ANY, self.patterns, self.patternTgt)
       fileDb.setReadOnlyPatterns('*.odb')
       fileDb.create()
       fileDb.showModal()
