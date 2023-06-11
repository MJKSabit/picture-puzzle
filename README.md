## Database Stuff
```sql
CREATE DATABASE db_name
CHARACTER SET charset_name
COLLATE collation_name

ALTER DATABASE db_name
CHARACTER SET charset_name
COLLATE collation_name
```


## Picture Puzzle: BUET CSE FEST 2022  
This repository contains the source code of Picture Puzzle Website for BUET CSE FEST 2022.  
  
## Project Configuration  
Create a `.env` file in the base directory. Add the mentioned variables in the file  

    WEB_CONCURRENCY= <number of web concurrency>
    SERVER = <if the code is in production>
    DEBUG = <set debug to true or false>
    SECRECT_KEY = <secret key for production>
    LEADERBOARD_PAGE = <how many users to load per page in leaderboard page>
    
    CONTEST_STARTED = <set if the contest has started>
    CONTEST_ENDED = <set if the contest has ended>
    SHOMOBAY_SHOMITI = <true or false, run shomiti detector>
    
    MEAN = <mean value>
    DEVIATION = <deviation value>
    SPREAD = <spread value>
    SCALE = <scaling value>
    TRANSITION00 = <transition00 value, -cheat(t+1)|-cheat(t)>
    TRANSITION01 = <transition01 value, -cheat(t+1)|+cheat(t)>
    TRANSITION10 = <transition10 value, +cheat(t+1)|-cheat(t)>
    TRANSITION11 = <transition11 value, +cheat(t+1)|+cheat(t)>
    EMISSION00 = <emission00 value, +time(t)|-cheat(t)>
    EMISSION01 = <emission01 value,  -time(t)|-cheat(t)>
    THRESHOLD = <threshold value>
    START_PROB = <starting probability>
    
    DB_HOST = <database host address>
    DB_PORT = <database connection port>
    DB_USER = <database username>
    DB_PASS = <database password>
    DB_NAME = <database name>
    
    MEME_WRONG = <after every MEME_WRONG unsuccessful submissions failure meme is shown>
    SHOW_MEME = <true or false, show meme>
    SHOW_HACK = <true or false, show hack>
    SHOW_SHOMITI = <true or false, show shomiti detection result>

    
    


  

  
## How To Run
1. Clone this project
2. Create a virtual environment in the cloned folder by `python -m venv .venv` in terminal and activate it
3. Install requirements by `pip install -r requirements.txt`  
4. Make sure you have PostGRE SQL Database (Local / Remote)
5. To create the database, run `python manage.py makemigrations`, `python manage.py makemigrations contest_arena` and `python manage.py migrate`, `python manage.py migrate contest_arena`
6. Run the server by `python manage.py runserver`
