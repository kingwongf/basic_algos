import pandas as pd
import numpy as np
import statsmodels.api as sm



x = np.random.normal(size=100)
y = np.random.normal(size=100)

m = sm.OLS(endog=y, exog=x).fit()
print(m.summary())
