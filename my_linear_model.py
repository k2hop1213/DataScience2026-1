import numpy as np
class MySimpleLinearRegression:
    def __init__(self):
        self.coef_ =None
        self.intercept_ = None

    def fit(self, X, Y):
        x = X[:,0]
        y = Y[:,0]

        xm = x.mean()
        ym = y.mean()
        ss = np.sum((x - xm)*(y - ym))
        xx = np.sum((x - xm)**2)
        self.coef_ = ss/xx
        self.intercept_ = ym - self.coef_ * xm
    
    def predict(self,X):
        x = X[:,0]
        return (self.intercept_ + self.coef_*x).reshape(-1,1)
    
