import matplotlib.pyplot as plt
import numpy as np


class NQueensVisualizer:
    def __init__(self, n):
        self.n = n
        self.fig, self.ax = plt.subplots()

        # шахматный фон
        board = np.fromfunction(
            lambda i, j: (i + j) % 2, (n, n)
        )
        self.ax.imshow(board, cmap="gray")

        self.ax.set_xticks(range(n))
        self.ax.set_yticks(range(n))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(True)

        self.queen_texts = []

    def draw_state(self, state):
        # убрать старых ферзей
        for txt in self.queen_texts:
            txt.remove()
        self.queen_texts.clear()

        # нарисовать новых
        for col, row in enumerate(state):
            txt = self.ax.text(
                col,
                row,
                "♛",
                ha="center",
                va="center",
                fontsize=28,
                color="red"
            )
            self.queen_texts.append(txt)

        plt.pause(0.6)
