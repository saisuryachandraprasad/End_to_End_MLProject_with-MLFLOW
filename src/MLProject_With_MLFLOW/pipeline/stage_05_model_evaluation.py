from src.MLProject_With_MLFLOW.config.configuration import ConfigurationManager
from src.MLProject_With_MLFLOW.component.model_evaluation import ModelEvaluation
from src.MLProject_With_MLFLOW.utils.common import logger


STAGE_NAME = "Model Evaluation Stage"



class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass



    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config= model_evaluation_config)
        model_evaluation.log_into_mlflow()




if __name__ == "__main__":

    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME} is started<<<<<<<<<<<")

        obj = ModelEvaluationTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>>>{STAGE_NAME} is completed <<<<<<<<<<<")

    except Exception as e:
        logger.info(e)
        raise e