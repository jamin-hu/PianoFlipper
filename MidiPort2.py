import mido
from mido import Message
from mido import MidiFile


import _thread, time

def input_thread(flipped):
    try:
        inport.close()
        outport.close()
    except:
        pass

    outports = mido.get_output_names()
    outIndex = [i for i, s in enumerate(outports) if 'VirtualMidiOut' in s] #Name of virtual MIDI output cable
    outport = mido.open_output(outports[outIndex[0]])
    print("Outport = " + str(outport.name))

    inports = mido.get_input_names()
    inIndex = [j for j, t in enumerate(inports) if 'VirtualMidiIn' in t] #Name of MIDI input cable

    with mido.open_input(inports[inIndex[0]]) as inport:
        print("Inport = " + str(inport.name))
        for msg in inport:
            if flipped == True:
                try:
                    note= msg.note
                    flippedMsg = msg.copy(note=127-note)
                    print(flippedMsg)
                    outport.send(flippedMsg)
                except:
                    pass
            elif flipped == False:
                print(msg)
                outport.send(msg)

def do_print():

    flipped = False
    _thread.start_new_thread(input_thread, (flipped,))
    while True:
        derp = input()
        if flipped == False:
            flipped = True
        elif flipped == True:
            flipped = False
        _thread.exit()
        _thread.start_new_thread(input_thread, (flipped,))

    # while True:
    #     print('hi mom')
    #     time.sleep(.1)
    #     if L:
    #         print(L[0])
    #         del(L[0])
    #         break
do_print()
