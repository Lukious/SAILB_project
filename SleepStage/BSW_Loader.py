import os
from os import listdir
from os import walk

from os.path import isfile, join, splitext, isdir
from scipy.signal import butter, lfilter 
import numpy as np

def dense_to_one_hot(labels_dense, num_classes=5):
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    labels_one_hot = np.zeros((num_labels, num_classes))
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1

    return labels_one_hot

def Data():
    subject_id = []
    # Used_Subject_id = []
    # Used_Subject_id = []
    # |1|-->Furthere Feature : Select Subject
    stages = ['2D_N1','2D_N2','2D_N3','2D_Rem','2D_Wake']
    file_list = []
    dir_re = []
    X = []
    Y = []
    
    mypath = './decompo_data'
    for (dirpath, dirnames, filenames) in walk(mypath):
        break
    
    subject_id = dirnames # Focus here For Featrue |1|
    
    for i in range(len(subject_id)):
        step_mypath = mypath + '/' +str(subject_id[i])
        for j in range(len(stages)) :
            sstep_mypath = step_mypath + '/' +str(stages[j])
            for (dirpath, dirnames, filenames) in walk(sstep_mypath):
                for k in range(len(filenames)):
                    dir_re.append(str(sstep_mypath) + '/'+ str(filenames[k]))
                    
    for i in range(len(dir_re)):
        processing_npz_name = dir_re[i]
        working_npz  = np.load(processing_npz_name)
        X.append(working_npz)
        ylabel = processing_npz_name[27:-10]
        if ylabel == 'N1':
            Y.append(1)
        elif ylabel == 'N2':
            Y.append(2)
        elif ylabel == 'N3':
            Y.append(3)
        elif ylabel == 'Rem':
            Y.append(4)
        elif ylabel == 'Wake':
            Y.append(5)        
    return X,Y
    #return X,dense_to_one_hot(Y)




def Data_spliter():
    X,Y = Data()
    