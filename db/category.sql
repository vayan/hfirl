CREATE TABLE "category" (
       "id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , 
       "name" VARCHAR NOT NULL  UNIQUE , 
       "upper_cat" INTEGER
);