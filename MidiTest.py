import mido
from mido import Message

outports = mido.get_output_names()
index = [i for i, s in enumerate(outports) if 'VirtualMidiPort1' in s]

testMsg = Message('note_on', note=60)

outport = mido.open_output(outports[index[0]])
outport.send(testMsg)

# with mido.open_input() as inport:
#     print('Inport = ' + inport.name)
#     for msg in inport:
#         print(msg)
