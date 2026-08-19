import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import joblib

df = pd.read_csv("housing.csv")
# print(df)

# # data set information
# print(df.info())

# print(df.columns)

x=df.drop(columns=["Price","Address"])
y=df[["Price"]]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
score=r2_score(y_test,y_pred)
print("The r2 score is: ",score *100,"%")


joblib.dump(model,"house_price.pkl")
print("Model saved")