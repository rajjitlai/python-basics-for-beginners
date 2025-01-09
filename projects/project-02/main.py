from PIL import ImageGrab
import time
import os
import datetime
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


# function for taking screenshot
def takeSS():
    # create automatic folder for storing image
    if not os.path.exists("images"):
        os.mkdir("images")

    timeFormat = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    imageFormat = f"IMG_{timeFormat}.png"
    image = ImageGrab.grab()

    # saving the image
    image.save(os.path.join("images", imageFormat))

    # create an application window
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("RJ Coding ScreenShot App")
    window.setGeometry(100, 100, 300, 200)

    label = QLabel("The screenshot has been saved!", window)
    label.move(100, 80)

    image.show()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    # delay
    time.sleep(3)
    takeSS()

print("App run with 0 errors")
