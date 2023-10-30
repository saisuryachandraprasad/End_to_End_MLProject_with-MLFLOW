import os
from pathlib import Path
import urllib.request as request
import zipfile
from src.MLProject_With_MLFLOW.utils.common import logger
from src.MLProject_With_MLFLOW.utils.common import get_size  
from src.MLProject_With_MLFLOW.entity.config_entity import DataIngestionConfig  




class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    def download_file(self):
        """this method is responsible for data downloading"""

        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url= self.config.source_URL,
                filename= self.config.local_data_file
            )
            logger.info(f"{filename} is downloaded with following info: \n{header}")

        else:
            logger.info(f"file is already exist {get_size(Path(self.config.local_data_file))}")

    
    def extract_zipfile(self):
        """ this mwthod is responsible to extract data from zip file"""

        unzip_data = self.config.unzip_dir
        os.makedirs(unzip_data, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_data)