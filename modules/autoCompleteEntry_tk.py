###################
# MOVER ESTO A UNA CLASE autoCompleteEntry_tk
import autoCompleteEntry_tk__
import Tkinter

class autoCompleteEntry_tk:
    
    def __init__(self, lista):
        self.subj_name = ""
        self.top = Tkinter.Tk()
        self.entry_lst = autoCompleteEntry_tk__.AutocompleteEntry(lista, self.top, width=35)
        B = Tkinter.Button(self.top, text="OK", command=self.finalizeIntroMessage, height=5, width=35)
        self.entry_lst.pack()
        B.pack()
        self.entry_lst.focus_set()
        self.entry_lst.enter_method = self.override_enter
        
        self.top.mainloop()
        # END MOVER ESTO A UNA CLASE autoCompleteEntry_tk
        ################################################
        pass

    def getSubjectName(self):
        return self.subj_name
    
    def finalizeIntroMessage(self):
        # print "dmy finalize"
        try:
            # print "subj_name: %s" % str( entry_lst.get() )
            self.subj_name = str(self.entry_lst.get())
        except:
            self.subj_name = ""
        # print "done: %s" % self.subj_name
        self.top.destroy()
        pass
    
    
    def override_enter(self):
        # print "dmy enter"
        try:
            # print "subj_name: %s" % str( entry_lst.get() )
            self.subj_name = str(self.entry_lst.get())
        except:
            self.subj_name = ""
        # print "done: %s" % self.subj_name
        self.top.destroy()
        pass



