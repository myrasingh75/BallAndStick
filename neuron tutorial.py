#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:45:27 2021

@author: singhmy
"""


from neuron import h
import matplotlib.pyplot as plt
try: 
    from neuron.units import ms, mV
except ModuleNotFoundError:
    ms = 1
    mV = 1

soma = h.Section(name='soma')

soma.L = 20
soma.diam = 20

soma.insert('hh')

iclamp = h.IClamp(soma(0.5))
print([item for item in dir(iclamp) if not item.startswith('__')])

iclamp.delay = 2
iclamp.dur = 0.1
iclamp.amp = 0.9

soma.psection()

v = h.Vector().record(soma(0.5)._ref_v) # membrane potential vector
t = h.Vector().record(h._ref_t) # time stamp vector

h.load_file('stdrun.hoc')

h.finitialize(-65 * mV)

h.continuerun(40 * ms)

f1 = plt.figure()
plt.plot(t, v)
plt.xlabel('t (ms)')
plt.ylabel('v (mV)')
plt.show()