# Getting Started with ML in Production

A hands-on, 2-day workshop for beginners on taking a machine learning model
from a notebook to a real, deployed, monitored production system.

## 🗓️ Schedule

| Day | Focus | Duration |
|-----|-------|----------|
| [Day 1](day1/README.md) | Intro & Your First API — entirely local | 3 hrs |
| [Day 2](day2/README.md) | Ship It on Render, then the Bigger Picture | 3 hrs |

## 🎯 Who This Is For

- Data scientists / ML practitioners who can train a model (sklearn-level) but have never deployed one
- Beginners wanting a practical, no-jargon path from `model.fit()` to a live API
- Zero prior knowledge of APIs, HTTP, or Docker is assumed

## 🔨 What You'll Build vs. What You'll Just Learn About

This workshop is deliberately split into two tiers, and it says so out loud
at the point each one starts:

- **Hands-on (you build every piece of this yourself):** packaging a model,
  a working FastAPI with two endpoints, deploying it live on Render, and
  watching real requests in a live log.
- **Awareness only (named and explained, nothing to build today):**
  containers/Docker, CI/CD, model versioning, feature stores,
  Champion/Challenger deployments, and the rest of the full MLOps picture —
  covered in Day 2's closing section so you recognize the terms later.

## ✅ Prerequisites

- Basic Python
- Familiarity with training a simple ML model (e.g., scikit-learn)
- A laptop with admin rights to install software — **Docker is not required**

## 🛠️ Tools You'll Need

Install/create these **before** the workshop — see [resources/setup.md](resources/setup.md) for full instructions.

- Python 3.10+
- Git
- A free GitHub account
- A free Render account (no credit card required)

## 📂 Repo Structure

```
.
├── day1/                  # Day 1: packaging a model, building your first API
│   ├── notebooks/         # Train + export the model
│   ├── api/               # FastAPI app 
│   └── README.md          # Day 1 session guide
├── day2/                  # Day 2: deploy on Render, monitor, then zoom out
│   ├── deployment/        # DEPLOY_GUIDE.md + render.yaml (native Python)
│   ├── monitoring/        # Logging example, read as a demo
│   └── README.md          # Day 2 session guide
├── bonus/
│   └── docker/            # Optional: try Docker yourself, after the workshop
├── slides/                # The workshop slide deck (.pptx)
├── datasets/              # Sample datasets used in exercises
└── resources/             # Setup guide, cheatsheet, further reading
```

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/getting-started-ml-production-shared.git
cd getting-started-ml-production-shared
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```



**## 📜 License**

The workshop's original teaching materials are licensed under [CC BY NC 4.0](LICENSE). You are free to use, adapt, and share the materials for non commercial educational purposes, with appropriate attribution.

