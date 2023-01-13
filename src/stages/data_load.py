import argparse
import pandas as pd
from sklearn.datasets import load_iris
from typing import Text
import yaml

def data_load(config_path: Text) -> None:

    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    data = load_iris(as_frame=True)
    dataset = data.frame

    # feature names
    dataset.columns = [colname.strip(' (cm)').replace(' ', '_') for colname in dataset.columns.tolist()]

    # Save raw data
    dataset.to_csv(config["data"]["dataset_csv"], index=False)

    print("Data load complete!")

#to run from CLI use a constructer that allows to parse config file as an argument to the data_load function
if __name__ == '__main__':
    
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)