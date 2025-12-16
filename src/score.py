import pandas as pd


HUB_LOCATIONS = [
    "boston",
    "cambridge",
    "san francisco",
    "bay area",
    "basel",
    "london",
    "oxford",
    "san diego"
]


def score_row(row):
    score = 0

    title = str(row["title"]).lower()
    funding = str(row["funding_stage"]).lower()
    paper = str(row["recent_paper"]).lower()
    tech = str(row["tech_used"]).lower()
    person_loc = str(row["person_location"]).lower()
    hq_loc = str(row["company_hq"]).lower()

    if any(word in title for word in ["toxicology", "safety", "hepatic", "3d"]):
        score += 30

    if "series a" in funding or "series b" in funding:
        score += 20

    if "in-vitro" in tech or "organ-on-chip" in tech or "3d" in tech:
        score += 15
    elif "cell" in tech:
        score += 10

    if any(hub in person_loc for hub in HUB_LOCATIONS) or any(
        hub in hq_loc for hub in HUB_LOCATIONS
    ):
        score += 10

    if paper == "yes":
        score += 40

    return min(score, 100)


def run_scoring(input_path, output_path):
    df = pd.read_csv(input_path)

    df["probability"] = df.apply(score_row, axis=1)
    df = df.sort_values("probability", ascending=False)
    df.insert(0, "rank", range(1, len(df) + 1))

    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    output = run_scoring(
        "data/raw_input.csv",
        "data/final_output.csv"
    )

    print(output[["rank", "name", "title", "company", "probability"]])
