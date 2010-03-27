import gtk

class ColorOptions: #This is basically just an enum
    standard = 0
    morseLeftNode = 1
    morseRightNode = 2
    morseCurrentNode = 3

class ColorHandler:

    # storage for the instance reference
    __instance = None

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

    def execute(self, node):
        button = self.buttonList.get(node.value)
        if button != None:
            button.clicked()

    def addButton(self, button, label):
        if self.buttonList.get(label) == None:
            self.buttonList[label] = button
        #if label == "num_punc":
            #self.setColor(button, ColorOptions.morseLeftNode)
        #if label == "abc":
            #self.setColor(button, ColorOptions.morseRightNode)

    def setColorFromEncodedChar(self, encodedchar, colorOption):
        char = unichr(encodedchar)
        setColorFromChar(char, colorOption)

    def setColorFromChar(self, char, colorOption):
        button = self.buttonList.get(char)
        if button != None:
            self.setColor(button, colorOption)

    def setColor(self, button, colorOption):
        button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
        button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

    def colorAll(self, colorOption):
        for button in self.buttonList.values():
            button.modify_bg(gtk.STATE_NORMAL, self.colorMap.get(colorOption))
            button.modify_bg(gtk.STATE_ACTIVE, self.colorMap.get(colorOption))

    def colorKeys(self, startingNode):
        self.colorAll(ColorOptions.standard) #Reset all colors to gray

        self.setColorFromChar(startingNode.value, 
        ColorOptions.morseCurrentNode) #color our current node in lowercase

        #self.setColorFromChar(startingNode.value.lower(), 
        #ColorOptions.morseCurrentNode) #color our current node in lowercase
        #self.setColorFromChar(startingNode.value.capitalize(), 
        #ColorOptions.morseCurrentNode) #color our current node in uppercase
        leftNode = startingNode.left
        rightNode = startingNode.right

        if leftNode != None:
            self.setColorFromChar(leftNode.value.lower(), 
            ColorOptions.morseLeftNode) #color our direct descendant in lowercase
            self.recursiveColorNodes(leftNode, ColorOptions.morseLeftNode) 
        if rightNode != None:
            self.setColorFromChar(rightNode.value.lower(), 
            ColorOptions.morseRightNode) #color our direct descendant in lowercase
            self.recursiveColorNodes(rightNode, ColorOptions.morseRightNode)

    def recursiveColorNodes(self, startingNode, color):
        if startingNode.left != None: #If we have an instantiated node to go to
            self.setColorFromChar(startingNode.left.value.lower(), color)
            self.setColorFromChar(startingNode.left.value.capitalize(), color)
            self.recursiveColorNodes(startingNode.left, color)
        if startingNode.right != None: #If we have an instantiated node to go to
            self.setColorFromChar(startingNode.right.value.lower(), color)
            self.setColorFromChar(startingNode.right.value.capitalize(), color)
            self.recursiveColorNodes(startingNode.right, color)
  
    #the following is all stuff related to making ColorHandler be a singleton
    def __init__(self):
        """Create singleton instance"""
        # Check whether we already have an instance
        if ColorHandler.__instance is None:
            # Create and remember instance
            ColorHandler.__instance = ColorHandler.__impl()
            # Store instance reference as the only member in the handle
            self.__dict__['_ColorHandler__instance'] = ColorHandler.__instance
  
    def __getattr__(self, attr):
        """Delegate access to implementation"""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
