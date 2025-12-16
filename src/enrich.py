def enrich_leads(df):
    df = df.copy()

    df["email"] = df.apply(
        lambda r: f"{r['name'].split()[0].lower()}@{r['company'].lower().replace(' ', '')}.com",
        axis=1
    )

    return df
