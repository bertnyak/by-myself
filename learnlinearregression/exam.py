import numpy as np
import pandas as pd


df = pd.read_csv('tvmarketing.csv')

class SimpleLinearRegression:
    coef = 0
    intercept = 0
    rsquared = 0
    def fit(self, x_train, y_train):
        sum_of_x = sum(x_train)
        sum_of_y = sum(y_train)
        sum_of_x2 = np.sum(np.square(x_train))
        sum_of_y2 = np.sum(np.square(y_train))
        dotproduct = np.dot(x_train,y_train)
        length = len(x_train)
        dif_x = sum_of_x2 - sum_of_x * sum_of_x/length
        dif_y = sum_of_y2 - sum_of_y * sum_of_y/length
        numerator = length * dotproduct - sum_of_x * sum_of_y
        denom = (length * sum_of_x2 - sum_of_x * sum_of_x) * (length * sum_of_y2 - (sum_of_y * sum_of_y))
        co = dotproduct - sum_of_x * sum_of_y / length
        self.rsquared = np.square(numerator / np.sqrt(denom))
        self.intercept = sum_of_y / length - ((co / dif_x) * sum_of_x/length)
        self.coef = co / dif_x
    def predict(self,x_test):
        return x_test * self.coef + self.intercept

x_train = np.array(df.TV)
y_train = np.array(df.Sales)

slr = SimpleLinearRegression()
slr.fit(x_train,y_train)
s = slr.coef
y_inter = slr.intercept
print(f"Coefficient: {s:.2f}")
print(f'Y-Intercept: {y_inter:.2f}')
print('R-Squared:',slr.rsquared)