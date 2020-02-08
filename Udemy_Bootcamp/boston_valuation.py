from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

# Gather Data
boston_dataset = load_boston()
data = pd.DataFrame(data=boston_dataset.data, columns=boston_dataset.feature_names)
features = data.drop(['INDUS', 'AGE'], axis=1)

log_prices = np.log(boston_dataset.target)
target = pd.DataFrame(log_prices, columns=['PRICE'])
target.shape

CRIME_IDX = 0
ZN_IDX = 1
CHAS_IDX = 2
RM_IDX = 4
PRTRATIO_IDX = 8

# Update prices based on Zillow webside

ZILLOW_MEDIAN_PRICE = 583.3
SCALE_FACTOR = ZILLOW_MEDIAN_PRICE / np.median(boston_dataset.target)

property_stats = features.mean().values.reshape(1, 11) # we have to reshape 'features' into 2D array
# 'property_stats' is like a template for our prediction

regr = LinearRegression().fit(features, target)
fitted_vals = regr.predict(features)

# MSE & RMSE
MSE = mean_squared_error(target, fitted_vals)
RMSE = np.sqrt(MSE)

def get_log_estimate(nr_rooms, 
                     students_per_classroom,
                     next_to_river=False, 
                     high_confidence=True):
  
  # Configure property
  property_stats[0][RM_IDX] = nr_rooms
  property_stats[0][PRTRATIO_IDX] = students_per_classroom
  
  if next_to_river:
    property_stats[0][CHAS_IDX] = 1
  else:
    property_stats[0][CHAS_IDX] = 0


  # Make prediction
  log_estimate = regr.predict(property_stats)[0][0]

  # Calc Range
  if high_confidence:
    upper_bound = log_estimate + 2*RMSE
    lower_bound = log_estimate - 2*RMSE
    interval = 95
  else:
    upper_bound = log_estimate + RMSE
    lower_bound = log_estimate - RMSE
    interval = 68

  return log_estimate, upper_bound, lower_bound, interval


def get_dollar_estimate(rm, ptration, chas=False, large_range=True):

  '''Estimate the price of a property in Boston.

  Keyword arguments:
  
  rm == number of room in the property

  ptration == number of students per teacher in the classroom for the school in the area
  
  chas == True if the property is next to the river, False otherwise
  
  large_range == True for a 95% prediction interval, False for a 68% interval.

  '''

  if rm < 1 or ptration < 1:
    print('That is unrealistic. Try again.')
    return
  
  log_est, upper, lower, conf = get_log_estimate(rm, students_per_classroom=ptration, next_to_river=chas, high_confidence=large_range)

  # Convert to today's dollars
  dollar_est = np.e**log_est * 1000 * SCALE_FACTOR
  dollar_high = np.e**upper * 1000 * SCALE_FACTOR
  dollar_low = np.e**lower * 1000 * SCALE_FACTOR

  # Round the dollar values to nearest thousand
  rounded_est = np.around(dollar_est, -3)
  rounded_high = np.around(dollar_high, -3)
  rounded_low = np.around(dollar_low, -3)

  print(f'The estimated property value is {rounded_est}.')
  print(f'At {conf}% confidence the valuation range is')
  print(f'USD {rounded_low} at the lower end to USD {rounded_high} at the high end.')
