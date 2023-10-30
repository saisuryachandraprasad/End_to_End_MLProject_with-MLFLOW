from src.MLProject_With_MLFLOW.entity.config_entity import DataValidationConfig
from src.MLProject_With_MLFLOW.config.configuration import ConfigurationManager
from src.MLProject_With_MLFLOW.component.data_validation import DataValiadtion
from src.MLProject_With_MLFLOW.utils.common import logger



STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()



if __name__ =="__main__":
    try:
        logger.info(f">>>>>>>>stage {STAGE_NAME} started<<<<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>stage {STAGE_NAME} completed <<<<<<<<")

    except Exception as e:
        raise e