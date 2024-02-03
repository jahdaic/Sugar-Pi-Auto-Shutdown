# Sugar-Pi-Auto-Shutdown
A small script to shutdown a Raspberry Pi 30 seconds after power has been disconnected

## Requirements
python 3.5+

## Usage
Installation
```
pip3 install pisugar
```

Run the script
```
$ python autoshutdown.py
```

Run in the background
```
python autoshutdown.py &
```

## Supported Parameters
| parameter | type   | example                               |
|------------------------------------------------------------|
| --timeout | number | `python autoshutdown.py --timeout=60` |

## License
See [License](https://github.com/jahdaic/Sugar-Pi-Auto-Shutdown/blob/master/LICENSE).
