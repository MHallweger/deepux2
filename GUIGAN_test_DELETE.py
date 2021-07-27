# -*- coding: utf-8 -*-

import sys

sys.path.append(r'application/modelGenerator')

# Basic Training Paramters
SEED = 88
BATCH_SIZE = 32
TOTAL_BATCH = 1
#TOTAL_BATCH = 10

POSITIVE_FILE = 'real' 
EVAL_FILE = 'eval' 

# Genrator Parameters
g_emb_dim = 32      # Embedding 
g_hidden_dim = 32   # nn.LSTM(emb_dim, hidden_dim)
g_sequence_len = 30

# Discriminator Parameters
d_emb_dim = 64
d_filter_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
d_num_filters = [100, 200, 200, 200, 200, 100, 100, 100, 100, 100, 160, 160]
d_dropout = 0.75
d_num_class = 2 

bank_dict = {'1':2, '2':6, '3':10, '4':20, '5':35, '6':50, '7':70, '8':100, '9':200, '10':300}
pre_built = True


