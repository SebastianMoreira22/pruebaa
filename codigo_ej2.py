import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal


class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso: float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} años de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        # Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guardar_mascota)

    def guardar_mascota(self):
        nombre = self.entrada_nombre.text()
        especie = self.entrada_especie.text()
        edad = self.entrada_edad.value()
        peso = self.entrada_peso.value()

        mascota = Mascota(nombre, especie, edad, peso)
        self.mostrar_ventana_secundaria(mascota)

    def mostrar_ventana_secundaria(self, mascota: Mascota):
        ventana_secundaria = VentanaSecundaria(mascota)
        ventana_secundaria.exec()


class VentanaSecundaria(QtWidgets.QDialog):
    def __init__(self, mascota: Mascota, parent=None):
        super(VentanaSecundaria, self).__init__(parent)
        self.setWindowTitle("Ventana Secundaria")
        self.setModal(True)

        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel(str(mascota))
        layout.addWidget(label)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    sys.exit(app.exec())
