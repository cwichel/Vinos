# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget_ReadSave_2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_ReadSaveData(object):
    def setupUi(self, ReadSaveData):
        ReadSaveData.setObjectName(_fromUtf8("ReadSaveData"))
        ReadSaveData.resize(692, 378)
        ReadSaveData.setMinimumSize(QtCore.QSize(550, 350))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(ReadSaveData)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Tabs = QtGui.QTabWidget(ReadSaveData)
        self.Tabs.setMinimumSize(QtCore.QSize(450, 300))
        self.Tabs.setObjectName(_fromUtf8("Tabs"))
        self.Adquirir = QtGui.QWidget()
        self.Adquirir.setMinimumSize(QtCore.QSize(400, 300))
        self.Adquirir.setObjectName(_fromUtf8("Adquirir"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.Adquirir)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_estanque = QtGui.QLabel(self.Adquirir)
        self.label_estanque.setMinimumSize(QtCore.QSize(90, 30))
        self.label_estanque.setMaximumSize(QtCore.QSize(90, 30))
        self.label_estanque.setAlignment(QtCore.Qt.AlignCenter)
        self.label_estanque.setObjectName(_fromUtf8("label_estanque"))
        self.horizontalLayout_4.addWidget(self.label_estanque)
        self.linedit_estanquein = QtGui.QLineEdit(self.Adquirir)
        self.linedit_estanquein.setMinimumSize(QtCore.QSize(150, 30))
        self.linedit_estanquein.setMaximumSize(QtCore.QSize(350, 30))
        self.linedit_estanquein.setObjectName(_fromUtf8("linedit_estanquein"))
        self.horizontalLayout_4.addWidget(self.linedit_estanquein)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(self.Adquirir)
        self.label.setMinimumSize(QtCore.QSize(90, 30))
        self.label.setMaximumSize(QtCore.QSize(90, 30))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.boton_estado = QtGui.QPushButton(self.Adquirir)
        self.boton_estado.setMinimumSize(QtCore.QSize(150, 30))
        self.boton_estado.setMaximumSize(QtCore.QSize(350, 30))
        self.boton_estado.setObjectName(_fromUtf8("boton_estado"))
        self.horizontalLayout_6.addWidget(self.boton_estado)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.display_estanques = QtGui.QTextBrowser(self.Adquirir)
        self.display_estanques.setMinimumSize(QtCore.QSize(195, 90))
        self.display_estanques.setMaximumSize(QtCore.QSize(250, 150))
        self.display_estanques.setObjectName(_fromUtf8("display_estanques"))
        self.verticalLayout_3.addWidget(self.display_estanques)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.groupBox = QtGui.QGroupBox(self.Adquirir)
        self.groupBox.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.listview_read = QtGui.QListView(self.groupBox)
        self.listview_read.setMinimumSize(QtCore.QSize(220, 70))
        self.listview_read.setMaximumSize(QtCore.QSize(1500, 150))
        self.listview_read.setObjectName(_fromUtf8("listview_read"))
        self.verticalLayout_9.addWidget(self.listview_read, QtCore.Qt.AlignHCenter)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.boton_load = QtGui.QPushButton(self.groupBox)
        self.boton_load.setMinimumSize(QtCore.QSize(95, 60))
        self.boton_load.setMaximumSize(QtCore.QSize(95, 70))
        self.boton_load.setObjectName(_fromUtf8("boton_load"))
        self.verticalLayout_14.addWidget(self.boton_load, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_14)
        self.verticalLayout_12 = QtGui.QVBoxLayout()
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.boton_clearall = QtGui.QPushButton(self.groupBox)
        self.boton_clearall.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearall.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearall.setObjectName(_fromUtf8("boton_clearall"))
        self.verticalLayout_12.addWidget(self.boton_clearall, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.boton_clearselect = QtGui.QPushButton(self.groupBox)
        self.boton_clearselect.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearselect.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearselect.setObjectName(_fromUtf8("boton_clearselect"))
        self.verticalLayout_12.addWidget(self.boton_clearselect, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_13.addLayout(self.verticalLayout_7)
        self.horizontalLayout_8.addWidget(self.groupBox, QtCore.Qt.AlignHCenter)
        self.groupBox_2 = QtGui.QGroupBox(self.Adquirir)
        self.groupBox_2.setMinimumSize(QtCore.QSize(100, 200))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.listview_save = QtGui.QListView(self.groupBox_2)
        self.listview_save.setMinimumSize(QtCore.QSize(220, 70))
        self.listview_save.setMaximumSize(QtCore.QSize(1500, 150))
        self.listview_save.setObjectName(_fromUtf8("listview_save"))
        self.verticalLayout_15.addWidget(self.listview_save)
        self.verticalLayout_10.addLayout(self.verticalLayout_15)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.boton_selecttosave = QtGui.QPushButton(self.groupBox_2)
        self.boton_selecttosave.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_selecttosave.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_selecttosave.setObjectName(_fromUtf8("boton_selecttosave"))
        self.verticalLayout_20.addWidget(self.boton_selecttosave, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.boton_clearsave = QtGui.QPushButton(self.groupBox_2)
        self.boton_clearsave.setMinimumSize(QtCore.QSize(95, 25))
        self.boton_clearsave.setMaximumSize(QtCore.QSize(140, 30))
        self.boton_clearsave.setObjectName(_fromUtf8("boton_clearsave"))
        self.verticalLayout_20.addWidget(self.boton_clearsave, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_20)
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.boton_save = QtGui.QPushButton(self.groupBox_2)
        self.boton_save.setMinimumSize(QtCore.QSize(95, 60))
        self.boton_save.setMaximumSize(QtCore.QSize(95, 70))
        self.boton_save.setObjectName(_fromUtf8("boton_save"))
        self.verticalLayout_16.addWidget(self.boton_save, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_17.addLayout(self.verticalLayout_10)
        self.horizontalLayout_8.addWidget(self.groupBox_2, QtCore.Qt.AlignHCenter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_5.addLayout(self.verticalLayout_8)
        self.Tabs.addTab(self.Adquirir, _fromUtf8(""))
        self.Visualizar = QtGui.QWidget()
        self.Visualizar.setMinimumSize(QtCore.QSize(400, 300))
        self.Visualizar.setObjectName(_fromUtf8("Visualizar"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Visualizar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_comboboxplot = QtGui.QLabel(self.Visualizar)
        self.label_comboboxplot.setMinimumSize(QtCore.QSize(120, 25))
        self.label_comboboxplot.setMaximumSize(QtCore.QSize(100, 25))
        self.label_comboboxplot.setObjectName(_fromUtf8("label_comboboxplot"))
        self.horizontalLayout_5.addWidget(self.label_comboboxplot)
        self.combobox_plot = QtGui.QComboBox(self.Visualizar)
        self.combobox_plot.setMinimumSize(QtCore.QSize(340, 25))
        self.combobox_plot.setMaximumSize(QtCore.QSize(1000, 25))
        self.combobox_plot.setObjectName(_fromUtf8("combobox_plot"))
        self.horizontalLayout_5.addWidget(self.combobox_plot)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.label_3 = QtGui.QLabel(self.Visualizar)
        self.label_3.setMinimumSize(QtCore.QSize(250, 25))
        self.label_3.setMaximumSize(QtCore.QSize(400, 25))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_19.addWidget(self.label_3)
        self.graphics_view = QtGui.QGraphicsView(self.Visualizar)
        self.graphics_view.setMinimumSize(QtCore.QSize(450, 145))
        self.graphics_view.setObjectName(_fromUtf8("graphics_view"))
        self.verticalLayout_19.addWidget(self.graphics_view)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.verticalLayout.addLayout(self.verticalLayout_18)
        self.Tabs.addTab(self.Visualizar, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.Tabs)

        self.retranslateUi(ReadSaveData)
        self.Tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ReadSaveData)

    def retranslateUi(self, ReadSaveData):
        ReadSaveData.setWindowTitle(_translate("ReadSaveData", "Adquisición y Visualización Espectros", None))
        self.label_estanque.setText(_translate("ReadSaveData", "  N° Estanque \n"
" a Analizar", None))
        self.boton_estado.setText(_translate("ReadSaveData", "Verificar", None))
        self.groupBox.setTitle(_translate("ReadSaveData", "Espectrómetro", None))
        self.boton_load.setText(_translate("ReadSaveData", "Adquirir", None))
        self.boton_clearall.setText(_translate("ReadSaveData", "Clear All", None))
        self.boton_clearselect.setText(_translate("ReadSaveData", "Clear Select", None))
        self.groupBox_2.setTitle(_translate("ReadSaveData", "Base de Datos", None))
        self.boton_selecttosave.setText(_translate("ReadSaveData", "Seleccionar", None))
        self.boton_clearsave.setText(_translate("ReadSaveData", "Clear Select", None))
        self.boton_save.setText(_translate("ReadSaveData", "Guardar a\n"
" Base de Datos", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Adquirir), _translate("ReadSaveData", "Adquirir", None))
        self.label_comboboxplot.setText(_translate("ReadSaveData", "Espectros Adquiridos", None))
        self.label_3.setText(_translate("ReadSaveData", "TextLabel", None))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Visualizar), _translate("ReadSaveData", "Visualizar", None))

