#!/usr/bin/env python

import csv
import json
import sqlalchemy
import pymysql
# connect to t pymysqlhe database
engine = sqlalchemy.create_engine('mysql+pymysql://root:password@127.0.0.1:3306/codetest')


connection = engine.connect()


metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
tbpeople = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)
tbplaces = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)

#read the CSV data file places into the table places    
with open('E:\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\places.csv', encoding="utf8") as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    connection.execute(tbplaces.insert().values(city = row[0],county = row[1],country = row[2]))



# read the CSV data file people into the table people
with open('E:\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\people.csv', encoding="utf8") as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    connection.execute(tbpeople.insert().values(given_name = row[0],family_name = row[1],date_of_birth = row[2],place_of_birth = row[3]))
#output the table to a JSON file
with open('E:\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\summary_output.json', 'w') as json_file:
  rows = connection.execute(sqlalchemy.sql.select([tbplaces.c.country,sqlalchemy.func.count(tbpeople.c.given_name)]).join(tbpeople,tbpeople.c.place_of_birth==tbplaces.c.city).group_by(tbplaces.c.country)).fetchall() 
  rows = {row[0]: row[1] for row in rows}
  json.dump(rows, json_file, separators=(',', ':'))

