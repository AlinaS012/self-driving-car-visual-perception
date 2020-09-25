import cv2
import numpy as np
import traffic_light as a


# cwd = os.path.dirname(os.path.realpath(__file__))


# os.chdir(cwd+'/models')

def grab_screen():
    video_capture = cv2.VideoCapture(0)
    #video_capture = cv2.VideoCapture(0)

    while (video_capture.isOpened()):
        ret, image = video_capture.read()
        color = a.generate_traffic_classifier(ret, image)
        print(color)
        # pass ret and image to function predict_traffic_light 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    #return cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)


grab_screen()
