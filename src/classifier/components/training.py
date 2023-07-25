from classifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

class Training: 
    def __init__(self, config: TrainingConfig):
        self.config = config
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):
        rescale = 1./255

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],  # num channels unneeded
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

        # Validation set datagenerator
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=rescale
        )
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.validation_data,
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                rescale=rescale
            )
        else:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rescale=rescale
            )

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
    
    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.train_generator.batch_size
        
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(self.config.trained_model_path, self.model)
