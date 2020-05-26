import os, sys
sys.path.insert(0,os.getcwd()) # Resolve Importing errors

class mac_Notifier():
    def __init__(self, title_notification, message_notification):
        self.title_notification = title_notification
        self.message_notification = message_notification
    
    def show_notification(self):
        os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(self.message_notification, self.title_notification))
