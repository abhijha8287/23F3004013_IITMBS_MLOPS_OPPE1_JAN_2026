from src.inference import predict

def test_prediction():

    # Sample input (same format as training)
    features = [5.1, 3.5, 1.4, 0.2]

    pred = predict(
        "models/model_v1.pkl",
        features
    )

    # Basic sanity checks
    assert pred is not None
