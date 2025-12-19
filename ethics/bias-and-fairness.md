# Ethics, Bias & Fairness — HealthTech Waitlist Decision Intelligence

## Purpose

This document outlines the ethical considerations, bias risks, and fairness principles guiding the design of the HealthTech Waitlist Decision Intelligence system.

The system is intended to support human review and prioritisation, not to automate or replace clinical or operational decisions.

---

## Ethical Positioning

Healthcare decisions directly affect patient wellbeing.  
For this reason, this project is designed as a **decision-support system**, not an automated decision engine.

The system:
- Highlights risk patterns
- Flags cases for review
- Supports transparency and oversight

Final decisions always remain with qualified professionals.

---

## Bias Risks in Waiting List Data

Waiting list data can reflect systemic biases, including:
- Age-related prioritisation
- Socioeconomic access disparities
- Referral pathway inconsistencies
- Regional resource variation

These biases may be historical rather than clinical.

---

## Mitigation Strategies

The project applies the following safeguards:

### 1. Feature Review
- Avoids using protected attributes directly
- Evaluates proxy variables that may encode bias

### 2. Explainability
- Prefers interpretable models
- Uses feature importance to understand drivers of risk

### 3. Fairness Monitoring
- Compares risk distribution across groups
- Flags disproportionate impacts for review

### 4. Human Oversight
- No automated action is taken based on model output
- Outputs are recommendations only

---

## Limitations

This project:
- Does not claim clinical accuracy
- Does not replace professional judgement
- Is limited by the quality and scope of input data

These limitations are documented to avoid misuse or overreliance.

---

## Ethical Outcome

By explicitly addressing ethics and fairness, this project aims to:
- Promote responsible use of analytics in healthcare
- Increase transparency in prioritisation decisions
- Support equitable patient review processes
