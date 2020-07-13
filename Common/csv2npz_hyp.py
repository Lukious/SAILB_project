# -*- coding: utf-8 -*-
"""
@author: BSW
"""

import numpy as np
import os

def csv2npz_hyp(filename,data):
    hyp = np.loadtxt(data,delimiter=',',dtype=np.float32)
    #print(hyp.shape)
    np.savez("./hyp_npz/"+filename+".npz",hyp=hyp) 
    """a = np.load(data)
    hyp = a['hyp']
    print(hyp)"""

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.csv': 
            csv2npz_hyp(filename,full_filename)
            pass

            
if __name__ == '__main__':
    #filename = input("Input .mat file name (only file name no '.mat'):")
    name = os.path.dirname( os.path.abspath( __file__ ) )
    #dir_name = name[:-6]
    Dataset_dir = "hyp"
    Dataset_dir = name + '\\' + Dataset_dir + '\\'
    search(Dataset_dir)



