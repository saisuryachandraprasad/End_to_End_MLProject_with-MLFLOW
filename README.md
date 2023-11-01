# End_to_End_MLProject_with-MLFLOW


# workflows

1.upate config.yaml

2.update schema.yaml

3.update params.yaml

4.update entity

5.update configuration manager in src/config

6.update components

7.update the pipeline

8.update the main.py

9.update app.py


# How to Run

### steps
 Clone the repository

```bash

 https://github.com/saisuryachandraprasad/End_to_End_MLProject_with-MLFLOW
```

### step-1
 ```bash
 conda create -p venv python==3.9
 ```

 ### step-2

 ``` bash
 conda env list
 conda activate YOUR VENV NAME
 ```

### step-03 Install required requirements
 ```bash
 pip install -r requirements.txt
 ```

 ### step-04 
 ```bash
 python app.py
 ```




 # MLFLOW


#### cmd
- mlflow ui


### dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/saisuryachandraprasad/End_to_End_MLProject_with-MLFLOW.mlflow \
MLFLOW_TRACKING_USERNAME=saisuryachandraprasad \
MLFLOW_TRACKING_PASSWORD=2dcd3ae6674d1754dae248d34dd8cce9a5c5aa0c  \
python script.py


Run this to export as env variable

```bash

export MLFLOW_TRACKING_URI = https://dagshub.com/saisuryachandraprasad/End_to_End_MLProject_with-MLFLOW.mlflow

export MLFLOW_TRACKING_USERNAME = saisuryachandraprasad

export MLFLOW_TRACKING_PASSWORD = 2dcd3ae6674d1754dae248d34dd8cce9a5c5aa0c
```