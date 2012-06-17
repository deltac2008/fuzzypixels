#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk
import subprocess, os
class CodeGenerator():

	def enter_update(self, widget, entry):
		self.generate_code(entry.get_text())
		self.image.set_from_file(self.tfilename)
		os.remove(self.tfilename)
		self.image.show()

	def save_image(self, button):
		x=gtk.FileChooserDialog(title="Save code image as...",\
			action=gtk.FILE_CHOOSER_ACTION_SAVE,\
			buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,\
			gtk.STOCK_OK,gtk.RESPONSE_OK))
		response=x.run()
		if response==gtk.RESPONSE_OK:
			p=self.image.get_pixbuf()
			p.save(x.get_filename(), "png")
			x.destroy()

	def generate_code(self,text):
		calltxt=["qrencode","-o"]
		calltxt.append(self.tfilename)
		calltxt.append('"'+text+'"')
		subprocess.check_call(calltxt)

	def __init__(self):
		#generate a temporary file to hold the image
		self.tfilename='/tmp/qrtemp.png'
		self.image=gtk.Image()
		self.generate_code("x")
		self.image.set_from_file(self.tfilename)
		self.image.show()
		#create a new window
		window=gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_size_request(200,160)
		window.set_title("2D Code Generator")
		window.connect("delete_event",lambda w,e: gtk.main_quit())

		vbox=gtk.VBox(False,0)
		window.add(vbox)
		vbox.show()

		entry=gtk.Entry()
		entry.set_max_length(60)
		entry.connect("changed", self.enter_update,entry)
		vbox.pack_start(entry,True,True,0)
		entry.show()
		button=gtk.Button()
		button.add(self.image)
		button.connect("clicked",self.save_image)
		vbox.pack_start(button,True,True,0)
		button.show()
		window.show()

def main():
	gtk.main()
	return 0

if __name__=="__main__":
	CodeGenerator()
	main()

