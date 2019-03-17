import mido
from mido import Message
from mido import MidiFile

filePath = 'MidiRecordings/Chopin/chpn_op10_e12.mid'

outports = mido.get_output_names()
index = [i for i, s in enumerate(outports) if 'VirtualMidiPort1' in s]
outport = mido.open_output(outports[index[0]])

for msg in MidiFile(filePath).play():
    outport.send(msg)


# with mido.open_input() as inport:
#     print('Inport = ' + inport.name)
#     for msg in inport:
#         print(msg)
