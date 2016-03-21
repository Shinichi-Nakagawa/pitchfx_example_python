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
        'FA': 'o',
        'FF': '.',
        'FT': ',',
        'FC': '6',
        'FS': '7',
        'FO': '7',
        'SI': '5',
        'SL': '4',
        'CU': '7',
        'KC': ',',
        'EP': 'D',
        'CH': 'o',
        'SC': 'H',
        'KN': '*',
        'UN': 'x',
    }

    # colors(matplotlib)
    PITCH_TYPES_COLORS = {
        'FA': 'r',
        'FF': 'r',
        'FT': 'r',
        'FC': 'r',
        'FS': 'r',
        'FO': 'b',
        'SI': 'b',
        'SL': 'b',
        'CU': 'g',
        'KC': 'g',
        'EP': 'g',
        'CH': 'g',
        'SC': 'g',
        'KN': 'g',
        'UN': 'g',
    }