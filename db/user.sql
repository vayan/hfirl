CREATE TABLE "user" (
       "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
       "pseudo" VARCHAR NOT NULL  UNIQUE , 
       "mail" VARCHAR NOT NULL  UNIQUE , 
       "password" TEXT NOT NULL , 
       "avatar" VARCHAR NOT NULL , 
       "name" VARCHAR, 
       "first_name" VARCHAR, 
       "rank" INTEGER NOT NULL , 
       "date"  NOT NULL  DEFAULT CURRENT_DATE, 
       "last_online"  NOT NULL , 
       "hf_ok" TEXT
);