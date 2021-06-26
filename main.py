# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from subtreeGenerator.save_subtree_info import save_subtree_info


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    json_rico = r'.\folders\Rico\jsons'  # Rico Json Dateien
    gui_dir_rico = r'.\folders\Rico\gui'  # Rico
    gui_information_dir = r'.\folders\gui_informations'
    control_elements_id_dir = r'.\folders\gui_control_elements'
    cutted_ui_elements = r'.\folders\cutted_ui_elements'
    cutted_resized_ui_elements = r'.\folders\cutted_resized_ui_elements'

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


    save_subtree_info(json_rico, gui_dir_rico, gui_information_dir, control_elements_id_dir, cutted_ui_elements,
                      cutted_resized_ui_elements)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
