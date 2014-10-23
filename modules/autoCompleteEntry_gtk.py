#from gi.repository import Gtk

import gtk
from docutils.utils.math.latex2mathml import mtr

class autoCompleteDialog():
            
            def enter_method(self, widget, data=None):
                print "dmy"
            
            def __init__(self, mtrz):
#                 Gtk.Window.__init__(self, title="Subject List")
#                 self.connect("delete-event", Gtk.main_quit)
#                 self.box = Gtk.Box(spacing=6)
#         
#                 liststore = Gtk.ListStore(str)
#                 for match in ["test1", "test2", "test3", "spam", "foo", "eggs", "bar"]:
#                     liststore.append([match])
#         
#                 completion = Gtk.EntryCompletion()
#                 completion.set_model(liststore)
#                 completion.set_text_column(0)
#         
#                 entry = Gtk.Entry()
#                 entry.set_completion(completion)
#                 
#                 self.button = Gtk.Button("OK")
#                 self.button.connect("clicked", self.enter_method, None)
#                 #self.box.set_activates_default(True)
#                 
#                 #self.add(self.button);
#                 self.box.pack_start(entry, True, True, 0)
#                 self.box.pack_start(self.button, True, True, 0)
#                 self.add(self.box)
#                 ##self.add(entry)
                
                
                dlg = gtk.Dialog('Subject List')
                dlg.show()
            
                entry2 = gtk.Entry()
                entry2.show()
                entry2.set_activates_default(gtk.TRUE)
                
                liststore = gtk.ListStore(str)
                print "subject list: %r" % mtrz
                for i in range(0, len(mtrz)):
                    #print mtrz[i]
                #for match in ["test1", "test2", "test3", "spam", "foo", "eggs", "bar"]:
                    liststore.append([mtrz[i]])
         
                completion = gtk.EntryCompletion()
                completion.set_model(liststore)
                completion.set_text_column(0)
                entry2.set_completion(completion)
                
                dlg.vbox.pack_start(entry2)
            
                #dlg.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
                dlg.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
                dlg.set_default_response(gtk.RESPONSE_OK)
                response = dlg.run()
            
                if response == gtk.RESPONSE_OK:
                  label = entry2.get_text()
                  print label
                dlg.destroy()
                
                
                
                #self.show_all()
        

if __name__ == "__main__":
            app = autoCompleteDialog( ["probando.", "prueba"])
