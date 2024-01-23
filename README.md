## 노션 페이지 : https://www.notion.so/3404a9116b304dc5871e6a2b97e0ce9f?v=cde676cbcd6d4181a11719320a6691b5&pvs=4   
 
## **팀** : 사타쿠(4たく)   
> * 명노아 : mathnoah@naver.com   
> * 이윤서 : pdbstj050303@gmail.com   
> * 옥영신 : yeongshin.ok@gmail.com   
> * 이시명 : holicalday@gmail.com   

## 주제 : Pandas와 Matplotlib을 활용한 애니메이션 데이터 분석 & 시각화   



## 사용하는 데이터 열 해석   

#### Anime-dataset-2023.csv   
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
<hr/>   
#### users-details-2023.csv     
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
<hr/>
#### users-score-2023.csv   
  1. user_id: 각 사용자의 고유 ID.   
  2. Username:  사용자의 사용자 이름입니다.   
  3. anime_id: 각 애니메이션의 고유 ID.   
  4. Anime Title: 애니메이션 제목.   
  5. rating: 사용자가 애니메이션에 부여한 등급입니다.   
<hr/>








## 관련 데이터 포털   
KOSIS 국가통계포털 : https://kosis.kr/index/index.do   
2023 대한민국 사회안전지수 : https://www.mt.co.kr/ksi/   
정보공개포털 : https://www.open.go.kr/com/main/mainView.do   
statista : https://www.statista.com/studies-and-reports/   
한국관광 데이터랩 : https://datalab.visitkorea.or.kr/datalab/portal/main/getMainForm.do   
OECD statistic : https://stats.oecd.org/   
세계은행 데이터 : https://data.worldbank.org/   
기상청 지진정보 데이터 : https://www.data.go.kr/data/15082971/fileData.do   
Out world in data : https://ourworldindata.org/search?q=democracy   
일본 애니 영화 순위 : https://www.kogyotsushin.com/archives/alltime/   
MyAnimeList : https://namu.wiki/w/MyAnimeList   
pyplot-bar차트 꾸미기 : https://zephyrus1111.tistory.com/9   
오타쿠 세대 정리 노트 : https://note.com/hogehoge_aichi/n/n4e1ca9d536ec   
깃허브 협업 git bash 코드 : https://velog.io/@minwest/github%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%98%91%EC%97%85-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0#basic   

## 애로사항   
VS code 에서 파일이 읽히지 않을 때 : https://barrer.tistory.com/67   
