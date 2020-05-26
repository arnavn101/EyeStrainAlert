from win10toast import ToastNotifier
import os, sys
sys.path.insert(0,os.getcwd()) # Resolve Importing errors

class windows_Notifier():
    def __init__(self):
        self.notifier = ToastNotifier()
    
    def show_notification(self, title_notification, message_notification, icon_path, duration_notification):
        self.notifier.show_toast(title_notification, message_notification, icon_path=icon_path, duration=duration_notification)

#windowsNotifications = windows_Notifier()
#windowsNotifications.show_notification("Healthy Reminder", "Please look away for 10-20 seconds to prevent eye strain",r"app_icon.ico", 10)