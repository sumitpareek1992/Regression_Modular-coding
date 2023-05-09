from src.components.data_ingesion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initia_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initaite_data_transformation(train_data,test_data)
    models_trainer=ModelTrainer()
    models_trainer.initate_model_training(train_arr,test_arr)