CREATE TABLE "hf" (
       "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
       "name" VARCHAR NOT NULL  UNIQUE , 
       "category" INTEGER NOT NULL , 
       "image" VARCHAR, 
       "text" TEXT NOT NULL , 
       "creator" INTEGER NOT NULL , 
       "date" DATETIME NOT NULL  DEFAULT CURRENT_DATE, 
       "point" INTEGER NOT NULL , 
       "score_vote" INTEGER NOT NULL , 
       "rank" INTEGER NOT NULL 
);