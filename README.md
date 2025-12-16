# Lead Intelligence Pipeline – 3D In-Vitro Models

This project is a demo lead-qualification system designed to identify, enrich, and rank life-science professionals based on their likelihood of working with 3D in-vitro models for drug and therapy development.

The system is built to think like a business development analyst, combining multiple signals into a single propensity score (0–100) and presenting the results in a clean, searchable dashboard.

Problem Overview

Business development teams often struggle to prioritize the right researchers and decision-makers from large datasets (LinkedIn, publications, conferences, etc.).
This demo shows how such leads can be:

Identified based on role relevance

Enriched with contextual information

Ranked using a transparent scoring logic

The focus of this implementation is on the ranking intelligence and reproducibility, rather than large-scale web scraping.

Architecture & Approach

The pipeline follows the same stages described in the assignment:

Stage 1: Identification

Relevant profiles are selected based on job titles such as:

Director of Toxicology

Head of Preclinical Safety

Safety / Hepatic / 3D-biology roles

For this demo, the output of the “crawler” stage is simulated using realistic data, representing profiles sourced from:

LinkedIn

PubMed

Scientific conferences

Stage 2: Enrichment

Each identified profile includes enriched attributes such as:

Person location vs company HQ

Funding stage of the company

Recent scientific publication activity

Technology exposure (e.g. in-vitro models, organ-on-chip)

This data is kept explicit in the CSV to make the scoring logic transparent.

Stage 3: Ranking (Propensity to Buy Engine)

Each lead is assigned a probability score (0–100) using a rule-based weighted system, as defined in the assignment.

Scoring signals include:

Role fit (seniority and relevance)

Company funding stage (Series A/B)

Technographic alignment (3D / in-vitro / NAMs)

Presence in biotech hubs

Recent relevant scientific publications

This approach is deterministic, explainable, and easy to audit, which is important for real BD workflows.

Output
1. CSV Output

The full output is generated as a CSV file containing:

Rank

Probability score

Name, title, company

Location (person vs HQ)

Raw scoring signals (funding, publications, tech, source)

This CSV is suitable for export to Google Sheets for verification and sharing.

2. Streamlit Dashboard

A lightweight Streamlit dashboard is included to provide a business-friendly view of the ranked leads.

Dashboard features:

Ranked table of leads

Free-text search (name, title, company, location)

Toggle to show/hide technical scoring columns
By default, the dashboard shows only actionable BD fields.
Technical scoring signals can be revealed using the toggle for transparency and review.

### Project Structure
ai-lead-scoring-engine/
│
├── data/
│   ├── raw_input.csv        # Simulated crawler output
│   └── final_output.csv     # Ranked leads
│
├── src/
│   ├── identify.py          # Identification logic
│   ├── enrich.py            # Enrichment logic
│   ├── score.py             # Propensity scoring engine
│   ├── pipeline.py          # End-to-end pipeline
│   └── dashboard.py         # Streamlit dashboard
│
├── README.md
└── requirements.txt

How to Run
1. Install dependencies
pip install -r requirements.txt

2. Run the full pipeline
python src/pipeline.py


This generates data/final_output.csv.

3. Launch the dashboard
streamlit run src/dashboard.py

Notes & Assumptions

Web crawling and API integrations are intentionally simulated for this demo to keep the project reproducible and easy to verify.

The core value demonstrated here is the ranking logic and decision framework, which can be scaled later using APIs or tools like LinkedIn, Proxycurl, Clay, or Apollo.

The dataset size is kept small on purpose to clearly illustrate score separation and logic.

Summary

This demo shows how a lead-qualification system for 3D in-vitro research can be:

Structured

Explainable

Business-friendly

Easily extensible to real data sources.
