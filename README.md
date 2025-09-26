# ❌ O Tic-Tac-Toe VS Unbeatable AI 🧠

A classic **Tic-Tac-Toe** (Noughts and Crosses) game developed in Python using the **`tkinter`** library for the graphical user interface (GUI). The defining feature of this game is its intelligent AI opponent, which utilizes the **Minimax algorithm** to ensure optimal play, making it a challenging game to win!

---

## ✨ Key Features

* **Unbeatable AI:** The AI opponent employs the **Minimax algorithm**, a search algorithm used in game theory for optimal decision-making. The AI will never lose if there is a possibility for a win or a draw.
* **Simple GUI:** A clean and intuitive graphical user interface built with the standard Python `tkinter` library.
* **Game Status Alerts:** Clear notifications for win, lose, or draw conditions.
* **Restart Functionality:** Easily start a new game with the "Restart Game" button.

---

## ⚙️ Requirements

To run this game, you only need to have **Python** installed on your system. No external libraries are required as `tkinter` and `messagebox` are part of Python's standard distribution.

---

## 🚀 How to Run

1.  **Clone the Repository:**
    ```bash
    git clone [Your-Repository-Link]
    cd [your-repository-name]
    ```

2.  **Save the Code:**
    Save the provided Python code into a file named `tictactoe_ai.py` (or any name ending with `.py`).

3.  **Execute the Game:**
    Open your terminal or command prompt in the folder containing the file and run the following command:
    ```bash
    python tictactoe_ai.py
    ```
    The game window should open immediately.

---

## 🎮 How to Play

* **You (Player):** You play as **"X"**.
* **The AI:** The AI plays as **"O"**.
* **Making a Move:** Click on any empty square on the board to place your "X".
* **AI's Turn:** After your move, the AI will make its optimal move automatically using the Minimax algorithm.
* **Ending the Game:** The game ends when one player achieves three of their marks in a horizontal, vertical, or diagonal row, or when the board is full without a winner (a draw).
* **New Game:** Click the **"Restart Game"** button to clear the board and begin a new round.

---

## 🧑‍💻 Code Structure (For Developers)

The game logic is encapsulated within the `TicTacToe` class:

| Component / Method | Description |
| :--- | :--- |
| **`class TicTacToe`** | The main class handling the game state and GUI elements. |
| **`create_widgets()`** | Sets up the game buttons and the restart button using `tkinter`. |
| **`on_click(row, col)`** | Handles the human player's move and triggers the AI's response. |
| **`ai_move()`** | Determines the best move for the AI by iterating through all possible moves and using the `minimax` function. |
| **`minimax(board, depth, is_maximizing)`** | **The core of the AI.** This function recursively calculates the optimal score for any given board state. |
| **`check_winner(board)`** | Checks for a winning condition (three in a row). |
| **`is_draw(board)`** | Checks if the board is full, resulting in a draw. |

---

## 🤝 Contribution

Contributions are welcome! If you have suggestions for GUI improvements, code refactoring, or algorithm optimization, please feel free to:

1.  **Fork** the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

---

**Good luck trying to beat the AI!** 🥳
