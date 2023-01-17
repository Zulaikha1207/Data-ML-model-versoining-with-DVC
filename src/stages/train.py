import argparse
import joblib
import pandas as pd
from typing import Text
import yaml

from src.train.train import train

def train_model(config_path: Text) -> None:
    
    with open("params.yaml") as config_file:
        config = yaml.safe_load(config_file)
        
    # Get X and Y
    print("Get X_train and y_train")
    train_dataset = pd.read_csv(config["train"]["trainset_path"])
    
    print('Get estimator name')
    estimator_name = config['model']['estimator_name']
    
    print('Fitting model..')
    model = train(df=train_dataset,
                 target_column=config['features']['target_column'],
                 estimator_name=estimator_name,
                 param_grid= config['model']['estimators'][estimator_name]['param_grid'],
                 cv=config['model']['cv'])
    
    print(f'Best score: {model.best_score_}')
    
    print('Saving model..')
    model_path= config["model"]["model_path"]
    joblib.dump(model, model_path)

if __name__=='__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    train_model(config_path=args.config)