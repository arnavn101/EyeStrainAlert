from win10toast import ToastNotifier
import os, sys
sys.path.insert(0,os.getcwd()) # Resolve Importing errors

class windows_Notifier():
    def __init__(self):
        self.notifier = ToastNotifier()
    
    def show_notification(self, title_notification, message_notification, icon_path, duration_notification):
        self.notifier.show_toast(title_notification, message_notification, icon_path=icon_path, duration=duration_notification)

