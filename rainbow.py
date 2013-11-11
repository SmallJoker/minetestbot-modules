#!/usr/bin/env python
"""
rainbow.py - Rainbows
Copyright 2013, sfan5
"""
import random

def colorize(text):
	out = ""
	for c in text:
		if c in list(str(i) for i in range(10)):
			c = u"\u200b" + c # 'ZERO WIDTH SPACE' cuz IRC clients are stupid
		out += "\x03" + str(random.randint(2, 15)) + c
	return out

def rainbow(phenny, input):
	for x in phenny.bot.commands["high"].values():
		if x[0].__name__ == "aa_hook":
			if x[0](phenny, input):
				return # Abort function
	arg = input.group(2)
	if not arg:
		return phenny.say(colorize("Rainbow") + "\x03 What?")
	if arg.startswith("#") and ' ' in arg and input.admin:
		ch = arg.split(" ")[0]
		arg = " ".join(arg.split(" ")[1:])
		phenny.write(['PRIVMSG', ch], colorize(arg))
	else:
		phenny.say(colorize(arg))

rainbow.commands = ['rainbow']
