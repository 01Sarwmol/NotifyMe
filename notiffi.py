import time
from plyer import notification

# This is my first Software which remind me to Strech my Back.

if __name__ == "__main__" :
    while True:
        notification.notify(
            title = "Stretch Your Back",
            message = "You are only as young as your spine is flexible",
            app_icon = "",
            timeout = 10

        )
        time.sleep(60*60)