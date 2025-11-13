from dataclasses import dataclass
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import StudentPerformanceException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    """Define where the output files will be located"""
    artifact_path:str = os.path.join("artifacts")
    data_train_file_path: str = os.path.join(artifact_path, "train.csv")
    data_test_file_path: str = os.path.join(artifact_path, "test.csv")
    raw_data_file_path: str = os.path.join(artifact_path, "raw.csv")

class DataIngestion:
    """Tread data from data source"""
    def __init__(self)-> DataIngestionConfig:
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df =  pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the dataset as DataFrame')

            os.makedirs(os.path.dirname(self.ingestion_config.data_train_file_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_file_path, index=False, header=True)
            # = os.makedirs(os.path.dirname('artifacts/train.csv'), exist_ok=True) = os.path.dirname('artifacts/train.csv')  →  'artifacts'
            df.to_csv(self.ingestion_config.raw_data_file_path, index=False, header=True)
            logging.info('Train and Test Splitting Initiated')
            train_set, test_set = train_test_split(df, test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.data_train_file_path, index=False, header = True)
            test_set.to_csv(self.ingestion_config.data_test_file_path, index=False, header = True)
            logging.info('Data Ingestion Completed!')
            return (
                self.ingestion_config.data_train_file_path,
                self.ingestion_config.data_test_file_path,
            )
        except Exception as e:
            raise StudentPerformanceException(e,sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    transformation_obj = DataTransformation()
    train_arr, test_arr, _= transformation_obj.initiate_data_transformation(train_data,test_data)

    model_trainer_obj = ModelTrainer()
    print(model_trainer_obj.initiate_model_trainer(train_array=train_arr, test_array=test_arr))
