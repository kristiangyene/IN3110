#!/usr/bin/env python3
import fitting
import data
import os

import numpy as np
import pylab as plt
from matplotlib.colors import ListedColormap



def plot_diabetes(data_training, data_validation, classifier, xaxis, yaxis):
    """Adds colored areas that represent which class the classifier predicts in 
    that area. Colors the areas in a slightly lighter color compared to the data 
    points of the same class so that you can see them.

     args:
        data_training(pandas dataset): the training dataset
        data_validation(pandas_dataset): the validation dataset
        classifier(classifier): trained classifier
        xaxis(string): feature for the x-axis
        yaxis(string): feature for the y-axis


     return:
          trained accuray, prediction accuracy(str): metrics.accuracy_score

    """

    cmap_light = ListedColormap(['#AAFFAA', '#FFAAAA']) #Colorcodes for colored areas

    X_train = data_training[[xaxis, yaxis]]
    y_train = data_training[["diabetes"]]

    X_val = data_validation[[xaxis, yaxis]]
    y_val = data_validation[["diabetes"]]

    #Calculate the colored areas
    classifier.fit(X_train, y_train.values.ravel())
    x_min, x_max = X_train[[xaxis]].min() - .1, X_train[[xaxis]].max() + .1
    y_min, y_max = X_train[[yaxis]].min() - .1, X_train[[yaxis]].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    #Put in colored areas
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    #Put points in the plot
    pos_train, neg_train = data.get_splitted_dataset(data_training, xaxis, yaxis)
    plt.scatter(pos_train[[xaxis]], pos_train[[yaxis]], color='r', label="pos")
    plt.scatter(neg_train[[xaxis]], neg_train[[yaxis]], color='g', label="neg")

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title("Data Visualizing")
    plt.legend(loc="upper right", title="diabetes")


    if not os.path. exists("static"):
        os.makedirs("static")
    plt.savefig("static/plot.jpg") #For webpage

    return plt


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
    plot_diabetes(data_training, data_validation, fitting.fit(data_training, data_validation, classifier, feature_x, feature_y), feature_x, feature_y).show()


if __name__ == '__main__':
    main()
