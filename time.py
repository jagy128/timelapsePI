import time
from picamera import PiCamera
import argparse


camera = PiCamera()

parser = argparse.ArgumentParser()
parser.add_argument("-Tm", "--TMinutos", help="Tiempo total en minutos.")
parser.add_argument("-Th", "--THoras", help="Tiempo total en horas.")
parser.add_argument("-S", "--SMinutos", help="Minutos entre fotos.")
args = parser.parse_args()

if args.THoras and args.TMinutos:
  TH = int(args.THoras)
  TM = int(args.TMinutos)
elif args.THoras:
  TH = int(args.THoras)
  TM = 0
else:
  TH = 0
  TM = int(args.TMinutos)

if args.SMinutos:
  SM = int(args.SMinutos)

print(TM,TH,SM) #Debug

def segundos(minutos, horas):
  if horas:
    minutos += horas*60

  return minutos*60

def timelapse(total,separacion):
  start = round(time.time())
  nume = 0
  print('start=',start) #Debug
  while (round(time.time()-start)) <= total:
    print('tiempo=',(round(time.time()-start))) #Debug
    print('total=',total) #Debug
    camera.capture("img"+(str(nume))+".jpg")
    nume += 1
    print('file=',nume) #Debug
    time.sleep(separacion)
    print('tiempomas=',(round(time.time()-start)))  #Debug
    print('totalmas=',total)   #Debug
    print('es?..',(round(time.time()-start)) <= total) #Debug

total = segundos(TM, TH)
separacion = segundos(SM, 0)
print(total,separacion)
print('debug')

timelapse(total, separacion)

