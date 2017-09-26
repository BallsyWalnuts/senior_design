import android
import time


new = [0,0,0]
old=new
droid = android.Android()
endTime = 1
timeSensed=0 
i=0
droid.startSensingTimed(2 ,10)
while timeSensed <= endTime: 
     time.sleep(.01)
     i=1+i
     new=droid.sensorsReadAccelerometer().result 
     delta = [(new[0]-old[0])*360/20//1 ,(new[1]-old[1]) *360/20//1,(new[2]-old[2]) *360/20//1,i] 
     print (delta) 
     old=new
droid.stopSensing()