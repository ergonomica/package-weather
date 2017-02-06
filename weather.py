#!/usr/bin/python
# -*- coding: utf-8 -*-

# pylint's name standards are insane
# pylint: disable=invalid-name

# this file is imported from a different directory
# pylint: disable=import-error

# positional arguments are a good standard for commands
# pylint: disable=unused-argument

"""
[weather.py]

Defines the "weather" command.
"""

import urllib2

verbs = {}

import re

def weather_for_city(city):
    """Return the weather for a specific city."""
    req = urllib2.Request("http://wttr.in/%s" % (city.strip().lower()))
    res = urllib2.urlopen(req)
    return res.read()
    
def weather(env, args, kwargs):
    """[CITYNAME,...]@Return the weather (wttr.in) for all cities specified."""
    return map(weather_for_city, args)

verbs["weather"] = weather
