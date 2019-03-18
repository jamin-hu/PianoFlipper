import mido
from mido import Message
from mido import MidiFile

outports = mido.get_output_names()
outIndex = [i for i, s in enumerate(outports) if 'VirtualMidiOut' in s]
outport = mido.open_output(outports[outIndex[0]])
print("Outport = " + str(outport.name))

inports = mido.get_input_names()
inIndex = [j for j, t in enumerate(inports) if 'VirtualMidiIn' in t]

with mido.open_input(inports[inIndex[0]]) as inport:
    print("Inport = " + str(inport.name))
    for msg in inport:
        outport.send(msg)
