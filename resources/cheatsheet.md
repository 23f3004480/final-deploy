# Workshop Cheatsheet

# Check installs
```bash
python --version
git --version
docker --version
```

## Model Packaging
```python
import joblib
joblib.dump(model, "model.pkl")
model = joblib.load("model.pkl")
```

## FastAPI Basics
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```
Run: `uvicorn main:app --reload`

## Git & Deploy
```bash
# One-time Git identity setup
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# First-time push to a new, empty GitHub repo
git init
git add -A
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/your-repo-name.git
git branch -M main
git push -u origin main        # Render redeploys automatically on push

# Every future update
git add -A
git commit -m "describe what you changed"
git push
```

# Docker
```bash
docker build -t ml-workshop-api .
docker run -p 8000:8000 ml-workshop-api
```

## Testing Your API
```bash
curl -X POST http://127.0.0.1:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## Key Vocabulary
| Term | Meaning |
|------|---------|
| Artifact | A saved, reusable version of your trained model |
| Endpoint | A URL your API exposes to accept requests |
| Container | A packaged, portable environment for your app |
| Drift | When your model's real-world performance degrades over time |
| Rollback | Reverting to a previous model version if something breaks |

## Further Reading
- [FastAPI docs](https://fastapi.tiangolo.com/)
- [Docker docs](https://docs.docker.com/get-started/)
- [Google's Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)
