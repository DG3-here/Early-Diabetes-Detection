import pickle

def load_model():
    model = pickle.load(open("models/diabetes_model.pkl", "rb"))
    scaler = pickle.load(open("models/scaler.pkl", "rb"))
    return model, scaler
