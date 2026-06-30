import os
import time

def get_temp():
  temp = os.popen(&quot;vcgencmd measure_temp&quot;).readline()
  temp = temp.replace(&quot;temp=&quot;, &quot;&quot;).replace(&quot;&#39;C\n&quot;, &quot;&quot;)
  return float(temp)

def monitor_temp():
  while True:
    temp = get_temp()
    print(f&quot;CPU Temp: {temp}°C&quot;)
    time.sleep(1)
