#!/usr/bin/env python
# coding: utf-8

# In[1]:


from args import get_parser
import torch
import torch.nn as nn
import torch.autograd as autograd
import numpy as np
import os
import random
import pickle



args = get_parser()
print(args)
pickle.dump(args, open('/home/ct2020dl5787/inversecooking/model/checkpoints/args.pkl', 'wb'))

