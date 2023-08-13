from .notification_observer import NotificationObserver


class MobileObserver(NotificationObserver):
    """
    MobileObserver is used to send push notification
    to client mobile using username
    """
    def __init__(self, username, observable):
        self.username = username
        self.observable = observable

    def update(self):
        self.send_push()

    def send_push(self):
        print(f"Send Push Notification - {self.username}")
