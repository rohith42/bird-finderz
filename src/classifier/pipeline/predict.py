import numpy as np
import tensorflow as tf
import os
import pandas
from classifier.config.configuration import ConfigurationManager
load_model = tf.keras.models.load_model
image = tf.keras.preprocessing.image


class PredictionPipeline:
    def __init__(self, filename: str):
        self.filename = filename
        config = ConfigurationManager()
        self.config = config.get_prediction_config()
    
    def get_labels(self):
        datafile = pandas.read_csv(self.config.data_file_path)
        return list(datafile[str(self.config.labels_column_name)].unique())
    
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        output = model.predict(test_image)  # returns [[x1,...,x525]]
        print(output)
        result = np.argmax(output, axis=1)[0]

        predictions = self.get_labels()
        return [{ 
            'image' : predictions[result], 
            'likelihood' : f"{output[0][result]:.2%}" 
        }]



     