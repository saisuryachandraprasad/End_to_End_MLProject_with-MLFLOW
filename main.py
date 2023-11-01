from src.MLProject_With_MLFLOW import logger
from src.MLProject_With_MLFLOW.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.MLProject_With_MLFLOW.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLProject_With_MLFLOW.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline




STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>stage {STAGE_NAME} started <<<<<<<<")

        obj = DataIngestionPipeline()
        obj.main()

        logger.info(f">>>>>>>stage {STAGE_NAME} is completed<<<<<<<<")

except Exception as e:
        raise e
    


STAGE_NAME = "Data Validation Stage"

try:
        
        logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage {STAGE_NAME} completed <<<<<<<<")

except Exception as e:
        raise e



STAGE_NAME = "Data Transformation Stage"

try:
        
        logger.info(f">>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<")

        obj = DataTransformationTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>> {STAGE_NAME} is completed <<<<<<<<< ")

except Exception as e:
        raise e