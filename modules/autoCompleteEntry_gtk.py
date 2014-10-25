#from gi.repository import Gtk

import time

class autoCompleteDialog():
            
            def getSubjectName(self):
                return self.subj_name
            
            def enter_method(self, widget, data=None):
                print "dmy"
            
            def __init__(self, mtrz):
                import gtk
                
                import copy
                self.subj_name = ""
                
                dlg = gtk.Dialog('Subject List')
                dlg.show_all()
            
                entry2 = gtk.Entry()
                entry2.show()
                entry2.set_activates_default(gtk.TRUE)
                
                
                liststore = gtk.ListStore(str)
                print "subject list: %r" % mtrz
                for i in range(0, len(mtrz)):
                    #print mtrz[i]
                #for match in ["test1", "test2", "test3", "spam", "foo", "eggs", "bar"]:
                    liststore.append([mtrz[i]])
                    pass
                completion = gtk.EntryCompletion()
                completion.set_model(liststore)
                completion.set_text_column(0)
                entry2.set_completion(completion)
                
                dlg.vbox.pack_start(entry2)
            
                #dlg.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
                btnOK = dlg.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)
                dlg.set_default_response(gtk.RESPONSE_OK)
                entry2.set_can_focus(True)
                dlg.set_can_focus(False)
                btnOK.set_can_focus(False)
                entry2.grab_focus()
                
                response = dlg.run() #this is the dlg main loop.
                del response
                #if response == gtk.RESPONSE_OK:
                self.subj_name = copy.deepcopy( entry2.get_text() )
                entry2.destroy()
                btnOK.destroy()
                #dlg.emit('delete-event')
                dlg.destroy()
                del entry2
                del btnOK
                del dlg
                
                print "gtk: %s" % self.subj_name
                print "gtk autoCompleteEntry_gtk finalized."
                

                #self.show_all()
                pass

if __name__ == "__main__":
            app = autoCompleteDialog( ["probando.", "prueba"])
            print "deleting."
            del app
            time.sleep(3)
            print "finish."
