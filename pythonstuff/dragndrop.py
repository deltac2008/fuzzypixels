import pygtk
import gtk
w=gtk.Window()
w.set_size_request(200,200)

#w.drag_dest_set(gtk.DEST_DEFAULT_MOTION|gtk.DEST_DEFAULT_HIGHLIGHT|gtk.DEST_DEFAULT_DROP,[("UTF8_STRING",0,0)],gtk.gdk.ACTION_COPY)

def dropped(widg,context,x,y,selection,info,time):
	filename=selection.data[7,-2]
	print filename
	type=mimetypes.guess_type(filename)[0]
	data=MediaSource(file_path=filename,content_type=type)
	client.Upload(data,'new file')
	
l=gtk.Label()
w.add(l)
w.show_all()