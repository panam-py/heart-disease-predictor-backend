
This is the backend application for a heart disease predictor. This app uses an trained AI which predicts a person's heart disease positivity.

# First Steps
In order for the application to work appropriately on your local system, the following steps have to be followed:

## Clone the project
Clone or download the repository from wherever it is hosted.

## Create and activate a virtual environment
After cloning the project `cd` into the project root and create and activate a virtual environment. Use this [guide](https://it.engineering.oregonstate.edu/setting-virtual-environments-python) as a reference

## Download the program requirements 
```python
pip install "requirements.txt"
```
Doing this installs all the python packages this project will need.

## Run the application

Move to the directory which contains the main file and start up the application using the `uvicorn` server.

```bsh
$ cd src
$ uvicorn main:app --reload
```
Now the server should be running and you can start making requests locally.