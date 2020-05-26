import os, sys, subprocess
sys.path.insert(0,os.getcwd()) # Resolve Importing errors

class linux_Notifier():
    def __init__(self, title_notification, message_notification, icon_path):
        self.title_notification = title_notification
        self.message_notification = message_notification
        self.icon_path = icon_path

    def show_notification(self):
        subprocess.Popen(['notify-send', self.title_notification, '-i', self.icon_path, self.message_notification])
