# -*- coding: utf-8 -*-

import os,time,random,math,csv,argparse
import numpy as np
from apted import APTED, Config
from  apted.helpers import Tree
import torch
import torch.nn as nn
import torch.optim as optim
from torch.autograd import Variable
from sklearn import (manifold, datasets, decomposition, ensemble,random_projection, metrics)
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.neighbors import kneighbors_graph
from scipy.stats import mode

from GUIGAN_test import BATCH_SIZE, g_sequence_len
from generator import Generator
from discriminator import Discriminator
from modelGenerator.load_data import get_s_app
from reward import Rollout
from data_iter import DisDataIter
from get_style_emb import read_data,get_ui_info
from comm import get_samples,get_bank_size,remove_0,get_Repository,get_list_wbk

import sys
sys.path.append(r'.\StyleEmbedding')


def generate_samples(model,batch_size,generated_num,output_file,x_info,x_ids,start_id_list,end_id_list,bank_dict,pre_st=0):
    samples = []
    samples1 = []
    torch.cuda.set_device(0)
    for _ in range(int(generated_num / batch_size)):
        if pre_st == 0:
            start_st = random.sample(start_id_list, batch_size)
            start_st = np.expand_dims(start_st, axis=1)
        else:   
            start_st = [pre_st for c in range(batch_size)]        
        start_st = Variable(torch.Tensor(start_st).long())        
        sample = model.sample(BATCH_SIZE, g_sequence_len, start_st).cpu().data.numpy().tolist()
        samples.extend(sample)
    samples1,samples_tree,samples_imgdir,samples0,real_DT,samples1_e,samples_lenth = get_samples(samples,x_info,x_ids,start_id_list,end_id_list,bank_dict)
    samples1 = samples1.cpu().data.numpy().tolist()
    
    with open(output_file+'.txt', 'w', encoding="utf-8") as fout:
        for sample in samples1:
            string = ' '.join([str(s) for s in sample])
            fout.write('%s\n' % string)
    with open(output_file+'imgdir.txt', 'w', encoding="utf-8") as fout:
        for sample in samples_imgdir:
            if sample in bank_dict.values():
                string = sample
            else:
                string = ' '.join([str(s) for s in sample])
            fout.write('%s\n' % string)
    with open(output_file+'_no_padding.txt', 'w', encoding="utf-8") as fout:
        for sample in samples0:
            string = ' '.join([str(s) for s in sample])
            fout.write('%s\n' % string)
            
    with open(output_file+'_e.txt', 'w', encoding="utf-8") as fout:
        for sample in samples1_e:
            fout.write('%s\n' % sample)
    return samples_lenth