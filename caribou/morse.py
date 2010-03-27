# -*- coding: utf-8 -*-
#
# Caribou - text entry and UI navigation application
#
# Copyright (C) 2010 John Kim <kim19@usc.edu>
# Copyright (C) 2010 Justin Lei <lei.justin@gmail.com>
# Copyright (C) 2010 Matthew Michihara <michihar@usc.edu>
# Copyright (C) 2010 James Myoung <jkmyoung@usc.edu>
# Copyright (C) 2010 Benjamin Walker <bwwalker@usc.edu>
# Copyright (C) 2010 Michael Wei <mikejwei@gmail.com>
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

import virtkey
import time
from morsetree import get_morse_tree

class Morse:
    """Traverses and selects from the morse tree according to user input.
    
    Supports the following controls:
        1. dot (lshift) - 
            Goes down the left branch of the current node.
        2. dash (rshift) - 
            Goes down the right branch of the current node.
        3. select (lshift+rshift) - 
            Select the current node (output the character represented by the 
            current node)
        4. backspace (hold lshift, tap rshift) - 
            Each tap deletes one character to the left of the caret.
        5. newline (hold rshift, tap lshift) - 
            Each tap outputs a newline.
        6. capslock (hold rshift+lshift) - 
            Toggle between uppercase and lowercase.
    """
    def  __init__(self):
        self.tree_update_callback = None
        self.mt = get_morse_tree()
        self.dot_down = False
        self.dash_down = False
        self.select_state = False
        self.firstkeydowntime = 0
        self.twokeys_starttime = 0
        self.backspace = False
        self.newline = False
        self.vk = virtkey.virtkey()
        self.morse_enabled = True
        
        # The following is a hack to make this program initially type with
        # lower-case letters instead of upper-case; because we're using
        # l-shift and r-shift as our two buttons, it capitalizes whatever
        # we type. We'll start with caps-lock on to reverse that.
        #self.vk.press_keycode(66)    # 66 is capslock
        #self.vk.release_keycode(66)

    def registerListener(self, callback):
        self.tree_update_callback = callback

    def fireToListener(self):
        self.tree_update_callback(self.mt.get_current_node(), False)

    def enable(self):
        self.morse_enabled = True

    def disable(self):
        self.morse_enabled = False

    def key_up(self, event):
        """Listens for when the dot button (l-shift) and the dash button
        (r-shift) are released.
        
        The morse code tree is traversed on button releases, and backspaces
        are entered by holding dash (r-shift) and tapping dot (l-shift). Also,
        newlines are entered by holding dot (l-shift) and tapping dash 
        (r-shift). Hold both buttons together for >0.5 seconds to toggle caps.
        """
        if self.morse_enabled == True:
            if event.event_string == "Shift_L":
                self.dot_down = False
                if self.backspace == True:
                    self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                    self.vk.release_keysym(0xff08)  
                    self.mt.reset()
                elif self.newline == True:
                    self.newline = False  
                    firstkeydowntime = 0
                elif self.select_state == False:
                    if self.mt.get_current_node().left:
                        self.mt.dot()
                    else:
                        self.mt.reset()
                    self.tree_update_callback(self.mt.get_current_node(), False)
                elif self.select_state == True and self.dash_down == False:
                    self.select_state = False  
                    if (time.time() - self.twokeys_starttime) > 0.5:
                        self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                        self.vk.release_keysym(0xff08)
                        self.vk.press_keycode(66)   # 66 is capslock
                        self.vk.release_keycode(66)          
            elif event.event_string == "Shift_R":
                self.dash_down = False
                if self.newline == True:
                    self.vk.press_keysym(0xff0d)    # 0xff0d is newline
                    self.vk.release_keysym(0xff0d)
                    self.mt.reset()
                elif self.backspace == True:
                    self.backspace = False
                    firstkeydowntime = 0    
                elif self.select_state == False:
                    if self.mt.get_current_node().right:
                        self.mt.dash()
                    else:
                        self.mt.reset()
                    self.tree_update_callback(self.mt.get_current_node(), False)
                elif self.select_state == True and self.dot_down == False:
                    self.select_state = False
                    if (time.time() - self.twokeys_starttime) > 0.5:
                        self.vk.press_keysym(0xff08)     # 0xff08 is backspace
                        self.vk.release_keysym(0xff08)
                        self.vk.press_keycode(66)   # 66 is capslock
                        self.vk.release_keycode(66)

    def key_down(self, event):
        """Listens for when the input buttons--the dot button (l-shift), the 
        dash button (r-shift), and the quit button (r-ctrl)--are pressed.
        
        If both the dot and the dash buttons are pressed, the current 
        character of the morse code tree is selected and the tree is reset.
        """
        if self.morse_enabled == True:
            if event.event_string == "Shift_L":
                self.dot_down = True
                if self.dash_down == False:
                    self.firstkeydowntime = time.time()
                else:
                    self.twokeys_starttime = time.time()
                    twokeytime = time.time() - self.firstkeydowntime
                    if twokeytime < 0.25:
                        self.select_state = True
                        #self.send_unicode(self.mt.current_node.value)
                        self.tree_update_callback(self.mt.get_current_node(), True)
                        if self.mt.get_current_node().value == "num_punct" or self.mt.get_current_node().value == "abc":
                            self.mt.switch_trees()
                        self.mt.reset()
                        self.tree_update_callback(self.mt.get_current_node(), False)
                    else:
                        self.backspace = True
            elif event.event_string == "Shift_R":
                self.dash_down = True
                if self.dot_down == False:
                    self.firstkeydowntime = time.time()
                else:
                    self.twokeys_starttime = time.time()
                    twokeytime = time.time() - self.firstkeydowntime
                    if twokeytime < 0.25:
                        self.select_state = True
                        #self.send_unicode(self.mt.current_node.value)
                        self.tree_update_callback(self.mt.get_current_node(), True)
                        if self.mt.get_current_node().value == "num_punct" or self.mt.get_current_node().value == "abc":
                            self.mt.switch_trees()
                        self.mt.reset()
                        self.tree_update_callback(self.mt.get_current_node(), False)
                    else:
                        self.newline = True

if __name__ == "__main__":
    morse = Morse()
    for x in range(10):
        print x
