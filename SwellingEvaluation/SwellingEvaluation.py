import logging
import os

import vtk

import qt
import slicer
from slicer.ScriptedLoadableModule import *
from slicer.util import VTKObservationMixin


#
# SwellingEvaluation
#

class SwellingEvaluation(ScriptedLoadableModule):
    """Uses ScriptedLoadableModule base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "SwellingEvaluation"  # TODO: make this more human readable by adding spaces
        self.parent.categories = ["Wizards"]  # TODO: set categories (folders where the module shows up in the module selector)
        self.parent.dependencies = []  # TODO: add here list of module names that this module requires
        self.parent.contributors = ["Michela Destito (Magna Graecia University of Catanzaro (Italy))", "Selene Barone (Magna Graecia University of Catanzaro (Italy))", "Paolo Zaffino (Magna Graecia University of Catanzaro (Italy))", "Amerigo Giudice (Magna Graecia University of Catanzaro (Italy))", "Maria Francesca Spadea (Karlsruher Intitute of Technology (Germany))"]  # TODO: replace with "Firstname Lastname (Organization)"
        # TODO: update with short description of the module and a link to online module documentation
        self.parent.helpText = """
This is an example of scripted loadable module bundled in an extension.
See more information in <a href="https://github.com/organization/projectname#SwellingEvaluation">module documentation</a>.
"""
        # TODO: replace with organization, grant and thanks
        self.parent.acknowledgementText = ""
        # Additional initialization step after application startup is complete
        slicer.app.connect("startupCompleted()", registerSampleData)


#
# Register sample data sets in Sample Data module
#
 
def registerSampleData():
    """
    Add data sets to Sample Data module.
    """
    # It is always recommended to provide sample data for users to make it easy to try the module,
    # but if no sample data is available then this method (and associated startupCompeted signal connection) can be removed.

    import SampleData
    iconsPath = os.path.join(os.path.dirname(__file__), 'Resources/Icons')

    # To ensure that the source code repository remains small (can be downloaded and installed quickly)
    # it is recommended to store data sets that are larger than a few MB in a Github release.

    # SwellingEvaluation1
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        # Category and sample name displayed in Sample Data module
        category='SwellingEvaluation',
        sampleName='SwellingEvaluation1',
        # Thumbnail should have size of approximately 260x280 pixels and stored in Resources/Icons folder.
        # It can be created by Screen Capture module, "Capture all views" option enabled, "Number of images" set to "Single".
        thumbnailFileName=os.path.join(iconsPath, 'SwellingEvaluation1.png'),
        # Download URL and target file name
        uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95",
        fileNames='SwellingEvaluation1.nrrd',
        # Checksum to ensure file integrity. Can be computed by this command:
        #  import hashlib; print(hashlib.sha256(open(filename, "rb").read()).hexdigest())
        checksums='SHA256:998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95',
        # This node name will be used when the data set is loaded
        nodeNames='SwellingEvaluation1'
    )

    # SwellingEvaluation2
    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        # Category and sample name displayed in Sample Data module
        category='SwellingEvaluation',
        sampleName='SwellingEvaluation2',
        thumbnailFileName=os.path.join(iconsPath, 'SwellingEvaluation2.png'),
        # Download URL and target file name
        uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97",
        fileNames='SwellingEvaluation2.nrrd',
        checksums='SHA256:1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97',
        # This node name will be used when the data set is loaded
        nodeNames='SwellingEvaluation2'
    )


#
# SwellingEvaluationWidget
#

class SwellingEvaluationWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    """Uses ScriptedLoadableModuleWidget base class, available at:
    https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/ScriptedLoadableModule.py
    """
    
    def setup(self):
    	ScriptedLoadableModuleWidget.setup(self)

    # Instantiate and connect widgets ...

    	indexPath = self.resourcePath("HTML/SwellingEvaluation/index.html.txt")
    	url = qt.QUrl.fromLocalFile(indexPath)

    	modulesTextBrowser = qt.QTextBrowser()
    	modulesTextBrowser.setSource(url)
    	modulesTextBrowser.connect('anchorClicked(QUrl)', self.onAnchorClicked)

    	sp = qt.QSizePolicy()
    	sp.setVerticalPolicy(qt.QSizePolicy.Expanding)
    	sp.setHorizontalPolicy(qt.QSizePolicy.Expanding)
    	sp.setVerticalStretch(1)
    	sp.setHorizontalStretch(1)

    	modulesTextBrowser.setSizePolicy(sp)

    	self.modulesTextBrowser = modulesTextBrowser
    	self.layout.addWidget(self.modulesTextBrowser)
    def cleanup(self):
    	pass
    	
    def onAnchorClicked(self, url):
      moduleName = url.fragment()
      slicer.util.selectModule(moduleName)
      
    def resourcePath(self, filename):
    	scriptedModulesPath = os.path.dirname(slicer.util.modulePath(self.moduleName))
    	return os.path.join(scriptedModulesPath, 'Resources', filename)

