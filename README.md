Command line interface for the Energenie Pi-Mote

https://energenie4u.co.uk/catalogue/product/ENER314

## Installation

```
python setup.py install
```

## Usage

```
Usage: energenie [OPTIONS]

Options:
  --socket [1|2|3|4|ALL]  [required]
  --command [on|off]      [required]
  --help                  Show this message and exit.
```

## Example

```
energenie --socket 1 --command on
```

## Wiring

The board uses the following pins (BCM GPIO numbers)

```
  3V3 ->  3V3 | 5V
        GPIO2 | 5V
        GPIO3 | GND     <- GND
        GPIO4 | GPIO14
          GND | GPIO15
D0 ->  GPIO17 | GPIO18
D3 ->  GPIO27 | GND
D1 ->  GPIO22 | GPIO23  <- D2
          3V3 | GPIO24  <- MODSEL
       GPIO10 | GND
        GPIO9 | GPIO25  <- CE
       GPIO11 | GPIO8
          GND | GPIO7
```
