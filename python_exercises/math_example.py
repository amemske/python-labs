# Suppose you are trying to compute a signal-to-noise
# ratio in decibels. The formula is SNRdb = 10 log10(Psignal/Pnoise).

import math

signal = 9
noise = 10

ratio = signal / noise

decibel = 10 * math.log10(ratio)

print(decibel)

#-0.4575