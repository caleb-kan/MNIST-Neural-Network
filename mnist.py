import TrainMnistModel 
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

ThisModel = 'mnist.model'
model = tf.keras.models.load_model(ThisModel)

image_num = 1
while os.path.isfile(f"mnist_images/image_{image_num}.png"):
    try:
        img = cv2.imread(f"mnist_images/image_{image_num}.png")[:,:,0]
        img = np.invert(np.array[img])
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error!")
    finally:
        image_num += 1