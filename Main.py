#args and system
import sys, os, argparse
#os.pathsep

#Image and text libs
import xerox
import pytesseract
import pyscreenshot

from PIL import ImageOps, ImageFilter, ImageEnhance

#Screenshooter
from pynput.mouse import Listener, Button

#Args Vars
parser = argparse.ArgumentParser(prog=sys.argv[0], description="OCR integraded with screenshooter", formatter_class=argparse.ArgumentDefaultsHelpFormatter, epilog="Treshhold technuiqes:1: THRESH_BINARY 2: THRESH_BINARY_INV 3: THRESH_TRUNC 4: THRESH_TOZERO 5: THRESH_TOZERO_INV")

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
parser.add_argument('-p','--print',action='store_true', help='prints output')

#parse them
args = parser.parse_args()

#functions
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

#mouse functions
def on_click(x, y, button, pressed):
	global sx, sy, img, listener	
	if button != Button.left:
		return

	if pressed:
		sx = x
		sy = y
		return
	
	#Make sure than sx < x and sy < y
	if sx == x:
		print("to small window!")	

		exit()
	if sy == y:
		print("to small window!")
		exit()
	
	tx = sx + x
	ty = sy + y	

	sx = (sx < x)*sx + (sx >= x)*x
	sy = (sy < y)*sy + (sy >= y)*y

	x = tx - sx
	y = ty - sy

	img = pyscreenshot.grab(bbox=(sx, sy, x, y))
	listener.stop()

#GetImage
img = None

sx, sy = (0, 0)

listener = Listener(on_click=on_click)
listener.start()
listener.join()

#Postproces image
if args.greyscale:
	img = GreyScale(img)
if args.medianfilter:
	img = Medianfilter(img)
if args.sharp:
	img = Sharpen(img)
if args.threshold:
	img = Threshold(img)

#Show image
if args.show:
	img.show()

#OCR
ocrOutput = pytesseract.image_to_string(img, config = args.config, lang = args.lang)


#if you want to add some string procesing do it here

#Save to clipboard
if args.print:
	print(ocrOutput)
xerox.copy(ocrOutput, xsel=True)
