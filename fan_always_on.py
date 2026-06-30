import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
FAN_PIN = 23
GPIO.setup(FAN_PIN, GPIO.OUT)

def fan_on():
  GPIO.output(FAN_PIN, GPIO.HIGH)
  print(&quot;Fan is ON&quot;)

def fan_off():
  GPIO.output(FAN_PIN, GPIO.LOW)
  print(&quot;Fan is OFF&quot;)
