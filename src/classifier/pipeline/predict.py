import numpy as np
import tensorflow as tf
import os
load_model = tf.keras.models.load_model
image = tf.keras.preprocessing.image


class PredictionPipeline:
    def __init__(self, filename: str):
        self.filename = filename
    
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        output = model.predict(test_image)  # returns [[x1, x2, x3, x4]]
        print(output)
        result = np.argmax(output, axis=1)[0]

        predictions = ['Coccidiosis', 'Healthy', 'New Castle Disease', 'Salmonella']
        return [{ 
            'image' : predictions[result], 
            'likelihood' : f"{output[0][result]:.2%}" 
        }]



     