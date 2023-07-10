# contain/have all the code that is related to reading the data and divide data into train and test 

from operator import index
import pandas as pd 
import numpy as np 


import os, sys
from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:

    raw_data_path:str = os.join.path("artifacts", "raw_data.csv")
    train_data_path:str = os.join.path("artifacts", "train_data.csv")
    test_data_path:str = os.join.path("artifacts", "test_data.csv")
    

class DataIngestion:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("initiate data ingestion")
        try:
            logging.info("reading input data as data frame")

            df = pd.read_csv("Notebook/stud.csv")
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok = True)
            df.to_csv(self.data_ingestion_config.raw_data_path, index= False, header=True)

            logging.info("train test split")

            train_set, test_set = train_test_split(df, test_size = 0.2, random_state = 42)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index= False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index= False, header=True)
            logging.info("data ingestion is completed")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e, sys)        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


