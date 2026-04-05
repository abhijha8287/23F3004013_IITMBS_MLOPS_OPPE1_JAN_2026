import pandas as pd
import os


def load_folder(folder):

    dfs=[]

    for file in os.listdir(folder):

        if file.endswith(".csv"):

            path=os.path.join(folder,file)

            temp=pd.read_csv(path).head(20000)

            temp["stock_name"]=file

            dfs.append(temp)

    return pd.concat(dfs)


def create_features(folder):

    df=load_folder(folder)

    df=df.sort_values(["stock_name","timestamp"])

    df["rolling_avg_10"]=(
        df.groupby("stock_name")["close"]
        .rolling(10)
        .mean()
        .reset_index(0,drop=True)
    )

    df["volume_sum_10"]=(
        df.groupby("stock_name")["volume"]
        .rolling(10)
        .sum()
        .reset_index(0,drop=True)
    )

    df["target"]=(
        df.groupby("stock_name")["close"]
        .shift(-5)>df["close"]
    ).astype(int)

    df=df.dropna()

    # SAFE sampling
    df=df.sample(min(50000,len(df)),random_state=42)

    return df