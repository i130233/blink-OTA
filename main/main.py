 from ota_update.main.ota_updater import OTAUpdater
 from machine import Pin
 from time import sleep

 led = Pin(2, Pin.OUT)
  
 def download_and_install_update_if_available():
     o = OTAUpdater('url-to-your-github-project')
     o.download_and_install_update_if_available('wifi-ssid', 'wifi-password')


 def start():
     # your custom code goes here. Something like this: ...
     # from main.x import YourProject
     # project = YourProject()
     # ...
     #while True:
     led.value(not led.value())
     sleep(0.1)

 def boot():
     download_and_install_update_if_available()
     start()


 boot()






