# Install VLC Player on PC
# Add Environtment System Variables: VLC_PLUGIN_PATH = C:\Program Files\VideoLAN\VLC\plugins
# pip install python-vlc
# WiFi connected to WiCam module (streaming video)
import cv2
import vlc

#player=vlc.MediaPlayer('rtsp://192.168.100.1/cam1/h264')
player=vlc.MediaPlayer('rtsp://192.168.100.1/cam1/mpeg4')
while 1:
    frame = player.play()
    cv2.imshow('VIDEO',frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()