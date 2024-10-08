import os
import sys
from source.exception import CustomException 
from source.logger import logging
import pandas as pd


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from source.components.data_transformation import DataTransformation , DataTransformationConfig

from source.components.model_trainer import ModelTrainer , ModelTrainerConfig



@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

        
    def initiate_data_ingestion(self):


        logging.info("data ingestion process started")

        try:
            df = pd.read_csv("notebook\data\stud.csv")
            logging.info("data read as dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.data_ingestion_config.raw_data_path , index = False , header=True)

            logging.info("Train Test Split initiated.")
            train_set , test_set = train_test_split(df , test_size=0.2 , random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path , index=False , header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path , index=False , header=True)

            logging.info("Train Test Split completed")
            logging.info("Ingestion of data completed.")

            return(
                self.data_ingestion_config.train_data_path , 
                self.data_ingestion_config.test_data_path
            )



        except Exception as e:
            raise CustomException(e,sys)
            

if __name__ == "__main__":


    obj = DataIngestion()
    train_path , test_path = obj.initiate_data_ingestion()

    obj2 = DataTransformation()

   # preprocessor = obj2.get_data_transformer_object()

    train_arr,test_arr ,preprocessor_file_path = obj2.initiate_data_transformation(train_path=train_path , test_path=test_path)

    trained_model = ModelTrainer()

    trained_model.initiate_model_trainer(train_arr, test_arr)












                




        

