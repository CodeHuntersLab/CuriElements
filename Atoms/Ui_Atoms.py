# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atoms.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Atoms(object):
    def setupUi(self, Atoms):
        Atoms.setObjectName("Atoms")
        Atoms.setWindowModality(QtCore.Qt.ApplicationModal)
        Atoms.resize(268, 268)
        self.verticalLayout = QtWidgets.QVBoxLayout(Atoms)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(Atoms)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(Atoms)
        QtCore.QMetaObject.connectSlotsByName(Atoms)

    def retranslateUi(self, Atoms):
        _translate = QtCore.QCoreApplication.translate
        Atoms.setWindowTitle(_translate("Atoms", "Atoms"))

