# -*- coding: utf-8 -*-
"""
"""

import copy
import numpy as np

class Rollout(object):
    def __init__(self, model, update_rate):
        self.ori_model = model
        self.own_model = copy.deepcopy(model)
        self.update_rate = update_rate

    def get_reward(self, x, num, discriminator):
        """
        Args:
            x : (batch_size, seq_len) input data
            num : 16, roll-out number
            discriminator : discrimanator model
        """
        rewards = []
        batch_size = x.size(0)
        seq_len = x.size(1)
        for i in range(num):
            for l in range(1, seq_len):
                data = x[:, 0:l]
                samples = self.own_model.sample(batch_size, seq_len, data)
                pred = discriminator(samples)
                pred = pred.cpu().data[:,1].numpy() # Get the score of each sentence
                if i == 0:
                    rewards.append(pred)
                else:
                    rewards[l-1] += pred # Add all the scores together

            # for the last token: The last one does not need to be sampled because it is already a complete sequence
            pred = discriminator(x) #You don’t need to run the last word to generate it, and read input_x directly
            pred = pred.cpu().data[:, 1].numpy()
            if i == 0:
                rewards.append(pred)
            else:
                rewards[seq_len-1] += pred
        rewards = np.transpose(np.array(rewards)) / (1.0 * num) # batch_size * seq_len, then average
        return rewards # In this way, the rewards for sentences of arbitrary length are obtained

    def update_params(self):
        dic = {}
        for name, param in self.ori_model.named_parameters():
            dic[name] = param.data
        for name, param in self.own_model.named_parameters():
            if name.startswith('emb'): # embedding weights do not need to be updated
                param.data = dic[name] # original
            else:
                param.data = self.update_rate * param.data + (1 - self.update_rate) * dic[name]