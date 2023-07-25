from classifier.components.get_trained_model import GetTrainedModel
from classifier.config.configuration import ConfigurationManager
from classifier import logger

STAGE_NAME = "Downloading trained model"

class DownloadModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        trained_model_config = config.get_trained_model_config()
        get_model_component = GetTrainedModel(trained_model_config)
        logger.info("Downloading data if needed...")
        get_model_component.download_file()
        get_model_component.extract_zip_file()
        return get_model_component.verify()


if __name__ == '__main__':
    try:
        logger.info(f"============ {STAGE_NAME} started ============")
        obj = DownloadModelPipeline()
        obj.main()
        logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e