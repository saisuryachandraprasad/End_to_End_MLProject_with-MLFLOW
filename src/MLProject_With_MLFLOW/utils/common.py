import os
from box.exceptions import BoxValueError
import yaml
from src.MLProject_With_MLFLOW import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml:Path) ->ConfigBox:
    """Read yaml file and return content in yaml file"""

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    


    

@ensure_annotations
def create_directory(directory_path: list, verbose =True):
    """ create directory"""

    for path in directory_path:
        os.makedirs(path,exist_ok= True)
        if verbose:
            logger.info(f"created directory at{path}")





@ensure_annotations
def save_json(path :Path, data:dict):
    """will used to save json file"""

    with open(path, "w") as f:
        json.dump(data,f,indent=4)
        logger.info(f"data is lodaed to json file")




@ensure_annotations
def load_json(path:Path) ->ConfigBox:
    """read data from json file"""

    with open(path) as f:
        content = json.load(f)
        logger.info(f"data is loaded from {path}")
    return ConfigBox(content)
    

@ensure_annotations
def save_bin(data:Any, path:Path):
    """Save binary data"""

    joblib.dump(data, filename=path)
    logger.info(f"bin data is saved")



@ensure_annotations
def load_bin(path:Path):
    """load binary data from given path"""


    data = joblib.load(path)
    logger.info(f"binary data is loaded from {path}")
    return data



@ensure_annotations
def get_size(path:Path)->str:
    """give size of file in kb"""


    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} kb"