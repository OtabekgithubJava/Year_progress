import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt, QDate


class YearProgressCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Year Progress Calculator")
        self.setGeometry(100, 100, 400, 200)

        self.date_label = QLabel("Enter the date (MM/DD):")
        self.date_input = QLineEdit()
        self.result_label = QLabel("Percentage of the year passed:")
        self.result_output = QLabel()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_progress)

        layout = QVBoxLayout()
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate_progress(self):
        date_str = self.date_input.text()
        try:
            # Parsing the date entered by the user
            date = QDate.fromString(date_str, "MM/dd")
            # Getting the current date
            current_date = QDate.currentDate()

            # Calculate days passed and days in the year
            days_passed = current_date.dayOfYear() - date.dayOfYear()
            total_days = current_date.daysInYear()

            # Calculate the percentage
            percentage = int((days_passed / total_days) * 100)

            self.result_output.setText(f"{percentage}%")
        except Exception as e:
            self.result_output.setText("Invalid date format. Please use MM/DD.")


def main():
    app = QApplication(sys.argv)
    year_progress_calculator = YearProgressCalculator()
    year_progress_calculator.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
