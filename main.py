from src.MLProject_With_MLFLOW import logger
from src.MLProject_With_MLFLOW.pipeline.stage_01_data_ingestion import DataIngestionPipeline




STAGE_NAME = "Data Ingestion Stage"


if __name__ =="__main__":

    try:

        logger.info(f">>>>stage {STAGE_NAME} started <<<<<<<<")

        obj = DataIngestionPipeline()
        obj.main()

        logger.info(f">>>>>>>stage {STAGE_NAME} is completed<<<<<<<<")

    except Exception as e:
        raise e