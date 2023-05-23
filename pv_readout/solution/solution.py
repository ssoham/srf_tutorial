from PyQt5.QtCore import pyqtSlot
from pydm import Display


class Solution(Display):
    
    def ui_filename(self):
        return "solution.ui"
    
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args)
        self.ui.pv_input_line_edit.returnPressed.connect(self.update_channel)
    
    @pyqtSlot()
    def update_channel(self):
        print(f"Setting output label channel to {self.ui.pv_input_line_edit.text()}")
        self.ui.output_pydm_label.channel = self.ui.pv_input_line_edit.text()
