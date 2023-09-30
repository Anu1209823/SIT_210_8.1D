# Import necessary libraries
import smbus, time, random
# Constants
TIME_BETWEEN_READINGS = 3
# Generate random threshold values for brightness levels
thresholds = [random.randint(20, 500) for _ in range(5)]
labels = ["Too Dark", "Dark", "Medium", "Bright", "Too Bright"]
# I2C sensor address and high-resolution mode
SENSOR_ADDR, HIGH_RES_MODE = 0x23, 0x13
# Initialize the SMBus object for communication with I2C devices
bus = smbus.SMBus(1)
# Define a lambda function to read light level from the sensor
get_light = lambda: bus.read_i2c_block_data(SENSOR_ADDR, HIGH_RES_MODE)[1]
# Define a lambda function to determine the brightness label based on the lux value
get_brightness = lambda lux: next(label for t, label in zip(thresholds, labels) if lux > t)
# Main function to continuously read and print light levels
def main():
    while True:
        light = get_light()
        print(f"Light level: {get_brightness(light)}")
        time.sleep(TIME_BETWEEN_READINGS)

if __name__ == "__main__":
    main() # Execute the main function if the script is run directly
