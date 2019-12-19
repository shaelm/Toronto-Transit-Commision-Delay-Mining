# Toronto TTC Streetcar Data Mining Project
Combining Toronto Open TTC Data with seperate weather data to mine frequent patterns that cause delays.

# External Links #

- GitHub Repository: https://github.com/shaelm/Toronto-Transit-Commision-Delay-Mining/
- Tableu Visualization: https://public.tableau.com/views/TTC_DM_Proj/DelaybyRain?:display_count=y&:origin=viz_share_link

# Data Sets Used #
https://toronto.weatherstats.ca/download.html - Download Climate Daily/Forecast/Sun- Toronto Weather Data
https://open.toronto.ca/dataset/ttc-streetcar-delay-data/ - Download All TTC StreetCar Delay Data

# Data Pre-Processing #

Weather data was downloaded for the same time frame as our streetcar delay data set. The two datasets were joined on their data. Daily snow,avg_wind_speed,avg_visibility,avg_hourly_temperature,rain was taken from the weather data set. This combined dataset was used to create categories for Rain,Snow,Wind,Visibility,Time of Day, Month of Year, Day of Week, Route number, Direction of StreetCar Travel, Delay amount,Temperature.


# Frequent Pattern Mining #


# Random Forest Regression #

One Hot Encoded FinalCategorizedData for the categorical variables. Used 40 estimators for the random forest ensemble
Model had:
Base line error of 10.62 minutes before training
Mean Prediction Error of 3.335 minutes after training




# Installing Dependencies #

We use conda to manage dependencies, install conda from https://docs.conda.io/projects/conda/en/latest/user-guide/install/ if you do not have it. The code was tested on conda version 4.7.12.

### Create the environment
1. Open the Conda Prompt
2. Run "conda env create -f environment.yml" using the environment.yml provided

### Activate the environment
1. Run "conda activate sjr-fall-2019-datamining-project"

This provides the dependencies needed for the python files.

# Download datasets #

Download the datasets from the links in the above section "Data Sets Used" and place them in a folder called 'datasets'. These should be
the downloaded datasets and they should be named as such.

- ttc-streetcar-delay-data-2014.xlsx
- ttc-streetcar-delay-data-2015.xlsx
- ttc-streetcar-delay-data-2016.xlsx
- ttc-streetcar-delay-data-2017.xlsx
- ttc-streetcar-delay-data-2018.xlsx
- ttc-streetcar-delay-data-2019.xlsx
- weatherstats_toronto_daily.csv

# Running the code #

You can recreate the processed datasets or just run the regressor and frequent pattern mining. Please make sure that a folder called 'datasets' exists with the datasets shown above, and a folder named 'processed_data' also exists. Both should be at the root level, on the same one as the python files.

### Run the regression
1. Run "python random_forest.py"

### Run the frequent pattern mining
1. Run "python mlxtend_test.py"

### Recreate the processed datasets
1. Run "python load_preproc.py"
2. Run "python preprocess_data.py"
3. Run "python Categorize_Data.py"
