from buildModel import SimpleLinearRegression
from dataIngest import DataIngestion
from dataPreprocess import DataPreprocess

data_ingest=DataIngestion("./data/Advertising.csv")

X,y,df=data_ingest.get_X_y()
df.to_csv("./data/Simple3.csv",index=False)
data_process=DataPreprocess(df)

outliers=data_process.identify_outliers_zscore(df["TV"])


lr_model=SimpleLinearRegression(X,y)
model=lr_model.summary()
