# harness-full-demo

A tiny Python module used to try the harness's Full flow end to end.

- Tests: `pip install pytest` then `pytest -q`. CI (`.github/workflows/ci.yml`) runs them on every pull request.
- Deploy: every push to `main` deploys by itself through `.github/workflows/deploy.yml` to GitHub Pages. Nothing is run by hand.
- Production: https://andresgarcia29.github.io/harness-full-demo/ ; `version.txt` there holds the commit of `main` it serves.
