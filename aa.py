import turtle
import random
import tkinter as tk
from tkinter import simpledialog, messagebox


initial_amount = 100000

def start_race():
    global initial_amount
    colors = ["red", "blue", "green"]
    turtles = []

    for i in range(3):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape("turtle")
        t.penup()
        t.goto(-390, (i - 1) * 50)
        turtles.append(t)


    while True:

        bet_amount = simpledialog.askinteger("베팅", "베팅할 금액을 입력하세요:", minvalue=1, maxvalue=initial_amount)
        if bet_amount is None:
            break 

        bet_turtle = simpledialog.askinteger("베팅", "어떤 색의 거북이에 베팅하시겠습니까?\n(1: 빨간색, 2: 파란색, 3: 초록색):", minvalue=1, maxvalue=3)


        race_on = True
        while race_on:
            for t in turtles:
                distance = random.randint(1, 10)
                t.forward(distance)

    
                if t.xcor() >= 390:
                    race_on = False
                    winner_color = t.color()[0]
                    break

    
        messagebox.showinfo("결과", f"우승한 거북이는 {winner_color}입니다.")

    
        if (bet_turtle == 1 and winner_color == "red") or \
           (bet_turtle == 2 and winner_color == "blue") or \
           (bet_turtle == 3 and winner_color == "green"):
            winnings = bet_amount * 2
            initial_amount += winnings - bet_amount  # 수익 반영
            messagebox.showinfo("결과", f"축하합니다! 당신의 수익은 {winnings}원이 되었습니다.\n현재 금액: {initial_amount}원")
        else:
            initial_amount -= bet_amount
            messagebox.showinfo("결과", f"안타깝습니다. 당신은 {bet_amount}원을 잃었습니다.\n현재 금액: {initial_amount}원")

     
        if initial_amount <= 0:
            messagebox.showinfo("게임 종료", "더 이상 베팅할 수 없습니다. 게임이 종료됩니다.")
            break

        play_again = messagebox.askquestion("다시 하시겠습니까?", "다시 하시겠습니까?\n(예: y / 아니오: n)")
        if play_again == 'no':
            messagebox.showinfo("게임 종료", "게임을 종료합니다.")
            break


root = tk.Tk()
root.withdraw()  


start_race()


turtle.mainloop()
