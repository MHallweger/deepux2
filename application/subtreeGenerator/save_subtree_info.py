import os, shutil
import numpy as np
from PIL import Image
from PIL import ImageFile

from application.subtreeGenerator.get_subtree import get_layerNum, get_resized_bounds, get_height, get_className, \
    get_component_byjson, get_width, compress_image


def get_clayer_nodes(Dom_list, layer1_ids=[]):
    print('layer1_ids:', layer1_ids)
    Dom_list1 = Dom_list.copy()
    # Find all nodes in the first layer
    Dom_listids = [c[0] for c in Dom_list1]
    r = np.min([get_layerNum(c) for c in Dom_listids])
    print('\nr:', r)
    # Save all the shortest nodes in layer1_ids for the first search
    layer1_ids += [c for c in Dom_listids if get_layerNum(c) == r and c not in layer1_ids]
    print('layer1_ids:', layer1_ids)
    # Delete the nodes in first layer
    for c in Dom_list1:
        if c[0] in layer1_ids:
            Dom_list1.remove(c)
    # Delete the children of the nodes from the first layer
    NC_dict = {}
    for c in Dom_list:
        for f in layer1_ids:
            if f in c[0] and f != c[0]:  # Find all the children of the first layer
                if c[0] not in NC_dict.keys():
                    NC_dict[f] = [c]
                else:
                    NC_dict[f].append(c)
                if c in Dom_list1:
                    Dom_list1.remove(c)
    if len(Dom_list1) == 0:
        print('\n', layer1_ids, 'no more layer1 Node')
        return layer1_ids
    else:
        print('\nExtra', len(Dom_list1), 'layer1 Node:')
        [print(c[0]) for c in Dom_list1]
        _ids = get_clayer_nodes(Dom_list1, layer1_ids)
        return _ids


# Find the items that only belong to c in DL and do not belong to any other leaves in Dd
def get_subLeafNodes_ofC(c, Dd, Dl):
    Dd_ids = [d[0] for d in Dd]
    Dl_ids = [l[0] for l in Dl]
    leaf_ids_inDd = []
    for d in Dd_ids:
        for l in Dl_ids:
            if d in l:
                if l not in leaf_ids_inDd:
                    leaf_ids_inDd.append(l)
    leaf_ids_offDd = [l for l in Dl_ids if l not in leaf_ids_inDd]
    c_leaf = []
    for l in leaf_ids_offDd:
        if c in l:
            if l not in c_leaf:
                c_leaf.append(l)
    return c_leaf


# Find the node that only belongs to c in Dd
def get_subNodes_ofC(c, Dd):
    Dd_ids = [d[0] for d in Dd]
    c_children = []
    for d in Dd_ids:
        if c in d:
            if d not in c_children:
                c_children.append(d)
                # Find subtree that only belongs to c
    others_subNodes = []
    for d in c_children:  # whether d has other father nodes
        c_children1 = c_children.copy()
        c_children1.remove(d)
        for f in c_children1:
            if f in d:
                if d not in others_subNodes:
                    others_subNodes.append(d)
    c_children = [c for c in c_children if c not in others_subNodes]
    return c_children


def write_NtD(c, node_tree, Dd, Dl):  # c is not in Dd, write the list of nodes to dict
    # k is the node number, V is the node number of its childre only
    # (1)Find the leaf of C (C only)
    c_leafs = get_subLeafNodes_ofC(c, Dd, Dl)
    Dl_out = [d for d in Dl if d[0] not in c_leafs]

    c_childrens = get_subNodes_ofC(c, Dd)
    Dd_out = [d for d in Dd if d[0] not in c_childrens]

    c_nodes_leaf = c_childrens + c_leafs
    node_tree[c] = c_nodes_leaf

    if c_childrens == []:
        return node_tree, Dd_out, Dl_out
    else:
        for c1 in c_childrens:
            node_tree1, Dd1, Dl1 = write_NtD(c1, node_tree, Dd_out, Dl_out)
        return node_tree1, Dd1, Dl1


def DtoT(c, tt, node_tree, id_class_d):
    if c not in node_tree.keys():
        tt += '}'
        return tt
    else:
        for d in node_tree[c]:
            tt += '{' + id_class_d[d]
            tt = DtoT(d, tt, node_tree, id_class_d)
        tt += '}'
    return tt


# Get the subtree structure of all nodes in DOMTree and Dom_list
def get_aptedTree(Dom_list, node_tree, id_class_d):
    aTree = []
    # root
    if 'root' in [c[0] for c in Dom_list]:
        tree_text = '{root'
        tree_text = DtoT('root', tree_text, node_tree, id_class_d)
        c_b = [c[2] for c in Dom_list if c[0] == 'root'][0]
        aTree.append(['root:', tree_text, c_b])

    # subtrees nodes
    for c in Dom_list:
        tree_text = '{' + c[1]
        tree_text = DtoT(c[0], tree_text, node_tree, id_class_d)
        aTree.append([c[0] + ':', tree_text, c[2]])

    return aTree


def save_subtree_img(_list, ui_dir, dst_dir,ui_id):
    if _list != []:
        for c in _list:
            if get_height(c[2]) >= 1280:
                _list.remove(c)


            #c[2][0] = 0
            ##c[2][1] = 400 ### height
            ##c[2][2] = 1440 ##fixed by json file
            ##c[2][3] = 700

        im = Image.open(ui_dir)
        for c in _list:
            resized_block = get_resized_bounds(c[2])
            cropedIm = im.crop(resized_block)
            # save_dir = os.path.join(dst_dir,str(ui_id))
            save_dir = dst_dir
            print("SAVE DIR: " + save_dir)
            if (not os.path.exists(save_dir)):
                os.makedirs(save_dir)
            shutil.copy(ui_dir, save_dir)
            # save_subtree_dir = os.path.join(save_dir,c[0])
            save_subtree_dir = os.path.join(save_dir, str(ui_id) + "_" + c[0])
            print("save_subtree_dir: " + save_subtree_dir)
            cropedIm.save(save_subtree_dir + '.png', "png")


'''save subtree info in .txt'''


def save_tree_process(jsns_dir, ui_id, img_dir, tree_dir, db_app_dir, dst_dir):
    cd0 = os.path.join(jsns_dir, ui_id + '.json')

    Dom_list, leaf_list, st_bank = get_component_byjson(cd0)

    save_subtree_img(Dom_list, img_dir, dst_dir,ui_id)

    if Dom_list != []:
        if Dom_list == []:
            print(ui_id, 'Dom_list is Empty!')
        else:
            print('Dom_list.len:', len(Dom_list))
            print('st_bank.len: ', len(st_bank))
            Dom_list = [(c[0], get_className(c[1]), c[2]) for c in Dom_list]
            leaf_list = [(c[0], get_className(c[1]), c[2]) for c in leaf_list]
            Dom_allnodes = Dom_list + leaf_list

            node_tree = {}
            dynamic_Dom_list = Dom_list.copy()
            dynamic_leaf_list = leaf_list.copy()

            print('layer', len(node_tree), 'root')
            print('\ndynamic_Dom_list', dynamic_Dom_list)
            layer1_ids = get_clayer_nodes(dynamic_Dom_list, [])  # from the first layer
            dynamic_Dom_list = [c for c in dynamic_Dom_list if c[0] not in layer1_ids]
            node_tree['root'] = layer1_ids
            print('\n\n', len(layer1_ids), 'first layers!')
            for c in layer1_ids:  # from the first layer to the next..
                node_tree, dynamic_Dom_list, dynamic_leaf_list = write_NtD(c, node_tree, dynamic_Dom_list,
                                                                           dynamic_leaf_list)

            node_tree1 = node_tree.copy()
            for (k, v) in node_tree.items():
                if k not in [c[0] for c in Dom_list]:
                    node_tree1.pop(k)

            # use node_tree to build st structure like: tree1=Tree.from_text('{A{B{M}{N}{F}}{C}}')
            id_class_d = {}  # Build a dict that stores all node id-class
            for c in Dom_allnodes:
                id_class_d[c[0]] = c[1]

            aTrees = get_aptedTree(Dom_list, node_tree1, id_class_d)
            ui_tree_dir = os.path.join(tree_dir, ui_id + '.txt')

            f1 = open(ui_tree_dir, 'w', encoding='utf-8')  # width, height
            [f1.write(
                t[0] + t[1] + ':' + str(get_width(t[2])) + '_' + str(get_height(t[2])) + ':' + str(t[2])[1:-1] + ',\n')
             for t in aTrees]
            f1.write(';\n')
            for (k, v) in node_tree1.items():
                f1.write(str(k) + ' ' + str(v) + '\n')
            f1.close()
        # save st_bank_in
        ui_db_dir = os.path.join(db_app_dir, ui_id + '.txt')
        f2 = open(ui_db_dir, 'w', encoding='utf-8')
        [f2.write(c + ',\n') for c in st_bank]


# Removes all empty folder of a directory
def remove_empty_folder(apps_dir):
    for app in os.listdir(apps_dir):
        app_dir = os.path.join(apps_dir, app)
        if not os.listdir(app_dir):  # empty folder
            print('Empty', app_dir)
            os.rmdir(app_dir)


# -------------------main start-----------------------------------
# save_tree_process(jsns_dir,ui_id,tree_dir):

# Tears the UI of RICO into different parts.
def save_subtree_info(json_rico, gui_dir_rico, gui_information_dir, control_elements_id_dir, cutted_ui_elements,cutted_resized_ui_elements):
    #jsns_dir = r'.\Rico\combined'  # json_dir
    #cd = r'.\P_app_resize_sub'  # GUI_dir ORIGINALEN RICO Bilder
    #dt = r'.\aTrees_dict_app'  # ourput_dir
    #db = r'.\st_bank_app'  # # save id_list with blank
    #dsts_dir = r'.\p_app_Td_sts'  # cut subtree imgs
    #resized_dir = r'.\p_app_Td_sts_resized'  # resize subtree imgs

    print("save_subtree_info function started!")
    if len(os.listdir(gui_dir_rico))  > 0:

        for app in os.listdir(gui_dir_rico):
            app_dir = os.path.join(gui_dir_rico, app)
            dt_app_dir = os.path.join(gui_information_dir, app)
            db_app_dir = os.path.join(control_elements_id_dir, app)
            dst_dir = os.path.join(cutted_ui_elements, app)
            if not os.path.exists(dt_app_dir):
                os.makedirs(dt_app_dir)
            if not os.path.exists(db_app_dir):
                os.makedirs(db_app_dir)
            for im in os.listdir(app_dir):
                img_dir = os.path.join(app_dir, im)
                ui_id = os.path.splitext(im)[0]
                print("ui_Id: " + ui_id)
                save_tree_process(json_rico, ui_id, img_dir, dt_app_dir, db_app_dir, dst_dir)
                original_image = os.path.join(cutted_ui_elements, app)
                original_image = os.path.join(original_image, im)
                print("original_image:" + original_image)
                if os.path.exists(original_image):
                    os.remove(original_image)
                else:
                    print('no original_image:', original_image)

        remove_empty_folder(gui_information_dir)
        remove_empty_folder(control_elements_id_dir)

        ImageFile.LOAD_TRUNCATED_IMAGES = True
        compress_image(cutted_ui_elements, cutted_resized_ui_elements, 512, 256)
    else:
        print("no rico files")