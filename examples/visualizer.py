from datetime import datetime
import pandas as pd

import sys
sys.path.append("..")
from src.apollo.html_visualizer import Presentation

presentation = Presentation(
    dark_mode=True,
    path_dir_statics='./statics'
)

presentation.add_h2('Report')
presentation.add_paragraph(' '.join(['hello its a sample report' for i in range(80)]))
presentation.add_scatter(x_data=[2.1, 2.2, 2.3, 4], y_data=[12,14,13,15.2], title='Random Scatter')


dict_price = [
    {'date': datetime(year=2023,month=1,day=1), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=2), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=3), 'high':12, 'low':9, 'close':11, 'open':11.8},
    {'date': datetime(year=2023,month=1,day=4), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=5), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=6), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
]

df_price = pd.DataFrame(dict_price)

presentation.add_table_zebra(df_table=df_price,title='Zebra table')
presentation.add_candlestick(df_price=df_price,title='Candle stick table')


presentation.save_html_file(path='random2.html')