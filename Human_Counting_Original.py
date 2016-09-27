import cv2
import serial
p = None
ser =0
#var =''
#def ok():
    #global var
    #serialPort ='COM4' #var.get()
    #baudRate = 9600
    #global ser
    #ser = serial.Serial(serialPort, baudRate, timeout=0, writeTimeout=0)
    #print "connected"
    #print serialPort
def display(c):
    global ser
    ser.write(str(c))
def human(e,val):
    global ser
    serialPort =val
    baudRate = 9600
    ser = serial.Serial(serialPort, baudRate, timeout=0, writeTimeout=0)
    face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    side_face = cv2.CascadeClassifier('haarcascade_profileface.xml')
    x = cv2.imread('x0.jpg')
    cap = cv2.VideoCapture(0)
    while(1):
        _, img= cap.read()
        _a,f=cap.read()
        f = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        #f= img
        #f = cv2.bitwise_xor(x, f)
        faces = face.detectMultiScale(f, 1.05, 5)
        c=0
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
            c+=1
            f[y:y+h, x:x+w] = [0,255,0]
        side = side_face.detectMultiScale(f, 1.05, 5)
        for (x,y,w,h) in side:
            img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),2)
            c+=1
        display(c)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,str(c),(20,480), font, 4,(255,255,255),2,cv2.LINE_AA)
        #cv2.namedWindow('image',cv2.WINDOW_NORMAL)
        cv2.imshow('image',img)
        k=cv2.waitKey(5)
        if(k==27):
            display(0)
            break
    cv2.destroyAllWindows()
    cap.release()
    ser.close()
human(e, 'COM4') 
