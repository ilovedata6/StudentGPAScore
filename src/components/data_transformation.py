import pandas as pd 
import numpy as np
import os
import sys

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.exception import  CustomException
from src.logger import logging
from src.utils import save_object

from dataclasses import dataclass


@dataclass
class DataTransformationConfig:
    """Data Transformation Configuartion Class"""
    preprocessor_obj_path : str = os.path.join('artifacts','preprocessor.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_data_transformation_obj(self):
        '''
        This method is used to get the data Transformation Pipeline
        '''
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
]
            
            numerical_pipeline = Pipeline(
                steps = [
                    ('imputer',SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
])
            logging.info("Numberical Columns Transformation Pipeline Created")
            
            categorical_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy="most_frequent")),
                    ("encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
])            
            logging.info("Categorical Columns Transformation Pipeline Created")
            
            preprocessor = ColumnTransformer(
                [
                    ("numerical",numerical_pipeline,numerical_columns),
                    ("categorical",categorical_pipeline,categorical_columns)
                ])
            
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
        
    def initiate_transformation(self,train_path,test_path):
        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            
            logging.info("The Train and Test data has been loaded")
            
            logging.info("Obtaining Preprocessing Object")
            
            preprocessor = self.get_data_transformation_obj()
            
            target_column = "math_score"
            
            training_features = train_data.drop(columns=[target_column],axis=1)
            training_target = train_data[target_column]
            
            testing_features = test_data.drop(columns=[target_column],axis=1)
            testing_target = test_data[target_column]
            
            logging.info("Applying Feature Engineering on train and test Data using Preprocessing Pipeline")
            
            training_features_arr = preprocessor.fit_transform(training_features)
            testing_features_arr = preprocessor.transform(testing_features)
            
            
            training_arr = np.c_[
                training_features_arr,np.array(training_target)
            ]
            testing_arr = np.c_[
                testing_features_arr,np.array(testing_target)
            ]
            
            logging.info("Saving Preprocessor Object")
            
            save_object(
                self.data_transformation_config.preprocessor_obj_path,preprocessor
            )
            logging.info("successfully saved preprocessing object!")
            return (
                training_arr,
                testing_arr,
                preprocessor
            )
            
        except Exception as e:
            raise CustomException(e,sys)