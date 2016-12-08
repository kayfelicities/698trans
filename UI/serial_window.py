# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serial_window.ui'
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

class Ui_SerialWindow(object):
    def setupUi(self, SerialWindow):
        SerialWindow.setObjectName(_fromUtf8("SerialWindow"))
        SerialWindow.setWindowModality(QtCore.Qt.NonModal)
        SerialWindow.resize(848, 669)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/698/698.ico")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        SerialWindow.setWindowIcon(icon)
        SerialWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        SerialWindow.setAnimated(True)
        SerialWindow.setTabShape(QtGui.QTabWidget.Rounded)
        SerialWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(SerialWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.server_addr_box = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_addr_box.sizePolicy().hasHeightForWidth())
        self.server_addr_box.setSizePolicy(sizePolicy)
        self.server_addr_box.setObjectName(_fromUtf8("server_addr_box"))
        self.horizontalLayout.addWidget(self.server_addr_box)
        spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.server_addr_len_box = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_addr_len_box.sizePolicy().hasHeightForWidth())
        self.server_addr_len_box.setSizePolicy(sizePolicy)
        self.server_addr_len_box.setObjectName(_fromUtf8("server_addr_len_box"))
        self.horizontalLayout.addWidget(self.server_addr_len_box)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.client_addr_box = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.client_addr_box.sizePolicy().hasHeightForWidth())
        self.client_addr_box.setSizePolicy(sizePolicy)
        self.client_addr_box.setObjectName(_fromUtf8("client_addr_box"))
        self.horizontalLayout.addWidget(self.client_addr_box)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.com_list = QtGui.QComboBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.com_list.sizePolicy().hasHeightForWidth())
        self.com_list.setSizePolicy(sizePolicy)
        self.com_list.setObjectName(_fromUtf8("com_list"))
        self.horizontalLayout.addWidget(self.com_list)
        self.open_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setObjectName(_fromUtf8("open_button"))
        self.horizontalLayout.addWidget(self.open_button)
        self.close_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout.addWidget(self.close_button)
        spacerItem4 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.translate_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translate_button.sizePolicy().hasHeightForWidth())
        self.translate_button.setSizePolicy(sizePolicy)
        self.translate_button.setObjectName(_fromUtf8("translate_button"))
        self.horizontalLayout_3.addWidget(self.translate_button)
        self.send_clear_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_clear_button.sizePolicy().hasHeightForWidth())
        self.send_clear_button.setSizePolicy(sizePolicy)
        self.send_clear_button.setObjectName(_fromUtf8("send_clear_button"))
        self.horizontalLayout_3.addWidget(self.send_clear_button)
        self.send_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_button.sizePolicy().hasHeightForWidth())
        self.send_button.setSizePolicy(sizePolicy)
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.horizontalLayout_3.addWidget(self.send_button)
        spacerItem6 = QtGui.QSpacerItem(120, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.receive_clear_button = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receive_clear_button.sizePolicy().hasHeightForWidth())
        self.receive_clear_button.setSizePolicy(sizePolicy)
        self.receive_clear_button.setObjectName(_fromUtf8("receive_clear_button"))
        self.horizontalLayout_3.addWidget(self.receive_clear_button)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(3)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter = QtGui.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(3)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.send_input_box = QtGui.QTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.send_input_box.sizePolicy().hasHeightForWidth())
        self.send_input_box.setSizePolicy(sizePolicy)
        self.send_input_box.setAcceptDrops(False)
        self.send_input_box.setToolTip(_fromUtf8(""))
        self.send_input_box.setStatusTip(_fromUtf8(""))
        self.send_input_box.setWhatsThis(_fromUtf8(""))
        self.send_input_box.setAccessibleName(_fromUtf8(""))
        self.send_input_box.setAccessibleDescription(_fromUtf8(""))
        self.send_input_box.setAutoFillBackground(False)
        self.send_input_box.setStyleSheet(_fromUtf8(""))
        self.send_input_box.setFrameShape(QtGui.QFrame.NoFrame)
        self.send_input_box.setFrameShadow(QtGui.QFrame.Sunken)
        self.send_input_box.setMidLineWidth(1)
        self.send_input_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.send_input_box.setDocumentTitle(_fromUtf8(""))
        self.send_input_box.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.send_input_box.setOverwriteMode(False)
        self.send_input_box.setAcceptRichText(True)
        self.send_input_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.send_input_box.setObjectName(_fromUtf8("send_input_box"))
        self.send_output_box = QtGui.QTextEdit(self.splitter)
        self.send_output_box.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.send_output_box.sizePolicy().hasHeightForWidth())
        self.send_output_box.setSizePolicy(sizePolicy)
        self.send_output_box.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.send_output_box.setAcceptDrops(False)
        self.send_output_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.send_output_box.setAutoFillBackground(False)
        self.send_output_box.setObjectName(_fromUtf8("send_output_box"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setHandleWidth(3)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.receive_input_box = QtGui.QTextEdit(self.splitter_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.receive_input_box.sizePolicy().hasHeightForWidth())
        self.receive_input_box.setSizePolicy(sizePolicy)
        self.receive_input_box.setAcceptDrops(False)
        self.receive_input_box.setToolTip(_fromUtf8(""))
        self.receive_input_box.setStatusTip(_fromUtf8(""))
        self.receive_input_box.setWhatsThis(_fromUtf8(""))
        self.receive_input_box.setAccessibleName(_fromUtf8(""))
        self.receive_input_box.setAccessibleDescription(_fromUtf8(""))
        self.receive_input_box.setAutoFillBackground(False)
        self.receive_input_box.setStyleSheet(_fromUtf8(""))
        self.receive_input_box.setFrameShape(QtGui.QFrame.NoFrame)
        self.receive_input_box.setFrameShadow(QtGui.QFrame.Sunken)
        self.receive_input_box.setMidLineWidth(1)
        self.receive_input_box.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.receive_input_box.setDocumentTitle(_fromUtf8(""))
        self.receive_input_box.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.receive_input_box.setOverwriteMode(False)
        self.receive_input_box.setAcceptRichText(True)
        self.receive_input_box.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)
        self.receive_input_box.setObjectName(_fromUtf8("receive_input_box"))
        self.receive_output_box = QtGui.QTextEdit(self.splitter_2)
        self.receive_output_box.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.receive_output_box.sizePolicy().hasHeightForWidth())
        self.receive_output_box.setSizePolicy(sizePolicy)
        self.receive_output_box.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.receive_output_box.setAcceptDrops(False)
        self.receive_output_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.receive_output_box.setAutoFillBackground(False)
        self.receive_output_box.setObjectName(_fromUtf8("receive_output_box"))
        self.gridLayout.addWidget(self.splitter_3, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.trans_mode_button = QtGui.QPushButton(self.centralwidget)
        self.trans_mode_button.setObjectName(_fromUtf8("trans_mode_button"))
        self.horizontalLayout_2.addWidget(self.trans_mode_button)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.always_top = QtGui.QCheckBox(self.centralwidget)
        self.always_top.setObjectName(_fromUtf8("always_top"))
        self.horizontalLayout_2.addWidget(self.always_top)
        spacerItem9 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.auto_trans = QtGui.QCheckBox(self.centralwidget)
        self.auto_trans.setChecked(True)
        self.auto_trans.setObjectName(_fromUtf8("auto_trans"))
        self.horizontalLayout_2.addWidget(self.auto_trans)
        spacerItem10 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.show_level = QtGui.QCheckBox(self.centralwidget)
        self.show_level.setChecked(True)
        self.show_level.setObjectName(_fromUtf8("show_level"))
        self.horizontalLayout_2.addWidget(self.show_level)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.splitter_3.raise_()
        SerialWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SerialWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 247, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.menubar.setPalette(palette)
        self.menubar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        SerialWindow.setMenuBar(self.menubar)
        self.about = QtGui.QAction(SerialWindow)
        self.about.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.about.setObjectName(_fromUtf8("about"))
        self.menu.addAction(self.about)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(SerialWindow)
        QtCore.QObject.connect(self.send_clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_output_box.clear)
        QtCore.QObject.connect(self.send_clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.send_input_box.clear)
        QtCore.QObject.connect(self.receive_clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.receive_input_box.clear)
        QtCore.QObject.connect(self.receive_clear_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.receive_output_box.clear)
        QtCore.QMetaObject.connectSlotsByName(SerialWindow)
        SerialWindow.setTabOrder(self.send_input_box, self.send_clear_button)
        SerialWindow.setTabOrder(self.send_clear_button, self.com_list)
        SerialWindow.setTabOrder(self.com_list, self.send_output_box)
        SerialWindow.setTabOrder(self.send_output_box, self.always_top)
        SerialWindow.setTabOrder(self.always_top, self.show_level)
        SerialWindow.setTabOrder(self.show_level, self.open_button)
        SerialWindow.setTabOrder(self.open_button, self.close_button)
        SerialWindow.setTabOrder(self.close_button, self.send_button)
        SerialWindow.setTabOrder(self.send_button, self.receive_clear_button)
        SerialWindow.setTabOrder(self.receive_clear_button, self.receive_input_box)
        SerialWindow.setTabOrder(self.receive_input_box, self.receive_output_box)
        SerialWindow.setTabOrder(self.receive_output_box, self.auto_trans)
        SerialWindow.setTabOrder(self.auto_trans, self.server_addr_box)
        SerialWindow.setTabOrder(self.server_addr_box, self.server_addr_len_box)
        SerialWindow.setTabOrder(self.server_addr_len_box, self.client_addr_box)

    def retranslateUi(self, SerialWindow):
        SerialWindow.setWindowTitle(_translate("SerialWindow", "698解析工具_V3.0(2016.12.00)", None))
        self.label_2.setText(_translate("SerialWindow", "服务器地址", None))
        self.server_addr_box.setText(_translate("SerialWindow", "1", None))
        self.label_3.setText(_translate("SerialWindow", "地址长度", None))
        self.server_addr_len_box.setText(_translate("SerialWindow", "6", None))
        self.label_4.setText(_translate("SerialWindow", "客户机地址", None))
        self.client_addr_box.setText(_translate("SerialWindow", "10", None))
        self.label.setText(_translate("SerialWindow", "串口", None))
        self.open_button.setText(_translate("SerialWindow", "打开", None))
        self.close_button.setText(_translate("SerialWindow", "关闭", None))
        self.translate_button.setText(_translate("SerialWindow", "解析", None))
        self.send_clear_button.setText(_translate("SerialWindow", "清空", None))
        self.send_button.setText(_translate("SerialWindow", "请打开串口", None))
        self.receive_clear_button.setText(_translate("SerialWindow", "清空", None))
        self.send_input_box.setHtml(_translate("SerialWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.send_output_box.setHtml(_translate("SerialWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">说明：</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.请先选择与终端485连接的串口并按“打开”按钮，按钮将提示“已打开”。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.在输入框内输入698完整报文，服务器地址等信息将被提取至上方地址信息框中。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.在输入框内输入APDU片段，软件将根据上方地址信息框中的信息自动添加链路层报文，以方便报文的发送。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.取消勾选下方“自动解析”将看到“解析”按钮。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.“清空”按钮括号中显示的是输入框内报文的总长度，按此按钮将清空输入、输出框。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5.勾选下方“显示层级结构”可启用SEQUENCE、array、structure类型的缩进显示。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">6.勾选下方“窗口置顶”可保持本软件在其他窗口之上。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">7.按下下方“解析模式”按钮可返回解析模式。</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">8.本软件为终端开发部内部测试软件。在软件使用过程中遇到任何问题，请向665593反馈，谢谢。</p></body></html>", None))
        self.receive_input_box.setHtml(_translate("SerialWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.receive_output_box.setHtml(_translate("SerialWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.trans_mode_button.setText(_translate("SerialWindow", "解析模式", None))
        self.always_top.setText(_translate("SerialWindow", "窗口置顶", None))
        self.auto_trans.setText(_translate("SerialWindow", "自动解析", None))
        self.show_level.setText(_translate("SerialWindow", "显示层级结构", None))
        self.menu.setTitle(_translate("SerialWindow", "帮助", None))
        self.about.setText(_translate("SerialWindow", "关于", None))

import icon_rc
