import gtk

class ColorOptions: #This is basically just an enum
	standard = 0
	morseLeftNode = 1
	morseRightNode = 2
	morseCurrentNode = 3

class ColorHandler:
    	class __impl:
        	""" Implementation of the singleton interface within ColorHandler """

		buttonList = dict() #key = letter of the button, value = the button itself

		#is there some way to make these static? Python needs a static keyword.
		e = gtk.Entry()
		map = e.get_colormap()
		morseLeftNodeColor = map.alloc_color("#c1c1f0")
		morseRightNodeColor = map.alloc_color("#f0a1a1")
		standardColor = map.alloc_color("#e2dbd1")
		morseCurrentNodeColor = map.alloc_color("#a1f0a1")

		colorMap = {ColorOptions.standard: standardColor, ColorOptions.morseLeftNode: morseLeftNodeColor, ColorOptions.morseRightNode: morseRightNodeColor, ColorOptions.morseCurrentNode: morseCurrentNodeColor}  #Map linking ColorOptions enum to the actual color they represent

		def addButton(self, button, colorOption):
			label = button.get_label()
			self.buttonList[label] = button
			self.setColor(button, colorOption)

		def setColorFromEncodedChar(self, encodedchar, colorOption):
			char = unichr(encodedchar)
			setColorFromChar(char, colorOption)

		def setColorFromChar(self, char, colorOption):
			button = self.buttonList.get(char)
			if button != None:
				self.setColor(self.buttonList.get(char), colorOption)

		def setColor(self, button, colorOption):
			button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
			button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

		def colorAll(self, colorOption):
			for button in self.buttonList.values():
				button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
				button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

    	# storage for the instance reference
    	__instance = None

	 


	def __init__(self):
	        """ Create singleton instance """
	        # Check whether we already have an instance
	        if ColorHandler.__instance is None:
	            # Create and remember instance
	            ColorHandler.__instance = ColorHandler.__impl()

	        # Store instance reference as the only member in the handle
	        self.__dict__['_ColorHandler__instance'] = ColorHandler.__instance
	
	def __getattr__(self, attr):
	        """ Delegate access to implementation """
	        return getattr(self.__instance, attr)

	def __setattr__(self, attr, value):
		""" Delegate access to implementation """
	        return setattr(self.__instance, attr, value)


