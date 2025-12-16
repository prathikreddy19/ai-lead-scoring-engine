from identify import identify_leads
from enrich import enrich_leads
from score import run_scoring


def run_pipeline():
    input_path = "data/raw_input.csv"
    output_path = "data/final_output.csv"

    leads = identify_leads(input_path)
    leads = enrich_leads(leads)

    leads.to_csv("data/temp_enriched.csv", index=False)

    run_scoring("data/temp_enriched.csv", output_path)


if __name__ == "__main__":
    run_pipeline()
