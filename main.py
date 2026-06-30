from state_machine import run_state_machine
from fan_always_on import fan_on

# Turn fan on at startup (if using GPIO fan)
try:
  fan_on()
except:
  pass # fan not on GPIO or not needed

# Start state machine
run_state_machine()
