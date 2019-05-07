# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Plotter(object):
    def setupUi(self, Plotter):
        Plotter.setObjectName(_fromUtf8("Plotter"))
        Plotter.resize(1024, 788)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Plotter.sizePolicy().hasHeightForWidth())
        Plotter.setSizePolicy(sizePolicy)
        Plotter.setMinimumSize(QtCore.QSize(1024, 768))
        Plotter.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtGui.QWidget(Plotter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 768))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.logButton = QtGui.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.logButton.setFont(font)
        self.logButton.setAutoExclusive(False)
        self.logButton.setObjectName(_fromUtf8("logButton"))
        self.verticalLayout_2.addWidget(self.logButton)
        self.filenameEdit = QtGui.QLineEdit(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameEdit.sizePolicy().hasHeightForWidth())
        self.filenameEdit.setSizePolicy(sizePolicy)
        self.filenameEdit.setMaximumSize(QtCore.QSize(220, 16777215))
        self.filenameEdit.setObjectName(_fromUtf8("filenameEdit"))
        self.verticalLayout_2.addWidget(self.filenameEdit)
        self.line_13 = QtGui.QFrame(self.verticalWidget)
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.verticalLayout_2.addWidget(self.line_13)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridWidget = QtGui.QWidget(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setMaximumSize(QtCore.QSize(220, 16777215))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.saveButton = QtGui.QPushButton(self.gridWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.gridLayout_3.addWidget(self.saveButton, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.gridWidget)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.horizontalLayout.addWidget(self.line_5)
        self.verticalWidget1 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget1.sizePolicy().hasHeightForWidth())
        self.verticalWidget1.setSizePolicy(sizePolicy)
        self.verticalWidget1.setMinimumSize(QtCore.QSize(512, 0))
        self.verticalWidget1.setObjectName(_fromUtf8("verticalWidget1"))
        self.PlotLayout = QtGui.QVBoxLayout(self.verticalWidget1)
        self.PlotLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.PlotLayout.setObjectName(_fromUtf8("PlotLayout"))
        self.PlotLayout_2 = QtGui.QVBoxLayout()
        self.PlotLayout_2.setObjectName(_fromUtf8("PlotLayout_2"))
        self.PlotLayout.addLayout(self.PlotLayout_2)
        self.horizontalLayout.addWidget(self.verticalWidget1)
        Plotter.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Plotter)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Plotter.setStatusBar(self.statusbar)

        self.retranslateUi(Plotter)
        QtCore.QMetaObject.connectSlotsByName(Plotter)

    def retranslateUi(self, Plotter):
        Plotter.setWindowTitle(_translate("Plotter", "Plotter", None))
        self.logButton.setText(_translate("Plotter", "Log Data", None))
        self.saveButton.setText(_translate("Plotter", "Save Plot To CSV", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Plotter = QtGui.QMainWindow()
    ui = Ui_Plotter()
    ui.setupUi(Plotter)
    Plotter.show()
    sys.exit(app.exec_())

