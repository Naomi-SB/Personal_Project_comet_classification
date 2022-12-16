# Personal_Project_comet_classification

**The main goal of this project is to get exposed to working with astronomical data**
* With this goal in mind, the project was a sucess!

# Data Acquisition 
 * data was downloaded to a csv file using a filtering user interface from NASA JPL website
 * I engaged the hyperbolic and parabolic filters
 
# Data Prepartaion
| Feature | Definition | Reason |
|:--------|:-----------|:----------|
|<img width=50/>|<img width=100/>|<img width=50/>|<img width=150/>|
|||**Dropped Columns**
|<img width=50/>|<img width=100/>|<img width=50/>|<img width=150/>|
|*e*|  eccentricity | The eccentricity defines the orbit class
|*A1*| non-grav radial parameter | Excessive null values
|*A2*| non-grav transverse parameter | Excessive null values
|*A3*| non-grav normal parameter | Excessive null values
|*D*| non-gravperihelion maximum offset | Excessive null values
|||**Dropped Rows**
<img width=50/>|<img width=100/>|<img width=50/>|<img width=150/>|
|*2 rows for tp_cal*| time of perihelion calculated | Dates were negative; assuming this means B.C.E
|*3 rows for data_arc *| Number of days spanned by the data arc | null values could not be imputed
|||**Altered Data**
||<img width=150/>|<img width=550/>|
|*tp_cal*| time of perihelion calculated | object data type could not be converted in Pandas as the time span is too large. Modified by dropping month, day, and time information. Resulting year was converted to int64|
|*two_body*| two-body dynamics used | Original data was T/F. Used dummies to get three columns for True, False, and Nans
|*full_name*| the name of the comet | Fit to index|
|*All*| all columns | Name changed to be more human readable|

## Data Dictionary

| Feature | Definition | Layman's Terms |
|:--------|:-----------|:----------|
|<img width=50/>|<img width=100/>|<img width=50/>|<img width=150/>|
|||**Data**
|<img width=50/>|<img width=100/>|<img width=50/>|<img width=150/>|
|*perihelion*|  The point nearest to the sun in the path of an orbiting celestial body  | Where the comet is closest to the sun
|*peri_distance*| The distance between the sun and an orbiting body when it at perihelion | How far the comet is from the sun when it is as close as it gets to the sun
|*time_of_peri*| The calculated time period of perihelion | What day on Earth it was/will be when the comet was closest to the sun
|*inclination*| the angle between the orbital plane of the object and the plane of the ecliptic | Measures the tilt of the comet's orbit
|*node*| the intersection of the orbit plane of some celestial body with the plane of the ecliptic  | The point where inclination 'pokes through'
|*days_of_data_arc*| the time period between its earliest and latest observations, used for tracing the body's path | The number of days the comet could be observed
|||**Two Body**
|*two_body*| two-body dynamics used |
|*True *| Number of days spanned by the data arc | null values could not be imputed
|*False*| time of perihelion calculated | object data type could not be converted in Pandas as the time span is too large. Modified by dropping month, day, and time information. Resulting year was converted to int64|
|*nan*| two-body dynamics used | Original data was T/F. Used dummies to get three columns for True, False, and Nans

# Data Split
* the data was originaly split into three dataframes for train, validate, and test
* the data was split a second time to create 6 dataframes the X's for train, validate, and test hold all features in the repective mother dataframes with the exception of 'orbit' which is the target variable. Y train, validate, and test are dataframes that only hold the target vaiable

# Exploration
* For this project I began my exploration by jumping right into statistical testing. I set parameters to separte the data based on orbit class and ran independedent T-tests comparing the means of all continuous features of Parabolic vs Hyperparabolic.
* Based off the results of my independent T-test I determined the relevent features to be perihelion distance, the degree of the node, degree of perihelion, and the time of perihelion. So I generated histograms to explore these features.
* These visualizations made it clear, that my data is not normally distributed. I decided to go back and use an independent statistical test where normalization is not assumed. I used the Mann-Whitney test, and ran all the continuous features
## Stat Tests
* by the Mann-Whitney statistical test we can see that all features are significant and should be used to create the best model.

# Scaling
* Because programing languages read all data as potatoes I needed to scale the data so they would be read as the same units
* I decided to use a standard scaler to get the standard deviation to 1

# Modeling
* I ran all continuous features (with the exception of orbit) through four models
* The four models I ran the X train and validate sets through were KNearest Neighbors, Decision Tree, Random Forest, and Logistic Regression
* The results of modeling were about 98% accuracy for predicting orbit class for train and validate
* I decided to use Random Froest for my test data which resulted in 97% accuracy. 

# Takeaways
* astonomical data can be incestuous
* caution is required when selecting features for exploration and modeling

# Recomendations
* if i could do this project again, I would change my target for prediction and use the features to try and determine how accurate past predictions of comet orbits could actually be
























*


