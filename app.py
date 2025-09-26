import tkinter as tk
from tkinter import messagebox

PLAYER = "X"
AI = "O"

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - VS AI")
        self.root.resizable(False, False)
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_over = False
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font=("Arial", 32), width=5, height=2,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        self.restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 14),
                                        command=self.restart_game)
        self.restart_button.pack(pady=10)

    def on_click(self, row, col):
        if self.board[row][col] == "" and not self.game_over:
            self.make_move(row, col, PLAYER)
            if not self.check_game_over(PLAYER):
                self.root.after(300, self.ai_move)

    def ai_move(self):
        best_score = float("-inf")
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = AI
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            self.make_move(best_move[0], best_move[1], AI)
            self.check_game_over(AI)

    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner == AI:
            return 1
        elif winner == PLAYER:
            return -1
        elif self.is_draw(board):
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = AI
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = PLAYER
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    def make_move(self, row, col, player):
        self.board[row][col] = player
        self.buttons[row][col].config(text=player, state="disabled")

    def check_game_over(self, player):
        if self.check_winner(self.board) == player:
            messagebox.showinfo("Game Over", f"{player} wins!")
            self.game_over = True
            return True
        elif self.is_draw(self.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game_over = True
            return True
        return False

    def check_winner(self, board):
        for i in range(3):
            if board[i][0] != "" and all(board[i][j] == board[i][0] for j in range(3)):
                return board[i][0]
            if board[0][i] != "" and all(board[j][i] == board[0][i] for j in range(3)):
                return board[0][i]
        if board[0][0] != "" and all(board[i][i] == board[0][0] for i in range(3)):
            return board[0][0]
        if board[0][2] != "" and all(board[i][2 - i] == board[0][2] for i in range(3)):
            return board[0][2]
        return None

    def is_draw(self, board):
        return all(board[i][j] != "" for i in range(3) for j in range(3))

    def restart_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
