# Movie Ticket Bookie for Zomentum

The assessment project for Zomentum.

## Getting Started

Given below is a step by step procedure explaining how to run this API in your localhost machine. Screenshots of all the API endpoints using Postman is inside the 'images' folder.

### Prerequisites

Before running my Flask API, make sure you have all the dependencies installed (preferably in a virtualenv).

```
pip install requirements.txt
```

### Running the App
In the root level folder run the following command.

On Windows:
```
python run.py
```
On Mac/Linux:
```
python3 run.py
```

### Scheduler (Optional Task)
A Python scheduler is automatically started whrn the Flask server is run. This scheduler scans the Database every 30 secs and deletes all tickets whose movie 'timing_start' was older than 8hrs.

### Unit Tests (Optional Task)
I have also writen some basic Unit Tests in Python using the 'unittest' library. They can be run using the command :

```
python unit_tests.py
```
## Built With

* Flask - A Python Backend Framework
* SQLAlchemy - An open-source SQL toolkit and object-relational mapper for the Python
* Scheduler - A Job Scheduler for Python

## Note

* This database makes use of Integers to represent Times. For eg: 830 -> 8:30am, 1525 -> 15:25pm. This was primarily done due to the time constraint of the tast due to which I refrained from dealing with any data processing I might had to do.
