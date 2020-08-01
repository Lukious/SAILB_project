# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:39:14 2020

@author: jw030
"""
import os
from os import listdir
from os.path import isfile, join, splitext, isdir
from scipy.signal import butter, lfilter
import numpy as np
############BPF#####################
def butter_bandpass_filter(data, lowcut, highcut, fs, order=9):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq

    b, a = butter(order, [low, high], btype='bandpass',analog=False)
    y = lfilter(b, a, data)
    return y
#####################################

##########Normalization##############
def MinusMin(X):
    Min = np.min(X)
    X = X-Min
    return X
#####################################
    
data_path = './data'
data_list = [f for f in listdir(data_path) if isdir(join(data_path, f))]

for i in range(len(data_list)):
        N1_path = './data/'+ data_list[i] + '/1D_N1'
        N1_list = [f for f in listdir(N1_path) if isfile(join(N1_path, f))]
        N2_path = './data/'+ data_list[i] + '/1D_N2'
        N2_list = [f for f in listdir(N2_path) if isfile(join(N2_path, f))]
        N3_path = './data/'+ data_list[i] + '/1D_N3'
        N3_list = [f for f in listdir(N3_path) if isfile(join(N3_path, f))]
        REM_path = './data/'+ data_list[i] + '/1D_Rem'
        REM_list = [f for f in listdir(REM_path) if isfile(join(REM_path, f))]
        Wake_path = './data/'+ data_list[i] + '/1D_Wake'
        Wake_list = [f for f in listdir(Wake_path) if isfile(join(Wake_path, f))]
        
 
        decompo_N1_path = './decompo_data/' + data_list[i] + '/2D_N1'
        if os.path.exists(decompo_N1_path) is False:
            os.makedirs(decompo_N1_path)
        decompo_N2_path = './decompo_data/' + data_list[i] + '/2D_N2'
        if os.path.exists(decompo_N2_path) is False:
            os.mkdir(decompo_N2_path)
        decompo_N3_path = './decompo_data/' + data_list[i] + '/2D_N3'
        if os.path.exists(decompo_N3_path) is False:
            os.mkdir(decompo_N3_path)
        decompo_REM_path = './decompo_data/' + data_list[i] + '/2D_Rem'
        if os.path.exists(decompo_REM_path) is False:
            os.mkdir(decompo_REM_path)
        decompo_Wake_path = './decompo_data/' + data_list[i] + '/2D_Wake'
        if os.path.exists(decompo_Wake_path) is False:
            os.mkdir(decompo_Wake_path)
        
        ##N1 sleepstage's EEG decomposition
        for j in range(len(N1_list)):
            with np.load(join(N1_path,N1_list[j])) as npz:
                filename, filepath = os.path.splitext(N1_list[j])
                raw = np.reshape(npz['x'],(1,3000))
                min_raw = MinusMin(raw)
                N3 = butter_bandpass_filter(raw,0.1,1,100)
                N3 = MinusMin(N3)
                N2 = butter_bandpass_filter(raw,1,3,100)
                N2 = MinusMin(N2)
                N1  = butter_bandpass_filter(raw,10.5,16,100)
                N1 = MinusMin(N1)
                REM  = butter_bandpass_filter(raw,16,30,100)
                REM = MinusMin(REM)
                Wake  = butter_bandpass_filter(raw,37,47,100)
                Wake = MinusMin(Wake)
                data = np.concatenate((min_raw,Wake,REM,N1,N2,N3),axis=0)
                np.save(join(decompo_N1_path,filename + '.npy'),data)
        
        ##N2 sleepstage's EEG decomposition   
        for j in range(len(N2_list)):
            with np.load(join(N2_path,N2_list[j])) as npz:
                filename, filepath = os.path.splitext(N2_list[j])
                raw = np.reshape(npz['x'],(1,3000))
                min_raw = MinusMin(raw)
                N3 = butter_bandpass_filter(raw,0.1,1,100)
                N3 = MinusMin(N3)
                N2 = butter_bandpass_filter(raw,1,3,100)
                N2 = MinusMin(N2)
                N1  = butter_bandpass_filter(raw,10.5,16,100)
                N1 = MinusMin(N1)
                REM  = butter_bandpass_filter(raw,16,30,100)
                REM = MinusMin(REM)
                Wake  = butter_bandpass_filter(raw,37,47,100)
                Wake = MinusMin(Wake)
                data = np.concatenate((min_raw,Wake,REM,N1,N2,N3),axis=0)
                np.save(join(decompo_N2_path,filename + '.npy'),data)
            

        ##N3 sleepstage's EEG decomposition 
        for j in range(len(N3_list)):
            with np.load(join(N3_path,N3_list[j])) as npz:
                filename, filepath = os.path.splitext(N3_list[j])
                raw = np.reshape(npz['x'],(1,3000))
                min_raw = MinusMin(raw)
                N3 = butter_bandpass_filter(raw,0.1,1,100)
                N3 = MinusMin(N3)
                N2 = butter_bandpass_filter(raw,1,3,100)
                N2 = MinusMin(N2)
                N1  = butter_bandpass_filter(raw,10.5,16,100)
                N1 = MinusMin(N1)
                REM  = butter_bandpass_filter(raw,16,30,100)
                REM = MinusMin(REM)
                Wake  = butter_bandpass_filter(raw,37,47,100)
                Wake = MinusMin(Wake)
                data = np.concatenate((min_raw,Wake,REM,N1,N2,N3),axis=0)
                np.save(join(decompo_N3_path,filename + '.npy'),data)      

        ##REM sleepstage's EEG decomposition         
        for j in range(len(REM_list)):
            with np.load(join(REM_path,REM_list[j])) as npz:
                filename, filepath = os.path.splitext(REM_list[j])
                raw = np.reshape(npz['x'],(1,3000))
                min_raw = MinusMin(raw)
                N3 = butter_bandpass_filter(raw,0.1,1,100)
                N3 = MinusMin(N3)
                N2 = butter_bandpass_filter(raw,1,3,100)
                N2 = MinusMin(N2)
                N1  = butter_bandpass_filter(raw,10.5,16,100)
                N1 = MinusMin(N1)
                REM  = butter_bandpass_filter(raw,16,30,100)
                REM = MinusMin(REM)
                Wake  = butter_bandpass_filter(raw,37,47,100)
                Wake = MinusMin(Wake)
                data = np.concatenate((min_raw,Wake,REM,N1,N2,N3),axis=0)
                np.save(join(decompo_REM_path,filename + '.npy'),data)            

        ##Wake sleepstage's EEG decomposition 
        for j in range(len(Wake_list)):
            with np.load(join(Wake_path,Wake_list[j])) as npz:
                filename, filepath = os.path.splitext(Wake_list[j])
                raw = np.reshape(npz['x'],(1,3000))
                min_raw = MinusMin(raw)
                N3 = butter_bandpass_filter(raw,0.1,1,100)
                N3 = MinusMin(N3)
                N2 = butter_bandpass_filter(raw,1,3,100)
                N2 = MinusMin(N2)
                N1  = butter_bandpass_filter(raw,10.5,16,100)
                N1 = MinusMin(N1)
                REM  = butter_bandpass_filter(raw,16,30,100)
                REM = MinusMin(REM)
                Wake  = butter_bandpass_filter(raw,37,47,100)
                Wake = MinusMin(Wake)
                data = np.concatenate((min_raw,Wake,REM,N1,N2,N3),axis=0)
                np.save(join(decompo_Wake_path,filename + '.npy'),data)    