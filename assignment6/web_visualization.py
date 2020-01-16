#!/usr/bin/env python3

import os
import visualize
import fitting
import data

from flask import Flask, render_template, request, url_for
import matplotlib

matplotlib.use('Agg')

classifiers = ['knn', 'svc']
features = ["pregnant", "glucose", "pressure", "triceps", "insulin", "mass", "pedigree", "age"]
data_training, data_validation = data.extract_data("diabetes.csv")


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def root():
    return render_template('frontpage.html')


@app.route("/plot")
def plot(error=False):
    plt = visualize.plot_diabetes(data_training, data_validation, fitting.fit(data_training, data_validation, classifiers[0], features[0], features[1]), features[0], features[1])
    acc_train, acc_val = fitting.getAccuracy(data_training, data_validation, classifiers[0], features[0], features[1])
    return render_template('show_plot.html', error=error, classifiers=classifiers, features=features, p1=acc_train, p2=acc_val)


@app.route("/values_changed", methods=['POST'])
def val_changed():
    classifier = request.form["classifiers"]
    x_feature = request.form["x_features"]
    y_feature = request.form["y_features"]
    try:
        plt = visualize.plot_diabetes(data_training, data_validation, fitting.fit(data_training, data_validation, classifier, x_feature, y_feature), x_feature, y_feature)
        acc_train, acc_val = fitting.getAccuracy(data_training, data_validation, classifiers[0], features[0], features[1])

    except AssertionError as e:
        print(e)
        return plot(error=True)
    return render_template('show_plot.html', error=False, classifiers=classifiers, features=features, p1=acc_train, p2=acc_val)



@app.route('/help')
def helper():
    return render_template('help.html')


@app.after_request
def add_header(response):
    response.headers["Cache-control"] = "no-store"
    return response



if __name__ == "__main__":
    app.run(debug=False)