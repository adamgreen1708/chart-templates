"""Optional data-driven table columns around a horizontal bar chart."""
from matplotlib.lines import Line2D


def apply_table_layout(fig, ax, rows, config, row_style):
    layout = config.get('table_layout')
    if not layout:
        return
    if config.get('chart_type') != 'bar' or config.get('orientation') != 'horizontal':
        raise ValueError('table_layout requires horizontal bars')
    rank_col = layout['rank_column']
    ordered = sorted(rows, key=lambda r: int(r[rank_col]))
    if [int(r[rank_col]) for r in ordered] != list(range(1, len(rows)+1)):
        raise ValueError('Ranked table requires unique consecutive ranks starting at 1')
    values = [float(r[config['x_col']]) for r in ordered]
    if any(a < b for a,b in zip(values, values[1:])):
        raise ValueError('Rank must follow descending bar values')
    lookup = {str(r[config['y_col']]): i for i,r in enumerate(rows)}
    ax.set_ylim(-.5, len(rows)-.5)
    ax.set_yticks([]); ax.set_xticks([]); ax.grid(False)
    for spine in ax.spines.values():
        spine.set_visible(False)
    artists = []
    for col in layout['columns']:
        fig.text(col['x'], layout['header_y'], col['label'], fontsize=12,
                 ha=col.get('ha','left'), va='center', color='#555555', weight='bold')
    h = layout['bar_header']
    fig.text(h['x'], layout['header_y'], h['text'], fontsize=12, weight='bold', color='#555555', va='center')
    for row in ordered:
        y = fig.transFigure.inverted().transform(ax.transData.transform((0,lookup[str(row[config['y_col']])])))[1]
        for col in layout['columns']:
            value = row[col['column']]
            text = format(float(value),col['format']) if col.get('format') else str(value)
            color = row_style(row).get('color','#7A7A7A') if col.get('semantic_color') else '#555555'
            artists.append(fig.text(col['x'],y,text,fontsize=12,ha=col.get('ha','left'),va='center',color=color))
        if int(row[rank_col]) < len(rows):
            gap = ax.get_position().height/len(rows)
            fig.add_artist(Line2D([.09,.91],[y-gap/2,y-gap/2], transform=fig.transFigure,color='#D9D9D9',lw=.35,zorder=0))
    for item in layout.get('legend',[]):
        fig.text(item['x'],layout['legend_y'],item['text'],fontsize=12,color=item['color'],va='center')
    for note in layout.get('notes',[]):
        fig.text(.09,note['y'],note['text'],fontsize=10.5,color='#555555')
    fig.canvas.draw()
    renderer=fig.canvas.get_renderer()
    n=len(layout['columns'])
    for i in range(len(rows)):
        boxes=[a.get_window_extent(renderer) for a in artists[i*n:(i+1)*n]]
        for a,b in zip(boxes,boxes[1:]):
            if a.x1+4 > b.x0:
                raise ValueError('Ranked table text columns collide; shorten display labels')
    return artists
