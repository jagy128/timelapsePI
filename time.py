import time
from picamera import PiCamera
import argparse


camera = PiCamera()

parser = argparse.ArgumentParser()
parser.add_argument("-Tm", "--TMinutos", help="Tiempo total en minutos.")
parser.add_argument("-Th", "--THoras", help="Tiempo total en horas.")
parser.add_argument("-S", "--SMinutos", help="Minutos entre fotos.")
args = parser.parse_args()

TM = 0
TH = 0
SM = 0

TM = int(args.TMinutos)
TH = args.THoras
SM = int(args.SMinutos)

print(TM,TH,SM)

def segundos(minutos, horas):
  if horas:
    minutos += horas*60

  return minutos*60

def timelapse(total,separacion):
  start = round(time.time())
  print('start=',start)
  while (round(time.time()-start)) <= total:
    print('tiempo=',(round(time.time()-start)))
    print('total=',total)
    #for filename in camera.capture_continuous('img{counter:03d}.jpg')
    camera.capture("img"+str((round(time.time()-start)))+".jpg")
    print("img"+str((round(time.time()-start)))+".jpg")
    time.sleep(separacion)
    print('tiempomas=',(round(time.time()-start)))
    print('totalmas=',total)
    print('es?..',(round(time.time()-start)) <= total)

total = segundos(TM, TH)
separacion = segundos(SM, 0)
print(total,separacion)
print('debug')

timelapse(total, separacion)

