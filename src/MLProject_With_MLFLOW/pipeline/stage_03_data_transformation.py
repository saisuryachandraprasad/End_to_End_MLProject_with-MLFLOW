from src.MLProject_With_MLFLOW.config.configuration import ConfigurationManager
from src.MLProject_With_MLFLOW.component.data_transformation import DataTransformation
from src.MLProject_With_MLFLOW.utils.common import logger
from pathlib import Path




STAGE_NAME = "Data Transformation stage"


class DataTransformationTrainingPipeline:
    
    def __init__(self) -> None:
        pass




    def main(self):

        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as status_file_obj:
                status = status_file_obj.read().split(" ")[-1]



            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_tranformation = DataTransformation(config=data_transformation_config)
                data_tranformation.train_test_spliting()

            else:
                raise Exception("your data schema is not valid")
            
        except Exception as e:
            print(e)




if __name__ =="__main__":

    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME} is started <<<<<<<<<<<")

        obj = DataTransformationTrainingPipeline()
        obj.main()

        logger.info(f">>>>>>>> {STAGE_NAME} is completed <<<<<<<<< ")

    except Exception as e:
        logger.info(e)
        raise e
