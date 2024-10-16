import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class DataPreprocess:
    def __init__(self,df) :
        self.df=df
    
    def identify_outliers(self , data:pd.DataFrame):
        fig, ax=plt.subplots()
        ax.boxplot(data)
        ax.set_title("box plot of data")
        ax.set_ylabel("value")
        plt.show()
    
    def identify_outliers_zscore(self,data:pd.Series,threshold:float=3):
        mean=np.mean(data)
        std=np.std(data)
        z_score=(data-mean)/std
        outliers=data[np.abs(z_score)>threshold]
        return outliers
    
""" # Assuming df is your DataFrame
df = pd.DataFrame({
    "TV": [230.1, 44.5, 17.2, 151.5, 180.8],
    "Sales": [22.1, 10.4, 9.3, 18.5, 12.9]
})

# Create an instance of DataPreprocess with the DataFrame
data_preprocess = DataPreprocess(df)

# Identify outliers using box plot for the 'TV' column
data_preprocess.identify_outliers(df["TV"])

# Identify outliers using Z-score for the 'Sales' column
outliers = data_preprocess.identify_outliers_zscore(df["Sales"])
print("Outliers based on Z-score:\n", outliers)
 """