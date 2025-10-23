# CI/CD for Business Students — Guided Workbook (Codespaces Edition)

This repository contains a small Flask personal website and supporting files so you can practice GitHub Codespaces and GitHub Actions (CI). The guided workbook walks through publishing, creating a Codespace, running the site, and adding CI.

## Quick start (local)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run locally (example uses port 5002 to avoid Docker conflicts):

```bash
export DB_PATH=projects.db
export PORT=5002
python3 app.py
```

3. Open http://localhost:5002 in your browser.

## Publish to GitHub (one-time)

1. Create a new repository on GitHub.
2. Add this repo as remote and push:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:<your-username>/<repo-name>.git
git push -u origin main
```

## Codespaces

1. On GitHub, open your repo and click **Code → Create codespace on main**.
2. In the Codespace terminal, run:

```bash
python3 app.py
```

3. When Codespaces shows the forwarded port (usually 5000), click **Open in Browser** to view the site.

## Continuous Integration (GitHub Actions)

A workflow `./github/workflows/ci.yml` is included to run `pytest` and build the Docker image on pushes to `main`.

## Screenshot checklist for submission

- Docker Desktop — Images (show `emilyrhee-portfolio:local`)
- Docker Desktop — Containers (show the `emilyrhee-portfolio` container running)
- Local browser — site running from container (e.g., http://localhost:5001/)
- GitHub — repository main page (show files)
- Codespaces — running site (open in browser) and Ports view
- GitHub Actions — showing the latest run and test/build steps

## Notes
- Make sure `.gitignore` is present before you push to avoid committing your virtual environment or database file.
- If using Docker locally, run the container with a bind mount to your project directory to see live edits (example included in the workbook).
