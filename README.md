# ScreenShootOCR

ScreenShootOCR is a Pythons script that integrates tesseract optical recogniton software with screenshooter.

## Installation
Clone this repository
```bash
git clone https://github.com/WellIDKRealy/ScreenShootOCR.git
```
Get inside 
```bash
cd ScreenShootOCR
```
Install python3 depedencies
```bash
pip3 install -r requirements.txt 
```
Install tesseract and language for it
```bash
#Example instalation commands
#arch linux based
sudo pacman -S tesseract
sudo pacman -S tesseract-data-eng #english language pack

#debian based
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-eng #english language pack
```
Install qt5
```bash
#Example instalation commands
#arch linux based
sudo pacman -S qt5

#debian based(im not sure about that)
sudo apt-get install qt5
```

# IMPORTANT
Please make sure that xclip is installed! otherwise copy to clipborad wont work.
```bash
#Example instalation commands
#arch linux based
sudo pacman -S xclip

#debian based
sudo apt-get install xclip

#rhel based
yum install xclip
```

## Usage
Take screenshot and copy OCR to clipboard.
```bash
ssocr
```
Take screenshot and copy OCR to clipboard with specified language.
```bash
ssocr -l de #set recogniton language to german
```
Take screenshot and save OCR output
```bash
ssocr -sv PATHTOFILE
```

Show screenshoted img after processing
```bash
ssocr -s
```
Options
```bash
#Output of ssocr --help
usage: Main.py [-h] [--version] [-l LANG] [-c CONFIG] [-g] [-t] [-tv THRESHOLDVAL] [-tmv THRESHOLDMAXVAL]
               [-tt THRESHOLDTECH] [-s] [-sh] [-sf SHARPFACTOR] [-mb] [-mbi MEDIANFILTERINTENSIFITY] [-sv SAVE]
               [-i INTERPRETER] [-clip] [-rfa REGEXFINDALL] [-rr REGEXREPLACE] [-rrs REGEXREPLACESTRING] [-col COLOUR]
               [-o OPACITY] [-p]

OCR integraded with screenshooter

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -l LANG, --lang LANG  recogniton language (default: eng)
  -c CONFIG, --config CONFIG
                        pytesseract config (default: --oem 3 --psm 6)
  -g, --greyscale       disable greyscale (default: True)
  -t, --threshold       enable threshold (default: False)
  -tv THRESHOLDVAL, --thresholdval THRESHOLDVAL
                        set threshold value (default: 128)
  -tmv THRESHOLDMAXVAL, --thresholdmaxval THRESHOLDMAXVAL
                        set maximal treshold value (default: 255)
  -tt THRESHOLDTECH, --thresholdtech THRESHOLDTECH
                        set treshold technuiqe (default: 0)
  -s, --show            show postprocesed image (default: False)
  -sh, --sharp          enable image sharpering (default: False)
  -sf SHARPFACTOR, --sharpfactor SHARPFACTOR
                        sharpering factor (default: 2)
  -mb, --medianfilter   enable median filter (default: False)
  -mbi MEDIANFILTERINTENSIFITY, --medianfilterintensifity MEDIANFILTERINTENSIFITY
                        set median filter intensifity (default: 21)
  -sv SAVE, --save SAVE
                        set median filter intensifity (default: )
  -i INTERPRETER, --interpreter INTERPRETER
                        sends ocr result to interpteter. args works (default: )
  -clip, --clipboard    disable copy to clipboard (default: True)
  -rfa REGEXFINDALL, --regexfindall REGEXFINDALL
                        apply regex to output and get all containg matches (default: )
  -rr REGEXREPLACE, --regexreplace REGEXREPLACE
                        apply regex to output and replace matches with -rrs value (default: )
  -rrs REGEXREPLACESTRING, --regexreplacestring REGEXREPLACESTRING
                        replace with this string default:
  -col COLOUR, --colour COLOUR
                        set screen shooter colour default: red
  -o OPACITY, --opacity OPACITY
                        set screen shooter opacity default: 0.2
  -p, --print           prints output (default: False)

IMPORTANT COPY TO CLIPBOARD WONT WORK WITHOUT XCLIP
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
