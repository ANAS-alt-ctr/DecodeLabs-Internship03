# Tech Stack Recommender — Project 3

**DecodeLabs Industrial Training Kit | Batch 2026**

A Python-based recommendation engine that suggests ideal career paths and job roles based on your current technical skill set. The engine uses a Content-Based Filtering algorithm leveraging **TF-IDF weighting** and **Cosine Similarity** to accurately match user profiles to industry roles.

## Features
- **Interactive CLI**: Easy-to-use terminal interface to input your skills.
- **Smart Matching**: Uses Term Frequency-Inverse Document Frequency (TF-IDF) to penalize generic skills and reward specific ones.
- **Cosine Similarity**: Provides a magnitude-invariant match score to rank job roles accurately.
- **Skill Gap Analysis**: Not only tells you what you match with, but also highlights exactly which skills you need to learn to reach that role.

## Available Career Paths
The engine currently supports matching against a variety of industry-standard roles:
- Data Scientist
- ML Engineer
- DevOps Engineer
- Backend Developer
- Frontend Developer
- Full Stack Developer
- Cloud Architect
- Cybersecurity Analyst
- Data Engineer
- AI Research Engineer
- Systems Administrator
- Mobile Developer
- Database Administrator

## How It Works
1. **Ingestion**: You input at least 3 technical skills you currently possess.
2. **Vector Mapping & TF-IDF Weighting**: The system builds a vocabulary matrix and weights your skills against our comprehensive dataset.
3. **Similarity Engine**: Calculates the Cosine Similarity between your skill vector and all job role vectors.
4. **Scoring & Sorting**: Ranks the roles by similarity score and presents the top recommendations along with the missing skills you need to learn.

## Quick Start

### Prerequisites
- Python 3.6+

### Running the Recommender
1. Clone the repository:
   ```bash
   git clone https://github.com/ANAS-alt-ctr/DecodeLabs-Internship03.git
   cd DecodeLabs-Internship03
   ```
2. Run the script:
   ```bash
   python tech_stack_recommender.py
   ```
3. Follow the on-screen prompts to enter your skills (e.g., `python`, `machine learning`, `sql`). Type `done` when finished!

## Output Example
```text
=======================================================
   TOP CAREER PATH RECOMMENDATIONS
=======================================================
   Profile: python, machine learning, sql

  🥇  Data Scientist
      [████████████░░░░░░░░] 60.5% match
      Builds predictive models and statistical analyses to extract insights from large datasets.
      ✓ Skills you have : python, machine learning, sql
      + Skills to learn : pandas, numpy, statistics, tensorflow
```
