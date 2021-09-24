# common library
import pandas as pd
import numpy as np
import time
from stable_baselines.common.vec_env import DummyVecEnv

# preprocessor
from preprocessing.preprocessors import *
# config
from config.config import *
# model
from model.models import *
import os

def run_model() -> None:
    """Train the model."""

    # read and preprocess data
    if os.path.exists(config.PREPROCESSED_PATH):
        data = pd.read_csv(config.PREPROCESSED_PATH, index_col=0)
    else:
        data = preprocess_data()
        data = add_turbulence(data)
        data.to_csv(config.PREPROCESSED_PATH)

    print(data.head())
    print(data.size)

    # 2015/10/01 is the date that validation starts
    # 2016/01/01 is the date that real trading starts
    # unique_trade_date needs to start from 2015/10/01 for validation purpose
    unique_trade_date = data[(data.datadate > config.START_VALIDATION)&(data.datadate <= config.ALMOST_END_TRADING)].datadate.unique()
    print(unique_trade_date)


    
    ## Ensemble Strategy
    run_ensemble_strategy(df=data, 
                          unique_trade_date= unique_trade_date,
                          rebalance_window = config.REBALANCE_WINDOW,
                          validation_window=config.VALIDATION_WINDOW)

    #_logger.info(f"saving model version: {_version}")

if __name__ == "__main__":
    run_model()
