from Windows.notifier import windows_Notifier
from Linux.notifier import linux_Notifier
from Mac_OS.notifier import mac_Notifier
import sys, argparse
from apscheduler.schedulers.blocking import BlockingScheduler

class Reduce_EyeStrain():
    def __init__(self):
        self.application_arguments = self.get_arguments()
        self.title_notification = "Healthy Reminder"
        self.text_notification = "Please look away for 10-20 seconds to prevent eye strain"
        self.app_icon = r"app_icon.ico"
        self.execute_main()
        
    def execute_main(self):
        self.display_notifications()
        self.scheduler = BlockingScheduler()
        self.scheduler.add_job(self.display_notifications, "interval", minutes=int(self.application_arguments.interval))
        self.scheduler.start()

    def get_arguments(self):
        parser = argparse.ArgumentParser(description='Eye Strain Reduction Application')
        parser.add_argument("-i", "--interval", dest="interval",help="Intervals between notifications (minutes)", required=True)
        parser.add_argument("-d", "--duration", dest="duration",help="Duration of notifications (seconds)", required=True)
        return parser.parse_args()

    def display_notifications(self):
        if sys.platform.startswith('win32'):
            notifier = windows_Notifier()
            notifier.show_notification(self.title_notification, self.text_notification, self.app_icon, int(self.application_arguments.duration))
        elif sys.platform.startswith('linux'):
            notifier = linux_Notifier(self.title_notification, self.text_notification, self.app_icon)
            notifier.show_notification()
        elif sys.platform.startswith('darwin'):
            notifier = mac_Notifier(self.title_notification, self.text_notification)
            notifier.show_notification()
        else:
            sys.exit(0)

Reduce_EyeStrain()