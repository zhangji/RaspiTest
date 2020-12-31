from gpiozero import PWMOutputDevice
from time import sleep
from signal import pause



def run():
    led = PWMOutputDevice(4)
    led.value = 0.5
    # while True:
    #     led.value = 0  # off
    #     sleep(1)
    #     led.value = 0.5  # half brightness
    #     sleep(1)
    #     led.value = 1  # full brightness
    #     sleep(1)

if __name__ == "__main__":
    run()
    pause()
