#!/bin/python3
#args and system
import sys, os, argparse
#os.pathsep

#Image and text libs
import xerox
import pytesseract
import re 

#screenshooter
from ScreenShooter import MakeScreenShoot

from PIL import ImageOps, ImageFilter, ImageEnhance

#Args Vars
parser = argparse.ArgumentParser(prog=sys.argv[0], description="OCR integraded with screenshooter", formatter_class=argparse.ArgumentDefaultsHelpFormatter, epilog="IMPORTANT COPY TO CLIPBOARD WONT WORK WITHOUT XCLIP")

#add args
parser.add_argument('--version', action='version', version='%(prog)s 0.1 pre realase')
parser.add_argument('-l','--lang',default="eng", type=str, help='recogniton language')
parser.add_argument('-c','--config',default="--oem 3 --psm 6",  type=str, help='pytesseract config')
parser.add_argument('-g','--greyscale', action='store_false', help='disable greyscale')
parser.add_argument('-t','--threshold', action='store_true', help='enable threshold')
parser.add_argument('-tv','--thresholdval',default=128, type=int, help='set threshold value')
parser.add_argument('-tmv','--thresholdmaxval',default=255, type=int, help='set maximal treshold value')
parser.add_argument('-tt','--thresholdtech',default=0, type=int, help='set treshold technuiqe')
parser.add_argument('-s','--show', action='store_true', help='show postprocesed image')
parser.add_argument('-sh','--sharp',action='store_true', help='enable image sharpering')
parser.add_argument('-sf','--sharpfactor',default=2, type=int, help='sharpering factor')
parser.add_argument('-mb','--medianfilter',action='store_true', help='enable median filter')
parser.add_argument('-mbi','--medianfilterintensifity',default=21, type=int, help='set median filter intensifity')
parser.add_argument('-sv','--save', default="", type=str, help='set median filter intensifity')
parser.add_argument('-i','--interpreter',default="", type=str, help='sends ocr result to interpteter. args works')
parser.add_argument('-clip','--clipboard', action='store_false', help='disable copy to clipboard')
parser.add_argument('-rfa','--regexfindall', default="", type=str, help='apply regex to output and get all containg matches')
parser.add_argument('-rr','--regexreplace', default="", type=str, help='apply regex to output and replace matches with -rrs value')
parser.add_argument('-rrs','--regexreplacestring', default="", type=str, help='replace with this string default: %(default)s')
parser.add_argument('-col','--colour', default="red", type=str, help='set screen shooter colour default: %(default)s')
parser.add_argument('-o','--opacity', default=0.2, type=float, help='set screen shooter opacity default: %(default)s')
parser.add_argument('-p','--print',action='store_true', help='prints output')

#parse them
args = parser.parse_args()

#Image functions
#Post Proces Image
GreyScale = lambda img : ImageOps.grayscale(img)
def MedianFilter(img):
	global args
	return img.filter(ImageFilter.ModeFilter(size = args.medianfilterintensifity))
def Sharpen(img):
	global args
	return ImageEnhance.Sharpness(img).enhance(args.sharpfactor)
def Threshold(img):
	global args
	return img.point(lambda p : (p > args.thresholdval)*args.thresholdmaxval)

#Postproces Image
def PostProces(img):
	global args
	if args.greyscale:
		img = GreyScale(img)
	if args.medianfilter:
		img = Medianfilter(img)
	if args.sharp:
		img = Sharpen(img)
	if args.threshold:
		img = Threshold(img)
	return img

#Show image
def Show(img):
	global args
	if args.show:
		img.show()

def OCR(img):
	global args
	return pytesseract.image_to_string(img, config = args.config, lang = args.lang)

def Regex(ocrOutput):
	global args
	if args.regexreplace != "":
		ocrOutput = re.sub(args.regexreplace, args.regexreplacestring, ocrOutput)

	if args.regexfindall != "":
		ocrOutput = "\n".join(re.findall(args.regexfindall, ocrOutput))

	return ocrOutput

def Rest(img, ocrOutput):
	#Interprpret
	if args.interpreter != "":
		os.system(args.interpreter + " " + ocrOutput)

	#Save output
	if args.save != "":
		with open(args.save, "w") as f:
			f.write(ocrOutput)

	#print
	if args.print:
		print(ocrOutput)

	#Save to clipboard
	if args.clipboard:
		try:
			xerox.copy(ocrOutput, xsel=True)
		except Exception as e:
			print(e)
			print("propably xclip is not installed!")
#Get screenshot
img = MakeScreenShoot(args.colour, args.opacity)

#image procesing
img = PostProces(img)
Show(img)

#string procesing
ocrOutput = OCR(img)
ocrOutput = Regex(ocrOutput)

#Rest
Rest(img, ocrOutput)
