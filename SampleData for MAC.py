import pandas as pd
import numpy as np
import datetime as dt

# 주피터 파일에서 읽어온 데이터를 import할 수 없어, 파이썬 파일에서 읽어온 데이터 사용
#=========================================================================
# 변수 정리
# d.anime : anime-dataset-2023.csv
# d.user_details : users-details-2023.csv
# d.user_score : users-score-2023.csv
# d.anime_filter : anime-filtered.csv
# d.Genre : Genres열에 있는 고유 값 리스트
# d.Producers : Producers열에 있는 고유 값 리스트
# d.Licensors : Licensor열에 있는 고유 값 리스트
# d.Studios : Studios열에 있는 고유 값 리스트
#=========================================================================
anime = pd.read_csv("../Data/anime-dataset-2023.csv")
japanMovieRank = pd.read_excel("../Data/일본 내 영화 순위 2.xlsx", sheet_name='korean')
koreanMovieRank = pd.read_excel("../Data/한국 내 영화 순위.xlsx", header=None)
# user_details = pd.read_csv("../Data/users-details-2023.csv")
# user_score=pd.read_csv("../Data/users-score-2023.csv")
# anime_filter=pd.read_csv("../Data/anime-filtered.csv")
#=========================================================================
#=======================anime 변수 전처리=================================
#=========================================================================
# anime : Aired, Premiered 열 삭제 후 상영 시작일(Start_date), 상영 종료일(End_date), 상영일(Aired_Duration)열 추가
anime["Aired"] # 월 일, 년 to 월 일, 년
                 # 월 일, 년 to ?
                 # 월 일, 년
                 
# 월별 숫자 딕셔너리 생성
month_dict={"Dec":12, "Nov":11, "Oct" :10, "Sep":9, "Aug":8, "Jul":7, "Jun":6, "May":5, "Apr":4, "Mar":3, "Feb":2, "Jan":1, "?":0} 

# "to" 를 기준으로 데이터 Parsing
#  Aired에서 날짜가 1개인 데이터는 Start_date와 End_date의 값이 같음
Start_date = anime["Aired"].apply(lambda x: x.split("to")[0])
End_date = anime["Aired"].apply(lambda x: x.split("to")[1] if "to" in x else x)

# 시작 방영일(Start_date) 배열 생성
insert_series=[]
for i in range(anime["Aired"].count()):
    if Start_date.iloc[i]=="Not available": # 결측값 처리
        insert_series.append(np.NaN)
    else :
        time=("").join(Start_date.iloc[i].split(",")).split()
        insert_series.append(dt.datetime( 
                        year=int(time[len(time)-1]), 
                        month=month_dict[time[0]] if len(time)>1 else 1, 
                        day=int(time[1] if len(time)==3 else 1)
                    ))
# 배열 생성 후 열 생성
anime["Start_date"]=insert_series

# 종료 방영일(End_date) 배열 생성
insert_series=[]
for i in range(anime["Aired"].count()):
    if End_date.iloc[i].strip() in ["Not available", "?"]: # 결측값 처리
        insert_series.append(np.NaN)
    else :
        time=("").join(End_date.iloc[i].split(",")).split()
        insert_series.append(dt.datetime( 
                        year=int(time[len(time)-1]), 
                        month=month_dict[time[0]] if len(time)>1 else 1, 
                        day=int(time[1] if len(time)==3 else 1)
                    ))
# 배열 생성 후 열 생성
anime["End_date"]=insert_series
 
# 상영일(Aired_Duration)행 추가
anime["Aired_Duration"]=anime["End_date"]-anime["Start_date"]

# 기존의 Aired, Premiered 행 삭제(중복 열 삭제)
anime.drop(columns=["Aired","Premiered"], inplace=True)

#=========================================================================
#=========================================================================
# 열 데이터 타입 변경
'''
Score : object -> float32로 변경 -> Unsianged int 로 변경
Type : object -> category로 변경
Episodes : Object -> float32 로 변경 -> Unsianged int 로 변경
Aired, Premiered 삭제( 상영 시작 컬럼, 종료 컬럼 및 상영 기간 컬럼 추가로 인한 불필요 데이터 삭제 )
Status : object -> category로 변경
Source : object -> category로 변경
Rating : object -> category로 변경
Rank : object -> float32 로 변경 -> Unsianged int 로 변경
Scored By : object -> float32 로 변경 -> Unsianged int 로 변경
'''
# 결측값 '0'으로 처리
anime["Score"].replace("UNKNOWN","0", inplace=True)
anime["Episodes"].replace("UNKNOWN","0", inplace=True)
anime["Rank"].replace("UNKNOWN","0", inplace=True)
anime["Scored By"].replace("UNKNOWN","0", inplace=True)

anime=anime.astype({"Score":"float32", "Type":"category", "Episodes":"float32", "Status":"category", "Source":"category", "Rating":"category", "Rank":"float32", "Scored By":"float32"})

# float 데이터 타입의 열들을 unsigned int형으로 변환 
anime=anime.astype({"Episodes":"uint8", "Rank":"uint8", "Scored By":"uint8"})
#=========================================================================
# 유용한 변수 추가(설명은 Pre_Processing.ipynb, 위의 주석 참고)

Genre=anime["Genres"].str.split(", ").apply(set).explode().reset_index(drop=True).value_counts().index # 장르 생성

Producers=anime["Producers"].str.split(", ").apply(set).explode().reset_index(drop=True).value_counts().index # 프로듀서 리스트 생성

Licensors=anime["Licensors"].str.split(", ").apply(set).explode().reset_index(drop=True).value_counts().index # 프로듀서 리스트 생성

Studios=anime["Studios"].str.split(", ").apply(set).explode().reset_index(drop=True).value_counts().index # 프로듀서 리스트 생성
#=========================================================================
# Duration 열 값 표준화(24min per ep, 24min => 24min으로 통일)
def delete_per_ep(str):
    if "per ep" in str:
        return str[:-7].strip()
    else :
        return str
    
anime["Duration"]=anime["Duration"].apply(delete_per_ep)
#=========================================================================
#==========================user_details변수 전처리========================
#=========================================================================

#=========================================================================
#===========================user_score변수 전처리=========================
#=========================================================================

#=========================================================================
#                        anime 변수, 열 한국어 설명
#=========================================================================
'''
(int)            anime_id:    각 애니메이션의 고유 ID.
(object)         Name:        원래 언어로 된 애니메이션의 이름.
(object)         English name:애니메이션의 영어 이름.
(object)         Other name : 애니메이션의 네이티브 이름 또는 제목(일본어, 중국어 또는 한국어로 가능).
(float)           Score:       애니메이션에 부여된 점수 또는 등급.
(object)         Genres:      쉼표로 구분된 애니메이션의 장르.
(object)         Synopsis :   애니메이션 줄거리에 대한 간략한 설명 또는 요약.
(category)       Type :       애니메이션의 유형(예: TV 시리즈, 영화, OVA 등).
(uint)           Episodes:    애니메이션의 에피소드 수.
(DELETE)         Aired:       애니메이션 방영일.
(DELETE)         Premiered:   애니메이션이 초연된 시즌과 연도.
(category)       Status:      애니메이션의 상태(예: 방영완료, 현재 방영중 등).
(object)         Producers:   애니메이션의 제작사 또는 제작자. 
(object)         Licensors:   애니메이션(예: 스트리밍 플랫폼)의 라이센서.
(object)         Studios:     애니메이션 작업을 했던 애니메이션 스튜디오.
(category)       Source:      애니메이션의 소스 자료(예: 만화, 라이트 노벨, 오리지널).
(object)         Duration:    각 회차의 듀레이션.
(category)       Rating:      애니메이션의 연령 등급.
(uint)           Rank:        인기도나 기타 기준에 의한 애니메이션의 랭크.
(int)            popularity:  애니메이션의 인기 순위.
(int)            Favorites:   애니메이션이 사용자가 즐겨찾기로 표시한 횟수
(uint)           Scored By:   애니메이션에 점수를 매긴 사용자 수.
(int)            Members:     플랫폼에서 애니메이션을 목록에 추가한 회원 수.
(object)         Image Url :  애니메이션 이미지 또는 포스터의 URL.
(datatime64[ns]) Start_date : 상영시작일
(datatime64[ns]) End_date :   상영종료일
(timedelta64[ns])Aired_Duration : 상영일
'''
# print(anime['English name'], anime['English name'].nunique(), anime['English name'].info())

# pd.set_option('display.max_columns', None)

# print(anime.columns)

# print(anime[['Type', 'Score', 'English name', 'Name']][anime['Type'] == 'Movie'].sort_values(by='Score', ascending=False).head(10))
# print('\n\n\n\n\n')
# # print(anime[['Type', 'Scored By', 'English name', 'Name']][anime['Type'] == 'Movie'].sort_values(by='Scored By', ascending=False).head(10))
# # print('\n\n\n\n\n')
# # print(anime[['Type', 'Popularity', 'English name', 'Name']][anime['Type'] == 'Movie'].sort_values(by='Popularity', ascending=False).head(10))
# # print('\n\n\n\n\n')
# print(anime[['Type', 'Favorites', 'English name', 'Name']][anime['Type'] == 'Movie'].sort_values(by='Favorites', ascending=False).head(10))
# print('\n\n\n\n\n')
# print(anime[['Type', 'Members', 'English name', 'Name']][anime['Type'] == 'Movie'].sort_values(by='Members', ascending=False).head(10))

# anime['English name'].astype(str)
# print(anime['English name'].info())
#
JAPTitleList = ['Kimetsu no Yaiba Movie: Mugen Ressha-hen',
             'Sen to Chihiro no Kamikakushi',
             'Kimi no Na wa.',
             'Howl no Ugoku Shiro',
             'The First Slam Dunk',
             'Gake no Ue no Ponyo',
             'Suzume no Tojimari'
             ]
#
# for j in JAPTitleList:
#     for i in anime['Name']:
#     # print(i)
#         if j in str(i) :
#             print(anime[anime['Name'] == i])
#

# print('Super Mario' in anime['English name'][0])

# print('Super Mario' in anime[anime['English name']])
# print(anime['English name'][0])


'''
발표 시작
'''

'''
0. 자료 출처 소개
0.1. 팀 공통 anime 2023 data set
0.2. 일본 영화 전체 흥행 순위
0.3. 한국 영화 전체 흥행 순위
'''

'''
1. 일본 영화 전체 흥행 순위 전처리
'''
# 1.1. japanMovieRank 일본 영화 전체 흥행 순위 DataFrame 불러오기
# print(japanMovieRank.head(20))

# 1.2. 애니메이션 영화만 10개 추리기, 인덱스 다시 0부터 순차적으로 부여
jMR2 = japanMovieRank.iloc[[0,1,4,5,7,8,12,13,14,15]]
jMR2.reset_index(inplace=True)
# print(jMR2)


'''
2. 한국 영화 전체 흥행 순위 전처리
'''
# 2.1 koreanMovieRank 한국 내 애니 영화 전체 흥행 순위 DataFrame 불러오기
# print(koreanMovieRank)

# 2.2 KMR 내 컬럼명 추가하기
KMRcolumns = ['한국순위', '작품제목', '제작 연도', '감독', '관객 수']
koreanMovieRank.columns = KMRcolumns
# print(koreanMovieRank)

# print(jMR2['작품제목'], koreanMovieRank['작품제목'])

# 2.3 작품제목 통일하기
# totalOuter = pd.merge(jMR2, koreanMovieRank, how = 'outer')
# print(totalOuter)
# print(pd.merge(jMR2['작품제목'], koreanMovieRank['작품제목'], how = 'outer'))

'''
함수로 바꾸기
# iList = [0,6,8,7]
# jList = [4,1,0,7]
#
# while i < len(iList):
#
#     jMR2['작품제목'][iList[i]] = jMR2['작품제목'][iList[i]].replace(jMR2['작품제목'][iList[i]], koreanMovieRank['작품제목'][jList[j]])
#     i += 1
'''

# '''
jMR2['작품제목'][0] = jMR2['작품제목'][0].replace(jMR2['작품제목'][0], koreanMovieRank['작품제목'][4])
jMR2['작품제목'][6] = jMR2['작품제목'][6].replace(jMR2['작품제목'][6], koreanMovieRank['작품제목'][1])
jMR2['작품제목'][8] = jMR2['작품제목'][8].replace(jMR2['작품제목'][8], koreanMovieRank['작품제목'][0])
jMR2['작품제목'][7] = jMR2['작품제목'][7].replace(jMR2['작품제목'][7], koreanMovieRank['작품제목'][7])
# '''


# print(jMR2.info(),koreanMovieRank.info())
# print(jMR2.columns, koreanMovieRank.columns)
# print(jMR2)
totalInner = pd.merge(jMR2, koreanMovieRank, left_on="작품제목", right_on="작품제목")
# print(totalInner)
# print(totalInner[['작품제목', '순위', '한국순위', '흥행 수입(억 엔)', '제작 연도', '감독', '관객 수']])

total = totalInner[['작품제목', '순위', '한국순위', '흥행 수입(억 엔)', '제작 연도', '감독', '관객 수']]
# print(total)
# print(pd.merge(jMR2['작품제목'], koreanMovieRank['작품제목'], how = 'inner'))

# dataAni = anime[['Name', 'Score', 'Favorites', 'Members']]
# print(dataAni)

# iiList =[]
# for j in JAPTitleList:
#     for i in dataAni['Name']:
#         if i == j:
#             iiList.append(i)
#             print(iiList)

total['Name'] = JAPTitleList

# total['Favorites'] =
print(anime[anime["Name"].isin(JAPTitleList)])

# print(total)



# if __name__=="__main__":
    # pass