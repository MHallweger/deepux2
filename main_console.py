#-*- coding:utf-8 -*-
import os
import sys


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

json_rico = '/folders/Rico/jsons'  # Rico Json Dateien
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
li_files = r'.\folders\li_files'




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



    print("########## XML-FILE ##########")


def start_recalculation():
    print("Start recalculation Button clicked!")



if __name__ == '__main__':
    # Console-call
    # Call. python main.py [function]
    #fire.Fire()

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



    save_subtree()
