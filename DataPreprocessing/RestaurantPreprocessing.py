import numpy as np
import pandas as pd

# load csv data in pandas
df = pd.read_csv(r'Cairo_Final1.csv')

# drop some of the columns which won't contribute much to our machine learning model
# cols = ['special_diets','open_time','close_time','meals','price_range']
# df = df.drop(cols , axis = 1)

# drop null values
df = df.dropna()

# drop None values
df = df.replace(to_replace='None', value=np.nan).dropna()
df = df.replace(to_replace='Non', value=np.nan).dropna()
print(df)
number_of_reviews=[]
for i in df['number of reviews']:
    # remove reviews word
    new_value= i[:(len(i) - 8)]
    # remove comma
    new_value=new_value.replace(",", "")
    number_of_reviews.append(new_value)

df['number of reviews'] = number_of_reviews
df.to_csv('Cairo_Final_2.csv')
