# -*- coding: UTF8 -*-

# 简单波束形成
import numpy
import pandas
import matplotlib.pyplot
import math


class Hydrology:
    Velocity = 1500
    Temperature = 20
    Salinity = 35  # 千分之35
    Depth = 300


class zheng:
    ArrayNum = 208


FrequencyCenter = 420 * 10 ^ 3
Bandwidth = 48 * 10 ^ 3
FrequencyLow = FrequencyCenter - Bandwidth / 2
SampleRate = 4e6
Period = 1 / FrequencyCenter  # -*- coding: cp-1252 -*-
PulseWide = 1e-3
LFM_slope = Bandwidth / PulseWide
Amplitude = 1
lmd = SoundVelocity / FrequencyCenter
ArrayDistance = lmd / 2
