import csv,runpy
from pathlib import Path
import pytest
import matplotlib.pyplot as plt
from src import render_538 as render
from src.ranked_table import apply_table_layout
ROOT=Path(__file__).resolve().parents[1]
D=ROOT/'archive/projects/2026-10-patrick-stewart'

def test_all_ranks_values_and_character_groups():
 runpy.run_path(str(D/'scripts/build_chart_views.py'))
 source=list(csv.DictReader((D/'data/films_expanded.csv').open()))
 expected=sorted([r for r in source if r['votes']],key=lambda r:-int(r['votes']))[:25]
 rows=list(csv.DictReader((D/'data/top25_votes.csv').open()))
 assert [int(r['rank']) for r in rows]==list(range(1,26))
 assert [(r['tconst'],r['votes'],r['year']) for r in rows]==[(r['tconst'],r['votes'],r['year']) for r in expected]
 assert [int(r['rank']) for r in rows if r['character_group']=='Picard']==[17,20,21,23]
 assert sum(r['character_group']=='Xavier' for r in rows)==8
 assert rows[11]['year']=='1984'

def test_table_rejects_false_ranks():
 fig,ax=plt.subplots()
 cfg={'chart_type':'bar','orientation':'horizontal','x_col':'votes','y_col':'name','table_layout':{'rank_column':'rank'}}
 with pytest.raises(ValueError,match='consecutive'):
  apply_table_layout(fig,ax,[{'rank':2}],cfg,lambda r:{})
 with pytest.raises(ValueError,match='descending'):
  apply_table_layout(fig,ax,[{'rank':1,'votes':1},{'rank':2,'votes':2}],cfg,lambda r:{})
 plt.close(fig)

def test_rendered_table_bars_have_exact_dataset_widths_and_colours(monkeypatch):
 cfg=runpy.run_path(str(D/'config/chart_1.py'))['CHART_CONFIG']
 monkeypatch.setattr(render,'CHART_CONFIG',cfg)
 render.main();ax=plt.gcf().axes[0]
 rows=sorted(list(csv.DictReader((D/'data/top25_votes.csv').open())),key=lambda r:float(r['votes_k']))
 assert len(ax.patches)==25
 colours={'Picard':'#C44E52','Xavier':'#1F8FA8','Other':'#7A7A7A'}
 from matplotlib.colors import to_rgba
 for bar,row in zip(ax.patches,rows):
  assert bar.get_width()==float(row['votes_k'])
  assert bar.get_facecolor()==to_rgba(colours[row['character_group']],.9)
 plt.close('all')
