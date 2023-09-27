import tkinter as tk
from tkinter import messagebox
import random

LARGURA = 10
ALTURA = 10
NUM_MINAS = 10

class CampoMinado:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.inicializar_tabuleiro()
        self.criar_interface()

    def inicializar_tabuleiro(self):
        self.tabuleiro = [[0 for _ in range(LARGURA)] for _ in range(ALTURA)]
        self.minas = set()
        for _ in range(NUM_MINAS):
            while True:
                x = random.randint(0, LARGURA - 1)
                y = random.randint(0, ALTURA - 1)
                if (x, y) not in self.minas:
                    self.minas.add((x, y))
                    self.tabuleiro[y][x] = -1
                    break

        for i in range(ALTURA):
            for j in range(LARGURA):
                if self.tabuleiro[i][j] == -1:
                    continue
                for ni in range(i - 1, i + 2):
                    for nj in range(j - 1, j + 2):
                        if 0 <= ni < ALTURA and 0 <= nj < LARGURA and self.tabuleiro[ni][nj] == -1:
                            self.tabuleiro[i][j] += 1

    def criar_interface(self):
        self.botoes = [[None for _ in range(LARGURA)] for _ in range(ALTURA)]
        for i in range(ALTURA):
            for j in range(LARGURA):
                self.botoes[i][j] = tk.Button(self.root, width=2, height=1, command=lambda i=i, j=j: self.clicar(i, j))
                self.botoes[i][j].grid(row=i, column=j)

    def clicar(self, i, j):
        if (i, j) in self.minas:
            messagebox.showinfo("You Lost", "You Lost! Try Again.")
            self.root.destroy()
        else:
            self.botoes[i][j].config(text=str(self.tabuleiro[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    app = CampoMinado(root)
    root.mainloop()
