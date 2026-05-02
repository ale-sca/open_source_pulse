# GitHub Repo Pulse Project

## Who is this for?
Open source maintainers and developers who have no easy way to track which projects are getting GitHub traction vs. which are getting funded. 

## Core Question:
"Which impactful project deserves my contribution?" 

## What does “impactful project” mean? 
GitHub Traction signal ranking: Forks > Open Issues > Stars. Minimum viability filter hardcoded in dbt (e.g. 50 stars AND 10 forks)

## Are there known limitations with this approach?
Yes, there are three main known limitations to bear in mind:
- GitHub stars ≠ real-world importance
- Forks are partially noisy (e.g., tutorials, classrooms) 
- Some funding ≠ well-funded

## What we'll build:
A weekly pipeline that ingests GitHub Stars/forks data (via GitHub API) + Open Collective / GitHub Sponsors public funding data, transforms it with dbt into clean models (traction score, funding score, gap score), and surfaces the results in a Streamlit dashboard where you can filter by language, topic, or region.
