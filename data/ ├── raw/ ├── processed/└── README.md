# Data Overview — HealthTech Waitlist Decision Intelligence

## Data Strategy

This project uses synthetic patient-level waiting list data inspired by publicly available healthcare statistics.

The use of synthetic data ensures:
- No patient-identifiable information is used
- Ethical safety for experimentation
- Full control over bias and fairness testing

---

## Data Layers

### Raw Data
The `raw/` directory contains:
- Synthetic patient waiting list records
- Initial fields before cleaning and transformation

### Processed Data
The `processed/` directory contains:
- Cleaned datasets
- Feature-engineered fields
- Model-ready tables

---

## Design Principles

The dataset is designed to:
- Reflect realistic waiting list patterns
- Support risk stratification analysis
- Enable fairness and bias evaluation
- Feed both analytics and machine learning workflows
