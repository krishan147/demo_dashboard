data = {'list 1':[2,4,6,8],'list 2':[4,16,36,64]}

import pandas as pd #To Convert your lists to pandas data frames convert your lists into pandas dataframes

df = pd.DataFrame(data, columns = ['list 1','list 2'])

from scipy import stats # For in-built method to get PCC

pearson_coef, p_value = stats.pearsonr(df["list 1"], df["list 2"]) #define the columns to perform calculations on
print("Pearson correlation coefficient: ", pearson_coef, "and a P-value of:", p_value)