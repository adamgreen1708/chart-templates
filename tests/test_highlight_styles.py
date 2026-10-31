import sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import render_538 as r
class HighlightStyles(unittest.TestCase):
 def setUp(self):
  self.old=r.CHART_CONFIG
  r.CHART_CONFIG={'chart_type':'scatter','x_col':'x','y_col':'y','highlight_style':{'color':'blue','size':90,'alpha':1},'highlight_points':[{'group':'Picard','color':'red','size':70},{'group':'Xavier','color':'blue'}]}
  self.rows=[{'x':1,'y':1,'group':'Picard'},{'x':2,'y':2,'group':'Xavier'},{'x':3,'y':3,'group':'Other'}]
 def tearDown(self):r.CHART_CONFIG=self.old;plt.close('all')
 def test_scatter_separate_colours_and_sizes(self):
  fig,ax=plt.subplots();r._plot_scatter(ax,self.rows);fig.canvas.draw();high=ax.collections[1]
  self.assertEqual(list(high.get_sizes()),[70,90])
  self.assertEqual(list(map(tuple,high.get_facecolors())),[to_rgba('red'),to_rgba('blue')])
 def test_bar_separate_colours(self):
  r.CHART_CONFIG.update(chart_type='bar',orientation='horizontal',bar_style={'color':'grey'});fig,ax=plt.subplots();r._plot_bar(ax,self.rows)
  self.assertEqual([p.get_facecolor() for p in ax.patches],[to_rgba('red',.9),to_rgba('blue',.9),to_rgba('grey',.9)])
 def test_fallback_first_match_and_colour_alias(self):
  r.CHART_CONFIG['highlight_points']=[{'group':'Picard','colour':'red'},{'group':'Picard','color':'green'},{'group':'Xavier'}]
  self.assertEqual(r._row_highlight_style(self.rows[0])['color'],'red')
  self.assertEqual(r._row_highlight_style(self.rows[1])['color'],'blue')
if __name__=='__main__':unittest.main()
