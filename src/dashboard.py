import pandas as pd
import streamlit as st


st.set_page_config(page_title="Lead Scoring Dashboard", layout="wide")

st.title("Lead Intelligence Dashboard")
st.write("Ranked list of high-probability biotech leads")

data_path = "data/final_output.csv"
df = pd.read_csv(data_path)

search = st.text_input("Search by name, title, company, or location")

if search:
    search = search.lower()
    df = df[df.apply(
        lambda row: search in " ".join(row.astype(str)).lower(),
        axis=1
    )]

st.dataframe(
    df[[
        "rank",
        "probability",
        "name",
        "title",
        "company",
        "person_location",
        "company_hq",
        "linkedin_url"
    ]],
    use_container_width=True
)
