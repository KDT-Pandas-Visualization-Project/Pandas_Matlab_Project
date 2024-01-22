import pandas as pd
KMRcolumns = ['순위', '영화 제목', '제작 연도', '감독', '관객 수']
koreanMovieRank = pd.read_excel("../Data/한국 내 영화 순위.xlsx", names=KMRcolumns)

# 2.1 koreanMovieRank 한국 내 애니 영화 전체 흥행 순위 DataFrame 불러오기
print(koreanMovieRank)

# 2.2 KMR 내 컬럼명 추가하기
