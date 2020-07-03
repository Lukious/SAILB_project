# -*- coding: utf-8 -*-
"""
@author: SAIBE
"""

from Preprocessing import Preprocessing
from data_loader import load_data

if __name__ == '__main__':
    # Implement Code From Here!
    ori_data = load_data()
    ori_data = Preprocessing(ori_data)
    
    