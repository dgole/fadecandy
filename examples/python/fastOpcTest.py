#!/usr/bin/env python

# Light each LED in sequence, and repeat.

import fastopc, time
import numpy as np

numLEDs = 60
client = fastopc.FastOPC('localhost:7890')

pixels = np.zeros([numLEDs,3])
pixels[10,0] = 100
pixels[10,2] = 100
pixels[12,1] = 200

client.put_pixels(pixels)
