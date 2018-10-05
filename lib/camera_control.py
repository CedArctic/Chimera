
import cv2
from datetime import datetime, timedelta
import sys
import asyncio

class CameraControl:
    
    @classmethod
    async def video_capture(
            cls,
            time=5,
            framerate=30.0,
            size=(640,480),
            codec='XVID',
            camera=0,
            filename='video.avi'
            ):
        
        #selects the first camera from all the cameras listed on the computer
        cap = cv2.VideoCapture(camera)
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*codec)
        out = cv2.VideoWriter(filename,fourcc, framerate, size)
        
        start = datetime.now()
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True and start + timedelta(seconds=int(time)) > datetime.now() :
                out.write(frame)
            else:
                break
        # Release everything if job is finished
        cap.release()
        out.release()
    
    @classmethod
    def photo_capture(cls,camera=0,filename='photo.jpg'):
        
        cap = cv2.VideoCapture(camera)
        ret, frame = cap.read()
        if ret==True:

            cv2.imwrite(filename,frame)

        cap.release()

#workaround due to bug on opencv lib - camera is not released if process is not killed
function = sys.argv[1]
if function == 'photo':
    CameraControl.photo_capture()
if function == 'video':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(CameraControl.video_capture(*sys.argv[2:]))
