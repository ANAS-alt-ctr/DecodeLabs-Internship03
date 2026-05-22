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
======================================================
    TECH STACK RECOMMENDER — DecodeLabs Project 3
======================================================
Enter your skills one by one. Press Enter after each.
Type 'done' when finished (minimum 3 skills required).

  Skill 1: Python
  ✓ Added: python

  Skill 2: Deep learning
  ✓ Added: deep learning

  Skill 3: Machine learning
  ✓ Added: machine learning

  Skill 4: LLMs
  ✓ Added: llms

  Skill 5: done

======================================================
  TOP CAREER PATH RECOMMENDATIONS
======================================================
  Profile: python, deep learning, machine learning, llms

🥇  Data Scientist                              41.1% match
    Builds predictive models and statistical analyses to extract insights from large datasets.
    ✓ Skills you have : python, machine learning, deep learning
    + Skills to learn : sql, pandas, numpy, statistics

🥈  AI Research Engineer                        40.3% match
    Advances state-of-the-art AI models and publishes novel research.
    ✓ Skills you have : python, deep learning, machine learning
    + Skills to learn : pytorch, research, mathematics, statistics

🥉  ML Engineer                                 24.0% match
    Deploys and scales machine learning models in production environments.
    ✓ Skills you have : python, machine learning
    + Skills to learn : tensorflow, pytorch, mlops, docker

──────────────────────────────────────────────────────
  Algorithm: TF-IDF weighting + Cosine Similarity
  Methodology: Content-Based Filtering (IPO Model)
======================================================
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

## 🖼️ Screenshot

![Demo Output](screenshot_project03.png)

---

*Powered by DecodeLabs Industrial Training Program.*
