from flask import Flask
from smbus import SMBus
import time
import json

# I2C simplified: 0x5E
EE895ADDRESS = 0x5E
I2CREGISTER = 0x00


app = Flask(__name__)

@app.route("/")
def hello_world():
    i2cbus = SMBus(1)
    try:
        read_data = i2cbus.read_i2c_block_data(EE895ADDRESS, I2CREGISTER, 8)
        # read_data contains ints, which we need to convert to bytes and merge
        # see datasheet
        co2 = read_data[0].to_bytes(1, 'big') + read_data[1].to_bytes(1, 'big')
        temperature = read_data[2].to_bytes(1, 'big') + read_data[3].to_bytes(1, 'big')
        # reserved value - useful to check that the sensor is reading out correctly
        # this should be 0x8000
        resvd = read_data[4].to_bytes(1, 'big') + read_data[5].to_bytes(1, 'big')
        pressure = read_data[6].to_bytes(1, 'big') + read_data[7].to_bytes(1, 'big')

        response_dict = {
            "co2_ppm": int.from_bytes(co2, "big"),
            "temperature_c": int.from_bytes(temperature, "big") / 100,
            "pressure_mbar": int.from_bytes(pressure, "big") / 10
	}
        return json.dumps(response_dict)
    except Exception:
        return json.dumps({"error": "cannot read sensor"})
