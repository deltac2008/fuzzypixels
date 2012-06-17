import pygtk, gtk

window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_size_request(200,160)
window.show()

vbox = gtk.VBox(False,0)
window.add(vbox)
vbox.show()

entry = gtk.Entry()
vbox.pack_start(entry,True,True,0)
entry.show()

button = gtk.Button()
vbox.pack_start(button,True,True,0)
button.show()

buttonpic = gtk.Image()
buttonpic.set_from_file("/home/david/Downloads/underconstruction_57x44.jpg")
button.add(buttonpic)
buttonpic.show()

x = gtk.FileChooserDialog(title="Save code image as...", action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OK,gtk.RESPONSE_OK))
rc=x.run()
print x.get_filename()
x.destroy()

