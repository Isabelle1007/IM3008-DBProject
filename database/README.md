### To Import SQL from Postgresql
[StackOverFlow](https://stackoverflow.com/questions/37984733/postgresql-database-export-to-sql-file)
1. Add C:\Program Files\PostgreSQL\14\bin to environment variables (Windows)  
2. Export through commandline/terminal.  
```shell=
pg_dump -U postgres -h localhost DBP >> test.sql
```
