from pydm import Display


class PVReadoutGUI(Display):
    
    def ui_filename(self):
        """
        Your code here
        """
        return "example.ui"
    
    def __init__(self, parent=None, args=None):
        super().__init__(parent=parent, args=args, ui_filename="example.ui")
        """
        Your code here
        """
        self.ui.example_pydm_spinbox.channel = "ACCL:L0B:0110:ADES"
