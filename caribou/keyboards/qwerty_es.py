# -*- coding: utf-8 -*-
#
# Caribou - text entry and UI navigation application
#
# Copyright (C) 2009 Adaptive Technology Resource Centre
#  * Contributor: Jorge Silva <jorge.silva@utoronto.ca>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
# for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import keysyms

###############################################################################
# keys with keysyms - use known keysyms from keysyms.py or used hex code
# format: ("label", keysym)
###############################################################################

# backspace
bs = ("⌫", keysyms.backspace)
# enter
en = ("↲", keysyms.enter)
# space
sp = ("␣", keysyms.space)
# up
up = ("↑", keysyms.up)
# down
dn = ("↓", keysyms.down)
# left
le = ("←", keysyms.left)
# right
ri = ("→", keysyms.right)

###############################################################################
# keys to switch layers
# format: ("label", "name of layer to switch to")
###############################################################################

# shift up
su = ("⇧", "uppercase")
# shift down
sd = ("⇩", "lowercase")
# number and punctuation
np = (".?12", "num_punct")
# letters
lt = ("abc", "lowercase")

###############################################################################
# keyboard layers
# rules:
#  * key can be a single utf-8 character or a tuple defined above
#  * at least one layer must contain the reserved label "pf" for preferences
#  * layers must be the same dimensions
###############################################################################

lowercase = ( ( "q",  "w", "e", "r", "t", "y", "u", "i", "o", "p", "@"),
              ( "a",  "s", "d", "f", "g", "h", "j", "k", "l", "ñ", "\""),
              ( su,   "z", "x", "c", "v", "b", "n", "m", sp,  ".", bs),
	      ( "pf", np,  "á", "é", "í", "ó", "ú", "ü", ":", ",",  en) )

uppercase = ( ( "Q",  "W", "E", "R", "T", "Y", "U", "I", "O", "P", "@"),
              ( "A",  "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "\""),
              ( sd,   "Z",  "X", "C", "V", "B", "N", "M", sp, ".", bs),
	      ( "pf", np,  "Á", "É", "Í", "Ó", "Ú", "Ü", ":", ",", en) )

num_punct = ( ( "1",  "2", "3", "4", "5", "6", "7", "8", "9", "0", "@"),
              ( "¡",  "!", "(", ")", "+", "-", "_", "=", "&", "/", "\\"),
              ( "¿",  "?", "[", "]", "$", "%", up,  "*", "<", ">", bs),
              ( "pf", lt,  "{", "}", "|", le,  dn,  ri,  ";", "#", en) )

###############################################################################
# list of keyboard layers - the layer in position 0 will be active when the
#                           keyboard is first created
###############################################################################

layers = ( "lowercase", "uppercase", "num_punct" )
