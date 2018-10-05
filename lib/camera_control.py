
import cv2
from datetime import datetime, timedelta

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
            if ret==True and start + timedelta(seconds=time) > datetime.now() :
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
        
        