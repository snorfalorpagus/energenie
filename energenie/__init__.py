"""
A simple command line interface to energenie sockets

Example usage:
    $ python energenie.py --socket 1 --command on
    $ python energenie.py --socket ALL --command off

Based on documentation: https://energenie4u.co.uk/res/pdfs/ENER314%20UM.pdf
"""

import RPi.GPIO as GPIO
import time
import click
import atexit

# encoder pins
K0 = 11
K1 = 15
K2 = 16
K3 = 13

# socket codes (K2, K1, K0)
SOCKET = {
    "ALL": [0, 1, 1],
    "1": [1, 1, 1],
    "2": [1, 1, 0],
    "3": [1, 0, 1],
    "4": [1, 0, 0],
}

# command codes (K3)
COMMAND = {
    "ON": 1,
    "OFF": 0,
}

INIT_DONE = False
def init():
    INIT_DONE = True
    GPIO.setmode(GPIO.BOARD)
    # select the GPIO pins used for the encoder K0-K3 data inputs
    # and initialise to 0000
    for pin in (K0, K1, K2, K3):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, False)
    # select the signal used to enable/disable the modulator
    GPIO.setup(22, GPIO.OUT)
    # disable the modulator by setting CE pin lo
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, False)

def cleanup():
    if INIT_DONE:
        GPIO.cleanup()
atexit.register(cleanup)

def send_command(socket, command):
    if socket == "ALL":
        print("Turning ALL sockets {}".format(command.upper()))
    else:
        print("Turning socket #{} {}".format(socket, command.upper()))
    D2, D1, D0 = SOCKET[str(socket)]
    D3 = COMMAND[command.upper()]
    _send(D0, D1, D2, D3)

def _send(D0, D1, D2, D3):
    # set K0-K3
    GPIO.output(K0, bool(D0))
    GPIO.output(K1, bool(D1))
    GPIO.output(K2, bool(D2))
    GPIO.output(K3, bool(D3))
    # let the encoder settle
    time.sleep(0.1)
    # enable the modulator
    GPIO.output(22, True)
    time.sleep(0.25)
    # disable the modulator
    GPIO.output(22, False)

def easy_send(socket, command, retry, wait):
    for n in range(0, retry):
        send_command(socket, command)
        if wait:
            time.sleep(wait)

@click.command()
@click.option("--socket", type=click.Choice(["1", "2", "3", "4", "ALL"]))
@click.option("--command", type=click.Choice(["on", "off"]))
@click.option("--retry", type=int, default=1, help="number of attempts")
@click.option("--wait", type=int, default=0, help="seconds to wait between retries")
def send(*args, **kwargs):
    easy_send(*args, **kwargs)

def main():
    try:
        init()
        send()
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
