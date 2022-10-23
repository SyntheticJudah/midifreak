from cgitb import text
import mido
import PySimpleGUI as sg
from threading import Thread
import platform

class midiFilter(object):
    def __init__(self):
        self.is_running = False
        self.stop_marker = False
        self.filtering_enabled = True

    def getInputs(self):
        return mido.get_input_names()

    def getOutputs(self):
        return mido.get_output_names()    

    def runFilter(self,in_port,out_port):   
        mido_in_port = mido.open_input(in_port)
        mido_out_port = mido.open_output(out_port)
        
        while True:
            self.is_running = True
            for msg in mido_in_port.iter_pending():
                midibyte = msg.bytes()
                # send filtered
                if self.filtering_enabled:
                    if ((midibyte != [248]) and (midibyte != [251]) and (midibyte != [252]) and (midibyte != [250]) ):
                        mido_out_port.send(msg)
                # TODO send unfiltered        
                else:
                    mido_out_port.send(msg)        
            if self.stop_marker == True:
                self.stop_marker = False
                break    
        
        mido_in_port.close()
        mido_out_port.close()    
        self.is_running = False        

class filterGUI(object):
    def __init__(self):
        
        self.filter = midiFilter()
        self.window = None

        # Colors and resources
        self.def_btn=(8,1)
        self.mf_white = '#dfdcd7'
        self.mf_orange = '#f76823'
        self.mf_grey = '#2b2b28'
        self.mf_logo = 'mf_logo.png'
        self.mf_icon = 'mf_icon.ico'
        sg.theme('DarkGrey2')  
        self.listbox_size = (30,10) # Windows
        if platform.system() == 'Darwin':
            self.listbox_size = (32,13) 

        # Layout
        self.column = [
                    [sg.Listbox(self.filter.getInputs(), size=self.listbox_size, key='INP_LIST_')],
                    [sg.Text('Input MIDI port (MicroFreak)')]]

        self.column1 = [
                        [sg.Image(self.mf_logo,size=(72,45))], # midifreak_logo.png
                        [sg.Button('START',size=self.def_btn, key='start',button_color = self.mf_orange)],
                        [sg.Button('Refresh',size=self.def_btn, key='refresh',button_color = self.mf_white)],
                        # TODO [sg.Button('Settings',size=self.def_btn, key='settings')],
                        [sg.Button('Exit',size=self.def_btn, key='exit',button_color = self.mf_white)]]

        self.column2 = [   
                    [sg.Listbox(self.filter.getOutputs(), size=self.listbox_size, key='OUT_LIST_')],
                    [sg.Text('Output MIDI port (Filtered)')], 
                    ]
       
        self.layout = [
                    [sg.Column(self.column, element_justification='left', key='LCOL'),
                    sg.Column(self.column1, element_justification='top',vertical_alignment='t', key='MCOL'),
                    sg.Column(self.column2, element_justification='right', key='RCOL')] #pad=(0, 10)
                    ]                  

    def updateLists(self):
        self.window.Element('INP_LIST_').update(values=self.filter.getInputs())
        self.window.Element('OUT_LIST_').update(values=self.filter.getOutputs())

    def loopGUI(self):
        self.window = sg.Window('MIDIFreak - MicroFreak MIDI Filter', self.layout, icon=self.mf_icon)
        
        while True:
            event, values = self.window.read()
  
            if event == sg.WIN_CLOSED or event == 'exit': 
                self.filter.stop_marker = True    
                break

            if event == 'INP_LIST_':
                print('list click!')

            if event == 'refresh':
                self.updateLists()
                
            if event == 'start':
                if not self.filter.is_running: 
                    in_port = values['INP_LIST_']
                    out_port = values['OUT_LIST_']
                    if (in_port != []) and (out_port != []):
                        self.window['start'].update(text='STOP',button_color = 'red')
                        self.window['refresh'].update(disabled=True, button_color=self.mf_grey)
                        print(in_port[0], out_port[0])
                        filter_manager = Thread(target=self.filter.runFilter,args=[in_port[0],out_port[0]])
                        filter_manager.start()
                        print('filter started!')
                    else:
                        sg.Popup('At first you need to\n'
                                'specify MIDI ports!')        
                else:
                    self.window['start'].update(text='START',button_color = self.mf_orange)
                    self.window['refresh'].update(disabled=False, button_color = self.mf_white)
                    self.filter.stop_marker = True        

        self.window.close()

if __name__ == "__main__":
    gui = filterGUI()
    gui.loopGUI()       

