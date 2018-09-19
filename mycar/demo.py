from donkeycar.vehicle import Vehicle
from cvcam3 import CvCam

V = Vehicle()

cam = CvCam()

V.add(cam, outputs=['camera/image'])

V.start()