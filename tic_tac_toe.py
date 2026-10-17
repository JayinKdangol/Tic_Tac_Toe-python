import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if button[combo[0]]["text"] == button [combo[1]]["text"] == button [combo[2]]["text"] !="":
            winner = True
            button[combo[0]].config(bg = "green")
            button[combo[1]].config(bg = "green")
            button[combo[2]].config(bg = "green")
            messagebox.showinfo("tic tac toe", f"player {button[combo[0]]['text']} wins")
            root.quit()



def check_draw():
    global winner
    if all(button[i]["text"] != "" for i in range(9)):
        winner = True
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        root.quit()


        
def button_click(index):
    if button[index]["text"] == "" and not winner:
        button[index]["text"] = current_player
        check_winner()
        check_draw()
        ai()




def ai():
    if winner:
        return
    
    #Secure computer win           
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
            if button[combo[0]]["text"] == "O" and button[combo[1]]["text"] == "O" and button[combo[2]]["text"] == "":
                button[combo[2]]["text"] = "O"
                check_winner()
                return
    
            elif button[combo[1]]["text"] == "O" and button[combo[2]]["text"] == "O" and button[combo[0]]["text"] == "":
                button[combo[0]]["text"] = "O"
                check_winner()
                return
    
            elif button[combo[2]]["text"] == "O" and button[combo[0]]["text"] == "O" and button[combo[1]]["text"] == "":
                button[combo[1]]["text"] = "O"
                check_winner()
                return

    #Prevent player immediate win
    for combo in [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]:
        if button[combo[0]]["text"] == "X" and button[combo[1]]["text"] == "X" and button[combo[2]]["text"] == "":
            button[combo[2]]["text"] = "O"
            check_winner()
            return

        elif button[combo[1]]["text"] == "X" and button[combo[2]]["text"] == "X" and button[combo[0]]["text"] == "":
            button[combo[0]]["text"] = "O"
            check_winner()
            return

        elif button[combo[2]]["text"] == "X" and button[combo[0]]["text"] == "X" and button[combo[1]]["text"] == "":
            button[combo[1]]["text"] = "O"
            check_winner()
            return

    #Capture center
    if button[4]["text"] == "":
        button[4]["text"] = "O"

    #Prevent zugzwang
    elif button[2]["text"] == "X" and button[4]["text"] == "O" and button[6]["text"] == "X" and button[7]["text"] == "":
        button[7]["text"] = "O"
    
    #Capture corner
    elif button[4]["text"] == "X" and button[0]["text"] == "":
        button[0]["text"] = "O"

    #Random move
    else:
        for i in range(9):
            if button[i]["text"] == "":
                button[i]["text"] = "O"
                break

    check_winner()




root = tk.Tk()
root.title("tic tac toe")


button = [tk.Button(root, text="", font = ("normal", 25), width = 6  , height = 2, command = lambda i=i:button_click(i)) for i in range(9)]
for i, btn in enumerate(button):
    btn.grid(row=i // 3, column=i % 3)


current_player = "X"
winner = False
label = tk.Label(root, text = f"player {current_player}'s turn", font =("normal", 16))
label.grid(row=3, column = 0, columnspan = 3)

root.mainloop()

