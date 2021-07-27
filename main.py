import os
import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QRect, QSize, QCoreApplication, QMetaObject
from PySide2.QtGui import QIcon, QFont, Qt, QPixmap
from PySide2.QtWidgets import QLabel, QPushButton, QWidget, QFrame, QStatusBar, QSizePolicy, QAction, QProgressBar, \
    QMenuBar, QMenu, QMessageBox

from GUIGAN_main import build_result_uis
from build_generator import build_generator
from get_style_emb import get_style_emb
from application.modelGenerator.load_data import load_data
from application.modelGenerator.load_subtrees import load_subtrees
from application.modelGenerator.train_siamese_net import train_siamese
from application.subtreeGenerator.save_subtree_info import save_subtree_info

# Console
import fire

from xml.dom import minidom
from tkinter import filedialog as fd

json_rico = r'.\folders\Rico\jsons'  # Rico Json Dateien
gui_dir_rico = r'.\folders\Rico\gui'  # Rico
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

# UI
class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setFixedSize(1143, 922)
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
        self.label_6.setGeometry(QRect(22, 646, 101, 31))
        self.label_6.setFont(font1)
        self.label_6.setFocusPolicy(Qt.NoFocus)
        self.label_6.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.raise_()
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(532, 646, 191, 31))
        self.label_7.setFont(font2)
        self.label_7.setFocusPolicy(Qt.NoFocus)
        self.label_7.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.raise_()

        # Icons
        icon = QIcon()
        icon.addFile(u"resources/images/information-button.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addFile(u"resources/images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3 = QIcon()
        icon3.addFile(u"resources/images/gear.png", QSize(), QIcon.Normal, QIcon.Off)

        # Buttons
        self.pushButton_1 = QPushButton(self.centralwidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(20, 690, 131, 51))
        self.pushButton_1.raise_()
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(180, 690, 131, 51))
        self.pushButton_2.raise_()
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(340, 690, 131, 51))
        self.pushButton_3.raise_()
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 775, 131, 51))
        self.pushButton_4.raise_()
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(180, 775, 131, 51))
        self.pushButton_5.raise_()
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 775, 131, 51))
        self.pushButton_6.raise_()
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(532, 690, 151, 51))
        self.pushButton_7.setToolTipDuration(3)
        self.pushButton_7.setIcon(icon2)
        self.pushButton_7.setIconSize(QSize(25, 25))
        self.pushButton_7.raise_()
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(532, 775, 151, 51))
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QSize(25, 25))
        self.pushButton_8.raise_()

        self.pushButton_1.clicked.connect(save_subtree)  # Cut UI's
        self.pushButton_2.clicked.connect(load_data_for_model)  # Load UI Data
        self.pushButton_3.clicked.connect(generateModel)  # Generate Model
        self.pushButton_4.clicked.connect(generate_categories)  # Generate Categories
        self.pushButton_5.clicked.connect(generate_generators)  # Generate Generators
        self.pushButton_6.clicked.connect(generate_uis)  # Generate UI Suggestions
        self.pushButton_7.clicked.connect(use_own_data_set)  # Use own Data Set
        self.pushButton_8.clicked.connect(start_recalculation)  # Start recalculation

        # Actions
        self.action_ueber = QAction(mainWindow)
        self.action_ueber.setObjectName(u"action_ueber")
        self.action_ueber.triggered.connect(about)
        self.action_ueber.setIcon(icon)

        # Lines
        self.line_1 = QFrame(self.centralwidget)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setGeometry(QRect(-10, 470, 1181, 16))
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.line_1.raise_()
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(0, 623, 1181, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.raise_()
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(501, 630, 20, 311))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.raise_()

        # ProgressBar
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 850, 485, 23))
        self.progressBar.setValue(50)
        self.progressBar.raise_()

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
        self.label_6.setText(QCoreApplication.translate("mainWindow", u"Action", None))
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
        self.pushButton_8.setText(QCoreApplication.translate("mainWindow", u"Start recalculation", None))

        self.pushButton_1.setStatusTip("Cut the existing screenshots into a specified substructure")
        self.pushButton_2.setStatusTip("Prepare the cutted user interface elements for the neural network")
        self.pushButton_3.setStatusTip("Train models with the help of the siamese network")
        self.pushButton_4.setStatusTip("???")
        self.pushButton_5.setStatusTip("Generate GAN-geneator ")
        self.pushButton_6.setStatusTip("Create new inspiring user interfaces with the help of the generator ")
        self.pushButton_7.setStatusTip("Open a folder where you can insert your own screenshots. These will be used for future calculations")
        self.pushButton_8.setStatusTip("Start a recalculation with the new screenshots")

# Create a "about" Message-Box
def about(self):
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
        "<p><b>Prof. Dr. Matthias Böhmer</b> <br>matthias.boehmer@th-koeln.de</p>",
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

def save_subtree(self):
    print("Cut UI's Button clicked!")
    save_subtree_info(json_rico, gui_dir_rico, gui_information_dir, control_elements_id_dir, cutted_ui_elements,
    cutted_resized_ui_elements)

def load_data_for_model(self):
    print("Load UI Data Button clicked!")
    load_data(cutted_resized_ui_elements,data_dir)
    load_subtrees(cutted_resized_ui_elements,data_dir)

def generateModel(self):
    print("Generate Model Button clicked!")
    train_siamese(cutted_resized_ui_elements,data_dir,models_torch_dir)

def generate_generators(self):
    print("Generate Generators Button clicked!")
    build_generator(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,cutted_ui_elements,cutted_resized_ui_elements)

def generate_uis(self):
    print("Generate UI Suggestions Button clicked!")
    build_result_uis(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,results_dir,results_pre_dir,cutted_ui_elements,cutted_resized_ui_elements)

def generate_categories(self):
    print("Generate Categories Button clicked!")
    get_style_emb(models_torch_dir,app_details_csv,categories_app_emb,cutted_ui_elements,cutted_resized_ui_elements)

def use_own_data_set(self):
    print("Use own Data Set Button clicked!")
    path = "C:\\Users\\Marvin\\Desktop\\HierAblegen"
    path = os.path.realpath(path)
    os.startfile(path)

def choose_xml_file(self):
    print("Choose .xml file Button clicked!")

    choosenXMLFile = fd.askopenfilename(
        title="Select .xml file to focus from the project folder...",
        filetypes=[('.xml files', '.xml')])
    xmldoc = minidom.parse(choosenXMLFile)
    print("########## XML-FILE ##########")
    print(xmldoc.toxml())

def start_recalculation(self):
    print("Start recalculation Button clicked!")

if __name__ == '__main__':
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


    # Console-call
    # https://stackoverflow.com/a/44360294
    fire.Fire(Ui_mainWindow)

    # Build UI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
