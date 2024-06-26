from pydm import Display
from PyQt5.QtCore import pyqtSlot

class PVReadoutGUI(Display):
    
    def ui_filename(self):
        """
        Your code here
        """
        return "pv_readout.ui"
    
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args, ui_filename="pv_readout.ui")
        """
        Your code here
        """
        self.ui.input_to_display.returnPressed.connect(self.update)

    @pyqtSlot()
    def update(self):
        self.ui.output_label.channel = self.ui.input_to_display.text()
    # .channel = "ACCL:L0B:0110:ADES"
