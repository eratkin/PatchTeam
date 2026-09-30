# PatchTeam - four agents that debate which vulnerabilities to patch first

PatchTeam reads CISA's free **Known Exploited Vulnerabilities (KEV)** list, then
four small agents work as a team to decide *which security holes you should fix
first* and writes a custom report.

| Agent | Job |
|---|---|
| Collector | Downloads the KEV catalog (falls back to cache or sample data) |
| Triage | Scores each vulnerability and records *why* |
| Reviewer | Second opinion: removes duplicates, downgrades noise, upgrades real risks |
| Reporter | Writes `reports/latest.md`|

## Run it
```bash
python -m venv .venv
.venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py                # live data
python main.py --offline      # sample data
```
Edit `config.json` to match your own tech stack.

## Automation
`.github/workflows/weekly.yml` runs the parliament every Monday on GitHub Actions and
commits the new report to `reports/`.

## Data
CISA KEV catalog (free, public): https://www.cisa.gov/known-exploited-vulnerabilities-catalog
Bundled `data/sample_kev.json` is illustrative demo data only.
