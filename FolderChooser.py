import pickle
import time
from threading import Thread
from tkinter import messagebox


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Folder(metaclass=Singleton):
    pass

    def __init__(self):
        try:
            f = open("C:/Users/user/Downloads/repertoire.txt", "rb")
            self.repertoire = pickle.load(f)
            f.close()

            def confirm():
                time.sleep(2)
                messagebox.showinfo("Confirmation",
                                    "Profile chrome chargé")

            thread1 = Thread(target=confirm)
            thread1.start()
        except:
            self.repertoire = ""

            def aide():
                time.sleep(10)
                messagebox.showinfo("Capsule d´aide",
                                    "1) Entrez ´chrome://version/´ dans votre navigateur\n 2) Recuperez le chemin de ´C:/Users/user/AppData/Local/Google/Chrome/User Data´ \n3) Fermez le navigateur tout de suite apres")

            thread1 = Thread(target=aide)
            thread1.start()

    # getter method
    def get_repertoire(self):
        return self.repertoire

    # setter method
    def set_repertoire(self, rep):
        self.repertoire = rep
