from src.visual.html_visualizer import Presentation
from datetime import datetime
import pandas as pd

presentation = Presentation(dark_mode=True)

presentation.add_h2('Report')
presentation.add_paragraph('hello its a sample report')
presentation.add_scatter(x_data=[2.1, 2.2, 2.3, 4], y_data=[12,14,13,15.2])


dict_price = [
    {'date': datetime(year=2023,month=1,day=1), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=2), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=3), 'high':12, 'low':9, 'close':11, 'open':11.8},
    {'date': datetime(year=2023,month=1,day=4), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=5), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
    {'date': datetime(year=2023,month=1,day=6), 'high':10, 'low':9, 'close':9.3, 'open':9.1},
]

df_price = pd.DataFrame(dict_price)

presentation.add_table_zebra(df_table=df_price)
presentation.add_candlestick(df_price=df_price)



print(f'result: {presentation.get_html_str()}')
presentation.save_html_file(path='random.html')