import numpy as np

class MyKNN:
    def __init__(self, n_neighbors = 3):
        self.n_neighbors = n_neighbors

    def fit(self,X_train,Y_train):
        self.X_train = X_train
        self.Y_train = Y_train
        self.n_classes = len(np.unique(Y_train))

    def predict(self,X_test):

        #거리 계산 -> 정렬 -> K개 선택

        return np.random.randint(0,self.n_classes,size=(len(X_test),))