import tkinter
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_pressed():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="25:00")
    status_txt.config(text="TIMER")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_pressed():
    global reps
    if reps == 0:
        start_timer()


def start_timer():
    play_sound()
    global reps
    reps += 1
    print(reps)

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        status_txt.config(text="Long Break", font="Courier 25 bold", fg=RED, bg=YELLOW)
        checkmark.config(text='🗸' * math.floor(reps / 2))
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        status_txt.config(text="Break", font="Courier 25 bold", fg=PINK, bg=YELLOW)
        checkmark.config(text='🗸'*math.floor(reps/2))
    elif reps % 2 != 0:
        countdown(WORK_MIN * 60)
        status_txt.config(text="Work", font="Courier 25 bold", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(x):
    count_min = math.floor(x/60)
    count_sec = x % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if x != 0:
        global timer
        timer = window.after(1000, countdown, x - 1)
    elif x == 0:
        start_timer()
    if reps % 2 != 0:
        if 5 < int(count_sec) < 55 and int(count_sec) != 0 and int(count_min) == 24:
            window.withdraw()
        elif int(count_sec) < 5 and int(count_sec) != 0 and int(count_min) == 0:
            window.deiconify()


# ------------------------- play sound
def play_sound():
    playsound("C:/Users/user/Desktop/pomodoro/countdown_sound.mp3", False)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)


# creating canvas and putting img
canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")


canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
start = tkinter.Button(window, text="Start", font="Courier 10 bold", command=start_pressed)
reset = tkinter.Button(window, text="Reset", font="Courier 10 bold", command=reset_pressed)
start.grid(row=2, column=0)
reset.grid(row=2, column=2)

# text and check mark
status_txt = Label(window, text="TIMER", font="Courier 25 bold", fg=GREEN, bg=YELLOW)
status_txt.grid(column=1, row=0)

checkmark = Label(window, font="Courier 25 bold", fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)


window.mainloop()
