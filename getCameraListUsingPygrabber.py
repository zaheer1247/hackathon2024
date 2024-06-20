from pygrabber.dshow_graph import FilterGraph
import time

# Perform pip install pygrabber

print("Initiating search for available cameras")
time.sleep(3)

print("Getting list of input devices")
devices = FilterGraph().get_input_devices()
time.sleep(3)

available_cameras = {}

print("Printing camera details")
for device_index, device_name in enumerate(devices):
    available_cameras[device_index] = device_name
    print(device_index, "-", device_name)

val = input("Select your camera : ")
print("You have selected ", available_cameras[int(val)])
