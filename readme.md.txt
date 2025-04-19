# A/B Testing Database Schema (db-9)

This branch defines the schema and logic for the A/B testing engine used to optimize product layout for e-commerce.

##  Tables

- **users**: stores customer identifiers and basic user data.
- **projects**: tracks testing experiments (e.g., different layout campaigns).
- **bandits**: represents layout variations (A/B/C) with Thompson Sampling parameters.
- **transactions**: logs user interaction with layouts (used for CTR analysis and bandit updating).

##  Thompson Sampling Parameters

The `bandits` table includes:
- `alpha` and `beta`: Bayesian parameters for the beta distribution
- `number_of_success`, `number_of_failures`: used to update click performance

##  Python Scripts

- `create_tables.py`: builds the full schema from scratch
- `seed_data.py`: inserts example rows into each table
- `update_bandits.py`: updates alpha/beta based on simulated user clicks
