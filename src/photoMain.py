# 
# Main Module to Photo Organizer
#

from wx import App
from lib.GUIExtender import MainForm

# Run the program
if __name__ == '__main__':
    app = App()
    frame = MainForm().Show()
    app.MainLoop() 