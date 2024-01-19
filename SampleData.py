import pandas as pd
import numpy as np

# 주피터 파일에서 읽어온 데이터를 import할 수 없어, 파이썬 파일에서 읽어온 데이터 사용
data = pd.read_csv(r'..\Data\anime-dataset-2023.csv')
print(data.head(2))