# 🧠 Tech Stack Recommender — Project 3

**DecodeLabs Industrial Training Kit | Batch 2026**

A Python-based recommendation engine that suggests ideal career paths and job roles based on your current technical skill set. The engine uses a **Content-Based Filtering** algorithm leveraging **TF-IDF weighting** and **Cosine Similarity** to accurately match user profiles to industry roles.

---

## ✨ Features

- **Interactive CLI**: Easy-to-use terminal interface to input your skills.
- **Smart Matching**: Uses Term Frequency-Inverse Document Frequency (TF-IDF) to penalize generic skills and reward specific ones.
- **Cosine Similarity**: Provides a magnitude-invariant match score to rank job roles accurately.
- **Skill Gap Analysis**: Highlights exactly which skills you still need to learn to reach a target role.
- **Progress Bar Display**: Visual match percentage bar rendered directly in the terminal.

---

## 🗂️ Project Structure

```
DecodeLabs-Internship03/
├── tech_stack_recommender.py   # Core recommendation engine
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.6+
- No external libraries required (uses Python standard library only)

### Running the Recommender

```bash
# Clone the repository
git clone https://github.com/ANAS-alt-ctr/DecodeLabs-Internship03.git
cd DecodeLabs-Internship03

# Run the recommender
python tech_stack_recommender.py
```

Then enter your skills one by one at the prompt and type `done` when finished.

---

## 📊 Output Example

```
Enter your skills (type 'done' when finished):
Skill 1: python
Skill 2: machine learning
Skill 3: sql
Skill 4: done

=======================================================
   TOP CAREER PATH RECOMMENDATIONS
=======================================================
   Profile: python, machine learning, sql

  🥇  Data Scientist
      [████████████░░░░░░░░] 60.5% match
      Builds predictive models and statistical analyses to extract
      insights from large datasets.
      ✓ Skills you have : python, machine learning, sql
      + Skills to learn : pandas, numpy, statistics, tensorflow

  🥈  ML Engineer
      [██████████░░░░░░░░░░] 52.3% match
      Deploys and scales machine learning models in production.
      ✓ Skills you have : python, machine learning
      + Skills to learn : docker, mlflow, fastapi, cloud

  🥉  Data Engineer
      [████████░░░░░░░░░░░░] 41.0% match
      Builds data pipelines and manages large-scale data infrastructure.
      ✓ Skills you have : python, sql
      + Skills to learn : spark, airflow, kafka, dbt
```

---

## 🧠 How It Works

1. **Ingestion** — You input at least 3 technical skills you currently possess.
2. **TF-IDF Weighting** — The system builds a vocabulary matrix and weights your skills against a comprehensive role dataset. Rare/specific skills are rewarded over common ones.
3. **Cosine Similarity** — Calculates the angle between your skill vector and each job role vector — magnitude-invariant, so a short list of strong skills isn't penalized.
4. **Scoring & Ranking** — Roles are sorted by similarity score. The top matches are displayed with medal rankings and skill gap breakdowns.

---

## 🎯 Available Career Paths

The engine currently matches against 13 industry-standard roles:

| Role | Domain |
|---|---|
| Data Scientist | Data & ML |
| ML Engineer | Machine Learning |
| AI Research Engineer | AI/Research |
| Data Engineer | Data Infrastructure |
| Backend Developer | Software Engineering |
| Frontend Developer | Software Engineering |
| Full Stack Developer | Software Engineering |
| DevOps Engineer | Infrastructure |
| Cloud Architect | Cloud |
| Cybersecurity Analyst | Security |
| Systems Administrator | IT/Ops |
| Mobile Developer | Mobile |
| Database Administrator | Data |

---

## 🖼️ Screenshots

> **Note:** Run the script locally and take a screenshot of your terminal output to add here.
> Replace this section by uploading your screenshot to the repo and using:
> ```
> <img width="1003" height="992" alt="image" src="https://github.com/user-attachments/assets/a6925c5b-f7a7-4c49-b9d6-5cf084119be0" />
)
> ```

---

*Powered by DecodeLabs Industrial Training Program.*
