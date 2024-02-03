# Sugar-Pi-Auto-Shutdown
A small script to shutdown a Raspberry Pi 30 seconds after power has been disconnected

## Requirements
python 3.5+

## Usage
Installation
```
pip3 install pisugar
git clone https://github.com/jahdaic/Sugar-Pi-Auto-Shutdown.git
printf "python autoshutdown.py &" >> ~/.bashrc
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
| Parameter         | Type   | Example                               | Description                                      |
|-------------------|--------|---------------------------------------| ------------------------------------------------ |
| **-t, --timeout** | number | `python autoshutdown.py --timeout=60` | How long to wait before shutting down in seconds |
| **-r, --rate**    | number | `python autoshutdown.py --rate=30`    | How often to check the charging state in seconds |

## License
See [License](https://github.com/jahdaic/Sugar-Pi-Auto-Shutdown/blob/master/LICENSE).
