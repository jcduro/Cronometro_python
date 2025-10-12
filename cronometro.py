# ------------------------------------------------------------------------------------------------

#       _  _____ _____  _    _ _____   ____  
#      | |/ ____|  __ \| |  | |  __ \ / __ \ 
#      | | |    | |  | | |  | | |__) | |  | |
#  _   | | |    | |  | | |  | |  _  /| |  | |
# | |__| | |____| |__| | |__| | | \ \| |__| |
#  \____/ \_____|_____/ \____/|_|  \_\\____/ 
                                           
                                           

#------------------------------------------------------------------------------------------------

import tkinter as tk

class Cronometro:

    def __init__(self, master):
        self.master = master
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milissegundos = 0  
        self.corriendo = False
        self.display = tk.StringVar()
        self.display.set("00:00:00.000")

        # Configuración de la ventana
        self.master.title("Cronómetro")
        self.master.configure(bg="#34495e")
        self.master.geometry("700x200")
        self.display_label = tk.Label(self.master, textvariable=self.display, 
                                      font=("Helvetica", 48), bg="#34495e", 
                                      fg="#ecf0f1")  
        self.display_label.pack()
        self.button_frame = tk.Frame(self.master, bg="#34495e")
        self.button_frame.pack()

        self.start_button = tk.Button(self.button_frame, text="Iniciar", 
                                      command=self.iniciar, bg="#2ecc71", 
                                      fg="#ecf0f1", font=("Helvetica", 12))
        self.start_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.stop_button = tk.Button(self.button_frame, text="Detener",
                                      command=self.detener, bg="#e74c3c", 
                                      fg="#ecf0f1", font=("Helvetica", 12))
        self.stop_button.pack(side=tk.LEFT, padx=5, pady=10)

        self.reset_button = tk.Button(self.button_frame, text="Reiniciar",
                                      command=self.reiniciar, bg="#3498db", 
                                      fg="#ecf0f1", font=("Helvetica", 12))
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=10)

    #actualizar display
    def actualizar_display(self, tiempo):   
        self.display.set(tiempo)
    #Iniciar
    def iniciar(self):
        if not self.corriendo:
            self.corriendo = True
            self.actualizar_cronometro()
    #Detener
    def detener(self):
        self.corriendo = False

    #Reiniciar
    def reiniciar(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.milissegundos = 0
        self.actualizar_display("00:00:00.000")

    #Actualizar cronometro
    def actualizar_cronometro(self):
        if self.corriendo:
            self.milissegundos += 10
            if self.milissegundos >= 1000:
                self.milissegundos = 0
                self.segundos += 1
            if self.segundos >= 60:
                self.segundos = 0
                self.minutos += 1
            if self.minutos >= 60:
                self.minutos = 0
                self.horas += 1

            tiempo_formateado = f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}.{self.milissegundos//10:02}"
            self.actualizar_display(tiempo_formateado)
            self.master.after(10, self.actualizar_cronometro)

if __name__ == "__main__": 
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()


