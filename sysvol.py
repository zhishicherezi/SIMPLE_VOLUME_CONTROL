# pip install keyboard
# pip install pycaw
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import keyboard
# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume 
def volume_up():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb - 1.0, None)
# NOTE: -6.0 dB = half volume !
def volume_down():
    currentVolumeDb = volume.GetMasterVolumeLevel()
    volume.SetMasterVolumeLevel(currentVolumeDb + 1.0, None)
keyboard.add_hotkey("ctrl+f11", volume_up)
keyboard.add_hotkey("ctrl+f12", volume_down)
input()