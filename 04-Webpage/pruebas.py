import pandas as pd
import pathlib
initial_path = r'/app/centralbankanalytics/'
path = r'..\02-Data\03-Gold_vs_silver_ratio\01-Gold_vs_silver_ratio.parquet'
a = pd.read_parquet(pathlib.Path(path).absolute())

path_2 = path[3:]
cwd = initial_path + path_2
print(cwd)