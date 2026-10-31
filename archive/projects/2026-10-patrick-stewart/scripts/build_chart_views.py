"""Derive ranks and chart views from the frozen IMDb/credit snapshot."""
from pathlib import Path
import csv,json
D=Path(__file__).resolve().parents[1]
rows=list(csv.DictReader((D/'data/films_expanded.csv').open()))
assert len(rows)==70 and len({r['tconst'] for r in rows})==70
rated=[r for r in rows if r['votes'] and r['rating']]
assert len(rated)==68
labels={r['tconst']:r['display_title'] for r in csv.DictReader((D/'data/title_labels.csv').open())}
top=sorted(rated,key=lambda r:(-int(r['votes']),r['tconst']))[:25]
for rank,row in enumerate(top,1):
 row.update(rank=rank,votes_k=int(row['votes'])/1000,display_title=labels[row['tconst']],display_label=row['tconst'])
with (D/'data/top25_votes.csv').open('w') as f:
 w=csv.DictWriter(f,list(top[0]));w.writeheader();w.writerows(top)
total=sum(int(r['votes']) for r in rated)
summary={'films':len(rows),'rated':len(rated),'total_votes':total,'top25_share':sum(int(r['votes']) for r in top)/total,'groups':{}}
for group in ['Xavier','Picard','Other']:
 selected=[r for r in rows if r['character_group']==group]
 votes=sum(int(r['votes']) for r in selected if r['votes'])
 summary['groups'][group]={'titles':len(selected),'votes':votes,'share':votes/total}
others=sorted([r for r in rated if r['character_group']=='Other' and int(r['votes'])>=1000],key=lambda r:(-float(r['rating']),-int(r['votes'])))[:3]
summary['highest_rated_other']=[{k:r[k] for k in ['tconst','primaryTitle','rating','votes']} for r in others]
(D/'data/verified_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
