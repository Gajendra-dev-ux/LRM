import pandas as pd
import statsmodels.api as sm

class SimpleLinearRegression:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.x=sm.add_constant(self.x)

    def fit(self):
        model=sm.OLS(self.y,self.x).fit()
        return model
    
    def summary(self):
        model=self.fit()
        print(model.summary())
        return model
    
""" # Sample data
data = {
    "TV": [230.1, 44.5, 17.2, 151.5, 180.8],
    "Sales": [22.1, 10.4, 9.3, 18.5, 12.9]
}
df = pd.DataFrame(data)
X = df[["TV"]]
y = df["Sales"]

# Create an instance of SimpleLinearRegression with the feature and target variable
regression = SimpleLinearRegression(X, y)

# Fit the model and print the summary
model = regression.summary()
 """