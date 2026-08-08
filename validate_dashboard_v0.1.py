from pathlib import Path
import csv, hashlib, json, re, sys
root=Path(__file__).resolve().parent
errors=[]
for req in ['index.html','assets/css/style.css','assets/js/data.js','assets/js/app.js','DATA_MANIFEST_SHA256.csv','downloads/ADAA_SSRN_Working_Paper_v1.17_FINAL_PUBLIC_RELEASE.pdf','downloads/ADAA_Public_Replication_Package_v1.0.2.zip']:
    if not (root/req).exists(): errors.append('missing '+req)
with open(root/'DATA_MANIFEST_SHA256.csv',encoding='utf-8') as f:
    for r in csv.DictReader(f):
        p=root/r['file']
        if not p.exists(): errors.append('missing '+r['file']);continue
        h=hashlib.sha256(p.read_bytes()).hexdigest()
        if h!=r['sha256']: errors.append('hash mismatch '+r['file'])
text=(root/'assets/js/data.js').read_text(encoding='utf-8')
for token in ['"historical_2023_rank":735','"total_five_rule_sets":4368','"decision_months":216','"performance_months":218','"paper_version":"v1.17 FINAL"','"replication_version":"v1.0.2"']:
    if token not in text: errors.append('missing frozen anchor '+token)
html=(root/'index.html').read_text(encoding='utf-8')
app=(root/'assets/js/app.js').read_text(encoding='utf-8')
for bad in ['TODO','TBD','PLACEHOLDER']:
    if bad in html.upper(): errors.append('placeholder token '+bad)
# final public-copy consistency checks
for bad in ['<div class="sub">Historical weights</div>', 'Blue dot = historical weight', 'The historical weights sit inside']:
    if bad in html: errors.append('stale reader label '+bad)
if 'th percentile' in app: errors.append('invalid decimal ordinal suffix in percentile label')
if "ADAA — practitioner weights" in app: errors.append('reader label omits later in later practitioner weights')
for url in ['https://slackquant80.github.io/adaa-slackquant/','https://github.com/slackquant80/adaa-decision-diversification','https://doi.org/10.5281/zenodo.21853533']:
    if url not in html and url not in (root/'README.md').read_text(encoding='utf-8'): errors.append('missing public URL '+url)
if "replaceAll('_',' ')" not in app: errors.append('historical set display does not normalize underscores')
print('ADAA dashboard v0.1 validation')
print('checks:', 7+sum(1 for _ in csv.DictReader(open(root/'DATA_MANIFEST_SHA256.csv',encoding='utf-8'))) + 5 + 3 + 7)
print('failures:',len(errors))
for e in errors: print('FAIL:',e)
sys.exit(1 if errors else 0)
