"""
Tech Stack Recommender — Project 3
DecodeLabs Industrial Training Kit | Batch 2026
Algorithm: Content-Based Filtering using TF-IDF + Cosine Similarity
"""

import math
from collections import Counter


# ─────────────────────────────────────────────
#  DATASET  (items in our recommendation engine)
# ─────────────────────────────────────────────

JOB_ROLES = [
    {
        "title": "Data Scientist",
        "description": "Builds predictive models and statistical analyses to extract insights from large datasets.",
        "skills": ["python", "machine learning", "sql", "pandas", "numpy", "statistics",
                   "tensorflow", "data analysis", "jupyter", "scikit-learn", "r", "deep learning"],
    },
    {
        "title": "ML Engineer",
        "description": "Deploys and scales machine learning models in production environments.",
        "skills": ["python", "tensorflow", "pytorch", "mlops", "docker", "kubernetes",
                   "aws", "machine learning", "model deployment", "ci/cd", "data pipelines", "api"],
    },
    {
        "title": "DevOps Engineer",
        "description": "Automates infrastructure and manages CI/CD pipelines for reliable deployments.",
        "skills": ["docker", "kubernetes", "aws", "linux", "ci/cd", "bash",
                   "terraform", "ansible", "git", "monitoring", "jenkins", "nginx"],
    },
    {
        "title": "Backend Developer",
        "description": "Builds scalable server-side applications and REST APIs.",
        "skills": ["python", "java", "nodejs", "sql", "api", "rest",
                   "postgresql", "redis", "microservices", "git", "docker", "aws"],
    },
    {
        "title": "Frontend Developer",
        "description": "Creates responsive user interfaces and interactive web applications.",
        "skills": ["javascript", "react", "html", "css", "typescript", "vue",
                   "figma", "webpack", "git", "rest", "tailwind", "ui/ux"],
    },
    {
        "title": "Full Stack Developer",
        "description": "Works across both frontend and backend to deliver end-to-end web features.",
        "skills": ["javascript", "react", "nodejs", "sql", "html", "css",
                   "python", "git", "api", "docker", "postgresql", "aws"],
    },
    {
        "title": "Cloud Architect",
        "description": "Designs and manages scalable cloud infrastructure across multi-cloud environments.",
        "skills": ["aws", "azure", "gcp", "terraform", "kubernetes", "docker",
                   "networking", "security", "cost optimization", "automation", "iam", "devops"],
    },
    {
        "title": "Cybersecurity Analyst",
        "description": "Protects systems by identifying vulnerabilities and responding to threats.",
        "skills": ["networking", "linux", "penetration testing", "security", "python", "firewall",
                   "cryptography", "siem", "incident response", "compliance", "bash", "wireshark"],
    },
    {
        "title": "Data Engineer",
        "description": "Builds and maintains data pipelines and warehouses for analytics teams.",
        "skills": ["python", "sql", "spark", "hadoop", "airflow", "data pipelines",
                   "aws", "etl", "kafka", "postgresql", "dbt", "bigquery"],
    },
    {
        "title": "AI Research Engineer",
        "description": "Advances state-of-the-art AI models and publishes novel research.",
        "skills": ["python", "pytorch", "deep learning", "machine learning", "research", "mathematics",
                   "statistics", "transformers", "nlp", "computer vision", "cuda", "tensorflow"],
    },
    {
        "title": "Systems Administrator",
        "description": "Manages and maintains servers, networks, and operating systems.",
        "skills": ["linux", "windows server", "networking", "bash", "automation", "powershell",
                   "monitoring", "backup", "security", "virtualization", "ansible", "active directory"],
    },
    {
        "title": "Mobile Developer",
        "description": "Develops native and cross-platform mobile apps for iOS and Android.",
        "skills": ["swift", "kotlin", "react native", "flutter", "java", "firebase",
                   "rest", "git", "xcode", "android", "ui/ux", "typescript"],
    },
    {
        "title": "Database Administrator",
        "description": "Manages and optimizes relational and NoSQL databases for performance.",
        "skills": ["sql", "postgresql", "mysql", "oracle", "mongodb", "performance tuning",
                   "backup", "security", "linux", "python", "replication", "indexing"],
    },
]


# ─────────────────────────────────────────────
#  STEP 1 — INGESTION
#  Capture the user state (minimum 3 skills)
# ─────────────────────────────────────────────

def get_user_skills() -> list[str]:
    """Prompt the user to enter at least 3 skills."""
    print("\n" + "=" * 55)
    print("   TECH STACK RECOMMENDER — DecodeLabs Project 3")
    print("=" * 55)
    print("Enter your skills one by one. Press Enter after each.")
    print("Type 'done' when finished (minimum 3 skills required).\n")

    skills = []
    while True:
        skill = input(f"  Skill {len(skills) + 1}: ").strip().lower()
        if skill == "done":
            if len(skills) < 3:
                print("  ⚠  Please add at least 3 skills for accurate matching.\n")
                continue
            break
        if skill == "":
            continue
        if skill in skills:
            print(f"  '{skill}' already added.\n")
            continue
        skills.append(skill)
        print(f"  ✓ Added: {skill}\n")

    return skills


# ─────────────────────────────────────────────
#  VECTOR MAPPING
#  Build a shared vocabulary from the dataset
# ─────────────────────────────────────────────

def build_vocabulary(jobs: list[dict]) -> list[str]:
    """Return the unique sorted vocabulary across all job roles."""
    vocab = set()
    for job in jobs:
        vocab.update(job["skills"])
    return sorted(vocab)


# ─────────────────────────────────────────────
#  TF-IDF WEIGHTING
#  Penalize generic terms, reward specific ones
# ─────────────────────────────────────────────

def compute_tf(skills: list[str], term: str) -> float:
    """Term Frequency: how often a term appears in a skill list."""
    count = skills.count(term)
    return count / len(skills) if skills else 0.0


def compute_idf(jobs: list[dict], term: str) -> float:
    """
    Inverse Document Frequency: penalizes terms common across all roles.
    Uses smoothed formula: log((N+1) / (df+1)) + 1
    The logarithm dampens the penalty so values stay comparable.
    """
    N = len(jobs)
    df = sum(1 for job in jobs if term in job["skills"])
    return math.log((N + 1) / (df + 1)) + 1


def build_tfidf_vector(skills: list[str], vocab: list[str], idf_scores: dict) -> list[float]:
    """Convert a skill list into a weighted TF-IDF vector."""
    return [compute_tf(skills, term) * idf_scores[term] for term in vocab]


# ─────────────────────────────────────────────
#  SIMILARITY ENGINE
#  Cosine Similarity: magnitude-invariant match
# ─────────────────────────────────────────────

def normalize(vector: list[float]) -> list[float]:
    """L2-normalize a vector so magnitude doesn't skew similarity."""
    magnitude = math.sqrt(sum(x ** 2 for x in vector))
    return [x / magnitude for x in vector] if magnitude > 0 else vector


def cosine_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """
    Dot product of two normalized vectors.
    Score 1.0 = perfectly aligned (identical orientation)
    Score 0.0 = orthogonal (no shared characteristics)
    """
    return sum(a * b for a, b in zip(vec_a, vec_b))


# ─────────────────────────────────────────────
#  STEP 2 — SCORING
#  Run cosine similarity against every job role
# ─────────────────────────────────────────────

def score_all_jobs(
    user_skills: list[str],
    jobs: list[dict],
    vocab: list[str],
    idf_scores: dict,
) -> list[dict]:
    """
    Build the user vector and compare it against every job role vector.
    Returns a list of jobs annotated with their similarity score.
    """
    user_vec = normalize(build_tfidf_vector(user_skills, vocab, idf_scores))

    scored = []
    for job in jobs:
        job_vec = normalize(build_tfidf_vector(job["skills"], vocab, idf_scores))
        score = cosine_similarity(user_vec, job_vec)
        matched = [s for s in job["skills"] if s in user_skills]
        gap = [s for s in job["skills"] if s not in user_skills]
        scored.append({**job, "score": score, "matched": matched, "gap": gap})

    return scored


# ─────────────────────────────────────────────
#  STEP 3 — SORTING
#  Push highest-scoring matches to the top
# ─────────────────────────────────────────────

def sort_by_score(scored_jobs: list[dict]) -> list[dict]:
    return sorted(scored_jobs, key=lambda j: j["score"], reverse=True)


# ─────────────────────────────────────────────
#  STEP 4 — FILTERING
#  Truncate to Top-N to prevent choice overload
# ─────────────────────────────────────────────

def top_n(scored_jobs: list[dict], n: int = 3) -> list[dict]:
    return scored_jobs[:n]


# ─────────────────────────────────────────────
#  OUTPUT
#  Display the ranked Top-N recommendations
# ─────────────────────────────────────────────

def display_results(recommendations: list[dict], user_skills: list[str]) -> None:
    MEDALS = ["🥇", "🥈", "🥉"]

    print("\n" + "=" * 55)
    print("   TOP CAREER PATH RECOMMENDATIONS")
    print("=" * 55)
    print(f"   Profile: {', '.join(user_skills)}\n")

    for i, job in enumerate(recommendations):
        score_pct = job["score"] * 100
        bar_filled = int(score_pct / 5)        # 20-char bar
        bar = "█" * bar_filled + "░" * (20 - bar_filled)

        print(f"  {MEDALS[i]}  {job['title']}")
        print(f"      [{bar}] {score_pct:.1f}% match")
        print(f"      {job['description']}")

        if job["matched"]:
            print(f"      ✓ Skills you have : {', '.join(job['matched'])}")
        if job["gap"]:
            print(f"      + Skills to learn : {', '.join(job['gap'][:4])}")
        print()

    print("─" * 55)
    print("  Algorithm: TF-IDF weighting + Cosine Similarity")
    print("  Methodology: Content-Based Filtering (IPO Model)")
    print("=" * 55 + "\n")


# ─────────────────────────────────────────────
#  MAIN PIPELINE
#  Ingestion → Scoring → Sorting → Filtering
# ─────────────────────────────────────────────

def recommend(user_skills: list[str], jobs: list[dict] = JOB_ROLES, top: int = 3) -> list[dict]:
    """
    Full recommendation pipeline.
    Can be called programmatically or via the CLI below.
    """
    vocab = build_vocabulary(jobs)
    idf_scores = {term: compute_idf(jobs, term) for term in vocab}
    scored = score_all_jobs(user_skills, jobs, vocab, idf_scores)
    ranked = sort_by_score(scored)
    return top_n(ranked, n=top)


def main():
    user_skills = get_user_skills()
    results = recommend(user_skills)
    display_results(results, user_skills)


if __name__ == "__main__":
    main()
