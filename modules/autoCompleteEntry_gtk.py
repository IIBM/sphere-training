import time
import logging
logger = logging.getLogger('autoCompleteEntry_gtk')

class multiproc_autoCompleteDialog():
    def __init__(self, mtrz, jobList=0):
                self.matrix = mtrz
                self.jobL = jobList
                import gtk
                import copy
                self.subj_name = ""
                
                dlg = gtk.Dialog('Subject List')
                dlg.show_all()
            
                entry2 = gtk.Entry()
                entry2.show()
                entry2.set_activates_default(gtk.TRUE)
                
                
                liststore = gtk.ListStore(str)
                #print "subject list: %r" % mtrz
                try:
                    logger.debug("subject list: %r" % self.matrix)
                except:
                    pass
                for i in range(0, len(self.matrix)):
                    #print mtrz[i]
                #for match in ["test1", "test2", "test3", "spam", "foo", "eggs", "bar"]:
                    liststore.append([self.matrix[i]])
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
                del liststore
                
                logger.debug( "gtk: %s" % self.subj_name)
                
                try:
                    self.jobL.put( self.subj_name )
                    self.jobL.join()
                except:
                    logger.debug( "Couldn't add to joblist.")
                logger.debug( "gtk autoCompleteEntry_gtk finalized.")

class autoCompleteDialog():
            dialog_finished = False;
            
            def getSubjectName(self):
                return self.subj_name
            
            def enter_method(self, widget, data=None):
                print "dmy"
            
            def internal_multiprocFunction(self):
                a = multiproc_autoCompleteDialog(self.matrix, self.jobL)
            
            
            def initAll(self):
                import multiprocessing
                GUIjobList = multiprocessing.JoinableQueue()
                self.jobL = GUIjobList
                self.procApp = multiprocessing.Process(target=self.internal_multiprocFunction ) ;
                self.procApp.start()
                tempvar = ""
                while True:
                    if (GUIjobList.qsize() > 0 or GUIjobList.empty() == False ):
                        logger.debug( "Message element detected on getSubjName")
                        try:
                                tempvar = GUIjobList.get()
                                GUIjobList.task_done()
                                break;
                        except:
                                pass
                    time.sleep(0.5)
                self.subj_name = str(tempvar).strip()
                print "finalizado."
                
            
            def __init__(self, mtrz):
                logger.debug("Started.")
                self.matrix = mtrz
                pass
            
            def exit(self):
                self.procApp.terminate()
                del self.procApp
                self.jobL.close()
                del self.jobL
                del self.matrix

if __name__ == "__main__":
            app = autoCompleteDialog( ["probando.", "prueba"])
            app.initAll()
            print "subj: %s" % app.getSubjectName()
            print "deleting."
            del app
            time.sleep(1)
            print "finish."
