from classifier import logger
from classifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from classifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from classifier.pipeline.stage03_training import ModelTrainingPipeline
from classifier.pipeline.stage04_evaluation import EvaluationPipeline


STAGE_NAME = "Data ingestion stage"
try:
    logger.info(f"============ {STAGE_NAME} started ============")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try:
    logger.info(f"============ {STAGE_NAME} started ============")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f"============ {STAGE_NAME} started ============")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"============ {STAGE_NAME} started ============")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f"=========== {STAGE_NAME} completed ===========\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e