import argparse
import pandas as pd
from typing import Text
import yaml

def featurize(config_path: Text) -> None:
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)
        
    print('Get raw data')    
    dataset = pd.read_csv(config["data"]["dataset_csv"])
    
    print('\nExtracting features..')   
    dataset['sepal_length_to_sepal_width'] = dataset['sepal_length'] / dataset['sepal_width']
    dataset['petal_length_to_petal_width'] = dataset['petal_length'] / dataset['petal_width']
    dataset = dataset[[
        'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
        'sepal_length_to_sepal_width', 'petal_length_to_petal_width',
        'target']]
    
    print(dataset.head())
    dataset.to_csv(config["data"]["features_path"], index=False)
    print('\nFeature engineering completed!') 

if __name__ == '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    featurize(config_path=args.config)
