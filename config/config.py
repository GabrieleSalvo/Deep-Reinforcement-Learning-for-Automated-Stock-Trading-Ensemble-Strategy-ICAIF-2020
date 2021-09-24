# from env.EnvMultipleStock_trade import STOCK_DIM
import pathlib

#import finrl

import pandas as pd
import datetime
import os
#pd.options.display.max_rows = 10
#pd.options.display.max_columns = 10


#PACKAGE_ROOT = pathlib.Path(finrl.__file__).resolve().parent
#PACKAGE_ROOT = pathlib.Path().resolve().parent

#TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
#DATASET_DIR = PACKAGE_ROOT / "data"

# data
#TRAINING_DATA_FILE = "data/ETF_SPY_2009_2020.csv"
# TRAINING_DATA_FILE = "data/dow_30_2009_2020.csv"
TRAINING_DATA_FILE = "data/nasdaq_100_daily.csv"


now = datetime.datetime.now().strftime("%y_%m_%d_%H_%M_%S")
TURBULENCE_DATA = "data/dow30_turbulence_index.csv"

TESTING_DATA_FILE = "test.csv"
nasdaq_data = True
if nasdaq_data:
    TRAINED_MODEL_DIR = f"./trained_models/nasdaq/{now}"
    PREPROCESSED_PATH = "nasdaq_done_data.csv"
    START_DATASET = 20181023
    START_VALIDATION = 20190523
    START_TRADING = 20190624
    ALMOST_END_TRADING = 20191020
    END_DATASET = 20191023
    REBALANCE_WINDOW = 21
    VALIDATION_WINDOW = 21
    STOCK_DIM = 101
    TRANSACTION_FEE_PERCENT = 0.0015

else:
    TRAINED_MODEL_DIR = f"./trained_models/{now}"
    PREPROCESSED_PATH = "done_data.csv"
    START_DATASET = 20090101
    START_VALIDATION = 20151001
    START_TRADING = 20160101
    ALMOST_END_TRADING = 20200707
    END_DATASET = 20200805
    # rebalance_window is the number of months to retrain the model
    # validation_window is the number of months to validation the model and select for trading
    REBALANCE_WINDOW = 63
    VALIDATION_WINDOW = 63
    STOCK_DIM = 30
    TRANSACTION_FEE_PERCENT = 0.001


os.makedirs(TRAINED_MODEL_DIR)



