import pandas as pd


def identify_leads(input_path):
    df = pd.read_csv(input_path)

    df = df[df["title"].str.contains(
        "Toxicology|Safety|Hepatic|3D",
        case=False,
        na=False
    )]

    return df
