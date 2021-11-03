# Database 
## Crawl and Download Data to Local PostgreSQL
1. Open up the `db_init.py`.
2. First, create a database named "DBP" and under database "DBP" create a schema named "COURSE".
3. Second, run every cell and type in your postgres username and password when the last cell executing. 
  * You can also change:
    ```python=
    username = input()
    password = input()
    ```
    the two `input()` to your username and password strings directly.
    
### Alternative Way to Directly Import the Data
* Use the file `test.sql` to restore the schema directly. 

### To Import SQL from Postgresql
[StackOverFlow](https://stackoverflow.com/questions/37984733/postgresql-database-export-to-sql-file)
1. Add C:\Program Files\PostgreSQL\14\bin to environment variables (Windows)  
2. Export through commandline/terminal.  
```shell=
pg_dump -U postgres -h localhost DBP >> test.sql
```
