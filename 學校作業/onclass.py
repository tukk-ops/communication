import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = ["" for _ in range(9)]
buttons = []

def check_winner():

   
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)             
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "":
            return board[combo[0]]

    if "" not in board:
        return "Draw"
    
    return None

def on_click(index):
    global current_player

    if board[index] != "":
        return
    
    board[index] = current_player
    buttons[index].config(text=current_player)

    winner = check_winner()
    if winner:
        if winner == "Draw":
            messagebox.showinfo("遊戲結束", "雙方平手！")
        else:
            messagebox.showinfo("遊戲結束", f"恭喜！玩家 {winner} 獲勝！")

        for btn in buttons:
            btn.config(state=tk.DISABLED)
        return

    current_player = "O" if current_player == "X" else "X"
    status_var.set(f"輪到玩家 {current_player}")

def restart_game():
    global current_player, board

    current_player = "X"
    board = ["" for _ in range(9)]
    status_var.set("輪到玩家 X")

    for btn in buttons:
        btn.config(text="", state=tk.NORMAL)

window = tk.Tk()
window.title("井字遊戲 Tic-Tac-Toe")
window.geometry("380x600")
window.resizable(False, False)

container = tk.Frame(window, padx=8, pady=8)
container.pack(fill="both", expand=True)

title = tk.Label(container, text="井字棋遊戲", font=("Helvetica", 20, "bold"))
title.pack(pady=(16, 8))

status_var = tk.StringVar(value="輪到玩家 X")
status_label = tk.Label(container, textvariable=status_var, font=("Helvetica", 13))
status_label.pack(pady=(0, 12))

board_frame = tk.Frame(container)
board_frame.pack()

for i in range(9):
    
    btn = tk.Button(
        board_frame, 
        text="", 
        width=6, 
        height=3, 
        font=("Helvetica", 20, "bold"), 
        command=lambda idx=i: on_click(idx)
    )
    
    btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)

    buttons.append(btn)

control_frame = tk.Frame(container)
control_frame.pack(pady=16)
restart_button = tk.Button(control_frame, text="重新開始", width=12, command=restart_game)
restart_button.grid(row=0, column=0, padx=6)
exit_button = tk.Button(control_frame, text="結束遊戲", width=12, command=window.destroy)
exit_button.grid(row=0, column=1, padx=6)
window.mainloop()