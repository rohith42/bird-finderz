from classifier.components.data_ingestion import DataIngestion
from classifier.config.configuration import ConfigurationManager
from classifier import logger

STAGE_NAME = "Data ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        logger.info("Downloading data if needed...")
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"============ {STAGE_NAME} started ============")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e