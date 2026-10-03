# Pre-Workshop Setup Guide

Please complete this **before** the workshop so we can spend our time
learning, not installing software. **You do not need Docker installed** —
nothing in this workshop requires it on your own machine.

## 1. Python 3.10+
Check your version:
```bash
python3 --version
```
If needed, install from [python.org](https://www.python.org/downloads/).

## 2. Git
```bash
git --version
```
Install from [git-scm.com](https://git-scm.com/downloads) if missing.

## 3. A GitHub Account
Free, at [github.com](https://github.com). You'll push your code here on
Day 2 so Render can deploy it.

## 4. A Render Account
Free, at [render.com](https://render.com) — no credit card required for the
free tier. You'll deploy your API here on Day 2.

## 5. Clone the Workshop Repo
```bash
git clone https://github.com/<your-username>/getting-started-ml-production.git
cd getting-started-ml-production
python3 -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
```


## Troubleshooting
- **pip install fails:** Try upgrading pip first: `pip install --upgrade pip`.
- Still stuck? Post in the workshop Slack/Discord channel before the session.

