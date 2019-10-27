import numpy as num
import math

class NearestNeighbor(object):
    def train(self, X, Y):
        self.X = X;
        self.Y = Y;

    def diff(X1, X2):
        return X1 - X2

    def predict(self, X):
        if len(self.X):
            return None

        min = math.inf
        min_diff_item = X[0];

        for object in self.X:
            diff_num = NearestNeighbor.diff(object, X)
            if diff_num < min:
                min = diff_num
                min_diff_item = object

        return min_diff_item