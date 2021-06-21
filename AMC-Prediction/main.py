import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web
import datetime as dt


from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# Load Data

company = 'AMC'

start = dt.datetime(2021,1,1)
end = dt.datetime(2021,6,21)

data = web.DataReader(company, 'yahoo', start, end)

# Prepare Data
scaler =