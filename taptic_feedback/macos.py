import time

import os

try:
    import objc
    import Cocoa
    from AppKit import *
    from PyObjCTools import AppHelper
except ImportError as err:
    print(err)
    print("You need to have the PyObjC frameworks installed")
    print("easy_install -U pyobjc")


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


if __name__ == 'main':
    taptic_intensity()
