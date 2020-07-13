# -*- coding: utf-8 -*-
"""
@author: BSW
"""

import scipy.io
import pandas as pd
import os

def mat2csv(filename,data):
    ori_data = scipy.io.loadmat(data)
    hyp=ori_data['hyp']
    xx=ori_data['xx']
    dfhyp = pd.DataFrame(hyp)
    dfxx = pd.DataFrame(xx)
    dfhyp.to_csv("./hyp/"+filename+".csv",header=False,index=False)
    dfxx.to_csv("./xx/"+filename+".csv",header=False,index=False)
    

def search(dirname):
    filenames = os.listdir(dirname)
    path = './hyp'
    os.makedirs(path, exist_ok=True)
    path = './xx'
    os.makedirs(path, exist_ok=True)
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

