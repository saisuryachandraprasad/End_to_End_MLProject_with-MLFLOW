import os
from src.MLProject_With_MLFLOW.utils.common import logger
from src.MLProject_With_MLFLOW.config.configuration import ConfigurationManager
from src.MLProject_With_MLFLOW.component.model_trainer import ModelTraining


STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass


    def main(self):

        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer()
        model_trainer = ModelTraining(config= model_trainer_config)
        model_trainer.train()




if __name__ == "__main__":

    try:
        logger.info(f">>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<")

        obj = ModelTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>{STAGE_NAME} is completed")

    except Exception  as e :
        logger.info(e)
        raise e
