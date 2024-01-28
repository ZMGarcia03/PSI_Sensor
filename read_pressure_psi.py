import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def read_pressure_psi():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create an analog input channel on the ADC
    channel = AnalogIn(ads, ADS.P0)

    # Conversion factor for PSI (adjust based on your sensor's characteristics)
    psi_conversion_factor = 10.0

    # Read the raw ADC value
    raw_value = channel.value

    # Convert the raw value to PSI
    psi_value = raw_value / 65535.0 * psi_conversion_factor

    return psi_value

if __name__ == "__main__":
    try:
        while True:
            pressure_psi = read_pressure_psi()
            print(f"Pressure: {pressure_psi:.2f} PSI")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by user.")
