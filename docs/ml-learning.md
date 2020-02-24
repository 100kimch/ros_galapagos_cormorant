# ml-learning tuorial

- author: Kim Jihyeong(kjhricky@gmail.com)
- written in 2020. Feb. 23

## Recognizing QR Code

### Install ZBar

- For Ubuntu

```bash
sudo apt-get install libzbar0
```

- For macOS

```bash
brew install zbar
```

### Install pyzbar

```bash
python3 -m pip install pyzbar
```

## Data Columns

| image resolution |

## Troubleshooting

## Issue

### [dependency] no module named 'ropkg'

- adding `python3-yaml` is successful whereas `python3-rospkg` comes to an error when `rosdep install`

```xml
<exec_depend>python3-yaml</exec_depend>
```
