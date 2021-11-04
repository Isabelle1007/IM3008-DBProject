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
整合臺灣四個較具規模的線上課程平台（Hahow、TibaMe、Yotta、Pressplay）之課程相關資訊，讓使用者能透過本網站取得及比較該四個平台的課程資訊，進而選擇最符合需求的線上課程平台進行消費。

## [Expected Interface](https://drive.google.com/file/d/14wYfgA65QhYEDV0naj6it6fKj0nA_tJf/view)


## Data Collection
* Collect data by web crawling.


## Database
* Use **PostgreSQL 14** and **pgAdmin**.
* [How to export db to a .sql file](https://stackoverflow.com/questions/37984733/postgresql-database-export-to-sql-file)

**\*: primary key**
### course
| \*course_id | course_name | website_id | course_intro | course_price | course_time | teacher_id | category_id | course_url | course_img_url | status_id | course_tag | 
| - | - | - | - | - | - | - | - | - | - | - | - |
| 00001	| 小資族圓夢計畫，第一次買房收租就上手 | 01	| 這門課程將教會你各種房產投資的知識，包括整層收租、隔套收租、二房東等，讓小資族的你可以了解不同包租公的進出場策略，以及如何降低風險，幫助你第一次買房收租就上手，並且創造穩定的被動收入。 | 3280 | 120 | 01031 | 07 | https://api.hahow.in/api/courses/6136ed9fafdea00006bdd8ee | https://images.api.hahow.in/images/6166a3dc2ba42d0007e344ea | 03	 |
| 00002 | J Team 小學堂－英雄聯盟爬分 10 大重點 | 01 | 想提升《英雄聯盟》牌位嗎？由 PLANET9 與電競戰隊 J Team 合作，帶來職業等級的遊戲觀念指導；從選角、對線、營運、團戰等細節，掌握致勝關鍵，帶你更懂英雄聯盟！ | 990 | 100 | 01031 | 09 | https://api.hahow.in/api/courses/6130753a26d20b0006d48dfe | https://images.api.hahow.in/images/614c237ddeb4b100078678a1	 | 03 |
| 00003 | Knitting好好玩！自己織圍巾、披肩、羊毛帽 | 01 | 輕鬆有趣的編織課，打造獨一無二的風格穿搭。不論是基本針法還是觀念小撇步，都是編織前你想知道的事，一步步完成屬於自己的毛線作品吧！ | 2480 | 150 | 01031 | 09 | https://api.hahow.in/api/courses/6107cd6c3cc7a0000689c1c6 | https://images.api.hahow.in/images/6149d8fc57da0b0006347fb2 | 03	 |

### teacher

### category
| \*cg_id | cg_name |
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

### fundRaising

### review

### discount

## Backend
* [API Design](https://hackmd.io/@K2V5EFQlTWCP33CWgxiuKg/Sy3baYQ8F/)

## Frontend
