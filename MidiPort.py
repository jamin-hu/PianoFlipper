import mido
from mido import Message
from mido import MidiFile

import _thread, time
from pynput import keyboard
import time
import sys

active = True

def on_press(key):
    global active
    print(key.char)
    if active == True:
        print("Normal")
        active = False
    elif active == False:
        print("FLIPPED!")
        active = True

listener = keyboard.Listener(on_press=on_press)
listener.start()

outports = mido.get_output_names()
outIndex = [i for i, s in enumerate(outports) if 'VirtualMidiOut' in s] #Name of virtual MIDI output cable
outport = mido.open_output(outports[outIndex[0]])
print("Outport = " + str(outport.name))

inports = mido.get_input_names()
inIndex = [j for j, t in enumerate(inports) if 'VirtualMidiIn' in t] #Name of MIDI input cable

with mido.open_input(inports[inIndex[0]]) as inport:
    print("Inport = " + str(inport.name))
    for msg in inport:
        if active == True:
            try:
                note= msg.note
                flippedMsg = msg.copy(note=127-note)
                print(flippedMsg)
                outport.send(flippedMsg)
            except:
                pass
        else:
            print(msg)
            outport.send(msg)
