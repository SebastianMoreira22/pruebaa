import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} años de la especie {self.especie} con {self.peso} Kg."


class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.guardar_mascota)

    def obtener_nombre(self) -> str:
        return self.entrada_nombre.text()

    def obtener_especie(self) -> str:
        return self.entrada_especie.text()

    def obtener_edad(self) -> int:
        return self.entrada_edad.value()

    def obtener_peso(self) -> float:
        return self.entrada_peso.value()

    def guardar_mascota(self):
        nombre = self.obtener_nombre()
        especie = self.obtener_especie()
        edad = self.obtener_edad()
        peso = self.obtener_peso()

        mascota = Mascota(nombre, especie, edad, peso)
        ventana_secundaria = VentanaSecundaria(mascota)
        ventana_secundaria.show()

class VentanaSecundaria(QtWidgets.QDialog):
    def __init__(self, mascota: Mascota, parent=None):
        super(VentanaSecundaria, self).__init__(parent)
        self.setWindowTitle("Ventana Secundaria")
        self.layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel(str(mascota))
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    vista = Ventana()
    vista.show()
    sys.exit(app.exec())
