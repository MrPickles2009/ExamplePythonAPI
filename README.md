# Example Python API
An example of how to use python, flask and sqlite to make a basic, functioning API

## To Use

To clone and run this repository you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/). From your command line:

```bash
# Clone this repository
git clone https://github.com/MrPickles2009/ExamplePythonAPI.git
# Go into the repository
cd ExamplePythonAPI
# Install dependencies
pip install flask flask-sqlalchemy flask-restful
```

```bash
# Run the app
python server.py
```

## To Use

The API request available in this code are:

### GET Vehicles
    /vehicles
### POST Vehicles
    /vehicles
    {
        "newData": {
            "makeName": "VEHICLE_MAKE",
            "modelName": "VEHICLE_MODEL",
            "modelYear": VEHICLE_YEAR,
            "maxSpeed": VEHICLE_MAX_SPEED
        }
    }

    makeName: string
    modelName: string
    modelYear: int
    maxSpeed: int
### GET Vehicle
    /getvehicle/{id}
### DELETE Vehicle
    /deletevehicle/{id}