from email import message
import time 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "ALERT!!!",
            message = "Take a break Tammy, It has been 1 hour! ",
            timeout = 10
        )
        time.sleep(3600)