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
