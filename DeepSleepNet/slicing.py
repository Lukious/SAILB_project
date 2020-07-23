# -*- coding: utf-8 -*-
"""
@author: BSW
"""

import numpy as np
import os

def mat2csv(filename,data):
    global wc#count for wake
    global n1c#count for n1
    global n2c#count for n2
    global n3c#count for n3
    global n4c#count for n4
    t=0
    
    npz = np.load(data)
    x = npz['x']
    y = npz['y']
    
    for i in y:
        if(i==0):
            if(wc<10):
                np.savez("./data/Wake/"+"0000"+str(wc)+".npz",x=x[t,:,0])
            elif(wc>=10 and wc<100):
                np.savez("./data/Wake/"+"000"+str(wc)+".npz",x=x[t,:,0])
            elif(wc>=100 and wc<1000):
                np.savez("./data/Wake/"+"00"+str(wc)+".npz",x=x[t,:,0])
            elif(wc>=1000 and wc<10000):
                np.savez("./data/Wake/"+"0"+str(wc)+".npz",x=x[t,:,0])
            else:
                np.savez("./data/Wake/"+str(wc)+".npz",x=x[t,:,0])
            wc+=1
            t+=1
                
        if(i==1):
            if(n1c<10):
                np.savez("./data/N1/"+"0000"+str(n1c)+".npz",x=x[t,:,0])
            elif(n1c>=10 and n1c<100):
                np.savez("./data/N1/"+"000"+str(n1c)+".npz",x=x[t,:,0])
            elif(n1c>=100 and n1c<1000):
                np.savez("./data/N1/"+"00"+str(n1c)+".npz",x=x[t,:,0])
            elif(n1c>=1000 and n1c<10000):
                np.savez("./data/N1/"+"0"+str(n1c)+".npz",x=x[t,:,0])
            else:
                np.savez("./data/N1/"+str(n1c)+".npz",x=x[t,:,0])
            n1c+=1
            t+=1
            
        if(i==2):
            if(n2c<10):
                np.savez("./data/N2/"+"0000"+str(n2c)+".npz",x=x[t,:,0])
            elif(n2c>=10 and n2c<100):
                np.savez("./data/N2/"+"000"+str(n2c)+".npz",x=x[t,:,0])
            elif(n2c>=100 and n2c<1000):
                np.savez("./data/N2/"+"00"+str(n2c)+".npz",x=x[t,:,0])
            elif(n2c>=1000 and n2c<10000):
                np.savez("./data/N2/"+"0"+str(n2c)+".npz",x=x[t,:,0])
            else:
                np.savez("./data/N2/"+str(n2c)+".npz",x=x[t,:,0])
            n2c+=1
            t+=1
            
        if(i==3):
            if(n3c<10):
                np.savez("./data/N3/"+"0000"+str(n3c)+".npz",x=x[t,:,0])
            elif(n3c>=10 and n3c<100):
                np.savez("./data/N3/"+"000"+str(n3c)+".npz",x=x[t,:,0])
            elif(n3c>=100 and n3c<1000):
                np.savez("./data/N3/"+"00"+str(n3c)+".npz",x=x[t,:,0])
            elif(n3c>=1000 and n3c<10000):
                np.savez("./data/N3/"+"0"+str(n3c)+".npz",x=x[t,:,0])
            else:
                np.savez("./data/N3/"+str(n3c)+".npz",x=x[t,:,0])
            n3c+=1
            t+=1
            
        if(i==4):
            if(n4c<10):
                np.savez("./data/N4/"+"0000"+str(n4c)+".npz",x=x[t,:,0])
            elif(n4c>=10 and n4c<100):
                np.savez("./data/N4/"+"000"+str(n4c)+".npz",x=x[t,:,0])
            elif(n4c>=100 and n4c<1000):
                np.savez("./data/N4/"+"00"+str(n4c)+".npz",x=x[t,:,0])
            elif(n4c>=1000 and n4c<10000):
                np.savez("./data/N4/"+"0"+str(n4c)+".npz",x=x[t,:,0])
            else:
                np.savez("./data/N4/"+str(n4c)+".npz",x=x[t,:,0])
            n4c+=1
            t+=1

def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext == '.npz': 
            mat2csv(filename,full_filename)
            pass

            
if __name__ == '__main__':
    c=0
    wc=1
    n1c=1
    n2c=1
    n3c=1
    n4c=1
    name = os.path.dirname( os.path.abspath( __file__ ) )
    Dataset_dir = "npzdata"
    Dataset_dir = name + '\\' + Dataset_dir + '\\'
    search(Dataset_dir)

