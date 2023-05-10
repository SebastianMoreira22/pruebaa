import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QSizePolicy, QAbstractScrollArea, QSpacerItem
from PyQt6 import QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejercicio 1 Sección Práctica Prueba Individual")

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        username_label = QLabel("NOMBRE DE USUARIO", self)
        username_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(username_label)

        box_layout = QHBoxLayout()
        main_layout.addLayout(box_layout)

        image_box = QVBoxLayout()
        box_layout.addLayout(image_box)

        image_label = QLabel(self)
        image_pixmap = QPixmap("amogus.png").scaledToWidth(200)
        image_label.setPixmap(image_pixmap)
        image_label.setScaledContents(True)
        image_box.addWidget(image_label)

        image_footer_label = QLabel("Texto descripción Usuario", self)
        image_footer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        image_box.addWidget(image_footer_label)

        table_box = QHBoxLayout()
        box_layout.addLayout(table_box)

        table_widget = QTableWidget(self)
        table_widget.setColumnCount(2)
        table_widget.setRowCount(6)

        table_widget.horizontalHeader().setVisible(False)
        table_widget.verticalHeader().setVisible(False)

        attributes_values = {
            "Atributo 1": "Valor 1",
            "Atributo 2": "Valor 2",
            "Atributo 3": "Valor 3",
            "Atributo 4": "Valor 4",
            "Atributo 5": "Valor 5",
            "Atributo 6": "Valor 6"
        }

        row = 0
        for attribute, value in attributes_values.items():
            attribute_item = QTableWidgetItem(attribute)
            value_item = QTableWidgetItem(value)

            table_widget.setItem(row, 0, attribute_item)
            table_widget.setItem(row, 1, value_item)

            row += 1

        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        table_widget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)

        table_box.addWidget(table_widget)

        ok_button = QPushButton("OK", self)
        spacer_box = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        main_layout.addItem(spacer_box)
        main_layout.addWidget(ok_button, alignment=QtCore.Qt.AlignmentFlag.AlignRight)


        ok_button.clicked.connect(self.ok_button_clicked)

    def ok_button_clicked(self):
        print("OK")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
