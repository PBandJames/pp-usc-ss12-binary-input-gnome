# Abstract #

[Caribou](http://live.gnome.org/Caribou) is a text entry and UI navigation application being developed as an alternative to the GNOME On-screen Keyboard. The overarching goal for Caribou is to create a usable solution for people whose primary way of accessing a computer is a switch device.  Our goal for this project in this competition is to allow a user to use a binary input, such as a button, to interface with Caribou rather than with a mouse.

# Team #

![http://img684.imageshack.us/img684/3016/dragonsb.jpg](http://img684.imageshack.us/img684/3016/dragonsb.jpg)

  * **John Kim** (kim19 at usc dot edu)
  * **Justin Lei** (justinyl at usc dot edu)
  * **Matthew Michihara** (michihar at usc dot edu)
  * **James Myoung** (jkmyoung at usc dot edu)
  * **Benjamin Walker** (bwwalker at usc dot edu)
  * **Michael Wei** (weim at usc dot edu)

# General Overview #

The **Binary Input for GNOME Caribou (BIFGC)** (or **Double Dragons**) project is intended to combine binary input interface with a morse code functionality.  Unlike a usual On-screen keyboard where a user is expected to mouse over the keys and click them, BIFGC allows a user to type all 26 alphabetic characters, numbers 0-9, punctuation marks and even allows for caps lock, character deletion and newline insertion with the use of only two keys.  It accomplishes this by allowing the user to instead input dots (·) and dashes (—) as one would in morse code, except with two specified dot and dash buttons.  The user is able to select and type their specified key after they are finished "signaling" by simultaneously pressing both buttons.  The user is further helped with the visual aid of a simplified morse-code decision tree as shown [here](http://gok.ca/morse.html), as well as a color-coded keyboard that informs the user of whether a dot or a dash is required to eventually get to a certain character.

![http://img121.imageshack.us/img121/3222/ss12blockdiagram.png](http://img121.imageshack.us/img121/3222/ss12blockdiagram.png)

# How to Use this Program #

Usually when [Caribou](http://live.gnome.org/Caribou) is used, it is evoked from the command line by the following:

python Caribou.py

In order to use the morse code and keyboard coloring functionality, you must enter either the "-b" or "--binary" flags.  For example:

python Caribou.py -b
or
python Caribou.py --binary

Then after selecting the desired program to input to,  morse code is used to navigate the [morse code tree](http://code.google.com/p/pp-usc-ss12-binary-input-gnome/wiki/MorseCodeModificationsForPunctuation) to select the character you wish to output to the screen. A dot is represented by the left 'Shift' key and a dash is represented by the right 'Shift' key. The currently selected character will be displayed at the top of the tree to the right of the keyboard. Additionally, every character accessible by a subsequent dot will be highlighted blue on the keyboard, and every character accessible by a subsequent dash will be highlighted in red on the keyboard (the selected character is highlighted in green). To accept the selected character and output it to the screen, simply press both the dot and the dash keys at once.

To backspace, hold the dash key and tap the dot key. Each tap will delete one character to the left of the caret.

To enter a newline, hold the dot key and tap the dash key. Each tap will output one newline.

To switch to uppercase, hold both the dot key and the dash key for >0.5 seconds. Repeat to switch back.

# Technical Overview #

[Caribou](http://live.gnome.org/Caribou) uses the [GTK+](http://www.gtk.org/) toolkit which allows a user to create "graphical user interfaces which boasts cross platform compatibility and an easy to use API."  [Caribou](http://live.gnome.org/Caribou) is written in the [Python Programming Language](http://www.python.org/) while [GTK+](http://www.gtk.org/) is written in C.  However, [GTK+](http://www.gtk.org/) has bindings to languages such as [Python](http://www.python.org/) which allows us to use it with [Caribou](http://live.gnome.org/Caribou) for all of our additions that make up BIFGC.

Our project uses preexisting keyboard listeners already used in
[Caribou](http://live.gnome.org/Caribou).  We added mappings to the left Ctrl key and the Super key (the Windows or Apple key) to simulate choosing between a dot or dash in morse code.

![http://img200.imageshack.us/img200/7048/keyboardus.png](http://img200.imageshack.us/img200/7048/keyboardus.png)

Keyboard without mini-tree

![http://imgur.com/LvgCZ.png](http://imgur.com/LvgCZ.png)

Building off of the pre-existing [Caribou](http://live.gnome.org/Caribou) keyboard, we added an automatic color-coding feature that helps illustrate to the user what they must type in order to get to a letter.  This is implemented with [GTK+](http://www.gtk.org/)'s color options for GUI components.  As the user enters dots and dashes, the keyboard's coloring changes in the following manner:

  1. The <b><font color='green'>Green</font></b> key represents the current character you're at in the decision tree.  If the user presses both buttons at this time, this character will be written to the target output.
  1. <b><font color='blue'>Blue</font></b> keys represent the characters that require at least another dot input to get to.
  1. <b><font color='red'>Red</font></b> keys represent the characters that require at least another dash input to get to.
  1. <b><font color='gray'>Gray</font></b> keys represent the characters already passed by in the decision tree and cannot be typed until the user inputs their next character.

# Future Improvements #

  1. Replace On-screen keyboard with a larger, more detailed decision tree.
  1. Add support for displaying numbers, punctuation marks, and various other special characters along with the alphabetic keyboard.
  1. Add support for non-English keyboard layouts.