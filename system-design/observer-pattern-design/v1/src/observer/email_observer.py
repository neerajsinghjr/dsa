from .notification_observer import NotificationObserver


class EmailObserver(NotificationObserver):
    """
    EmailObserver will notify the user through
    the emails.
    """
    def __init__(self, email, observable):
        self.email = email
        self.observable = observable

    def update(self):
        self.send_mail()

    def send_mail(self):
        print(f"Mail Send to {self.email}")