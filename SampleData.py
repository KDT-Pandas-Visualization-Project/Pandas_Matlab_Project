import pandas as pd
import numpy as np

# 주피터 파일에서 읽어온 데이터를 import할 수 없어, 파이썬 파일에서 읽어온 데이터 사용
anime = pd.read_csv(r"..\Data\anime-dataset-2023.csv")
user_details = pd.read_csv(r"..\Data\users-details-2023.csv")
user_score=pd.read_csv(r"..\Data\users-score-2023.csv")
anime_filter=pd.read_csv(r"..\Data\anime-filtered.csv")
print("Complete!")