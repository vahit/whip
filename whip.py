#!/usr/bin/python

##################################
# Whip Sound App For NOKIA N900. #
# Just For Fun.                  #
# Vahid.Maani@gmail.com          #
##################################

# pyglet and mutagen modules sould be installed.
import pyglet
import sys
import mutagen

pyglet.options['audio'] = ('alsa','silent')
sound = pyglet.media.load("whip.mp3", streaming=False)
source = mutagen.File("whip.mp3")
sound.play()
pyglet.clock.schedule_once(pyglet.app.exit(), source.info.length)
pyglet.app.run()
