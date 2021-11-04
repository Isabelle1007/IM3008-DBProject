# IM3008-Database Management Midterm Project
# 台灣線上課程平台資訊整合網站

## Contributor and Tasks
* 楊佳芊: Data Collection
* 王亭勻: User Interface Design
* 林暐倫: User Needs Research
* 葉柏辰: Frontend
* 施芊羽: Database Schema Design, Backend
* 陳亮瑜: Data Collection
* 陳旻浚: Frontend
* 黃晨亘: User Needs Research, Backend

## Target
整合臺灣四個較具規模的線上課程平台（Hahow、TibaMe、Pressplay、Yotta）之課程相關資訊，讓使用者能透過本網站取得及比較該四個平台的課程資訊，進而選擇最符合需求的線上課程平台進行消費。

## [Expected Interface](https://drive.google.com/file/d/14wYfgA65QhYEDV0naj6it6fKj0nA_tJf/view)


## Data Collection
* Collect data by web crawling.


## Database
* Use **PostgreSQL 14** and **pgAdmin**.
* [How to export db to a .sql file](https://stackoverflow.com/questions/37984733/postgresql-database-export-to-sql-file)
* [Schema](https://drive.google.com/drive/u/1/folders/1GssFT7IbZgx6FETD6IzUqBgVSUw7BDop)

**\*: primary key**
### course
記錄所有課程相關的詳細資料
| \*course_id | course_name | website_id | course_intro | course_price | course_time | teacher_id | category_id | course_url | course_img_url | status_id | course_tag | 
| - | - | - | - | - | - | - | - | - | - | - | - |
| 00001	| 小資族圓夢計畫，第一次買房收租就上手 | 01	| 這門課程將教會你各種房產投資的知識，包括整層收租、隔套收租、二房東等，讓小資族的你可以了解不同包租公的進出場策略，以及如何降低風險，幫助你第一次買房收租就上手，並且創造穩定的被動收入。 | 3280 | 120 | 01031 | 07 | https://hahow.in/courses/6136ed9fafdea00006bdd8ee | https://images.api.hahow.in/images/6166a3dc2ba42d0007e344ea | 03	 |
| 00002 | J Team 小學堂－英雄聯盟爬分 10 大重點 | 01 | 想提升《英雄聯盟》牌位嗎？由 PLANET9 與電競戰隊 J Team 合作，帶來職業等級的遊戲觀念指導；從選角、對線、營運、團戰等細節，掌握致勝關鍵，帶你更懂英雄聯盟！ | 990 | 100 | 01031 | 09 | https://hahow.in/courses/6130753a26d20b0006d48dfe | https://images.api.hahow.in/images/614c237ddeb4b100078678a1	 | 03 |
| 00003 | Knitting好好玩！自己織圍巾、披肩、羊毛帽 | 01 | 輕鬆有趣的編織課，打造獨一無二的風格穿搭。不論是基本針法還是觀念小撇步，都是編織前你想知道的事，一步步完成屬於自己的毛線作品吧！ | 2480 | 150 | 01031 | 09 | https://hahow.in/courses/6107cd6c3cc7a0000689c1c6 | https://images.api.hahow.in/images/6149d8fc57da0b0006347fb2 | 03	 |

### teacher
記錄授課老師相關資訊
| \*teacher_id | teacher_name | teacher_intro | teacher_img_url |
| - | - | - | - |
| 00001 | RICHARK | 是一個「全方位教練系統 Total Coaching System」，為創辦人「吳建賢Cosmo」所成立，以「方舟計劃」尊榮會員制運作，人脈資源整合及教練諮詢並結合教育訓練系統，透過實戰操練及創業輔導，協助學員打造被動收入邁向「財富自由」。 | https://images.api.hahow.in/images/5d2fdd5bfe9fef0021fadfe6 |
| 00002 | PLANET9 | PLANET9提供全球玩家全方位的遊戲體驗，從「組隊」、「找教練」到「賽事舉辦」等多元化服務；今年PLANET9更將著重於優質「電競課程」；在PLANET9平台上有來自世界各地教練所設計的電競課程，將針對不同級別玩家提供各種選擇，讓PLANET9能伴隨玩家「Master Your Play」顯示部份資訊 | https://images.api.hahow.in/images/613071b126d20b0006d48a24 | 
| 00003 | May｜就是愛編織 | May，專職玩毛線十多年，有一間靠近海的手染編織工作室，有植物，好咖啡，和機靈的狗朋友Oreo | https://images.api.hahow.in/images/60ee725d6f72e50006f594df | 


### category
課程的分類
| \*category_id | category_name |
| ------- | ------- |
| 01      | 語言     |
| 02      | 藝術     |
| 03      | 設計     |
| 04      | 多媒體設計 |
| 05      | 程式     |
| 06      | 行銷     |
| 07      | 投資理財  |
| 08      | 職場技能  |
| 09      | 生活品味  |

### website 
記錄四個線上課程平台的基本資訊
| \*website_id | website_name | website_url |
| - | - | - |
| 01 | hahow | https://hahow.in/courses |
| 02 | tibame | https://www.tibame.com/courselibrary |
| 03 | pressplay | https://www.pressplay.cc/ |
| 04 | yotta |https://www.yottau.com.tw/home |

### fundRaising
記錄課程募資相關的資訊
| \* fundraise_id | fundraise_due_date | fundraise_percent | course_id |
| 00001 | 2021-12-02T16:00:00.000Z | \\N | 00001 |
| 00002 | 2021-11-01T16:00:00.000Z | \\N | 00002 |
| 00003 | 2021-11-26T16:00:00.000Z | \\N | 00003 |

### review
記錄使用者對各課程留下的評價及留言
| \*review_id | review_star | review_content | review_time | course_id |
| 00001	| \\N | 請教一下會指導吃兵訣竅嗎？多謝 | 2021-11-03T09:32:04.171Z | 00002 |
| 00002	| \\N | 竟然有英雄聯盟課程也太酷了吧~ | 2021-11-02T04:11:16.135Z | 00002 |
| 00003 | \\N | 不只是伊隆·馬斯克的SpaceX, 我已經準備好要跟火星人Mars 飛向調酒宇宙了!!!! | 2021-11-02T12:45:05.923Z | 00004 |

### discount
記錄各課程的優惠資訊

## Backend
* [API Design](https://hackmd.io/@K2V5EFQlTWCP33CWgxiuKg/Sy3baYQ8F/)

## Frontend
