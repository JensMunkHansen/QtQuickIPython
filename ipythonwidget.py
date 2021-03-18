import sip

from PyQt5 import QtCore
from PyQt5 import sip

sip.setapi(u'QDate', 2)
sip.setapi(u'QDateTime', 2)
sip.setapi(u'QString', 2)
sip.setapi(u'QTextStream', 2)
sip.setapi(u'QTime', 2)
sip.setapi(u'QUrl', 2)
sip.setapi(u'QVariant', 2)

from IPython.lib import guisupport

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager

from qtpy.QtWidgets import QStyleOption, QStyle
from qtpy.QtGui import QPainter

from qtpy import QtCore
import qtpy.QtCore
from qtpy.QtCore import Qt

class IPythonWidget(RichJupyterWidget):
  def __init__(self, customBanner=None, displayBanner=True, *args, **kwargs):
    if customBanner is not None:
      self.banner=customBanner
    super(IPythonWidget, self).__init__(*args,**kwargs)
    super(IPythonWidget, self).setAttribute(Qt.WA_StyledBackground, True)

    # To write to the input: jupyter_widget.input_buffer = 'text'
    self.kernel_manager = kernel_manager = QtInProcessKernelManager()
    if not(displayBanner):
      self._display_banner = False

    kernel_manager.start_kernel()
    kernel_manager.kernel.gui = 'qt4' # Ignored
    self.kernel_client = kernel_client = self._kernel_manager.client()
    kernel_client.start_channels()

    def stop():
      kernel_client.stop_channels()
      kernel_manager.shutdown_kernel()
      guisupport.get_app_qt4().exit()
    self.exit_requested.connect(stop)
    self.setAttribute(QtCore.Qt.WA_StyledBackground, True)

  def pushVariables(self, variableDict):
    """ Given a dictionary containing name / value pairs, push those variables to the IPython console widget """
    self.kernel_manager.kernel.shell.push(variableDict)

  def clearTerminal(self):
    """ Clears the terminal """
    self._control.clear()

  def printText(self,text):
    """ Prints some plain text to the console """
    self.append_stream(text)

  def executeCommand(self, command):
    """ Execute a command in the frame of the console widget """
    self.execute(command, False)

# Local variables: #
# tab-width: 2 #
# python-indent: 2 #
# indent-tabs-mode: nil #
# End: #
