# EUREKA TEST


## About

This is a Tech Task solution for eureka:
```
Please develop a Flask application consisting of Admin Panel and a set of RESTful API endpoints for a mobile app.
The application should represent a system for a factory orders management. 
The factory has only one machine that does the entire production. This machine can share statuses with the Flask app. The machine is able to share:
1.	The status: OFF, STANDBY, BUSY.
2.	The last order number.
Please mock the machine as a separate Python app (Flask-based or just pure Python, be creative). The main app should be integrated with this mock. 
Each order should have:
1.	Number
2.	Cost
3.	Description
4.	Duration
In the admin panel the user should be able to see the list of all orders with their statuses (taken directly from the machine).
The RESTful API should provide the same data as the admin panel, just to be used within a mobile app.
```

## Project Setup

```
clone this project
cd to this project folder

docker-compose build
docker-compose up
```

## Orders Admin Endpoints

```
http://127.0.0.1:5000/admin/ -> Index
http://127.0.0.1:5000/admin/order/ -> Orders List
http://127.0.0.1:5000/admin/order/new/?url=/admin/order/ -> Orders Create
```

## Orders API Endpoints

```
http://127.0.0.1:5000/api/machine -> Machine status and last order number
http://127.0.0.1:5000/api/orders -> Orders List
Extra params:
?page=1&per_page=100
```