import cv2
import tensorflow as tf
import keras
import numpy as np
import pathlib
import os
from os.path import isfile, join
from os import listdir
import glob
path_to_image = "static/upload/"
mnist_kek = [
    '0', 
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]
mnist_kek = np.array(mnist_kek)
model4 = keras.models.load_model('static/digit_classifaer.h5')
def predproc():
    onlyfiles = [f for f in listdir(path_to_image) if isfile(join(path_to_image, f))]
    n = cv2.imread(path_to_image+str(onlyfiles[0]))
    w = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
    w = w[200:950,:]
    thresh1 = cv2.adaptiveThreshold(w, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 199, 30)
    dim = (28,28)
    resized = cv2.resize(thresh1, dim, interpolation = cv2.INTER_AREA)
    w = cv2.bitwise_not(resized)
    w = w.reshape(1,28,28,1)
    w=w/255
    return w

def get_info(n):
    onlyfiles = [f for f in listdir(path_to_image) if isfile(join(path_to_image, f))]
    p = str(path_to_image+str(onlyfiles[0]))
    pred = model4.predict(n,verbose=0)
    d = dict(zip(mnist_kek,  list(map(lambda x: round(x,4), pred.tolist()[0]))))
    return d,p,np.argmax(pred)

def clearing_folder():
    files = glob.glob(path_to_image+"*")
    for f in files:
        os.remove(f)
