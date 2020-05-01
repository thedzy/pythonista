import ui
import sound
import time
import data

from objc_util import *

def taptic_device(type=0):
    UIDevice = ObjCClass('UIDevice')
    device = UIDevice.new()
    taptic = device._tapticEngine()
    taptic.actuateFeedback_(type)
    UIDevice.release()
    
def taptic_intensity(intesity=1.0, style=0):
    UIImpactFeedbackGenerator = ObjCClass('UIImpactFeedbackGenerator')
    feedback = UIImpactFeedbackGenerator.new().initWithStyle_(style)
    feedback.prepare()
    feedback.impactOccurredWithIntensity_(intesity)
    UIImpactFeedbackGenerator.release()
    
def taptic_generator(type=0):
    UINotificationFeedbackGenerator = ObjCClass('UINotificationFeedbackGenerator')
    feedback = UINotificationFeedbackGenerator.new()
    feedback.prepare()
    feedback.notificationOccurred_(type)
    UINotificationFeedbackGenerator.release()
    
def taptic_selection():
    UISelectionFeedbackGenerator = ObjCClass('UISelectionFeedbackGenerator')
    feedback = UISelectionFeedbackGenerator.new()
    feedback.selectionChanged()
    UISelectionFeedbackGenerator.release()
    
def taptic_tone(tone=''):
    # it semms it needs to reload this for feedback to be called again
    for tone_bit in tone.split(','):
        taptic_intensity(int(tone_bit)/9,2)
        time.sleep(0.1)

def button_method_1(sender):
    taptic_device(sender.selected_index)

def button_method_2(sender):
    data.TAPTIC_STYLE = sender.selected_index
    taptic_intensity(data.TAPTIC_INTESITY, data.TAPTIC_STYLE)

def slider_method_2(sender):
    data.TAPTIC_INTESITY = sender.value
    data.TAPTIC_TEST = sender.value
    taptic_intensity(data.TAPTIC_INTESITY, data.TAPTIC_STYLE)
    time.sleep(.05)

def button_method_3(sender):
    taptic_generator(sender.selected_index)

def button_method_4(sender):
    taptic_selection()

def text_haptic_tone(sender):
    data.TAPTIC_TONE = sender.text

def button_taptic_tone(sender):
    taptic_tone(data.TAPTIC_TONE)

v = ui.load_view()
v.flex = 'WH'
v.present('sheet')

