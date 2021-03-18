# This Python file uses the following encoding: utf-8
import sys
import os

from qtpy import QtWidgets

from qtpy.QtWidgets import QApplication
from qtpy.QtQml import qmlRegisterType
from qtpy.QtQuick import QQuickView
from qtpy.QtCore import QUrl

from InterpreterItem import InterpreterItem

if __name__ == "__main__":
  app = QApplication(sys.argv)
  # For C++, use qmlRegisterType<PyObject*>(....) from PySide2.h
  qmlRegisterType(InterpreterItem, "QmlInterpreter", 1, 0, "InterpreterItem")

  from ipythonwidget import IPythonWidget
  view = QQuickView(QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__),
                                                    "main.qml")))
  view.setResizeMode(QQuickView.SizeRootObjectToView)
  view.resize(500, 500)
  view.show()

  sys.exit(app.exec_())
