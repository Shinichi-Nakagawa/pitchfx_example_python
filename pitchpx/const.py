#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


class PitchPxConst(object):


    # 球種はこのリンクを参照 http://pitchfx.texasleaguers.com/
    PITCH_TYPES = {
        'FA': 'Fastball',
        'FF': 'four-seam Fastball',
        'FT': 'two-seam Fastball',
        'FC': 'Cut Fastball',
        'FS': 'Split-finger Fastball',
        'FO': 'Forkball',
        'SI': 'Sinker',
        'SL': 'Slider',
        'CU': 'Curveball',
        'KC': 'Knuckle Curve',
        'EP': 'Ephuus',
        'CH': 'Change-up',
        'SC': 'Screwball',
        'KN': 'Knuckleball',
        'UN': 'Unknown',
    }

    # markers(matplotlib)
    PITCH_TYPES_MARKERS = {
        'FA': '.',
        'FF': 'o',
        'FT': ',',
        'FC': 'p',
        'FS': 'v',
        'FO': 'v',
        'SI': '>',
        'SL': '<',
        'CU': '+',
        'KC': ',',
        'EP': 'D',
        'CH': 'o',
        'SC': 'H',
        'KN': '*',
        'UN': 'x',
    }

    # colors(matplotlib)
    PITCH_TYPES_COLORS = {
        'FA': 'red',
        'FF': 'red',
        'FT': 'red',
        'FC': 'red',
        'FS': 'red',
        'FO': 'blue',
        'SI': 'red',
        'SL': 'blue',
        'CU': 'green',
        'KC': 'yellow',
        'EP': 'green',
        'CH': 'green',
        'SC': 'yellow',
        'KN': 'white',
        'UN': 'black',
    }