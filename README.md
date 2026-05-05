# GitHub Repo Pulse Project

## Who is this for?
Open source maintainers and developers who have no easy way to track which projects are getting GitHub traction vs. which are getting funded. 

## Core Question:
"Which impactful project deserves my contribution?". The app aims at reducing the information asymmetry between traction and funding in open source repositories.

## What does “impactful project” mean? 
GitHub Traction signal ranking: Forks > Open Issues > Stars. Minimum viability filter hardcoded in dbt (see known limitations below)

## Are there known limitations with this approach?
Yes, there are three main known limitations to bear in mind:
- GitHub stars ≠ real-world importance
- Forks are partially noisy (e.g., tutorials, classrooms) 
- Some funding ≠ well-funded
- Working assumption for the Minimum Viability Filter: 50 stars and 10 forks
- Contributor count was excluded from the traction score due to API rate limit constraints and ambiguous signal value

## What we'll build:
A weekly pipeline that ingests GitHub Stars/forks data (via GitHub API) + Open Collective / GitHub Sponsors public funding data, transforms it with dbt into clean models (traction score, funding score, gap score), and surfaces the results in a Streamlit dashboard where you can filter by language, topic, or region.
