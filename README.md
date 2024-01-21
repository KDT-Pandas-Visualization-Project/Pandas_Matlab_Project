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

옥영신 :

이시명 : 
> 1.  dataset에 들어있는 일본 애니 영화 순위 및 평점 분석

> 2. 한국 개봉 일본 애니 10위까지 분석
- 박스오피스 외화 500위 자료 - 일본 애니 3위까지 밖에 없음
- 추가자료로 영진위 DB분석해야함. 순위자료에는 관객수가 없어서 추가 검색을 통해 DB를 보충해야 함.
https://www.kofic.or.kr/kofic/business/infm/introData.do

> 3. 일본 내에서 개봉한 애니 영화 순위 파악
- 아직 DB 못구함






