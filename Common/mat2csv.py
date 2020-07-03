# -*- coding: utf-8 -*-
"""
@author: BSW
"""

import scipy.io
import numpy as np
import pandas as pd
import os

def mat2csv(filename,data):
    ori_data = scipy.io.loadmat(data)
    pd_data = pd.Series(ori_data)
    pd_data.to_csv("./SleepData_csv/"+filename+".csv",mode = 'w')
    

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.mat': 
            mat2csv(filename,full_filename)
            pass

            
if __name__ == '__main__':
    #filename = input("Input .mat file name (only file name no '.mat'):")
    name = os.path.dirname( os.path.abspath( __file__ ) )
    dir_name = name[:-6]
    Dataset_dir = "SleepData"
    Dataset_dir = dir_name + Dataset_dir + '\\'
    search(Dataset_dir)



