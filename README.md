# Toronto TTC Streetcar Data Mining Project
Combining Toronto Open TTC Data with seperate weather data to mine frequent patterns that cause delays.

# Data Sets Used #
https://toronto.weatherstats.ca/download.html- Download Climate Daily/Forecast/Sun- Toronto Weather Data
https://open.toronto.ca/dataset/ttc-streetcar-delay-data/- TTC StreetCar Delay Data

# Data Pre-Processing #

Weather data was downloaded for the same time frame as our streetcar delay data set. The two datasets were joined on their data. Daily snow,avg_wind_speed,avg_visibility,avg_hourly_temperature,rain was taken from the weather data set. This combined dataset was used to create categories for Rain,Snow,Wind,Visibility,Time of Day, Month of Year, Day of Week, Route number, Direction of StreetCar Travel, Delay amount,Temperature.


# Frequent Pattern Mining #


# Random Forest Regression #

One Hot Encoded FinalCategorizedData for the categorical variables. Used 40 estimators for the random forest ensemble
Model had:
Base line error of 10.62 minutes before training
Mean Prediction Error of 3.335 minutes after training








