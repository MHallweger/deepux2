import os

import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable

from GUIGAN_main import build_generator
from GUIGAN_test import build_result_uis
from get_style_emb import get_style_emb
from modelGenerator.load_data import load_data
from modelGenerator.load_subtrees import load_subtrees
from modelGenerator.train_siamese_net import train_siamese
from subtreeGenerator.save_subtree_info import save_subtree_info
import tkinter as tk

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


def build_ui():
    window = tk.Tk()

    window.geometry("300x200+10+20")

    # Textausgabe erzeugen
    label1 = tk.Label(window, text="Hallo Welt")
    label1.pack()

    schaltf1 = tk.Button(window, text="1. UIs zerschneiden.", command = save_subtree)
    schaltf1.pack()

    load_data_button = tk.Button(window, text="1. Lade UI Daten.", command = load_data_for_model)
    load_data_button.pack()

    load_subtrees = tk.Button(window, text="Model genieren", command = generateModel)
    load_subtrees.pack()

    build_result_uis_button = tk.Button(window, text="generate_categories", command = generate_categories)
    build_result_uis_button.pack()

    build_result_uis_button = tk.Button(window, text="generate_generators", command = generate_generators)
    build_result_uis_button.pack()

    build_result_uis_button = tk.Button(window, text="build_result_uis_button", command = generate_uis)
    build_result_uis_button.pack()

    window.mainloop()

def save_subtree():
    save_subtree_info(json_rico, gui_dir_rico, gui_information_dir, control_elements_id_dir, cutted_ui_elements,
                      cutted_resized_ui_elements)

def load_data_for_model():
    load_data(cutted_resized_ui_elements,data_dir)
    load_subtrees(cutted_resized_ui_elements,data_dir)

def generateModel():
    train_siamese(cutted_resized_ui_elements,data_dir,models_torch_dir)

def generate_generators():
    build_generator(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,results_dir,results_pre_dir,cutted_ui_elements,cutted_resized_ui_elements)

def generate_uis():
    build_result_uis(app_details_csv,models_dir,gui_information_dir,control_elements_id_dir,categories_app_emb,results_dir,results_pre_dir,cutted_ui_elements,cutted_resized_ui_elements)

def generate_categories():
    get_style_emb(models_torch_dir,app_details_csv,categories_app_emb,cutted_ui_elements,cutted_resized_ui_elements)

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

    build_ui()

