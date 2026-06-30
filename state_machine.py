import time
from servo_control import release

STATE_IDLE = 0
STATE_ARMED = 1
STATE_RELEASE = 2

state = STATE_IDLE

def run_state_machine():
  global state

while True:
  if state == STATE_IDLE:
    print("Idle...")
    time.sleep(1)

  elif state == STATE_ARMED:
    print("Armed...")
    time.sleep(1)

  elif state == STATE_RELEASE:
    release()
    state = STATE_IDLE

  cmd = input("Command:").lower()
  if cmd == "arm":
    state = STATE_ARMED
  elif cmd == "release":
    state = STATE_RELEASE
