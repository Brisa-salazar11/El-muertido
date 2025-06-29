import tkinter as tk
import random

# Diccionario de palabras con sus respectivas pistas
PALABRAS_CON_PISTAS = {
    "python": "Lenguaje de programación popular.",
    "java": "Lenguaje de programación utilizado en aplicaciones móviles.",
    "PUMA": "Marca famosa de ropa deportiva.",
    "SAMSUNG": "Empresa surcoreana de tecnología antes hacia tanques de guerra.",
    "XIAOMI": "Marca de teléfonos inteligentes y tecnología que tiene un conejo como mascota.",
    "MONO": "Animal primate que se caracteriza por su agilidad.",
    "SHAWARMA": "Comida típica de Oriente Medio que se asemeja a un taco de pollo.",
    "UIDE": "PODEROSISIMA UNIVERSIDAD UBICADA EN QUITO Y TIENE ASOSIACION CON ASU.",
    "MANGO": "Fruta tropical amarilla y ligeramente roja, los ecuatorianos se lo comen cuando esta verde y le agregan sal.",
    "software": "Conjunto de programas informáticos con un fin ."
}

# Función para seleccionar una palabra y su pista al azar
def elegir_palabra():
    # Seleccionar aleatoriamente una palabra de las claves del diccionario
    palabra = random.choice(list(PALABRAS_CON_PISTAS.keys()))
    # Obtener la pista asociada a la palabra seleccionada
    pista = PALABRAS_CON_PISTAS[palabra]
    return palabra.upper(), pista

# Clase principal del juego
class AhorcadoJuego:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego del Ahorcado")
        self.root.geometry("900x450")  # Ajustamos el tamaño para acomodar todo

        self.palabra, self.pista = elegir_palabra()  # Palabra y pista aleatoria
        self.intentos = 6  # Intentos máximos
        self.letras_adivinadas = []  # Letras adivinadas
        self.guiones = ['_'] * len(self.palabra)  # Representación de la palabra con guiones

        # Elementos de la interfaz
        self.label_palabra = tk.Label(self.root, text=" ".join(self.guiones), font=("Helvetica", 18))
        self.label_palabra.pack(pady=20)

        self.intentos_label = tk.Label(self.root, text=f"Intentos restantes: {self.intentos}", font=("Helvetica", 12))
        self.intentos_label.pack()

        self.input_letra = tk.Entry(self.root, font=("Helvetica", 14), width=2)
        self.input_letra.pack(pady=10)

        self.boton_adivinar = tk.Button(self.root, text="Adivinar Letra", command=self.adivinar, font=("Helvetica", 12))
        self.boton_adivinar.pack(pady=5)

        self.mensaje = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.mensaje.pack(pady=10)

        # Mostrar la pista
        self.label_pista = tk.Label(self.root, text=f"Pista: {self.pista}", font=("Helvetica", 12, "italic"))
        self.label_pista.pack(pady=10)

    # Función para adivinar la letra
    def adivinar(self):
        letra = self.input_letra.get().upper()
        if len(letra) != 1 or not letra.isalpha():
            self.mensaje.config(text="Por favor, ingresa una sola letra válida.", fg="red")
            return

        if letra in self.letras_adivinadas:
            self.mensaje.config(text="Ya has adivinado esa letra.", fg="red")
            return

        self.letras_adivinadas.append(letra)

        if letra in self.palabra:
            # Si la letra está en la palabra, actualizamos los guiones
            for i in range(len(self.palabra)):
                if self.palabra[i] == letra:
                    self.guiones[i] = letra
            self.mensaje.config(text="¡Bien hecho!", fg="green")
        else:
            # Si la letra no está en la palabra, restamos un intento
            self.intentos -= 1
            self.mensaje.config(text=f"Letra incorrecta. Intentos restantes: {self.intentos}", fg="red")

        # Actualizar la visualización
        self.label_palabra.config(text=" ".join(self.guiones))
        self.intentos_label.config(text=f"Intentos restantes: {self.intentos}")

        # Verificar si el jugador ganó o perdió
        if "_" not in self.guiones:
            self.mensaje.config(text="¡Ganaste! Has adivinado la palabra.", fg="blue")
            self.boton_adivinar.config(state="disabled")
        elif self.intentos == 0:
            self.mensaje.config(text=f"Perdiste. La palabra era: {self.palabra}", fg="red")
            self.boton_adivinar.config(state="disabled")

        # Limpiar el campo de entrada
        self.input_letra.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()

# Crear una instancia del juego
juego = AhorcadoJuego(root)

# Ejecutar la aplicación
root.mainloop()