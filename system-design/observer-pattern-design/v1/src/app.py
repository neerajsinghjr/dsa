from observable.gadget_observable import GadgetObservable
from observable.outfit_observable import OutfitObservable
from observer.mobile_observer import MobileObserver
from observer.email_observer import EmailObserver


if __name__ == "__main__":
    ob1 = GadgetObservable()
    ob2 = OutfitObservable()

    u1 = MobileObserver(username="Neeraj78", observable=ob1)
    u2 = EmailObserver(email="abhi@gmail.com", observable=ob2)
    u3 = MobileObserver(username="Shreya91", observable=ob2)
    u4 = EmailObserver(email="sana90@gmail.com", observable=ob1)

    ob1.add([u1, u4])
    ob2.add([u2, u3])

    ob1.set_data(100)
    ob1.set_data(0)
    ob1.set_data(50)

    ob2.set_data(100)
    ob2.set_data(50)
