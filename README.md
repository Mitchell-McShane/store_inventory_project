# STORE INVENTORY PROJECT APP

This project was built using only:

HTML/CSS
Python
Flask
PostgreSQL and the psycopg

## INSTRUCTIONS

Once cloning the repo. To make the app run as intended the database stock_inventory. 
To be created, to do that.

```
# terminal
createdb stock_inventory
psql -d stock_inventory -f db/stock_inventory.sql
```

That will set up an empty database with the name stock_inventory.

## Adding data to the database

Use the command 
```
# terminal
python3 console.py 
```
That will add data that is implemented in the console.

## Running the app

Use this command that will run the flask app.

```
# terminal
flask run
```

Once that is running open the browser of choice and type this into the search bar.

```
localhost:5000
```

You will now be able to view the app.

## Brief

This app can:
Check inventory from a list of stock that is already on the database
Able to add a new list if stock came in
Check the staff that currently work there
Able to tell if stock is low or out of stock
Delete if stock is no more

Relationships

A worker is able to edit one game on the list

A worker is able to delete many games on the list as well as the app page

A worker can view one game on the list using the more info tab.

A worker can view many games on the app 