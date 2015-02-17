import Tkinter
#from Tkinter import *
import re
import time
import logging
logger = logging.getLogger('autoCompleteEntry_tk')


class multiproc_autoCompleteDialog:
    def __init__(self, lista, jobL):
        logger.debug("Started.")
        self.jobL = jobL
        self.subj_name = ""
        self.top = Tkinter.Tk()
        self.entry_lst = AutocompleteEntry(lista, self.top, width=35)
        B = Tkinter.Button(self.top, text="OK", command=self.finalizeIntroMessage, height=5, width=35)
        self.entry_lst.pack()
        B.pack()
        self.entry_lst.focus_set()
        self.entry_lst.enter_method = self.override_enter
        
        self.top.mainloop()
        try:
                    self.jobL.put( self.subj_name )
                    self.jobL.join()
        except:
                    logger.debug( "Couldn't add to joblist.")
        logger.debug("Finished.")
        pass
    
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
    

class AutocompleteEntry(Tkinter.Entry):
    
    
    def __init__(self, lista, *args, **kwargs):
        
        Tkinter.Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = Tkinter.StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        self.bind("<Return>", self.enter)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            try:
                self.lb.destroy()
            except:
                pass
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Tkinter.Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, Tkinter.END)
                for w in words:
                    self.lb.insert(Tkinter.END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
    
    def set_list(self, lst):
        self.lista = lst
    
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(Tkinter.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(Tkinter.END)
    
    def enter(self, event):
        #do the same as Right.
        if (self.lb_up):
            self.selection(event)
        else:
            #print "not int lbup"
            self.enter_method()
            pass
    
    def enter_method(self):
        #print "."
        pass
    
    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != Tkinter.END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]



class autoCompleteEntry_tk:
    
    def internal_multiprocFunction(self):
        a = multiproc_autoCompleteDialog(self.matrix, self.jobL)
    
    def __init__(self, lista):
                self.matrix = lista
                logger.debug("Started.")
    
    def initAll(self):
                import multiprocessing
                self.jobL = multiprocessing.JoinableQueue()
                self.procApp = multiprocessing.Process(target=self.internal_multiprocFunction ) ;
                self.procApp.start()
                tempvar = ""
                while True:
                    if (self.jobL.qsize() > 0 or self.jobL.empty() == False ):
                        logger.debug( "Message element detected on getSubjName")
                        try:
                                tempvar = self.jobL.get()
                                self.jobL.task_done()
                                break;
                        except:
                                pass
                    time.sleep(0.5)
                self.subj_name = str(tempvar).strip()
                pass

    def getSubjectName(self):
        logger.debug("getting subject name.")
        return self.subj_name
    
    def exit(self):
        self.procApp.terminate()
        del self.procApp
        self.jobL.close()
        del self.jobL
        logger.debug("Exiting module.")
    
    



if __name__ == '__main__':
    #mode 1:
    lista = ['a', 'actions', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets', 'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field', 'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind', 'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part', 'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless', 'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you']
#     root = Tk()
# 
#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)
#     Button(text='nothing').grid(row=1, column=0)
#     Button(text='nothing').grid(row=2, column=0)
#     Button(text='nothing').grid(row=3, column=0)
# 
#     root.mainloop()
    #mode 2:
    app3 =  autoCompleteEntry_tk(lista)
    app3.initAll()
    print ".-"
    print app3.getSubjectName()
    print ".-"
    app3.exit()
