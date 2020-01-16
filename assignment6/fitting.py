#!/usr/bin/env python3
import data

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC



def fit(data_training, data_validation, classifier, xaxis, yaxis, n_neighbors=1):
     """Calls on the suited method for classifier calculation.

     args:
          data_training(pandas dataset): the training dataset
          data_validation(pandas_dataset): the validation dataset
          classifier(classifier): trained classifier
          xaxis(string): feature for the x-axis
          yaxis(string): feature for the y-axis
          n_neighbors(int): number of neighbors for the KNN calculation


     return:
          trained accuray, prediction accuracy(str): metrics.accuracy_score

     """



     if(classifier.lower() == "svc"):
          return SVC_classifier(data_training, data_validation, xaxis, yaxis)
     elif(classifier.lower() == "knn"):
          return KNN_classifier(data_training, data_validation, xaxis, yaxis, n_neighbors)
     else: "Sorry, this classifier is not implemented."



def SVC_classifier(data_training, data_validation, xaxis, yaxis):
     """The function calculates a trained classifier using Support Vector 
     Classifier (SVC).

     args:
          data_training(pandas dataset): the training dataset
          data_validation(pandas_dataset): the validation dataset
          xaxis(string): feature for the x-axis
          yaxis(string): feature for the y-axis

     ret:
          logreg(classifier): trained classifier
     
     """
     X_train = data_training[[xaxis, yaxis]]
     y_train = data_training[["diabetes"]]

     X_val = data_validation[[xaxis, yaxis]]
     y_val = data_validation[["diabetes"]]

     logreg = SVC(gamma='scale')
     logreg.fit(X_train, y_train.values.ravel())
     
     y_pred = logreg.predict(X_val)
     
     return logreg



def KNN_classifier(data_training, data_validation, xaxis, yaxis, n):
     """The function calculates a trained classifier using the k-nearest 
     neighbors (KNN) algorithm.

     args:
          data_training(pandas dataset): the training dataset
          data_validation(pandas_dataset): the validation dataset
          xaxis(string): feature for the x-axis
          yaxis(string): feature for the y-axis
          n(int): number of neighbors for the calculation

     ret:
          logreg(classifier): trained classifier
     
     """
     X_train = data_training[[xaxis, yaxis]]
     y_train = data_training[["diabetes"]]

     X_val = data_validation[[xaxis, yaxis]]
     y_val = data_validation[["diabetes"]]
     
     knn = KNeighborsClassifier(n_neighbors=n)
     knn.fit(X_train, y_train.values.ravel())

     y_pred = knn.predict(X_val)

     return knn

  

def getAccuracy(data_training, data_validation, classifier, xaxis, yaxis):
     """Calculates the accuracy score for both the training set and validation
     set by predicting with the classifier.

     args:
          data_training(pandas dataset): the training dataset
          data_validation(pandas_dataset): the validation dataset
          classifier(classifier): trained classifier
          xaxis(string): feature for the x-axis
          yaxis(string): feature for the y-axis


     return:
          trained accuray, prediction accuracy(str): metrics.accuracy_score

     """

     X_train, y_train = data_training[[xaxis, yaxis]], data_training[["diabetes"]]
     X_val, y_val = data_validation[[xaxis, yaxis]], data_validation[["diabetes"]]

     classifier = fit(data_training, data_validation, classifier, xaxis, yaxis, n_neighbors=1)

     y_pred = classifier.predict(X_val)
     y_train = classifier.predict(X_train)

     return str(round(metrics.accuracy_score(y_train, y_train), 2)), str(round(metrics.accuracy_score(y_val, y_pred), 2))




def main(): 
     """Simple main program to test the methods of the file.
     
    """
     feature_x, feature_y, classifier = "", "", ""
     data_training, data_validation = data.extract_data("diabetes.csv")
     while classifier == "" or classifier != "svc" and classifier != "knn":
          classifier = input("ENTER CLASSIFIER\nSVC or KNN?\n(Enter 'q' to exit)\n>").lower()
          if classifier == "q": exit(0)
          if classifier != "svc" and classifier != "knn": print("\n\nInput is not a valid classifier, try again..")
     feature_string = "ENTER {} FEATURE\npregnant\nglucose\npressure\ntriceps\ninsulin\nmass\npedigree\nage\n(Enter 'q' to exit)\n>"
     while feature_x == "" or feature_x not in list(data_training):
          feature_x = input("\n" + feature_string.format("FIRST")).lower()
          if feature_x == "q": exit(0)
          if feature_x not in list(data_training): print("\n\nInput is not a valid feature, try again..")
     while feature_y == "" or feature_y not in list(data_training):
          feature_y = input("\n" + feature_string.replace(feature_x + "\n", "").format("SECOND")).lower()
          if feature_y == "q": exit(0)
          if feature_y not in list(data_training): print("\n\nInput is not a valid feature, try again..")
     fit(data_training, data_validation, classifier, feature_x, feature_y)
     acc_train, acc_val = getAccuracy(data_training, data_validation, classifier, feature_x, feature_y)
     print("\nAccuracy for features {} and {} (using {}):\ntraining set: {}\nvalidation set: {}".format(feature_x, feature_y, classifier.upper(), acc_train, acc_val))

     
     
if __name__ == '__main__':
    main()
