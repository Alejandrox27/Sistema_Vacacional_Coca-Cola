import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMainWindow
from gui.Pagina_inicio import Ui_Ventana_uno
from gui.TerminosYCondiciones import Ui_Terminos_y_condiciones
from gui.Calculo_vacaciones import Ui_Coca_cola_principal
from PyQt5.QtGui import QIcon
import os


class Inicio(QDialog):
    def __init__(self):
        super().__init__()
        
        self.Terminos_y_condiciones = None
        
        self.Pagina_inicio()
        
        
    def Pagina_inicio(self):
        self.ui = Ui_Ventana_uno()
        self.ui.setupUi(self)
        
        
        ruta_icono = os.path.abspath(os.path.join(os.path.dirname(__file__), 'imagenes', 'icon.png'))
        self.setWindowIcon(QIcon(ruta_icono))
        
        self.ui.btn_ingresar.clicked.connect(self.ingresar)
        self.ui.lbl_copyright.setText('©2017 The Coca-Cola Company')
        
        
    def ingresar(self):
        nombre = self.ui.txt_nombre.text().strip()
        
        if len(nombre) > 0:
            if nombre.isalpha():
                self.Terminos_y_condiciones = Terminos_y_condiciones(nombre)
                self.close()
                self.Terminos_y_condiciones.show()
                
            else:
                mensaje = QMessageBox(self)
                mensaje.setText('Solo puede ingresar letras en su nombre y preferiblemente no su nombre completo')
                mensaje.setIcon(QMessageBox.Information)
                mensaje.setWindowTitle('Información')
                
                mensaje.exec_()     
        else:
            mensaje = QMessageBox(self)
            mensaje.setText('Debe ingresar texto en su nombre')
            mensaje.setIcon(QMessageBox.Information)
            mensaje.setWindowTitle('Información')
                
            mensaje.exec_()
            
class Terminos_y_condiciones(QDialog):
    def __init__(self, nombre):
        super().__init__()
        
        self.Principal = None
        self.Inicio = None
        self.nombre = nombre
        self.TerminosYCondiciones(nombre)
        
    def TerminosYCondiciones(self, nombre):
        self.ui = Ui_Terminos_y_condiciones()
        self.ui.setupUi(self)
        
        ruta_icono = os.path.abspath(os.path.join(os.path.dirname(__file__), 'imagenes', 'icon.png'))
        self.setWindowIcon(QIcon(ruta_icono))
        
        self.ui.chk_Aceptar.setText(f'yo {nombre} acepto')
        
        self.ui.chk_Aceptar.stateChanged.connect(self.cambio_botones)
        self.ui.btn_acepto.clicked.connect(self.continuar)
        self.ui.btn_noAcepto.clicked.connect(self.NoAcepto)
        
    def cambio_botones(self):
        if self.ui.chk_Aceptar.isChecked():
            self.ui.btn_acepto.setEnabled(True)
            self.ui.btn_noAcepto.setEnabled(False)
        else:
            self.ui.btn_acepto.setEnabled(False)
            self.ui.btn_noAcepto.setEnabled(True)
        
    def continuar(self):
        self.Principal = Principal(self.nombre)
        self.close()
        self.Principal.show()
    
    def NoAcepto(self):
        self.Inicio = Inicio()
        self.close()
        self.Inicio.show() 
        
class Principal(QMainWindow):
    def __init__(self, nombre):
        super().__init__()
        
        self.Inicio = None
        self.PaginaPrincipal(nombre)
        
    def PaginaPrincipal(self, nombre):
        self.ui = Ui_Coca_cola_principal()
        
        self.ui.setupUi(self)  
        
        ruta_icono = os.path.abspath(os.path.join(os.path.dirname(__file__), 'imagenes', 'icon.png'))
        self.setWindowIcon(QIcon(ruta_icono))
        
        self.ui.txt_resultado.setPlainText('Aca aparecerán los resultados del calculo de las vacaciones')
        
        self.ui.lbl_Bienvenida.setText(f'Bienvenid@ {nombre}')
        self.ui.actionSalir.triggered.connect(self.salir)
        self.ui.actionCreador.triggered.connect(self.creador)
        self.ui.actionCalcular.triggered.connect(self.Calcular)
        self.ui.actionRojo.triggered.connect(self.rojo)
        self.ui.actionMorado.triggered.connect(self.morado)
        self.ui.actionNegro.triggered.connect(self.negro)
        self.ui.actionNuevo.triggered.connect(self.nuevo)
        
    def salir(self):
        self.Inicio = Inicio()
        self.close()
        self.Inicio.show()
        
    def creador(self):
        mensaje = QMessageBox(self)
        mensaje.setIcon(QMessageBox.Information)
        mensaje.setWindowTitle('Creador')
        mensaje.setText('Creador:\nAlejandro Mejía\nVersión: 1.0')
        mensaje.exec_()
        
    def nuevo(self):
        self.ui.txt_apellido_materno.setText('')
        self.ui.txt_apellido_paterno.setText('')
        self.ui.txt_nombre_completo.setText('')
        self.ui.txt_resultado.setPlainText('Aca aparecerán los resultados del calculo de las vacaciones')
        self.ui.cbx_antiguedad.setCurrentIndex(0)
        self.ui.cbx_departamento.setCurrentIndex(0)
        
    def Calcular(self):
        departamento = self.ui.cbx_departamento.currentText()
        antiguedad = self.ui.cbx_antiguedad.currentIndex()
        antiguedad_resultado = self.ui.cbx_antiguedad.itemText(antiguedad)
        nombre = self.ui.txt_nombre_completo.text().strip()
        apellido_paterno = self.ui.txt_apellido_paterno.text().strip()
        apellido_materno = self.ui.txt_apellido_materno.text().strip()
        
        if departamento == '' or antiguedad == 0 or nombre == '' or apellido_materno == '' or apellido_paterno == '':
            mensaje = QMessageBox(self)
            mensaje.setText('Todos los campos se deben llenar')
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.setWindowTitle('Advertencia')
            mensaje.exec_()
            
        if departamento == 'Atención al cliente':
            if antiguedad == 1:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 6 días de vacaciones')
            elif antiguedad == 2:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 14 días de vacaciones')
            elif antiguedad == 3:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 20 días de vacaciones')
        elif departamento == 'Departamento de logística':
            if antiguedad == 1:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 7 días de vacaciones')
            elif antiguedad == 2:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 15 días de vacaciones')
            elif antiguedad == 3:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 21 días de vacaciones')
        elif departamento == 'Departamento de gerencia':
            if antiguedad == 1:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 10 días de vacaciones')
            elif antiguedad == 2:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 20 días de vacaciones')
            elif antiguedad == 3:
                self.ui.txt_resultado.setPlainText(f'El trabajador {nombre} {apellido_paterno} {apellido_materno}\n'
                                                   f'quien labora en el departamento {departamento} y antigüedad {antiguedad_resultado}\n'
                                                   f'tiene derecho a 30 días de vacaciones')
    
    def rojo(self):
        self.ui.wgd_principal.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ui.txt_resultado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_paterno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_materno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_nombre_completo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_antiguedad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_departamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
    
    
    def morado(self):
        self.ui.wgd_principal.setStyleSheet("background-color: rgb(134, 0, 130);")
        
        self.ui.txt_resultado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_paterno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_materno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_nombre_completo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_antiguedad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_departamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(134, 0, 130);\n"
"font: 87 8pt \"Arial Black\";")
    
    def negro(self):
        self.ui.wgd_principal.setStyleSheet("background-color: rgb(0, 0, 0);")
        
        self.ui.txt_resultado.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_paterno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_apellido_materno.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.txt_nombre_completo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_antiguedad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
        self.ui.cbx_departamento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 8pt \"Arial Black\";")
        
def main():
    app = QApplication(sys.argv)
    ventana = Inicio()
    ventana.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()