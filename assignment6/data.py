#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt


def plot_data(data_training, data_validation, xaxis, yaxis):
    """Creates a scatter plot coloring the two classes differently.

    args:
        data_training(pandas dataset): the training dataset
        data_validation(pandas_dataset): the validation dataset
        xaxis(string): feature for the x-axis
        yaxis(string): feature for the y-axis

    """
        
    pos_train, neg_train = get_splitted_dataset(data_training, xaxis, yaxis)

    plt.scatter(neg_train[[xaxis]], neg_train[[yaxis]], color='g', label="neg")
    plt.scatter(pos_train[[xaxis]], pos_train[[yaxis]], color='r', label="pos")

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title("Data Visualizing")
    plt.legend(loc="upper right", title="diabetes")
    plt.show()



def get_splitted_dataset(dataset, xaxis, yaxis):
    """Splits the dataset into two. Separated by the "diabetes" value. 

    args:
        dataset(pandas dataset): data from the sourcefile
        xaxis(string): feature for the x-axis
        yaxis(string): feature for the y-axis

    ret:
        dataset_pos, dataset_neg(pandas dataset): separated datasets

    """
    dataset = dataset[[xaxis, yaxis, "diabetes"]]
    dataset_neg = dataset[dataset["diabetes"] == 0]
    dataset_pos = dataset[dataset["diabetes"] == 1]
    return dataset_pos, dataset_neg



def extract_data(filename):
    """Removes the missing values. Then splits the data into a training set and 
    a validation set. Lets the training set be 80% of the total samples, and
    still keeps the proportions of the positive samples the same in the 
    training and validation sets. 

    args:
        filename(string): filename for the file containing data

    ret:
        data_training, data_validation(pandas dataset): separated datasets


    Dataset proportions:
        data_training length: 314
        data_validation length: 78

        Total negative values: 262 
            80%: 210 
            20%: 52

        Total positive values: 130
            80%: 104
            20%: 26

    """
    data = pd.read_csv(filename, sep=",")
    #Switch the "neg" and "pos" diabetes values to "0" and "1"
    data["diabetes"] = data["diabetes"].replace("neg", 0)
    data["diabetes"] = data["diabetes"].replace("pos", 1)

    #Shuffled lists with diabetes values "pos" and "neg" separated
    data_neg = data[data["diabetes"] == 0].sample(frac=1)
    data_pos = data[data["diabetes"] == 1].sample(frac=1)
    data_training = data_pos.iloc[0:104].append(data_neg.iloc[0:210])
    data_validation = data_pos.iloc[104:].append(data_neg.iloc[210:])

    return data_training, data_validation






def main():
    """Simple main program to test the methods of the file.

    """
    data_training, data_validation = extract_data("diabetes.csv")
    feature_string = "ENTER {} FEATURE\npregnant\nglucose\npressure\ntriceps\ninsulin\nmass\npedigree\nage\n(Enter 'q' to exit)\n>"
    feature_x, feature_y = "", ""
    while feature_x == "" or feature_x not in list(data_training):
        feature_x = input("\n" + feature_string.format("FIRST")).lower()
        if feature_x == "q": exit(0)
        if feature_x not in list(data_training): print("\n\nInput is not a valid feature, try again..")
    while feature_y == "" or feature_y not in list(data_training):
        feature_y = input("\n" + feature_string.replace(feature_x + "\n", "").format("SECOND")).lower()
        if feature_y == "q": exit(0)
        if feature_y not in list(data_training): print("\n\nInput is not a valid feature, try again..")
    plot_data(data_training, data_validation, feature_x, feature_y)


if __name__ == '__main__':
    main()

