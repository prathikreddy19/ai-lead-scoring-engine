import pandas as pd
import streamlit as st


st.set_page_config(page_title="Lead Intelligence Dashboard", layout="wide")

st.title("Lead Intelligence Dashboard")
st.write("Ranked list of high-probability biotech leads")

df = pd.read_csv("data/final_output.csv")

search = st.text_input("Search by name, title, company, or location")

if search:
    search = search.lower()
    df = df[df.apply(
        lambda row: search in " ".join(row.astype(str)).lower(),
        axis=1
    )]

show_technical = st.checkbox("Show technical scoring columns")

if show_technical:
    columns_to_show = [
        "rank",
        "probability",
        "name",
        "title",
        "company",
        "person_location",
        "company_hq",
        "funding_stage",
        "recent_paper",
        "tech_used",
        "source",
        "linkedin_url"
    ]
else:
    columns_to_show = [
        "rank",
        "probability",
        "name",
        "title",
        "company",
        "person_location",
        "company_hq",
        "linkedin_url"
    ]

st.dataframe(
    df[columns_to_show],
    use_container_width=True
)
