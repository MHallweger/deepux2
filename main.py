import os
import sys
import tkinter
from tkinter import filedialog
import cv2
from pathlib import Path
from threading import Thread

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PySide2.QtGui import QIcon, QFont, Qt, QPixmap, QMovie
from PySide2.QtWidgets import QLabel, QPushButton, QWidget, QFrame, QStatusBar, QSizePolicy, QAction, QProgressBar, \
    QMenuBar, QMenu, QMessageBox, QHBoxLayout, QCheckBox, QLineEdit

from PySide2.QtCore import *
from PySide2.QtGui import *

from GUIGAN_main import build_result_uis
import build_generator
from deepux1_metrics import metrics_check
from application.parser.main import parse_li_to_json
from get_style_emb import get_style_embeddings
from application.modelGenerator.load_data import load_data
from application.modelGenerator.load_subtrees import load_subtrees
from application.modelGenerator.train_siamese_net import train_siamese
from application.subtreeGenerator.save_subtree_info import save_subtree_info

# Console
import fire

from xml.dom import minidom

json_rico = r'.\folders\Rico\jsons'
gui_dir_rico = r'.\folders\Rico\gui'
gui_information_dir = r'.\folders\gui_informations'
control_elements_id_dir = r'.\folders\gui_control_elements'
cutted_ui_elements = r'.\folders\cutted_ui_elements'
cutted_resized_ui_elements = r'.\folders\cutted_resized_ui_elements'
data_dir = r'.\folders\data'
models_torch_dir = r'.\folders\models_torch_dir'
app_details_csv = r'.\folders\app_details.csv'
categories_app_emb = r'.\folders\categories_app_emb'
models_dir = r'.\folders\models'
results_dir = r'.\folders\results'
results_pre_dir = r'.\folders\results_pre'
li_files = r'.\folders\li_files'

# UI
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setFixedSize(1143, 710)
        mainWindow.setMouseTracking(False)
        mainWindow.setWindowIcon(QIcon(u"resources/images/bulb.png"))

        # Widgets
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        mainWindow.setCentralWidget(self.centralwidget)

        # Status Bar
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        # Fonts
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(29)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(50)
        font1.setKerning(True)

        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)

        # Labels
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 10, 271, 451))
        self.label_1.setStyleSheet(u"")
        self.label_1.setPixmap(QPixmap(u"resources/images/Standard_1.png"))
        self.label_1.setScaledContents(True)
        self.label_1.raise_()

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 10, 271, 451))
        self.label_2.setStyleSheet(u"")
        self.label_2.raise_()
        self.label_2.setPixmap(QPixmap(u"resources/images/Standard_2.png"))
        self.label_2.setScaledContents(True)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 10, 271, 451))
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u"resources/images/Standard_3.png"))
        self.label_3.setScaledContents(True)
        self.label_3.raise_()

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(850, 10, 271, 451))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u"resources/images/Standard_4.png"))
        self.label_4.setScaledContents(True)
        self.label_4.raise_()

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 490, 1111, 131))
        self.label_5.setFont(font)
        self.label_5.setFocusPolicy(Qt.NoFocus)
        self.label_5.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.raise_()

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(22, 490, 101, 31))
        self.label_6.setFont(font1)
        self.label_6.setFocusPolicy(Qt.NoFocus)
        self.label_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.raise_()

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(532, 490, 191, 31))
        self.label_7.setFont(font2)
        self.label_7.setFocusPolicy(Qt.NoFocus)
        self.label_7.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.raise_()

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setGeometry(QRect(115, 180, 271, 200))
        self.label_8.hide()
        self.label_8.raise_()

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setGeometry(QRect(395, 180, 271, 200))
        self.label_9.hide()
        self.label_9.raise_()

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setGeometry(QRect(675, 180, 271, 200))
        self.label_10.hide()
        self.label_10.raise_()

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setGeometry(QRect(955, 180, 271, 200))
        self.label_11.hide()
        self.label_11.raise_()

        # Icons
        icon = QIcon()
        icon.addFile(u"resources/images/information-button.png", QSize(), QIcon.Normal, QIcon.Off)

        # Gifs
        self.movie = QMovie(u"resources/images/loading.gif")
        self.label_8.setMovie(self.movie)
        self.label_9.setMovie(self.movie)
        self.label_10.setMovie(self.movie)
        self.label_11.setMovie(self.movie)
        self.movie.start()

        # Label-Icons
        self.label_icon_1 = QLabel(self.centralwidget)
        self.label_icon_1.setObjectName(u"label_icon_1")
        self.label_icon_1.setGeometry(QRect(100,493,25,25))
        self.label_icon_1.setStyleSheet(u"")
        self.label_icon_1.setPixmap(QPixmap(u"resources/images/gear.png"))
        self.label_icon_1.setScaledContents(True)
        self.label_icon_1.raise_()

        self.label_icon_2 = QLabel(self.centralwidget)
        self.label_icon_2.setObjectName(u"label_icon_2")
        self.label_icon_2.setGeometry(QRect(705,493,25,25))
        self.label_icon_2.setStyleSheet(u"")
        self.label_icon_2.setPixmap(QPixmap(u"resources/images/folder.png"))
        self.label_icon_2.setScaledContents(True)
        self.label_icon_2.raise_()

        # Buttons
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 535, 131, 51))
        self.pushButton_1.raise_()

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 535, 131, 51))
        self.pushButton_2.raise_()

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 535, 131, 51))
        self.pushButton_3.raise_()

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 610, 131, 51))
        self.pushButton_4.raise_()

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(180, 610, 131, 51))
        self.pushButton_5.raise_()

        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 610, 131, 51))
        self.pushButton_6.raise_()

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(532, 535, 151, 51))
        self.pushButton_7.setToolTipDuration(3)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.pushButton_7.raise_()

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(532, 610, 151, 51))
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton_8.raise_()

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(700, 535, 151, 51))
        self.pushButton_9.setIconSize(QSize(25, 25))
        self.pushButton_9.raise_()

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(700, 610, 151, 51))
        self.pushButton_10.setIconSize(QSize(25, 25))
        self.pushButton_10.raise_()

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(980, 490, 75, 25)
        self.pushButton_11.raise_()

        # Input-fields
        self.if1 = QLineEdit(self.centralwidget)
        self.if1.setMaxLength(3)
        self.if1.setPlaceholderText("Accuracy (metrics)")
        self.if1.setGeometry(875, 490, 100, 25)

        # Checkbox
        self.cb1 = QCheckBox("distinct_rgb_values", self.centralwidget)
        self.cb1.setGeometry(QRect(875, 517, 151, 25))
        self.cb1.stateChanged.connect(lambda:checkbox_check(self.cb1))
        self.cb1.setChecked(True)
        self.cb1.raise_()

        self.cb2 = QCheckBox("figure_ground_contrast", self.centralwidget)
        self.cb2.setGeometry(QRect(1000, 517, 151, 25))
        self.cb2.stateChanged.connect(lambda:checkbox_check(self.cb2))
        self.cb2.setChecked(True)
        self.cb2.raise_()

        self.cb3 = QCheckBox("white_space", self.centralwidget)
        self.cb3.setGeometry(QRect(875, 535, 151, 25))
        self.cb3.stateChanged.connect(lambda:checkbox_check(self.cb3))
        self.cb3.setChecked(True)
        self.cb3.raise_()

        self.cb4 = QCheckBox("grid_quality", self.centralwidget)
        self.cb4.setGeometry(QRect(1000, 535, 151, 25))
        self.cb4.stateChanged.connect(lambda:checkbox_check(self.cb4))
        self.cb4.setChecked(True)
        self.cb4.raise_()

        self.cb5 = QCheckBox("colourfulness", self.centralwidget)
        self.cb5.setGeometry(QRect(875, 553, 151, 25))
        self.cb5.stateChanged.connect(lambda:checkbox_check(self.cb5))
        self.cb5.setChecked(True)
        self.cb5.raise_()

        self.cb6 = QCheckBox("hsv_colours", self.centralwidget)
        self.cb6.setGeometry(QRect(1000, 553, 151, 25))
        self.cb6.stateChanged.connect(lambda:checkbox_check(self.cb6))
        self.cb6.setChecked(True)
        self.cb6.raise_()

        self.cb7 = QCheckBox("hsv_unique", self.centralwidget)
        self.cb7.setGeometry(QRect(875, 571, 151, 25))
        self.cb7.stateChanged.connect(lambda:checkbox_check(self.cb7))
        self.cb7.setChecked(True)
        self.cb7.raise_()

        self.cb8 = QCheckBox("lab_avg", self.centralwidget)
        self.cb8.setGeometry(QRect(1000, 571, 151, 25))
        self.cb8.stateChanged.connect(lambda:checkbox_check(self.cb8))
        self.cb8.setChecked(True)
        self.cb8.raise_()

        self.cb9 = QCheckBox("static_colour_clusters", self.centralwidget)
        self.cb9.setGeometry(QRect(875, 589, 151, 25))
        self.cb9.stateChanged.connect(lambda:checkbox_check(self.cb9))
        self.cb9.setChecked(True)
        self.cb9.raise_()

        self.cb10 = QCheckBox("dynamic_colour_clusters", self.centralwidget)
        self.cb10.setGeometry(QRect(1000, 589, 151, 25))
        self.cb10.stateChanged.connect(lambda:checkbox_check(self.cb10))
        self.cb10.setChecked(True)
        self.cb10.raise_()

        self.cb11 = QCheckBox("luminance_sd", self.centralwidget)
        self.cb11.setGeometry(QRect(875, 607, 151, 25))
        self.cb11.stateChanged.connect(lambda:checkbox_check(self.cb11))
        self.cb11.setChecked(True)
        self.cb11.raise_()

        self.cb12 = QCheckBox("wave", self.centralwidget)
        self.cb12.setGeometry(QRect(1000, 607, 151, 25))
        self.cb12.stateChanged.connect(lambda:checkbox_check(self.cb12))
        self.cb12.setChecked(True)
        self.cb12.raise_()

        self.cb13 = QCheckBox("contour_density", self.centralwidget)
        self.cb13.setGeometry(QRect(875, 625, 151, 25))
        self.cb13.stateChanged.connect(lambda:checkbox_check(self.cb13))
        self.cb13.setChecked(True)
        self.cb13.raise_()

        self.cb14 = QCheckBox("contour_congestion", self.centralwidget)
        self.cb14.setGeometry(QRect(1000, 625, 151, 25))
        self.cb14.stateChanged.connect(lambda:checkbox_check(self.cb14))
        self.cb14.setChecked(True)
        self.cb14.raise_()

        self.cb15 = QCheckBox("pixel_symmetry", self.centralwidget)
        self.cb15.setGeometry(QRect(875, 643, 151, 25))
        self.cb15.stateChanged.connect(lambda:checkbox_check(self.cb15))
        self.cb15.setChecked(True)
        self.cb15.raise_()

        self.cb16 = QCheckBox("quadtree_decomposition", self.centralwidget)
        self.cb16.setGeometry(QRect(1000, 643, 151, 25))
        self.cb16.stateChanged.connect(lambda:checkbox_check(self.cb16))
        self.cb16.setChecked(True)
        self.cb16.raise_()

        # Button Actions
        self.pushButton_1.clicked.connect(save_subtree)  # Cut UI's
        self.pushButton_2.clicked.connect(load_data_for_model)  # Load UI Data
        self.pushButton_3.clicked.connect(generateModel)  # Generate Model
        self.pushButton_4.clicked.connect(generate_categories)  # Generate Categories
        self.pushButton_5.clicked.connect(generate_generators)  # Generate Generators
        self.pushButton_6.clicked.connect(generate_uis)  # Generate UI Suggestions
        self.pushButton_7.clicked.connect(edit_data)  # Open the project folder to edit the existing data
        self.pushButton_8.clicked.connect(calc_with_metrics)  # Start metric calculation
        self.pushButton_9.clicked.connect(open_parser_window)  # Start open_parser_window
        self.pushButton_10.clicked.connect(cancel_calc_with_metrics)  # Start calc_with_metrics
        self.pushButton_11.clicked.connect(lambda: metrics_ok(self.if1))  # Save new metrics Accuracy

        # Actions
        self.action_ueber = QAction(mainWindow)
        self.action_ueber.setObjectName(u"action_ueber")
        self.action_ueber.triggered.connect(about)
        self.action_ueber.setIcon(icon)

        # Lines
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 465, 1181, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.raise_()

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(501, 472, 20, 311))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.raise_()

        # MenuBar
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1143, 21))
        self.menuhILFE = QMenu(self.menubar)
        self.menuhILFE.setObjectName(u"menuhILFE")
        mainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuhILFE.menuAction())
        self.menuhILFE.addAction(self.action_ueber)

        # Size Policy
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)

        self.retranslateUi(mainWindow)
        QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.menuhILFE.setTitle(QCoreApplication.translate("mainWindow", u"More", None))

        # Label
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("mainWindow", u"", None))
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Actions", None))
        self.label_7.setText(QCoreApplication.translate("mainWindow", u"Individualization", None))

        self.label_1.setStatusTip("Suggestion 1")
        self.label_2.setStatusTip("Suggestion 2")
        self.label_3.setStatusTip("Suggestion 3")
        self.label_4.setStatusTip("Suggestion 4")

        # Action
        self.action_ueber.setText(QCoreApplication.translate("mainWindow", u"About", None))

        # Buttons
        self.pushButton_1.setText(QCoreApplication.translate("mainWindow", u"Cut UI's", None))
        self.pushButton_2.setText(QCoreApplication.translate("mainWindow", u"Load UI Data", None))
        self.pushButton_3.setText(QCoreApplication.translate("mainWindow", u"Generate Model", None))
        self.pushButton_4.setText(QCoreApplication.translate("mainWindow", u"Generate Categories", None))
        self.pushButton_5.setText(QCoreApplication.translate("mainWindow", u"Generate Generators", None))
        self.pushButton_6.setText(QCoreApplication.translate("mainWindow", u"Generate UI Suggestions", None))
        self.pushButton_7.setText(QCoreApplication.translate("mainWindow", u"Edit Program-Data", None))
        self.pushButton_8.setText(QCoreApplication.translate("mainWindow", u"Calculate Metrics", None))
        self.pushButton_9.setText(QCoreApplication.translate("mainWindow", u"*.li Parser", None))
        self.pushButton_10.setText(QCoreApplication.translate("mainWindow", u"Cancel Metric-Calculation", None))
        self.pushButton_11.setText(QCoreApplication.translate("mainWindow", u"Save", None))

        self.pushButton_1.setStatusTip("Cut the existing Screenshots into a specified substructure")
        self.pushButton_2.setStatusTip("Prepare the cutted user interface elements for the neural network")
        self.pushButton_3.setStatusTip("Train models with the help of the siamese network")
        self.pushButton_4.setStatusTip("Generate pairs (using the model) from the individual cropped user interface elements and categorize them")
        self.pushButton_5.setStatusTip("Generate GAN-Generator")
        self.pushButton_6.setStatusTip("Create new inspiring user interfaces with the help of the generator")
        self.pushButton_7.setStatusTip("Open the project folder to adjust the basic image structure")
        self.pushButton_8.setStatusTip("Check the generated images with chosen metrics")
        self.pushButton_9.setStatusTip("Select a .li file and parse it into a .json file")
        self.pushButton_10.setStatusTip("Cancel Metric-Calculation")
        self.pushButton_11.setStatusTip("Save new metrics Accuracy")

        self.if1.setStatusTip("Insert a new Accuracy-value for future metric calculations")

def save_subtree():
    print("Cut UI's Button clicked!")
    save_subtree_info(json_rico, gui_dir_rico, gui_information_dir, control_elements_id_dir, cutted_ui_elements, cutted_resized_ui_elements)

def load_data_for_model():
    print("Load UI Data Button clicked!")
    load_data(cutted_resized_ui_elements,data_dir)
    load_subtrees(cutted_resized_ui_elements,data_dir)

def generateModel():
    print("Generate Model Button clicked!")
    train_siamese(cutted_resized_ui_elements,data_dir,models_torch_dir)

def generate_generators():
    print("Generate Generators Button clicked!")
    build_generator.build_generator(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,cutted_ui_elements,cutted_resized_ui_elements)

def generate_uis():
    print("Generate UI Suggestions Button clicked!")
    build_result_uis(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,results_dir,results_pre_dir,cutted_ui_elements,cutted_resized_ui_elements)

def generate_categories():
    print("Generate Categories Button clicked!")
    get_style_embeddings(models_torch_dir, app_details_csv, categories_app_emb, cutted_ui_elements, cutted_resized_ui_elements)

# Create a "about" Message-Box
def about():
    widget = QWidget()
    widget.setWindowIcon(QIcon(u"resources/images/bulb.png"))
    QMessageBox.about(
        widget,
        "About this Tool",
        "<p>This tool was developed by a so-called Guided Project in the context of the computer science master of the TH Cologne Campus Gummersbach.</p>"
        "<p><h3><u>The tool was developed by:</h3></u></p>"
        "<p><b>Muhammet Burhan Topcu</b> <br>muhammet_burhan.topcu@smail.th-koeln.de</p>"
        "<p><b>Marvin Nicholas Hallweger</b> <br>marvin_nicholas.hallweger@smail.th-koeln.de</p>"
        "<p><h3><u>And supported by:</h3></u></p>"
        "<p><b>Prof. Dr. Matthias Böhmer</b> <br>matthias.boehmer@th-koeln.de</p>"
        "<p><b>David Petersen</b> <br>david.petersen@th-koeln.de</p>",
    )

# Check checkbox-state
def checkbox_check(cb):
    if cb.text() == "distinct_rgb_values":
        if cb.isChecked() == True:
            metrics_check.distinct_rgb_values = True
        else:
            metrics_check.distinct_rgb_values = False
    elif cb.text() == "figure_ground_contrast":
        if cb.isChecked() == True:
            metrics_check.figure_ground_contrast = True
        else:
            metrics_check.figure_ground_contrast = False
    elif cb.text() == "white_space":
        if cb.isChecked() == True:
            metrics_check.white_space = True
        else:
            metrics_check.white_space = False
    elif cb.text() == "grid_quality":
        if cb.isChecked() == True:
            metrics_check.grid_quality = True
        else:
            metrics_check.grid_quality = False
    elif cb.text() == "colourfulness":
        if cb.isChecked() == True:
            metrics_check.colourfulness = True
        else:
            metrics_check.colourfulness = False
    elif cb.text() == "hsv_colours":
        if cb.isChecked() == True:
            metrics_check.hsv_colours = True
        else:
            metrics_check.hsv_colours = False
    elif cb.text() == "hsv_unique":
        if cb.isChecked() == True:
            metrics_check.hsv_unique = True
        else:
            metrics_check.hsv_unique = False
    elif cb.text() == "lab_avg":
        if cb.isChecked() == True:
            metrics_check.lab_avg = True
        else:
            metrics_check.lab_avg = False
    elif cb.text() == "static_colour_clusters":
        if cb.isChecked() == True:
            metrics_check.static_colour_clusters = True
        else:
            metrics_check.static_colour_clusters = False
    elif cb.text() == "dynamic_colour_clusters":
        if cb.isChecked() == True:
            metrics_check.dynamic_colour_clusters = True
        else:
            metrics_check.dynamic_colour_clusters = False
    elif cb.text() == "luminance_sd":
        if cb.isChecked() == True:
            metrics_check.luminance_sd = True
        else:
            metrics_check.luminance_sd = False
    elif cb.text() == "wave":
        if cb.isChecked() == True:
            metrics_check.wave = True
        else:
            metrics_check.wave = False
    elif cb.text() == "contour_density":
        if cb.isChecked() == True:
            metrics_check.contour_density = True
        else:
            metrics_check.contour_density = False
    elif cb.text() == "contour_congestion":
        if cb.isChecked() == True:
            metrics_check.contour_congestion = True
        else:
            metrics_check.contour_congestion = False
    elif cb.text() == "pixel_symmetry":
        if cb.isChecked() == True:
            metrics_check.pixel_symmetry = True
        else:
            metrics_check.pixel_symmetry = False
    elif cb.text() == "quadtree_decomposition":
        if cb.isChecked() == True:
            metrics_check.quadtree_decomposition = True
        else:
            metrics_check.quadtree_decomposition = False


# Open the project folder to edit the existing data
def edit_data():
    path = r".\folders"
    path = os.path.realpath(path)
    os.startfile(path)

def open_parser_window():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if file_path != "":
        parse_li_to_json(file_path)
        print(file_path)

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

uiObj = ""
MainWindowObj = ""
thread = ""
def threaded_function(arg):
    positionOnLayout = 0
    first_start_check_metrics = True
    for i in range(arg):
        print("Calculate metrics...")
        root_dir = r".\folders\results"

        results = list(Path(root_dir).rglob("**/*.jpg"))
        for result in results:

            if(positionOnLayout > 3):
                positionOnLayout = 0

            print("")
            print(str("Next image: ") + str(result))
            from deepux1_metrics import metrics_check
            pathtest = "..\\..\\..\\" + str(result)

            if (positionOnLayout == 0):
                uiObj.label_8.show()
            elif (positionOnLayout == 1):
                uiObj.label_9.show()
            elif (positionOnLayout == 2):
                uiObj.label_10.show()
            elif (positionOnLayout == 3):
                uiObj.label_11.show()

            evaluation_percentage = metrics_check.check_metrics(pathtest, first_start_check_metrics)
            first_start_check_metrics = False


            if (evaluation_percentage > metrics_check.Accuracy):
                print("Add image to ui...")
                if (positionOnLayout == 0):
                    uiObj.label_1.setPixmap(QPixmap(str(pathtest)))
                    uiObj.label_8.hide()
                elif (positionOnLayout == 1):
                    uiObj.label_2.setPixmap(QPixmap(str(pathtest)))
                    uiObj.label_9.hide()
                elif (positionOnLayout == 2):
                    uiObj.label_3.setPixmap(QPixmap(str(pathtest)))
                    uiObj.label_10.hide()
                elif (positionOnLayout == 3):
                    uiObj.label_4.setPixmap(QPixmap(str(pathtest)))
                    uiObj.label_11.hide()

                print("Position on Layout 1" + str(positionOnLayout))
                positionOnLayout = positionOnLayout + 1
                print("Position on Layout 2" + str(positionOnLayout))

def calc_with_metrics():
    thread = Thread(target=threaded_function, args=(10,))
    thread.start()

def cancel_calc_with_metrics():
    # TODO: Cancel Thread
    print("TODO: Implement a way to cancel thread")

# Save new metrics-value
def metrics_ok(if1):
    print("Old Accuracy: " + str(metrics_check.Accuracy))
    metrics_check.Accuracy = int(if1.text())
    print("Accuracy changed! New Accuracy: " + str(metrics_check.Accuracy))

if __name__ == '__main__':
    # Console-call
    # Call: python main.py [function]
    fire.Fire(Ui_mainWindow)

    if not os.path.exists(json_rico):
        os.makedirs(json_rico)

    if not os.path.exists(gui_dir_rico):
        os.makedirs(gui_dir_rico)

    if not os.path.exists(gui_information_dir):
        os.makedirs(gui_information_dir)

    if not os.path.exists(control_elements_id_dir):
        os.makedirs(control_elements_id_dir)

    if not os.path.exists(cutted_ui_elements):
        os.makedirs(cutted_ui_elements)

    if not os.path.exists(cutted_resized_ui_elements):
        os.makedirs(cutted_resized_ui_elements)

    if not os.path.exists(categories_app_emb):
        os.makedirs(categories_app_emb)

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    if not os.path.exists(results_pre_dir):
        os.makedirs(results_pre_dir)

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if not os.path.exists(models_torch_dir):
        os.makedirs(models_torch_dir)

    if not os.path.exists(li_files):
        os.makedirs(li_files)

    # Build UI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindowObj = MainWindow
    MainWindow.show()
    uiObj = ui
    sys.exit(app.exec_())
