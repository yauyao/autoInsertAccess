# AutoInsertAccess - 自動化網頁爬蟲輸入至本地資料庫 
將網頁抓的內容存入Access中(以基金現值為例)
### 一、前言
主要目的為自動化抓取網頁資訊(例如：基金每日淨值)，並將其輸入至本地資料庫，再利用本地資料庫的報表功能展現數據，希望藉此減少資料收集所需要的時間。
### 二、環境需求
1. [Python 3.6]("https://www.python.org") 
2. Datebase: Microsoft Access
3. [ODBC(x64)]("https://www.microsoft.com/zh-tw/download/details.aspx?id=13255")

如果Access在讀取時常常出現錯誤，請查詢Window中的 **ODBC資料來源管理員(64位元)** 中的 **驅動程式**是否有出現 **Microsoft Access Driver**
### 三、程式架構
```
autoInsertAccess
│
└───model
│   │   
│   └── Price.py
│   
└───controller
│   │
│   └──Access
│   │   │ 
│   │   └── insertAccess.py  
│   │
│   └──WebCrawler
│       │ 
│       └── crawler.py
│ 
└───README.md
│
└───requirements.txt 
│
└───.gitignore
