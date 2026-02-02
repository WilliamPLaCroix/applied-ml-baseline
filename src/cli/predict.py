"""
Prediction routines for machine learning models.
"""


import Fire

def load_model(model_path):
    raise NotImplementedError("Model loading routine not implemented yet.")


def predict(model, data):
    raise NotImplementedError("Prediction routine not implemented yet.")


if __name__ == "__main__":
    Fire(predict)