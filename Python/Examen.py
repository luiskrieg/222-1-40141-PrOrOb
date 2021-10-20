class Celular: 

    marca = "iPhone"
    modelo = "12"
    color = "256"

    def iniciar(self):
        return "Iniciando..."

    def apagar(self):
        return "Apagando..."

    def saludar_usuario(self, nombre_usuario):
        print("Hola " + nombre_usuario)

celular_uno = Celular()
print(celular_uno.iniciar())
print(celular_uno.apagar())
celular_uno.saludar_usuario("Nefer")


