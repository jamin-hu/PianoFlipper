import mido
from mido import Message
from mido import MidiFile

import _thread, time

def input_thread(L, flipped):
    derp = input()
    if flipped == True:
        print("Flipping mode deactivated")
    elif flipped == False:
        print("Flipping mode activated")
    L.append(derp)


def do_print():

    outports = mido.get_output_names()
    outIndex = [i for i, s in enumerate(outports) if 'VirtualMidiOut' in s] #Name of virtual MIDI output cable
    outport = mido.open_output(outports[outIndex[0]])
    print("Outport = " + str(outport.name))

    inports = mido.get_input_names()
    inIndex = [j for j, t in enumerate(inports) if 'VirtualMidiIn' in t] #Name of MIDI input cable

    with mido.open_input(inports[inIndex[0]]) as inport:
        L = []
        flipped = False
        _thread.start_new_thread(input_thread, (L, flipped,))

        print("Inport = " + str(inport.name))
        for msg in inport:

            if L:
                del(L[0])
                if flipped == True:
                    flipped = False
                    _thread.start_new_thread(input_thread, (L,flipped))
                elif flipped == False:
                    flipped = True
                    _thread.start_new_thread(input_thread, (L,flipped))

            if flipped == True:
                try:
                    note= msg.note
                    flippedMsg = msg.copy(note=127-note)
                    print(flippedMsg)
                    outport.send(flippedMsg)
                except:
                    pass

            if flipped == False:
                print(msg)
                outport.send(msg)
do_print()
