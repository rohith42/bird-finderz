from classifier.components.get_trained_model import GetTrainedModel
from classifier.config.configuration import ConfigurationManager
from classifier import logger

STAGE_NAME = "Downloading trained model"

class DownloadModelPipeline:
    def __init__(self) -> None:
        config = ConfigurationManager()
        self.trained_model_config = config.get_trained_model_config()
        self.get_model_component = GetTrainedModel(self.trained_model_config)

    def main(self):
        logger.info("Downloading data if needed...")
        self.get_model_component.download_file()
        self.get_model_component.extract_zip_file()
        return self.get_model_component.verify()
    
    def readyToPredict(self) -> bool:
        return self.get_model_component.modelExists()


if __name__ == '__main__':
    try:
        logger.info(f"============ {STAGE_NAME} started ============")
        obj = DownloadModelPipeline()
        obj.main()
        logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e