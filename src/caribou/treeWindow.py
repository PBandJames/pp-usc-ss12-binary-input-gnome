import gconf
import gobject
import gtk
import sys
import colorhandler

class TreeWindow(gtk.Frame):
  __gtype_name__ = "TreeWindow"
  
  e = gtk.Entry()
  map = e.get_colormap()
  morseLeftNodeColor = map.alloc_color("#c1c1f0")
  morseRightNodeColor = map.alloc_color("#f0a1a1")
  standardColor = map.alloc_color("#e2dbd1")
  morseCurrentNodeColor = map.alloc_color("#a1f0a1")
  #colorMap = {ColorOptions.standard: standardColor, ColorOptions.morseLeftNode: morseLeftNodeColor, ColorOptions.morseRightNode: morseRightNodeColor, ColorOptions.morseCurrentNode: morseCurrentNodeColor}
  
  def __init__(self):
    gtk.Frame.__init__(self)
    #self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    
    #green = gdk.Color(0, 65000, 0)
    self.parentNode = gtk.Button("")
    self.parentNode.set_size_request(32, 32)
    self.parentNode.modify_bg(gtk.STATE_ACTIVE, self.morseCurrentNodeColor)
    self.parentNode.modify_bg(gtk.STATE_NORMAL, self.morseCurrentNodeColor)

    self.leftChild = gtk.Button("e")
    self.leftChild.set_size_request(32, 32)
    self.leftChild.modify_bg(gtk.STATE_ACTIVE, self.morseLeftNodeColor)
    self.leftChild.modify_bg(gtk.STATE_NORMAL, self.morseLeftNodeColor)

    self.rightChild = gtk.Button("t")
    self.rightChild.set_size_request(32, 32)
    self.rightChild.modify_bg(gtk.STATE_ACTIVE, self.morseRightNodeColor)
    self.rightChild.modify_bg(gtk.STATE_NORMAL, self.morseRightNodeColor)

    vbox = gtk.VBox(True, 0)
    parentRow = gtk.HBox(True, 0)
    parentRow.pack_start(self.parentNode, expand = False, fill = False, padding = 8)
    childrenRow = gtk.HBox(True, 0)
    childrenRow.pack_start(self.leftChild, expand = True, fill = True, padding = 8)
    childrenRow.pack_start(self.rightChild, expand = True, fill = True, padding = 8)
    
    vbox.pack_start(parentRow, True, False, 8)
    vbox.pack_start(childrenRow, True, False, 8)
    self.add(vbox)
    #self.fixed = gtk.Fixed()
    #self.fixed.put(self.nodeButton, 30, 0)
    #self.fixed.put(self.leftChild, 10, 50)
    #self.fixed.put(self.rightChild, 50, 50)
    #self.morseRoot.show()
    #self.morseLeft.show()
    #self.morseRight.show()
    #self.fixed.show()
    self.show_all()
    
  def refresh(self, currentNode):
        if currentNode != None:
            self.parentNode.set_label(currentNode.value)
            if currentNode.left != None:
                self.leftChild.set_label(currentNode.left.value)
            else:
                self.leftChild.set_label("")

            if currentNode.right != None:
                self.rightChild.set_label(currentNode.right.value)
            else:
                self.rightChild.set_label("")
        else:
            self.parentNode.set_label("")
            self.leftChild.set_label("")
            self.rightChild.set_label("")
            
if __name__ == "__main__":
  treeWindow = TreeWindow()
  window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  window.add(treeWindow)
  window.show_all()
  gtk.main()
