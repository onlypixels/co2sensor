# Serve CO2 Sensor details from a Raspberry Pi with EE895 Breakout Board



## Virtual environment
Worth creating a virtual environment"
```
python3 -m venv venv
```
To activate:
```
. venv/bin/activate
```
Check the Python version:
```
python --version
```

## Install
```
pip install flask
pip install smbus
```


## Run
The below command will run it so it can be accessed by other machines on the network:

```
export FLASK_APP=application
flask run --host=0.0.0.0
```
