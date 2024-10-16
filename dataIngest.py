import pandas as pd

class DataIngestion:
    def __init__(self,filePath):
        self.filePath=filePath
    
    def loadData(self):
        data=pd.read_csv(self.filePath)
        return data
    
    def get_X_y(self):
        data=self.loadData()
        X=data[["TV"]]
        y=data[["Sales"]]
        df=pd.concat([X,y],axis=1)
        return X,y,df

""" # Create an instance of DataIngestion with the file path
data_ingestion = DataIngestion('data\Advertising.csv')

# Load the data
data = data_ingestion.loadData()

# Get the feature, target, and combined DataFrame
X, y, df = data_ingestion.get_X_y()

# Display the data
print(df.head())
 """