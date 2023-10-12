import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import math
import statsmodels.formula.api as smf
import datetime
from statsmodels.api import add_constant
from linearmodels import IV2SLS
from linearmodels import PanelOLS


url = "https://github.com/MartinFrancoIrabedra/Regression-with-fixed-effects/blob/main/data/guns.dta"
data = pd.read_stata(url, index_col=0)
data.to_csv(url)
print(data)


##### Run a regression of ln(vio) against shall on the pooled data set.

#### vio being crime rate (incidents per 100,000 members of the population),
#### rob being robbery rate (incidents per 100,000),
#### mur being murder rate (incidents per 100,000),
#### shall being = 1 if the state has a shall-carry law in effect in that year and = 0 otherwise. 




data['vio_ln'] = np.log(data.vio)

model_1 = smf.ols("vio_ln~shall", data=data).fit(cov_type="HC1")
print(model_1.summary())

#### shall variable is -0.443

#### Since it is statistically significant we can suggest that shall issue laws may reduce crime but we are still threathened by biases.

#### Lets add some control variables

model_2 = smf.ols("vio_ln~ shall + incarc_rate + pb1064 + pw1064 + pm1029 + pop + avginc + density", data=data).fit(cov_type="HC1")
print(model_2.summary())

#### incarc_rate is the incarceration rate in the state in the previous year (sentenced prisoners per 100,000 residents; value for the previous year),
#### pb1064 is the percentage of state population that is white, ages 10 to 64,
#### pw1064 is the percent of state population that is black, ages 10 to 64,
#### pm1029 is the percent of state population that is male, ages 10 to 29,
#### pop is state population (in millions)
#### avginc is real per capita personal income in the state, in thousands of dollars,
#### and density is the population per square mile of land area, divided by 1000.

#### We can see that the Condition Number is very large (1.28e+04) which can mean the model has multicolinearity problems.


#### Now lets apply fixed effects which accounts for time invariant characteristics.
#### A state fixed effect for example will control for all unobserved factors that remain the same in a state over time.

model_3 = smf.ols("vio_ln~shall + C(stateid) ", data=data).fit(cov_type="HC1")
print(model_3.summary())

#### Now lets add a year fixed effect 

model_4 = smf.ols("vio_ln~shall + C(stateid) + C(year) ", data=data).fit(cov_type="HC1")
print(model_4.summary())

#### with the covariates

model_5 = smf.ols("vio_ln~ shall + incarc_rate + pb1064 + pw1064 + pm1029 + pop + avginc + density + C(stateid) + C(year)", data=data).fit(cov_type="HC1")
print(model_5.summary())

#### We see that by adding the fixed effects the results turned positive (0.0107) and it stopped being satistically significant.
#### We cannot conclude that the Shall Issue laws increased or decreased crime.











































































