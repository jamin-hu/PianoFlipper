import mido
from mido import Message
from mido import MidiFile

filePath = 'MidiRecordings/Chopin/chpn_op10_e12.mid'

outports = mido.get_output_names()
index = [i for i, s in enumerate(outports) if 'VirtualMidiOut' in s]
outport = mido.open_output(outports[index[0]])

for msg in MidiFile(filePath).play():
    try:
        note= msg.note
        flippedMsg = msg.copy(note=127-note)
        print(flippedMsg)
        outport.send(flippedMsg)
    except:
        pass
