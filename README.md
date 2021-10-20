# Serve CO2 Sensor details from a Raspberry Pi with EE895 Breakout Board

## Hardware
- [Raspberry Pi 4b](https://thepihut.com/collections/raspberry-pi-kits-and-bundles/products/raspberry-pi-starter-kit) (here's a starter pack, but you can just get the Pi if you have the rest)
- [Advanced CO2 Sensor Breakout Board for Raspberry Pi (EE895) by Pi3g](https://thepihut.com/products/advanced-co2-sensor-breakout-board-for-raspberry-pi)

Ensure you have Raspbian installed as the OS.

## Configure the Pi
You may need to enable I2C

In a terminal type
```
sudo raspi-config
```

Go to interface options and enable I2C.

Altnatively go via the Menu > Preferences > Raspberry Pi Configuration, go to interfaces and enable I2C.


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
