import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse
from keras.models import model_from_json
from tkinter import *
from tkinter.filedialog import askopenfilename

categories = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']

window = Tk()
window.geometry("800x800")
window.configure(bg='grey')

def choose():
    filename = askopenfilename()
    read_image(filename)

def read_image(address):
    img = cv2.imread(address,1)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    preprocess_input(img)

def preprocess_input(image):
    img = cv2.resize(image,(32,32))
    img = np.transpose(img,(2,0,1))
    img = np.reshape(img,(1,3,32,32))
    img = img / 255.0
    prediction(img)

def probability_plot(predictions):
    y_pos = np.arange(len(categories))
    plt.figure()
    plt.barh(y_pos,predictions,align='center',alpha=0.5)
    plt.yticks(y_pos,categories)
    plt.xlabel('Probability')
    plt.show()

def prediction(input_image):
    model = model_from_json(open('mytrainedmodel_arch.json').read())
    model.load_weights('mytrainedmodel_weights.h5')
    # Get the predicitons.
    predictions = model.predict(input_image,verbose=0).flatten()
    top_results = predictions.argsort()
    print('Top predictions: %s: %0.4f, %s: %0.4f, %s: %0.4f' % 
            (categories[top_results[9]], predictions[top_results[9]],
                    categories[top_results[8]], predictions[top_results[8]], 
                    categories[top_results[7]],predictions[top_results[7]]))
    # Plot the probability bar chart.
    probability_plot(predictions)


button1 = Button(window, text='Choose Image', width=26, command=choose)
button1.grid(row=500, column=700)
button1.configure(bg='dark salmon')

window.mainloop()    
    


