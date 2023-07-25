import tensorflow as tf
from pathlib import Path
from classifier.entity.config_entity import EvaluationConfig
from classifier.utils.common import save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _test_generator(self):
        # Test set datagenerator
        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            validation_split=0
        )
        self.test_generator = test_datagenerator.flow_from_directory(
            directory=self.config.test_data,
            shuffle=False,
            target_size = self.config.params_image_size[:-1],  # num channels unneeded
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._test_generator()
        self.score = self.model.evaluate(self.test_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)