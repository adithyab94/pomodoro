from PyQt5 import QtWidgets, QtCore, QtGui
import time

class Pomodoro(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro Timer")
        self.setFixedSize(400, 300)

        # Set up the font
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)

        # Set up the labels
        self.timer_label = QtWidgets.QLabel("25:00")
        self.timer_label.setFont(font)
        self.timer_label.setAlignment(QtCore.Qt.AlignCenter)

        self.message_label = QtWidgets.QLabel("Click to start")
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)

        # Set up the buttons
        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.setStyleSheet("""
            background-color: #ff5e5b;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 10px;
            padding: 10px;
            """)
        self.start_button.clicked.connect(self.start_timer)

        # Set up the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.timer_label)
        layout.addWidget(self.message_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def start_timer(self):
        # Set up counter for Pomodoro cycles
        cycle_count = 0

        # Disable the start button
        self.start_button.setEnabled(False)

        # Infinite loop for Pomodoro cycles
        while True:
            # Work period
            for i in range(25, 0, -1):
                minutes = str(i).zfill(2)
                seconds = "00"
                self.timer_label.setText(f"{minutes}:{seconds}")
                QtCore.QCoreApplication.processEvents()
                time.sleep(60)
            self.timer_label.setText("Time's up!")
            self.message_label.setText("Take a break!")
            QtCore.QCoreApplication.processEvents()

            # Increment Pomodoro cycle counter
            cycle_count += 1

            # Check if it's time for a long break
            if cycle_count % 4 == 0:
                # Long break period
                for i in range(30, 0, -1):
                    minutes = str(i).zfill(2)
                    seconds = "00"
                    self.timer_label.setText(f"Long Break: {minutes}:{seconds}")
                    QtCore.QCoreApplication.processEvents()
                    time.sleep(60)
                self.timer_label.setText("Break's over!")
                self.message_label.setText("Click to start")
                QtCore.QCoreApplication.processEvents()
            else:
                # Short break period
                for i in range(5, 0, -1):
                    minutes = str(i).zfill(2)
                    seconds = "00"
                    self.timer_label.setText(f"Short Break: {minutes}:{seconds}")
                    QtCore.QCoreApplication.processEvents()
                    time.sleep(60)
                self.timer_label.setText("Break's over!")
                self.message_label.setText("Click to start")
                QtCore.QCoreApplication.processEvents()

            # Re-enable the start button
            self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    pomodoro = Pomodoro()
    pomodoro.show()
    app.exec_()
