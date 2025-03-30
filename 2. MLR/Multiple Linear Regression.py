Multiple Linear Regression

From warnings import filterwarnings
filterwarnings("ignore")

PROFIT ~  RND, ADMIN, MKT
PROFIT = B0 +B1*RND + B2*ADMIN + B3*MKT

Step 1 - Read the dataset

import pandas as pd
df = pd.read_csv("50_Startups.csv")
df.head()
