import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Text
import yaml

def data_split(config_path: Text) -> None:
    """Split dataset into train/test.
    Args:
        config_path {Text}: path to config
    """
    
    with open("params.yaml") as config_file:
        config = yaml.safe_load(config_file)

    #load dataset and split using sklearn
    dataset = pd.read_csv(config["data"]["features_path"])
    train_dataset, test_dataset = train_test_split(dataset, 
        test_size=config["test"]["test_size"], 
        random_state=config["base"]["random_state"])
    print('Train data shape: ', train_dataset.shape)
    print("Test data shape: ", test_dataset.shape)
    
    # Save train and test sets
    print('Saving train and test sets..')
    trainset_path = config["train"]["trainset_path"]
    testset_path = config["test"]["testset_path"]
    print('Data split completed!')
    train_dataset.to_csv(trainset_path, index=False)
    test_dataset.to_csv(testset_path, index=False)


if __name__== '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_split(config_path=args.config)