import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.metrics import accuracy_score

def predict(data):
    """
    Takes health related data for the prediction (using an AI model) of heart disease in a particular user/patient
    """

    sample_dataset = pd.read_csv("/home/panam/Documents/heart disease backend/assets/heart.csv")
    

    # # y = sample_dataset["target"]
    # # Removing the target column
    sample_dataset.drop(columns = "target", axis=1, inplace=True)

    # data_structure = {}

    # for i in sample_dataset.columns:
    #     if i == "oldpeak":
    #         data_structure[i] = 0.0
    #     else:
    #         data_structure[i] = 0

    sample_dataset = sample_dataset._append(data, ignore_index=True)
    # Setting data to be in the "dataframe" format
    # dataframe = pd.DataFrame(data)

    # Standardizing the data values into a standard data format
    scaler = StandardScaler()
    data = scaler.fit_transform(sample_dataset)

    # De-serialize the model from the file
    with open("/home/panam/Documents/heart disease backend/assets/model.pickle", "rb") as f:
        loaded = pickle.load(f)


    prediction = loaded.predict(data)

    # sample_dataset = scaler.fit_transform(sample_dataset)
    # prediction_2 = loaded.predict(sample_dataset)
    # test_data_accuracy_xgb=accuracy_score(prediction_2, y)

    # print(test_data_accuracy_xgb * 100)

    print("PREDICTION", prediction[-1], sample_dataset.tail(), prediction)

    return [prediction[-1]]

    

# print(predict([{'age': 52, 'sex': 1, 'cp': 0, 'trestbps': 125, 'chol': 212, 'fbs': 0, 'restecg': 1, 'thalach': 168, 'exang': 0, 'oldpeak': 1, 'slope': 2, 'ca': 2, 'thal': 3}]))