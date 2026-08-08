from pathlib import Path
import csv, hashlib, zipfile, sys, re

dash=Path(__file__).resolve().parent
project=dash.parent if dash.name=='07_Dashboard' else None
errs=[]; notes=[]; checks=0

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
# internal dashboard validation
for req in ['index.html','assets/css/style.css','assets/js/data.js','assets/js/app.js','DATA_MANIFEST_SHA256.csv','downloads/ADAA_SSRN_Working_Paper_v1.21_FINAL_PUBLIC_RELEASE.pdf','downloads/ADAA_Public_Replication_Package_v1.0.2.zip']:
    checks+=1
    if not (dash/req).exists(): errs.append('missing '+req)
rows=list(csv.DictReader(open(dash/'DATA_MANIFEST_SHA256.csv',encoding='utf-8')))
for r in rows:
    checks+=1; p=dash/r['file']
    if not p.exists(): errs.append('missing '+r['file']); continue
    if sha(p)!=r['sha256']: errs.append('dashboard source hash mismatch '+r['file'])
# static/offline policy
for p in [dash/'index.html',dash/'assets/js/app.js']:
    txt=p.read_text(encoding='utf-8')
    for bad in ['fetch(','XMLHttpRequest','<script src="http','<link href="http']:
        checks+=1
        if bad in txt: errs.append(f'external/runtime dependency {bad} in {p.name}')
# frozen anchors
js=(dash/'assets/js/data.js').read_text(encoding='utf-8')
for token in ['"historical_2023_rank":735','"total_five_rule_sets":4368','"decision_months":216','"performance_months":218','"historical_2023_score":0.8171374401867475','"paper_version":"v1.21 FINAL"']:
    checks+=1
    if token not in js: errs.append('frozen anchor missing '+token)
# project sync when installed under 05_ADAA/07_Dashboard
if project and project.name=='05_ADAA':
    canon_paper=project/'05_Practical_Paper/01_Manuscript/ADAA_SSRN_Working_Paper_v1.21_FINAL_PUBLIC_RELEASE.pdf'
    canon_repl=project/'06_Replication/ADAA_Public_Replication_Package_v1.0.2.zip'
    for canon,copy,label in [(canon_paper,dash/'downloads/ADAA_SSRN_Working_Paper_v1.21_FINAL_PUBLIC_RELEASE.pdf','paper'),(canon_repl,dash/'downloads/ADAA_Public_Replication_Package_v1.0.2.zip','replication')]:
        checks+=1
        if not canon.exists(): errs.append('canonical '+label+' missing: '+str(canon))
        elif sha(canon)!=sha(copy): errs.append(label+' download copy differs from canonical project file')
    if canon_repl.exists():
        with zipfile.ZipFile(canon_repl) as z:
            names=set(z.namelist())
            for r in rows:
                checks+=1
                member='05_ADAA/'+r['replication_path']
                if member not in names: errs.append('replication member missing '+member); continue
                zh=hashlib.sha256(z.read(member)).hexdigest()
                if zh!=r['sha256']: errs.append('dashboard source differs from replication member '+member)
else:
    notes.append('project-level paper/replication cross-check skipped: standalone dashboard layout')

print('ADAA dashboard project-sync validation v0.1')
print('checks:',checks)
print('failures:',len(errs))
for e in errs: print('FAIL:',e)
for n in notes: print('NOTE:',n)
sys.exit(1 if errs else 0)
