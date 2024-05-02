import time
import asyncio
import keyboard
from dotenv import dotenv_values
from twitchio.ext import commands
import tkinter as tk
from threading import Thread


env_vars = dotenv_values(".env")
token = env_vars['TOKEN']

# Definir el límite de mensajes por minuto y el tiempo de espera en segundos
MESSAGE_LIMIT = 2
TIME_LIMIT = 1

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=token, prefix='?', initial_channels=['madelain'])
        self.message_count = 0
        self.last_message_time = time.time()

    async def event_ready(self):
        global status_label
        status_label.config(text=f'Logged in | {self.nick}')
        print(f'Logged in as | {self.nick}')
        self.getNyachel = self.get_channel('madelain')
        print(f'Channel obtenido.')

    async def check_message_limit(self):
        current_time = time.time()
        if current_time - self.last_message_time >= TIME_LIMIT:
            # Se ha superado el tiempo límite, reiniciamos el contador de mensajes y actualizamos el tiempo
            self.message_count = 0
            self.last_message_time = current_time
        if self.message_count >= MESSAGE_LIMIT:
            # Se ha superado el límite de mensajes, devolvemos False para indicar que no se puede enviar más mensajes
            return False
        return True

    async def send_message(self, message):
        if await self.check_message_limit():
            await self.getNyachel.send(message)
            self.message_count += 1

class Inter():
    def __init__(self):
        self.bot = Bot()
        self.root = tk.Tk()
        self.hilo = None

    def twitch(self):
        self.hilo = Thread(target=self.bot.run)
        self.hilo.start()

    def on_close_win(self):
        if self.hilo and self.hilo.is_alive():
            self.hilo.join()
            self.root.destroy()

    def window(self):        
        self.root.title("ArmyBomb")
        self.root.geometry("600x200")
        font_style = ("Helvetica", 30 )

        global status_label
        status_label = tk.Label(self.root, text="Sin conectar",font=font_style)
        status_label.pack(pady=10)

        label = tk.Label(self.root, text="Presiona una tecla...",font=font_style)
        label.pack(pady=10)
        self.root.bind("<Key>", lambda event: asyncio.run( self.key_pressed(event,label) ))
        boton_ejecutar = tk.Button(self.root, text="Conectar", command=self.twitch)
        boton_ejecutar.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close_win)
        self.root.mainloop()

    async def key_pressed(self,event,label):
        if event.keysym == '1':
            label.config(text="Tecla presionada: 1")
            await self.bot.send_message("madelaHeart2 DinoDance DinoDance DinoDance DinoDance")

        elif event.keysym == '2':
            label.config(text="Tecla presionada: 2")
            await self.bot.send_message("DinoDance madelaHeart2 DinoDance DinoDance DinoDance")

        elif event.keysym == '3':
            label.config(text="Tecla presionada: 3")
            await self.bot.send_message("DinoDance DinoDance madelaHeart2 DinoDance DinoDance")


        elif event.keysym == '4':
            label.config(text="Tecla presionada: 4")
            await self.bot.send_message("DinoDance DinoDance DinoDance madelaHeart2 DinoDance")

        elif event.keysym == '5':
            label.config(text="Tecla presionada: 5")
            await self.bot.send_message("DinoDance DinoDance DinoDance DinoDance madelaHeart2")

        else:
            label.config(text=f"Usa los numeros 1,2,3,4,5")

def main():
    ventana = Inter()
    ventana.window()


if __name__ == "__main__":
    main()