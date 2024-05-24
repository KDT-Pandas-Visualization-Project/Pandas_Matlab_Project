
KDT(Korea Digital Training) 경북대학교, Pandas-Matplotlib을 사용한 데이터 분석 단기 프로젝트

# 팀 구성 <hr/>

명노아 : mathnoah@naver.com  
이윤서 : pdbstj050303@gmail.com  
옥영신 : yeongshin.ok@gmail.com  
이시명 : holicalday@gmail.com   

Reference about DB URL  
1 https://kosis.kr/index/index.do  
2 https://www.mt.co.kr/ksi/  
3 https://www.open.go.kr/com/main/mainView.do  
4 https://www.statista.com/studies-and-reports/  
5 https://stats.oecd.org/  
6 https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do  
7 https://data.worldbank.org/  


# 0. 후보작들 중 아이디어 선정

1. 뉴스와 함께 알아보는 대한민국에 직접 표시하는 분기별 이동 인구와 이슈 분석 시각화 프로그램  
https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B26006_A01&vw_cd=MT_ZTITLE&list_id=A_1&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE  
https://skyseven73.tistory.com/23  
https://github.com/vuski/admdongkor  
https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B26001_A02&vw_cd=MT_ZTITLE&list_id=A34_3&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE  
https://kosis.kr/statHtml/statHtml.do?orgId=101&tblId=DT_1B040A3&vw_cd=MT_ZTITLE&list_id=A_7&seqNo=&lang_mode=ko&language=kor&obj_var_id=&itm_id=&conn_path=MT_ZTITLE  

2. 전세계 애니메이션 분석&시각화 + 애니메이션 추천 프로그램  
https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?resource=download  

3. 대구인이 느끼는 기후변화 위기  
https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70  

4. MZ의 삶(노동/결혼/경제/갈등?/범죄/교육/여가)  
https://mdis.kostat.go.kr/index.do  (데이터 URL -> MDIS-자료이용-다운로드서비스)  

5. 질 리포베츠키의 유혹과 덧없음 이론에 기반한 패션과 민주주의의 상관관계  
https://ourworldindata.org/grapher/democracy-index-eiu?tab=table  
https://www.statista.com/forecasts/1156486/fashion-consumer-spending-per-capita-by-country  

6. Sporty를 이용한 국내 및 해외 음원 차트 순위 및 점유도 분석  
https://www.sportybet.com/gh/  


=> 2번 아이디어로 결정!


# 1. 역할분담

명노아 :  
  > 1. "Anime-dataset-2023.csv"를 활용하여 제작사(Producers) 마다 만들어내는 장르(Genres) 와 애니메이션의 소스 자료(Source) 분석 -> 파이차트로 시각화, Bar of pie를 사용하여 제작사가 만든 장르를 확대하여 인기작품 나열  
사용 컬럼 : Other name, Score, Genres(전처리 필요), Producers, Source  

  > 2.  "Anime-dataset-2023.csv"를 활용하여 오타쿠 세대를 6개로 분류하여, 세대별 유명했던 애니메이션(Score, Aired) 종류 및 장르 분석 하여 세대별 TOP5 작품 뽑아내기  
>  > -> Bar chart on polar axis로 시각화 및  Grouped bar chart with labels로 시각화  
사용 컬럼 : Aired(전처리 및 열 추가작업 필요), Score, Genres(전처리 필요)   

  > 3.  "Anime-dataset-2023.csv","user-details-2023.csv","user-score-2023.csv"를 사용하여 연령 등급(Rating)별 남녀 시청 비율 및 남녀별 등급 부여 차이 분석  
  >  > -> plot ,Bar chart with gradients 으로 시각화  
사용 컬럼 :   

이윤서 :

옥영신 : - 국가별 일본 무역량과 일본 애니 인기의 상관관계, user detail
    1. 애니메이션 시청자 국가 분포도
        - 국가와 도시 정보, 전세계 도시 이름 영어/라틴어로 된 자료로 inner join 15만 ⇒ 3만
        - 국가별 이용자 수 애니 시청자 수 - 언어문제로 날아간듯?
    2. 500편 이상은 오타쿠, 각 국가 별 인구 대비
        - 인구자료 출처 : worldmeter
    3. 수출국 순위와 인구 대비 전체 애니 시청자수/오타쿠 수 - 국가별 상관관계
        - 각 국 인구대비 순위
    4. 수출국 순위와 단순 애니 시청자 수

이시명 : 
> 1.  dataset에 들어있는 일본 애니 영화 순위 및 평점 분석  

> 2. 한국 개봉 일본 애니 10위까지 분석
- 박스오피스 외화 500위 자료 - 일본 애니 3위까지 밖에 없음  
- 추가자료로 영진위 DB분석해야함. 순위자료에는 관객수가 없어서 추가 검색을 통해 DB를 보충해야 함.  
https://www.kofic.or.kr/kofic/business/infm/introData.do  
 
> 3. 일본 내에서 개봉한 애니 영화 순위 파악  
- 아직 DB 못구함  






=======
# Pandas + Matplotlib 응용 프로젝트
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgjbae1212%2Fhit-counter&count_bg=%23386317&title_bg=%23000000&icon=cliqz.svg&icon_color=%23E7E7E7&title=hits%28%EC%A1%B0%ED%9A%8C%EC%88%98%29&edge_flat=false"/></a>

## 노션 페이지 : [Notion](https://www.notion.so/3404a9116b304dc5871e6a2b97e0ce9f?v=cde676cbcd6d4181a11719320a6691b5&pvs=4   )
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Microsoft PowerPoint](https://img.shields.io/badge/Microsoft_PowerPoint-B7472A?style=for-the-badge&logo=microsoft-powerpoint&logoColor=white)
![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
![KakaoTalk](https://img.shields.io/badge/kakaotalk-ffcd00.svg?style=for-the-badge&logo=kakaotalk&logoColor=000000)
![Notion](https://img.shields.io/badge/Notion-%23000000.svg?style=for-the-badge&logo=notion&logoColor=white)

## **팀** : 사타쿠(4たく)   
> * 명노아 : mathnoah@naver.com   
> * 이윤서 : pdbstj050303@gmail.com   
> * 옥영신 : yeongshin.ok@gmail.com   
> * 이시명 : holicalday@gmail.com   

## 주제 : Pandas와 Matplotlib을 활용한 애니메이션 데이터 분석 & 시각화   


## 데이터셋 링크 : [myanimelist-dataset](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset?resource=download)   
<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F11299784%2Fcaaff69976c0a1e97c7d55eb82383680%2Fstatic-assets-upload6207184415643227018.jpg?generation=1686492418151095&alt=media" width="1200" height="500">

## 멤버별 분석 항목
> ### 이시명 : 한/일에서 인기 있는 일본 애니 영화는 어떤 평을 받고 있을까?   
> ### 명노아 : 애니 데이터를 "장르" 로 바라보았다   
> ### 이윤서 : 애니 데이터 평점과 선호도 분석   
> ### 옥영신 : 일본어 상업과 애니메이션 인기의 필연적 연결고리를 찾다
<hr/>


## 사용하는 데이터 열 해석   

#### Anime-dataset-2023.csv   
```
  1. anime_id: 각 애니메이션의 고유 ID.   
  2. Name:원래 언어로 된 애니메이션의 이름.   
  3. English name:애니메이션의 영어 이름.   
  4. Other name :애니메이션의 네이티브 이름 또는 제목(일본어, 중국어 또는 한국어로 가능).   
  5. Score:애니메이션에 부여된 점수 또는 등급.   
  6. Genres:쉼표로 구분된 애니메이션의 장르.   
  7. Synopsis :애니메이션 줄거리에 대한 간략한 설명 또는 요약.   
  8. Type :애니메이션의 유형(예: TV 시리즈, 영화, OVA 등).   
  9. Episodes:애니메이션의 에피소드 수.   
  10. Aired:애니메이션 방영일.   
  11. Premiered: 애니메이션이 초연된 시즌과 연도.   
  12. Status:애니메이션의 상태(예: 방영완료, 현재 방영중 등).   
  13. Producers:애니메이션의 제작사 또는 제작자.   
  14. Licensors: 애니메이션(예: 스트리밍 플랫폼)의 라이센서.   
  15. Studios: 애니메이션 작업을 했던 애니메이션 스튜디오.   
  16. Source:애니메이션의 소스 자료(예: 만화, 라이트 노벨, 오리지널).   
  17. Duration: 각 회차의 듀레이션.    
  18. Rating:애니메이션의 연령 등급.   
  19. Rank:인기도나 기타 기준에 의한 애니메이션의 랭크.   
  20. popularity:애니메이션의 인기 순위.   
  21. Favorites:애니메이션이 사용자가 즐겨찾기로 표시한 횟수   
  22. Scored By:애니메이션에 점수를 매긴 사용자 수.   
  23. Members: 플랫폼에서 애니메이션을 목록에 추가한 회원 수.   
  24. Image Url : 애니메이션 이미지 또는 포스터의 URL.
```
<hr/>   

#### users-details-2023.csv     
```
  1. Mal ID: 각 사용자의 고유 ID.   
  2. Username: 사용자의 사용자 이름입니다.   
  3. Gender:사용자의 성별.   
  4. Birthday: 사용자의 생일(ISO 형식).   
  5. Location:  사용자의 위치 또는 국가.   
  6. Joined: 사용자가 플랫폼에 가입한 날짜(ISO 형식).   
  7. Days Watched: 사용자가 애니메이션을 시청한 총 일 수.   
  8. Mean Score: 사용자가 본 애니메이션에 부여한 평균 점수입니다.   
  9. Watching: 현재 사용자가 시청중인 애니메이션의 수.   
  10. Completed: 사용자가 완료한 애니메이션 수.   
  11. On Hold: 사용자가 보류 중인 애니메이션 수.   
  12. Dropped: 사용자가 삭제한 애니메이션 수.   
  13. Plan to Watch:  사용자가 앞으로 볼 예정인 애니메이션의 개수.   
  14. Total Entries: 사용자 목록에 있는 애니메이션 항목의 총 수.   
  15. Rewatched: 사용자가 다시 본 애니메이션의 수.   
  16. Episodes Watched: 사용자가 시청한 총 에피소드 수.
```
<hr/>

#### users-score-2023.csv   
```
  1. user_id: 각 사용자의 고유 ID.   
  2. Username:  사용자의 사용자 이름입니다.   
  3. anime_id: 각 애니메이션의 고유 ID.   
  4. Anime Title: 애니메이션 제목.   
  5. rating: 사용자가 애니메이션에 부여한 등급입니다.
```
<hr/>

<hr/>

1p 넣기


## 이시명 : 한/일에서 인기있는 일본 애니 영화는 어떤 평을 받고 있을까?

### 일본 내 일본 애니메이션 영화 TOP 100 자료수집
- https://www.kogyotsushin.com/archives/alltime
### 데이터 전처리
> 1. 일본 영화 전체 흥행 순위 전처리
>>   - japanMovieRank 일본 영화 전체 흥행 순위 DataFrame 불러오기
>>  - 애니메이션 영화만 10개 추리기, 인덱스 다시 0부터 순차적으로 부여
>> 11p 넣기
> 2. 한국 영화 전체 흥행 순위 전처리
>>  - 한국 영화진흥위원회는 API 미이용시 총 순위 200위까지만 제공
>>  - 나무위키 역대 일본 애니메이션 영화 한국 흥행 순위 참고
>>  - koreanMovieRank 한국 내 애니 영화 전체 흥행 순위 DataFrame 생성
>> 18p 넣기
>3. KMR 내 컬럼명 추가
>4. 일본 영화DF, 한국 영화DF outer join
>5. 이름이 다른 경우 확인하여 replace로 동일하게 변경
>6. 다시 일본 영화DF, 한국 영화DF inner join
>7. 공통된 7작품 확인
>> 23p 넣기
>8. anime-dataset-2023에서 7작품 찾기
>9. 필요 컬럼 추가 후 데이터 전처리 완료
>> 28p 넣기

### 데이터 분석

>1. 감독별 갯수 확인
>2. 컬럼별 산포도 확인
>3. 컬럼별 분산 확인
>4. 컬럼별 히트맵 확인

#### 5. 데이터 분석
>5.1 순위/흥행 수입(억 엔), 한국순위/관객 수, 순위/Members
>관객 수에 따른 순위이며 자연스럽게 흥행 수익과 연관되며 해당 팬들이 많을 것임을 짐작해볼 수 있는 지표
>5.2 Favorites / 순위
>5.3 한국순위 / 제작연도
>5.4 Popularity / 한국순위
>5.5 제작연도/관객 수

<bold> 각 컬럼 간의 관계를 영화별로 살펴볼 수 있었다</bold>
























## 관련 데이터 포털   
  + KOSIS 국가통계포털 : https://kosis.kr/index/index.do   
  + 2023 대한민국 사회안전지수 : https://www.mt.co.kr/ksi/   
  + 정보공개포털 : https://www.open.go.kr/com/main/mainView.do   
  + statista : https://www.statista.com/studies-and-reports/   
  + 한국관광 데이터랩 : https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do   
  + OECD statistic : https://stats.oecd.org/   
  + 세계은행 데이터 : https://data.worldbank.org/   
  + 기상청 지진정보 데이터 : https://www.data.go.kr/data/15082971/fileData.do   
  + Out world in data : https://ourworldindata.org/search?q=democracy   
  + 일본 애니 영화 순위 : https://www.kogyotsushin.com/archives/alltime/   
  + MyAnimeList : https://namu.wiki/w/MyAnimeList   
  + pyplot-bar차트 꾸미기 : https://zephyrus1111.tistory.com/9   
  + 오타쿠 세대 정리 노트 : https://note.com/hogehoge_aichi/n/n4e1ca9d536ec   
  + 깃허브 협업 git bash 코드 : https://velog.io/@minwest/github%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%98%91%EC%97%85-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0#+basic   

<hr/>

## 애로사항   
VS code 에서 파일이 읽히지 않을 때 : https://barrer.tistory.com/67   

