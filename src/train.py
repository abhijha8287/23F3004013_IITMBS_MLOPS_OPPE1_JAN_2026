import mlflow
import mlflow.sklearn
import pickle
import sys
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from features import create_features


mlflow.set_tracking_uri("file:./mlruns")

mlflow.set_experiment("stock_exp")


def train(folder,model_path):

    df=create_features(folder)

    X=df[[
        "rolling_avg_10",
        "volume_sum_10"
    ]]

    y=df["target"]

    X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.2,random_state=42
    )

    mlflow.start_run()

    # MODEL DEFINITION (this was missing)
    model=RandomForestClassifier(
        n_estimators=15,
        max_depth=5,
        n_jobs=-1,
        random_state=42
    )

    model.fit(X_train,y_train)

    pred=model.predict(X_test)

    acc=accuracy_score(y_test,pred)

    mlflow.log_metric("accuracy",acc)

    mlflow.sklearn.log_model(
        model,
        "model",
        registered_model_name="stock_model"
    )

    os.makedirs("models",exist_ok=True)

    pickle.dump(
        model,
        open(model_path,"wb")
    )

    mlflow.end_run()


if __name__=="__main__":

    train(sys.argv[1],sys.argv[2])