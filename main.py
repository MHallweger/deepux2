import os
import sys
import tkinter
from tkinter import filedialog
from turtle import fd
import cv2
import glob
from PIL import Image
from pathlib import Path
from threading import Thread
from time import sleep

from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PySide2.QtGui import QIcon, QFont, Qt, QPixmap, QMovie
from PySide2.QtWidgets import QLabel, QPushButton, QWidget, QFrame, QStatusBar, QSizePolicy, QAction, QProgressBar, \
    QMenuBar, QMenu, QMessageBox, QHBoxLayout, QCheckBox

from GUIGAN_main import build_result_uis
import build_generator
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
        self.label_1.setPixmap(QPixmap(u"resources/images/Screenshot_1624995967.png"))
        self.label_1.setScaledContents(True)
        self.label_1.raise_()
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 10, 271, 451))
        self.label_2.setStyleSheet(u"")
        self.label_2.raise_()
        self.label_2.setPixmap(QPixmap(u"resources/images/Screenshot_1624995967.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(570, 10, 271, 451))
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u"resources/images/Screenshot_1624995967.png"))
        self.label_3.setScaledContents(True)
        self.label_3.raise_()
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(850, 10, 271, 451))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u"resources/images/Screenshot_1624995967.png"))
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

        # Icons
        icon = QIcon()
        icon.addFile(u"resources/images/information-button.png", QSize(), QIcon.Normal, QIcon.Off)

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



        self.b1 = QCheckBox(self.centralwidget)
        self.b1.setObjectName(u"pushButton_2")
        self.b1.setGeometry(QRect(750, 590, 151, 51))
        self.b1.setIconSize(QSize(25, 25))
        self.b1.raise_()


        self.pushButton_1.clicked.connect(save_subtree)  # Cut UI's
        self.pushButton_2.clicked.connect(load_data_for_model)  # Load UI Data
        self.pushButton_3.clicked.connect(generateModel)  # Generate Model
        self.pushButton_4.clicked.connect(generate_categories)  # Generate Categories
        self.pushButton_5.clicked.connect(generate_generators)  # Generate Generators
        self.pushButton_6.clicked.connect(generate_uis)  # Generate UI Suggestions
        self.pushButton_7.clicked.connect(use_own_data_set)  # Use own Data Set
        self.pushButton_8.clicked.connect(calc_with_metrics)  # Start recalculation
        self.pushButton_9.clicked.connect(open_parser_window)  # Start open_parser_window
        self.pushButton_10.clicked.connect(cancle_calc_with_metrics)  # Start calc_with_metrics

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
        self.pushButton_7.setText(QCoreApplication.translate("mainWindow", u"Use own Data-Set", None))
        self.pushButton_8.setText(QCoreApplication.translate("mainWindow", u"Calculate Metrics", None))
        self.pushButton_9.setText(QCoreApplication.translate("mainWindow", u"*.li Parser", None))
        self.pushButton_10.setText(QCoreApplication.translate("mainWindow", u"Cancle Metric-Calculation", None))

        self.pushButton_1.setStatusTip("Cut the existing Screenshots into a specified substructure")
        self.pushButton_2.setStatusTip("Prepare the cutted user interface elements for the neural network")
        self.pushButton_3.setStatusTip("Train models with the help of the siamese network")
        self.pushButton_4.setStatusTip("Generate pairs (using the model) from the individual cropped user interface elements and categorize them")
        self.pushButton_5.setStatusTip("Generate GAN-Generator")
        self.pushButton_6.setStatusTip("Create new inspiring user interfaces with the help of the generator")
        self.pushButton_7.setStatusTip("Open a folder where you can insert your own Screenshots. These will be used for future calculations")
        self.pushButton_8.setStatusTip("The generated images are checked with various metrics")
        self.pushButton_9.setStatusTip("Select a .li file and parse it into a .json file")
        self.pushButton_10.setStatusTip("Cancle Metric-Calculation")



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

# Method for changing label images
# for example: image1 = u"image.png"
def insert_label_images(self, image1, image2, image3, image4):
    if image1 is not None:
        self.label_1.setPixmap(QPixmap(image1))
    if image2 is not None:
        self.label_2.setPixmap(QPixmap(image2))
    if image3 is not None:
        self.label_3.setPixmap(QPixmap(image3))
    if image4 is not None:
        self.label_4.setPixmap(QPixmap(image4))

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

def use_own_data_set():
    print("Use own Data Set Button clicked!")
    path = "C:\\Users\\Marvin\\Desktop\\HierAblegen"
    path = os.path.realpath(path)
    os.startfile(path)

def choose_xml_file():
    print("Choose .xml file Button clicked!")

    choosenXMLFile = fd.askopenfilename(
        title="Select .xml file to focus from the project folder...",
        filetypes=[('.xml files', '.xml')])
    xmldoc = minidom.parse(choosenXMLFile)
    print("########## XML-FILE ##########")
    print(xmldoc.toxml())

def start_recalculation():
    print("Start recalculation Button clicked!")

def open_parser_window():
    root = tkinter.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
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
        print("calc_with_metrics")
        root_dir = r".\folders\results"

        results = list(Path(root_dir).rglob("**/*.jpg"))
        for result in results:

            if(positionOnLayout > 3):
                positionOnLayout = 0

            print(result)
            from deepux1_metrics import metrics_check
            pathtest = "..\\..\\..\\" + str(result)

            if (positionOnLayout == 0):
                uiObj.label_1.setText("LOADING")
            elif (positionOnLayout == 1):
                uiObj.label_2.setText("LOADING")
            elif (positionOnLayout == 2):
                uiObj.label_3.setText("LOADING")
            elif (positionOnLayout == 3):
                uiObj.label_4.setText("LOADING")

            evaluation_percentage = metrics_check.check_metrics(pathtest,first_start_check_metrics)
            first_start_check_metrics = False


            if (evaluation_percentage > 54):
                print("add to ui")
                if (positionOnLayout == 0):
                    uiObj.label_1.setPixmap(QPixmap(str(pathtest)))
                elif (positionOnLayout == 1):
                    uiObj.label_2.setPixmap(QPixmap(str(pathtest)))
                elif (positionOnLayout == 2):
                    uiObj.label_3.setPixmap(QPixmap(str(pathtest)))
                elif (positionOnLayout == 3):
                    uiObj.label_4.setPixmap(QPixmap(str(pathtest)))

                print("positionOnLayout1" + str(positionOnLayout))
                positionOnLayout = positionOnLayout + 1
                print("positionOnLayout2" + str(positionOnLayout))

def calc_with_metrics():

    thread = Thread(target=threaded_function, args=(10,))
    thread.start()

def cancle_calc_with_metrics():
    ## TODO Interrupt thread
    print("TODO Interrupt thread")

if __name__ == '__main__':
    # Console-call
    # Call. python main.py [function]
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
