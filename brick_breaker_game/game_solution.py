"""
Date:
Version: 2.0
Description: Brick Breaker Game
Resolution: 1280x720
"""


import tkinter as tk

from tkinter import Label,Button,Canvas,LEFT,BOTH,messagebox
import random
import math
from PIL import ImageTk, Image





class MainMenu:
    """
    Handles the main menu of the game.
    It includes the start game, settings and leaderboard buttons.
    """
    def __init__(self, windowmenu,ball_color,paddle_color):
        self.window = windowmenu
        self.ball_color=ball_color
        self.paddle_color=paddle_color
        self.left_key="<Left>"
        self.right_key="<Right>"
        self.name_label=None
        self.pause_key="<Escape>"
        self.boss_key="b"
        self.bosskey_active = False
        #Credits for image of bosskey:
        "https://www.freepik.com/free-vector/coding_2903956.htm"
        self.boss_keyimg="assets/bosskey.jpg"
        self.bosskeypimg=Image.open(self.boss_keyimg)
        self.bosskeypimg=self.bosskeypimg.resize((1280,720))
        self.bosskeypimg=ImageTk.PhotoImage(self.bosskeypimg)
        #Credits for image of flags:
        #https://www.vecteezy.com
        self.flagsimg="assets/flags.png"
        self.flagspimg=Image.open(self.flagsimg)
        self.flagspimg=self.flagspimg.resize((1280,600))
        self.flagspimg=ImageTk.PhotoImage(self.flagspimg)
        self.current_level=1
        self.bosskey_label = None
        self.leaderboard_canvas = None
        self.name_entry = None
        self.player_name = None
        self.close_leaderboard_button = None
        self.game = None
        self.settings_frame = None
        self.settings_title_label = None
        self.textnote = None
        self.left_entry = None
        self.right_entry = None
        self.pause_entry = None
        self.bosskey_entry = None
        self.option_button = None
        self.sellected_option = None
        self.option_menu = None
        self.selected_color = None
        self.color_button = None
        self.color_menu = None
        self.save_settings = None
        self.confirm_button = None
        self.selected_option = None
        self.menu() #Start the main menu



    def menu(self):
        """
        This method initializes the main menu of the game. It sets the current level to 1,
        creates the main frame, and places the background image label.
        """
        self.current_level=1 #Set the current level to 1
        self.name_label=None
        self.main_frame= tk.Frame(self.window) #Create the main frame
        self.main_frame.pack(fill='both', expand=True)
        self.main_frame.configure(bg="black")
        self.image_label=Label(self.main_frame,
                               image=self.flagspimg,
                               bg="black")
        #Create the background image label
        self.image_label.place(relx=0.5, rely=0.7, anchor="center")
        self.title_label = tk.Label(
            self.main_frame,
            text="Blast Breaker",
            font=("Helvetica", 100),
            bg="black",
            fg="white")
        #Create the title
        self.title_label.place(relx=0.5,rely=0.2,anchor="center")
        #Create the start button
        self.start_button = Button(
            self.main_frame,
            text="Start Game",
            command= self.pressstart,
            font=("Helvetica", 20))
        #Create the settings button
        self.settings_button = Button(
            self.main_frame,
            text="Settings",
            command=self.open_settings,
            font=("Helvetica", 20))
        #Create the leaderboard button
        self.leaderboard_button = Button(
            self.main_frame,
            text="Leaderboard",
            command=self.open_leaderboard,
            font=("Helvetica", 20))
        self.bosskey_label = None
        #Add the bosskey to the main frame
        self.main_frame.bind(self.boss_key , self.toggle_bosskey)
        self.main_frame.focus_set()
        self.window.after(10, self.place_buttons) #Place the buttons on the main frame

    def place_buttons(self):
        """
        This method places the start, settings and leaderboard buttons on the main frame.
        """
        button_width = 300
        button_height = 100
        button_x = self.window.winfo_width() / 2 - button_width / 2
        start_button_y = self.window.winfo_height() / 2 - button_height / 2
        settings_button_y = start_button_y + button_height + 20
        leaderboard_button_y = settings_button_y + button_height + 20
        self.start_button.place(
            x=button_x,y=start_button_y,
            width=button_width,
            height=button_height)

        self.settings_button.place(
            x=button_x,
            y=settings_button_y,
            width=button_width,
            height=button_height)

        self.leaderboard_button.place(
            x=button_x,
            y=leaderboard_button_y,
            width=button_width,
            height=button_height)

    def toggle_bosskey(self, event=None):
        """
        This method toggles the bosskey for the main menu.
        """
        if self.bosskey_active:
            #Hide the bosskey image when the bosskey is pressed
            self.bosskey_label.pack_forget()
            self.bosskey_label = None
        else:
            #Show the bosskey image on the main frame
            self.bosskey_label = Label(self.main_frame, image=self.bosskeypimg)
            #Show the bosskey image when the bosskey is pressed
            self.bosskey_label.pack()
        #Toggle the bosskey_active variable
        self.bosskey_active = not self.bosskey_active

    def pressstart(self):
        """
        This method starts the game.
        """
        #If the name label is not on the main frame, then start the game
        if  self.name_label is None:
            self.start_game()

    def toggle_bosskeyleaderboard(self, event=None):
        """
        This method toggles the bosskey for the leaderboard.
        """
        if self.bosskey_active:
            #Hide the bosskey image when the bosskey is pressed
            self.bosskey_label.pack_forget()
            self.bosskey_label = None
        else:
            #Show the bosskey image on the canvas
            self.bosskey_label = Label(
                self.leaderboard_canvas,
                image=self.bosskeypimg)

            self.bosskey_label.pack() #Show the bosskey image when the bosskey is pressed
        #Toggle the bosskey_active variable
        self.bosskey_active = not self.bosskey_active

    def open_leaderboard(self):
        """
        This method opens the leaderboard.
        """
        self.main_frame.destroy() #Destroy the main frame
        self.name_label=None
        self.leaderboard_canvas = Canvas(
            self.window,
            width=window.winfo_width(),
            height=window.winfo_height(),
            bd=0,background="black",
            highlightthickness=0)
        #Place the canvas on the window
        self.leaderboard_canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.close_leaderboard_button = Button(
            self.leaderboard_canvas,
            text="Close",
            command=self.close_leaderboard,
            background="black",
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="white",
            highlightcolor="white",
            height=3,
            width=10,
            font=("Helvetica", 20))
        #Place the exit button on the left corner of the canvas
        self.close_leaderboard_button.place(x=0, y=0, anchor='nw')

        self.bosskey_label = None
        #Add the bosskey to the canvas
        self.leaderboard_canvas.bind(self.boss_key, self.toggle_bosskeyleaderboard)
        self.leaderboard_canvas.focus_set() #Focus on the canvas

        with open("leaderboard.txt", "r", encoding="utf-8") as leaderboard_file:
            scores = [line.strip().split() for line in leaderboard_file]
        #Remove any scores that are not in the correct format
        scores = [score for score in scores if len(score) >= 2]
        #Sort the scores in descending order
        scores = sorted(scores, key=lambda x: int(x[1]), reverse=True)
        #Create the leaderboard title
        self.leaderboard_canvas.create_text(
            self.window.winfo_width()//2,75,
            text="Leader Board",
            font=("Helvetica", 60),
            fill="white",
            anchor="center")

        for i, (player, score) in enumerate(scores): #Create the leaderboard
            self.leaderboard_canvas.create_text(
                self.window.winfo_width()//2-85, 180 + i * 50,
                text=f"{i+1}. {player}: {score}",
                font=("Helvetica", 25), fill="white",anchor="w")
            if i==9: #Only show the top 10 scores
                break

    def close_leaderboard(self):
        """
        This method closes the leaderboard.
        """
        self.leaderboard_canvas.destroy() #Destroy the leaderboard canvas
        self.menu() #Go back to the main menu

    def start_game(self):
        """
        This method starts the game.
        """
        #Create the name label
        self.name_label = tk.Label(
            self.main_frame,
            text="Enter your player name:",
            font=("Helvetica", 20),
            background="black",
            fg="white")
        self.name_label.pack()
        #Create the name entry
        self.name_entry = tk.Entry(
            self.main_frame,
            font=("Helvetica", 20),
            bg="white",
            fg="black")
        self.name_entry.pack()
        #Create the confirm button
        self.confirm_button = tk.Button(
            self.main_frame,
            text="Confirm",
            command=self.confirm_name)
        self.confirm_button.pack()
        self.confirm_button.configure(bg="white", fg="black", font=("Helvetica", 20))

    def confirm_name(self):
        """
        This method confirms the player name and starts the game.
        """
        self.player_name = self.name_entry.get()
        #If the player name is empty, then show an error message
        if not self.player_name.strip():
            tk.messagebox.showerror("Error", "Player name is required")
            return
        loadname=[]
        loadlevel=[]

        with open("save_load.txt", "r", encoding="utf-8") as myfile:
            for line in myfile: #Read the file
                if line=="\n": #If the line is empty stop reading the file
                    break
                #Split the line into name and level
                name, level = line.strip().split(": ")
                loadname.append(name)
                loadlevel.append(level)
        #If the player name is in the file, then load the level
        if self.player_name in loadname:
            self.current_level=loadlevel[loadname.index(self.player_name)]

        self.main_frame.pack_forget() #Hide the main frame
        #Start the game
        self.game = Game(
            self.window,
            self.left_key,
            self.right_key,
            self.pause_key,self.boss_key,
            self.player_name,
            self.current_level,
            self.paddle_color,
            self.ball_color)


    def set_option(self,option):
        """
        This method sets the paddle colour.
        """

        #Set the selected option to the option that was clicked
        self.selected_option.set(option)
        self.paddle_color=option

    def show_menu(self,event):
        """
        This method shows the paddle colour menu.
        """
        self.option_menu.post(event.x_root, event.y_root) #Show the option menu

    def set_color(self, color):
        """
        This method sets the ball colour.
        """

        self.selected_color.set(color) #Set the selected color to the color that was clicked
        self.ball_color=color

    def open_settings(self):
        """
        This method opens the settings.
        """
        self.main_frame.destroy() #Destroy the main frame
        self.name_label=None
        self.settings_frame = tk.Frame(self.window,bg="black")  #Create the settings frame
        self.settings_frame.pack(fill='both', expand=True)
        #Create the settings title
        self.settings_title_label = tk.Label(
            self.settings_frame,
            text="Configure Settings",
            font=("Helvetica", 80),
            bg="black",
            fg="white")
        self.settings_title_label.place(relx=0.5,rely=0.20,anchor="center")
        #Create the note
        self.textnote=tk.Label(
            self.settings_frame,
            text="Note: To configure Move Left and Move Right, click on the entry and press the key you would like to bind.",
            font=("Helvetica", 20),
            bg="black", fg="white")
        self.textnote.place(relx=0.5,rely=0.35,anchor="n")

        #Create the move left label
        tk.Label(
            self.settings_frame,
            text="Move Left:",
            bg="white",
            fg="black",
            font=("Helvetica", 20)).place(
                relx=0.45,
                rely=0.45,
                anchor='e')
        #Create the move right label
        tk.Label(self.settings_frame,
                text="Move Right:",
                bg="white",
                fg="black",
                font=("Helvetica", 20)).place(
                    relx=0.45,
                    rely=0.50,
                    anchor='e')
        #Create the pause button label
        tk.Label(
            self.settings_frame,
            text="Pause Button",
            bg="white",
            fg="black",
            font=("Helvetica", 20)).place(
                relx=0.45,
                rely=0.55,
                anchor='e')
        #Create the boss key label
        tk.Label(
            self.settings_frame,
            text="Boss Key:",
            bg="white",
            fg="black",
            font=("Helvetica", 20)).place(
                relx=0.45,
                rely=0.60,
                anchor='e')
        #Create the paddle colour label
        tk.Label(
            self.settings_frame,
            text="Paddle colour:",
            bg="white",
            fg="black",
            font=("Helvetica", 20)).place(
                relx=0.45,
                rely=0.65,
                anchor='e')
        #Create the ball colour label
        tk.Label(
            self.settings_frame,
            text="Ball colour:",
            bg="white", fg="black",
            font=("Helvetica", 20)).place(
                relx=0.45,
                rely=0.70,
                anchor='e')

        #Create the move left entry
        self.left_entry = tk.Entry(
            self.settings_frame,bg="white",
            fg="black",
            font=("Helvetica", 20),
            border=0,borderwidth=0,
            highlightthickness=0,
            highlightbackground="black")
        self.left_entry.focus_set()
        #Insert the current key into the entry
        self.left_entry.insert(0, self.left_key)
        #Create the move right entry
        self.right_entry = tk.Entry(
            self.settings_frame,
            bg="white",
            fg="black",
            font=("Helvetica", 20),
            border=0,borderwidth=0,
            highlightthickness=0,
            highlightbackground="black")
        self.right_entry.insert(0, self.right_key) #Insert the current key into the entry
        #Create the pause button entry
        self.pause_entry = tk.Entry(
            self.settings_frame,
            bg="white",
            fg="black",
            font=("Helvetica", 20),
            border=0,
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="black")
        #Insert the current key into the entry
        self.pause_entry.insert(0, self.pause_key)
        #Create the boss key entry
        self.bosskey_entry = tk.Entry(
            self.settings_frame,
            bg="white",
            fg="black",
            font=("Helvetica", 20),
            border=0,borderwidth=0,
            highlightthickness=0,
            highlightbackground="black")
        #Insert the current key into the entry
        self.bosskey_entry.insert(0, self.boss_key)
        #Place the move left entry
        self.left_entry.place(relx=0.455, rely=0.45, anchor='w')
        #Place the move right entry
        self.right_entry.place(relx=0.455, rely=0.50, anchor='w')
        #Place the pause button entry
        self.pause_entry.place(relx=0.455, rely=0.55, anchor='w')
        #Place the boss key entry
        self.bosskey_entry.place(relx=0.455, rely=0.60, anchor='w')


        options = ["Blue", "Red", "Yellow", "Green", "Purple", "Orange", "Pink", "White"]
        #Create the paddle colour options
        self.selected_option = tk.StringVar() #Create the selected option variable
        #Set the selected option to the current paddle colour
        self.selected_option.set(self.paddle_color)

        #Create the paddle colour button
        self.option_button = tk.Label(
            self.settings_frame,
            textvariable=self.selected_option,
            bg="white",
            fg="black",
            font=("Helvetica", 20),
            width=20,anchor="w")
        self.option_button.place(relx=0.453, rely=0.65, anchor='w')

        #Create the paddle colour menu
        self.option_menu = tk.Menu(self.settings_frame, tearoff=0)
        for option in options:
            #Add the options to the menu
            self.option_menu.add_command(
                label=option,
                command=lambda option=option: self.set_option(option))
        #Show the menu when the button is clicked
        self.option_button.bind("<Button-1>",self.show_menu)
        #Update the entry when a key is pressed
        self.left_entry.bind("<KeyPress>", self.update_entry)
        #Update the entry when a key is pressed
        self.right_entry.bind("<KeyPress>", self.update_entry)
        #Update the entry when a key is pressed
        self.pause_entry.bind("<KeyPress>", self.update_entry)
        #Update the entry when a key is pressed
        self.bosskey_entry.bind("<KeyPress>", self.update_entry)
        #Show the menu when the button is clicked
        self.option_button.bind(
            "<Button-1>",
            lambda event: self.option_menu.post(event.x_root, event.y_root))

        self.selected_color = tk.StringVar() #Create the selected color variable
        self.selected_color.set(self.ball_color)  #Set the selected color to the current ball colour
        #Create the ball colour button
        self.color_button = tk.Label(
            self.settings_frame,
            textvariable=self.selected_color,
            bg="white",
            fg="black",
            font=("Helvetica", 20),
            width=20, anchor="w")
        self.color_button.place(relx=0.453, rely=0.70, anchor='w')

        self.color_menu = tk.Menu(self.settings_frame, tearoff=0) #Create the ball colour menu
        for color in options:
            #Add the options to the menu
            self.color_menu.add_command(
                label=color,
                command=lambda color=color: self.set_color(color))

        #Show the menu when the button is clicked
        self.color_button.bind(
            "<Button-1>",
            lambda event: self.color_menu.post(event.x_root, event.y_root))

        #Create the save/exit button
        self.save_settings = Button(
            self.settings_frame,
            text="Save",
            command=self.close_settings,
            background="black",
            borderwidth=0,
            highlightthickness=0,
            highlightbackground="white",
            highlightcolor="white",
            height=3,
            width=10,
            font=("Helvetica", 20))
        self.save_settings.place(x=0, y=0, anchor='nw')

    def update_entry(self, event):
        """
        This method updates the entry when a key is pressed.
        """
        current_entry = self.settings_frame.focus_get() #Get the current entry
        #If the current entry is the move left entry, then update the entry
        if current_entry == self.left_entry:
            self.left_entry.delete(0, tk.END)
            #If the key pressed is a letter, then insert the letter into the entry
            if len(event.keysym)==1:
                self.left_entry.insert(0, event.keysym)
            else:
                #If the key pressed is not a letter, then insert the key into the entry with <>
                self.left_entry.insert(0, f"<{event.keysym}>")
        #If the current entry is the move right entry, then update the entry
        elif current_entry == self.right_entry:
            self.right_entry.delete(0, tk.END)
            #If the key pressed is a letter, then insert the letter into the entry
            if len(event.keysym)==1:
                self.right_entry.insert(0, event.keysym)
            else:
                #If the key pressed is not a letter, then insert the key into the entry with <>
                self.right_entry.insert(0, f"<{event.keysym}>")
        elif current_entry == self.pause_entry:
            #If the current entry is the pause button entry, then update the entry
            self.pause_entry.delete(0, tk.END)
            if len(event.keysym)==1:
                #If the key pressed is a letter, then insert the letter into the entry
                self.pause_entry.insert(0, event.keysym)
            else:
                #If the key pressed is not a letter, then insert the key into the entry with <>
                self.pause_entry.insert(0, f"<{event.keysym}>")
        elif current_entry == self.bosskey_entry:
            #If the current entry is the boss key entry, then update the entry
            self.bosskey_entry.delete(0, tk.END)
            if len(event.keysym)==1:
                #If the key pressed is a letter, then insert the letter into the entry
                self.bosskey_entry.insert(0, event.keysym)
            else:
                #If the key pressed is not a letter, then insert the key into the entry with <>
                self.bosskey_entry.insert(0, f"<{event.keysym}>")
        return "break" #Return break to stop the entry from updating



    def close_settings(self):
        """
        This method closes the settings.
        """
        self.left_key = self.left_entry.get() #Update the move left key
        self.right_key = self.right_entry.get() #Update the move right key
        self.pause_key = self.pause_entry.get() #Update the pause button key
        self.boss_key = self.bosskey_entry.get() #Update the boss key
        self.settings_frame.destroy() #Destroy the settings frame
        self.menu() #Go back to the main menu

class Game:
    """
    Class to handle the game.
    """
    def __init__(
            self,
            windowgame,
            leftkey,
            rightkey,
            pausekey,
            bosskey,
            player_name,
            currentlevel,
            paddlecolor,
            ballcolor,
            score=0):

        self.current_level=int(currentlevel)
        self.window = windowgame
        self.brick_width=0
        self.game_paused = False
        self.paddle_color=paddlecolor
        self.ball_color=ballcolor
        self.paddle_width=PADDLE_WIDTH
        self.paddle_speed=PADDLE_SPEED
        self.ball_speed=BALL_SPEED
        self.player_name=player_name
        self.leftkey=leftkey
        self.rightkey=rightkey
        self.bosskey=bosskey
        #Credits for images of powerups:
        #https://opengameart.org/content/breakout-brick-breaker-tile-set-free
        self.expandimg="assets/expand.png"
        self.shrinkimg="assets/shrink.png"
        self.fastimg="assets/fast.png"
        self.slowimg="assets/slow.png"
        self.fastballimg="assets/fastball.png"
        self.slowballimg="assets/slowball.png"
        self.points100img="assets/points100.png"
        self.points250img="assets/points250.png"
        #Add the path of the powerups to a list
        self.oldpowerups=[
            self.expandimg,
            self.shrinkimg,
            self.fastimg,
            self.slowimg,
            self.fastballimg,
            self.slowballimg,
            self.points100img,
            self.points250img]
        self.powerups=[]
        self.score=score
        self.leftkey=leftkey
        self.rightkey=rightkey
        self.pausekey=pausekey
        self.currentpowerup=None
        self.bosskey_label = None
        self.main_menu_button = None
        self.ball_dx=None
        self.ball_dy=None
        self.currentpowerup=None
        self.paddle_velocity=None
        self.pausedtext=None
        self.save_button=None
        self.next_level_button=None
        #Credits for image of bosskey:
        #https://www.freepik.com/free-vector/coding_2903956.htm
        self.boss_keyimg="assets/bosskey.jpg"
        self.bosskeypimg=Image.open(self.boss_keyimg) #Create the boss key image
        self.bosskeypimg=self.bosskeypimg.resize((1280,720))
        self.bosskeypimg=ImageTk.PhotoImage(self.bosskeypimg) #Resize the boss key image
        self.bosskey_active = False


        self.go_to_next_level()

        for power in self.oldpowerups:

            img = Image.open(power)
            new_size = (img.size[0]//7, img.size[1]//7)

            img_resized = img.resize(new_size) # Resize the powerups


            self.powerup_image = ImageTk.PhotoImage(img_resized) #Create the powerup image
            self.powerups.append(self.powerup_image)



    def toggle_bosskey(self, event=None):
        """
        This method toggles the bosskey for the game.
        """
        if self.bosskey_active:
            if self.bosskey_label is not None:
                #Hide the bosskey image when the bosskey is pressed
                self.bosskey_label.pack_forget()
            self.bosskey_label = None
            #If the save button is hidden, then show the save button
            if self.save_button.winfo_viewable():
                self.save_button.pack_forget()


        else:
            if not self.game_paused:
                self.toggle_pause()
            #Show the bosskey image on the canvas
            self.bosskey_label = Label(self.canvas, image=self.bosskeypimg)
            self.bosskey_label.pack()
            self.save_button.pack_forget() #Hide the save button when the bosskey is pressed

        self.bosskey_active = not self.bosskey_active #Toggle the bosskey_active variable


    def go_to_next_level(self):
        """
        This method handles the transition to the next level.
        """

        #Create the canvas
        self.canvas= tk.Canvas(
            self.window,
            width=self.window.winfo_width(),
            height=self.window.winfo_height(),
            bd=0,
            background="black",
            highlightthickness=0)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        #Create the paddle
        self.paddle = self.canvas.create_rectangle(
            WIDTH // 2 - self.paddle_width // 2,
            HEIGHT - PADDLE_HEIGHT,
            WIDTH // 2 + self.paddle_width // 2,
            HEIGHT,
            fill=self.paddle_color)
        #Create the ball
        self.ball = self.canvas.create_oval(
            WIDTH // 2 - BALL_RADIUS,
            HEIGHT // 2 - BALL_RADIUS,
            WIDTH // 2 + BALL_RADIUS,
            HEIGHT // 2 + BALL_RADIUS,
            fill=self.ball_color)
        self.main_menu_button = None

        self.ball_dx = self.ball_speed
        self.ball_dy = self.ball_speed

        self.currentpowerup=None


        self.bricks=[]

        self.pressed_keys = set() #Create a set to store the pressed keys
        window.bind("<KeyPress>", self.key_press)  #
        window.bind("<KeyRelease>", self.key_release)

        #Create the start text
        self.start_text=self.canvas.create_text(
            CANVAS_WIDTH//2,
            CANVAS_HEIGHT//1.5,
            text="Press enter to launch game",
            font=("Helvetica", 30),
            fill="red",
            anchor="center")
        window.bind("<Return>", self.start_game) #Bind the enter key to the start game function
        #Create the score text
        self.scoretext=self.canvas.create_text(
            0,
            0,
            text=f"Score: {self.score}",
            font=("Helvetica", 20),
            fill="red",
            anchor="nw")
        self.create_brick_design() #Create the brick design based on the current level

    def start_game(self, event):
        """
        This method starts the game.
        """
        window.unbind("<Return>") #Unbind the enter key from the start game function
        self.canvas.delete(self.start_text) #Delete the start text
        self.paddle_velocity = 0
        #Bind the move left key to the start move paddle left function
        window.bind(self.leftkey, self.start_move_paddle_left)
        #If the move left key is a letter, then remove the <>
        if len(self.leftkey)==1:
            leftkeyr=self.leftkey
        else:
            #If the move left key is not a letter, then remove the <>
            leftkeyr=self.leftkey[1:-1]
        #Bind the release of the move left key to the stop moving paddle function
        window.bind(f"<KeyRelease-{leftkeyr}>", self.stop_moving_paddle)
        #If the move right key is a letter, then remove the <>
        if len(self.rightkey)==1:
            rightkeyr=self.rightkey
        else:
            #If the move right key is not a letter, then remove the <>
            rightkeyr=self.rightkey[1:-1]
        #Bind the move right key to the start move paddle right function
        window.bind(self.rightkey, self.start_move_paddle_right)
        #Bind the release of the move right key to the stop moving paddle function
        window.bind(f"<KeyRelease-{rightkeyr}>", self.stop_moving_paddle)
        self.move_paddle() #Move the paddle

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy) #Move the ball
        self.game_loop() #Start the game loop


    def key_press(self, event):
        """
        This method adds the key pressed to the set of pressed keys to check for the cheat code
        """
        if self.game_paused:
            return
        self.pressed_keys.add(event.keysym) #Add the pressed key to the set
        self.check_cheat_code() #Check if the cheat code is activated

    def key_release(self, event):
        """
        This method removes the key released from the set of pressed keys
        """
        if self.game_paused:
            return
        self.pressed_keys.discard(event.keysym) #Remove the released key from the set

    def check_cheat_code(self):
        """
        This method checks if the cheat code is activated
        """
        if 'c' in self.pressed_keys and 'h' in self.pressed_keys:
            self.activate_cheat_code()

    def activate_cheat_code(self):
        """
        This method activates the cheat code
        """
        if self.bricks:
            self.canvas.delete(self.bricks[-1])
            del self.bricks[-1]


    def powerup(self):
        """
        This method handles the powerups
        """
        self.powerup_image=random.choice(self.powerups) #Choose a random powerup
        #Create the powerup
        self.currentpowerup=self.canvas.create_image(
            random.randint(0,1210),
            0,
            image=self.powerup_image,
            anchor="nw")

    def create_brick_design(self):
        """
        This method creates the brick design based on the current level
        """

        if self.current_level==1:
            brick_colours = ["blue", "white","red"]
            self.brick_width=426
            for row in range(7):
                for col in range(CANVAS_WIDTH//self.brick_width):
                    x1 = col * self.brick_width
                    y1 = row * BRICK_HEIGHT
                    x2 = x1 + self.brick_width
                    y2 = y1 + BRICK_HEIGHT

                    if col < CANVAS_WIDTH // (3 * self.brick_width):
                        color = brick_colours[0]
                    elif col < 2 * CANVAS_WIDTH // (3 * self.brick_width):
                        color = brick_colours[1]
                    else:
                        color =brick_colours[2]


                    brick=self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                    self.bricks.append(brick) #Add the brick to the list of bricks
            self.canvas.tag_raise(self.scoretext) #Raise the score text to the top

        elif self.current_level==2:
            self.brick_width=85
            brick_colours = ["white", "red"]
            num_bricks = CANVAS_WIDTH // self.brick_width

            for row in range(7):
                for col in range(num_bricks):
                    x1 = col * self.brick_width
                    y1 = row * BRICK_HEIGHT
                    x2 = x1 + self.brick_width
                    y2 = y1 + BRICK_HEIGHT


                    color = brick_colours[1] if (row == 3 or col==7) else brick_colours[0]


                    brick=self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                    self.bricks.append(brick) #Add the brick to the list of bricks
            self.canvas.tag_raise(self.scoretext) #Raise the score text to the top


        elif self.current_level==3:
            self.brick_width=80
            for row in range(9):
                for col in range(CANVAS_WIDTH // self.brick_width):
                    x1 = col * self.brick_width
                    y1 = row * BRICK_HEIGHT
                    x2 = x1 + self.brick_width
                    y2 = y1 + BRICK_HEIGHT


                    color = BRICK_COLORS[row % len(BRICK_COLORS)]


                    brick=self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                    self.bricks.append(brick) #Add the brick to the list of bricks

            self.canvas.itemconfig(self.bricks[2],fill="white")
            self.canvas.itemconfig(self.bricks[16], fill="blue")
            self.canvas.itemconfig(self.bricks[17], fill="blue")
            self.canvas.itemconfig(self.bricks[19], fill="blue")
            self.canvas.itemconfig(self.bricks[20], fill="blue")
            for i in range(31,37):
                self.canvas.itemconfig(self.bricks[i], fill="white")
            self.canvas.itemconfig(self.bricks[48], fill="blue")
            self.canvas.itemconfig(self.bricks[49], fill="blue")
            self.canvas.itemconfig(self.bricks[51], fill="blue")
            self.canvas.itemconfig(self.bricks[52], fill="blue")
            self.canvas.itemconfig(self.bricks[66], fill="white")
            self.canvas.tag_raise(self.scoretext) #Raise the score text to the top

    def start_move_paddle_left(self, event):
        """
        This method starts moving the paddle left.
        """
        if self.game_paused: #If the game is paused, then dont move the paddle
            return
        self.paddle_velocity = -self.paddle_speed #Set the paddle speed to the negative paddle speed

    def start_move_paddle_right(self, event):
        """
        This method starts moving the paddle right.
        """
        if self.game_paused: #If the game is paused, then dont move the paddle
            return
        self.paddle_velocity = self.paddle_speed #Set the paddle speed to the paddle speed

    def stop_moving_paddle(self, event):
        """
        This method stops moving the paddle.
        """
        self.paddle_velocity = 0

    def move_paddle(self):
        """
        This method moves the paddle.
        """
        current_position = self.canvas.coords(self.paddle) #Get the current position of the paddle
        if len(current_position) < 4: #If the paddle is not on the canvas, then dont move the paddle
            return False
        #If the paddle is not on the left edge of the canvas
        # and the paddle speed is negative, move the paddle
        if current_position[0]-10 > 0 and self.paddle_velocity < 0:
            self.canvas.move(self.paddle, self.paddle_velocity, 0)
        #If the paddle is not on the right edge of the canvas
        # and the paddle speed is positive, move the paddle
        elif current_position[2]+10 < WIDTH and self.paddle_velocity > 0:
            self.canvas.move(self.paddle, self.paddle_velocity, 0)
        # Call this function again after 5 ms to move the paddle
        self.window.after(5, self.move_paddle)
        return None
    def check_collisions_ball_on_screen(self):
        """
        This method checks if the ball is on the screen and also handles collisions with
        paddle or bricks.
        """
        ball_position=self.canvas.coords(self.ball) #Get the current position of the ball
        paddle_position=self.canvas.coords(self.paddle) #Get the current position of the paddle
        #If the ball or paddle is not on the canvas, then dont check for collisions
        if  len(ball_position) < 4 or len(paddle_position) < 4:
            return False
        #If the ball is on the left or right edge of the canvas,
        # then change the x direction of the ball
        if ball_position is not None and (ball_position[0]<=0 or ball_position[2]>=WIDTH):
            if self.ball_dx is not None:
                self.ball_dx= -(self.ball_dx)
        #If the ball is on the top edge of the canvas, then change the y direction of the ball
        if ball_position[1]<=0 :
            if self.ball_dy is not None:
                self.ball_dy = -self.ball_dy

        #If the ball is on the paddle, then change the y direction of the ball
        if (ball_position[2]>= paddle_position[0]and
            ball_position[0]<=paddle_position[2] and
            ball_position[3]>=paddle_position[1] and
            ball_position[3]<=paddle_position[3]):
            if self.ball_dy is not None:
                self.ball_dy = -self.ball_dy

        for brick in self.bricks: #Check if the ball is on a brick
            brick_position=self.canvas.coords(brick)
            if (ball_position[2] >= brick_position[0] and
                ball_position[0] <= brick_position[2] and
                ball_position[3] >= brick_position[1] and
                ball_position[3] <= brick_position[3]):
                self.canvas.delete(brick) #Delete the brick
                self.bricks.remove(brick) #Remove the brick from the list of bricks
                self.score+=10 #Increase the score by 10
                #Update the score text
                self.canvas.itemconfig(self.scoretext, text=f"Score: {self.score}")
                if self.ball_dy is not None:
                    self.ball_dy = -self.ball_dy

        #If the ball is on the bottom edge of the canvas, then end the game
        flag = ball_position[3] >= HEIGHT
        return flag

    def check_collision_powerup(self):
        """
        This method checks if the ball is on a powerup and activates the powerup.
        """
        if self.currentpowerup is None: #If there is no powerup, then dont check for collisions
            return

        #Get the current position of the powerup
        powerup_position = self.canvas.bbox(self.currentpowerup)
        #If the powerup is not on the canvas, then dont check for collisions
        if powerup_position is None:
            return
        paddle_position=self.canvas.coords(self.paddle) #Get the current position of the paddle

        # If the powerup is on the paddle, then activate the powerup
        if (powerup_position[2] >= paddle_position[0] and
            powerup_position[0] <= paddle_position[2] and
            powerup_position[3] >= paddle_position[1] and
            powerup_position[3] <= paddle_position[3]):
            self.canvas.delete(self.currentpowerup) #Delete the powerup
            self.currentpowerup = None
            #If the powerup is the expand powerup, then expand the paddle
            if self.powerup_image == self.powerups[0]:
                self.paddle_width *= 1.5
                paddle_x = paddle_position[0] - self.paddle_width // 1.5
                self.canvas.coords(
                    self.paddle,
                    paddle_x,
                    paddle_position[1],
                    paddle_x + self.paddle_width,
                    paddle_position[3]
                    )
                self.canvas.itemconfig(self.paddle, fill=self.paddle_color)

            #If the powerup is the shrink powerup, then shrink the paddle
            elif self.powerup_image == self.powerups[1]:
                self.paddle_width //= 1.5
                paddle_x = paddle_position[0] + self.paddle_width // 1.5
                self.canvas.coords(
                    self.paddle,
                    paddle_x,
                    paddle_position[1],
                    paddle_x + self.paddle_width,
                    paddle_position[3])
                self.canvas.itemconfig(self.paddle, fill=self.paddle_color)

            #If the powerup is the fast powerup, then increase the paddle speed
            elif self.powerup_image == self.powerups[2]:
                self.paddle_speed *= 1.5

            #If the powerup is the slow powerup, then decrease the paddle speed
            elif self.powerup_image == self.powerups[3]:
                self.paddle_speed //= 1.5

            #If the powerup is the fast ball powerup, then increase the ball speed
            elif self.powerup_image==self.powerups[4]:
                speed_increase_factor = 1.1

                # Calculate the current speed of the ball
                current_speed = (self.ball_dx**2 + self.ball_dy**2)**0.5

                # Increase the speed
                new_speed = current_speed * speed_increase_factor

                # Calculate the current direction of the ball
                direction = math.atan2(self.ball_dy, self.ball_dx)

                # Update the velocities
                self.ball_dx = new_speed * math.cos(direction)
                self.ball_dy = new_speed * math.sin(direction)



            elif self.powerup_image==self.powerups[5]:
                speed_increase_factor = 0.9

                # Calculate the current speed of the ball
                current_speed = (self.ball_dx**2 + self.ball_dy**2)**0.5

                # Increase the speed
                new_speed = current_speed * speed_increase_factor

                # Calculate the current direction of the ball
                direction = math.atan2(self.ball_dy, self.ball_dx)

                # Update the velocities
                self.ball_dx = new_speed * math.cos(direction)
                self.ball_dy = new_speed * math.sin(direction)

            #If the powerup is the 100 points powerup, then increase the score by 100
            elif self.powerup_image==self.powerups[6]:
                self.score+=100
                #Update the score text
                self.canvas.itemconfig(self.scoretext, text=f"Score: {self.score}")
            #If the powerup is the 250 points powerup, then increase the score by 250
            elif self.powerup_image==self.powerups[7]:
                self.score+=250
                #Update the score text
                self.canvas.itemconfig(self.scoretext, text=f"Score: {self.score}")


    def toggle_pause(self):
        """
        This method toggles the pause for the game.
        """
        self.game_paused = not self.game_paused
        if not self.game_paused:
            self.canvas.delete(self.pausedtext)
            self.save_button.pack_forget()
            self.game_loop()
        else:
            self.pausedtext=self.canvas.create_text(
                WIDTH // 2,
                HEIGHT // 2,
                text="Game Paused",
                font=("Helvetica", 30),
                fill="red",
                anchor="center"
            )
            self.save_button = Button(self.canvas, text="Save Progress", command=self.save_progress)
            self.save_button.pack()

    def save_progress(self):
        """
        This method saves the progress of the game.
        """
        loadname=[]
        with open("save_load.txt", "r",encoding="utf-8") as myfile:
            for line in myfile:
                if line == "\n":  # If the line is empty, then stop reading
                    break
                name,_ = line.strip().split(": ")  # Split the line into the name and level
                loadname.append(name)  # Add the name to the list of names
        #If the player name is not in the file, then add the player name and level to the file
        if self.player_name not in loadname:
            with open("save_load.txt", "a",encoding="utf-8") as myfile:
                myfile.write(f"{self.player_name}: {self.current_level}\n")
        else: #If the player name is in the file, then update the level of the player
            with open("save_load.txt", "r",encoding="utf-8") as myfile:
                lines = myfile.readlines()

            with open("save_load.txt", "w",encoding="utf-8") as myfile:
                for line in lines:
                    name, _ = line.strip().split(": ")
                    if name == self.player_name:
                        #Update the level of the player
                        myfile.write(f"{self.player_name}: {self.current_level}\n")


            myfile.close()
        self.save_button.pack_forget()
        self.go_to_main_menu()


    def remove_progress(self):
        """
        #Remove the progress of the game if a player lost the game or completed the game.
        """
        with open("save_load.txt", "r",encoding="utf-8") as myfile:
            lines = myfile.readlines()
        lines=[line for line in lines if line.strip()!=f"{self.player_name}: {self.current_level}"]
        myfile.close()
        with open("save_load.txt", "w",encoding="utf-8") as myfile:
            myfile.writelines(lines)

    def game_loop(self):
        """
        This method handles the game loop.
        """#Bind the pause key to the toggle pause function
        self.canvas.bind(self.pausekey, lambda event: self.toggle_pause())
        #Bind the boss key to the toggle boss key function
        self.canvas.bind(self.bosskey, lambda event : self.toggle_bosskey())
        self.canvas.focus_set()

        if self.game_paused: #If the game is paused, then dont move the ball
            return

        self.canvas.move(self.ball, self.ball_dx, self.ball_dy) #Move the ball
        if self.currentpowerup is None: #If there is no powerup, then create a powerup
            self.powerup()

        #If there is a powerup, then move the powerup
        if self.currentpowerup is not None and self.canvas.coords(self.currentpowerup):
            #If the powerup is on the bottom edge of the canvas, create a new powerup
            if self.canvas.coords(self.currentpowerup)[1]>=HEIGHT:
                self.canvas.delete(self.currentpowerup)
                self.currentpowerup = None
                self.powerup()
            else:
                self.canvas.move(self.currentpowerup,0,2) #Move the powerup


        if len(self.bricks) == 0: #If there are no bricks, then go to the next level
            if self.current_level==3: #If the current level is 3, then the player won the game
                self.remove_progress()
                self.canvas.unbind(self.pausekey)
                self.canvas.create_text(
                    WIDTH // 2,
                    HEIGHT // 2,
                    text="Congratulations! You Win!",
                    font=("Helvetica", 30),
                    fill="red",
                    anchor="center"
                )
            else: #If the current level is not 3, then the player completed the level
                self.canvas.create_text(
                    WIDTH // 2,
                    HEIGHT // 2,
                    text=f"Level {self.current_level} Complete",
                    font=("Helvetica", 30),
                    fill="red",
                    anchor="center"
                )
            self.canvas.delete(self.ball)
            self.canvas.delete(self.paddle)

            self.window.unbind("<Left>")
            self.window.unbind("<Right>")
            self.window.unbind("<KeyRelease-Left>")
            self.window.unbind("<KeyRelease-Right>")
            self.window.unbind(self.pausekey)
            self.canvas.delete(self.currentpowerup)
            self.paddle_width = 100

            self.paddle_speed = PADDLE_SPEED
            self.ball_speed = BALL_SPEED

            if self.current_level!=3: #If the current level is not 3, then go to the next level
                self.current_level+=1

                self.next_level_button = Button(
                    self.window,
                    text="Next Level",
                    command=self.handlecanvas)
                #Create the next level button
                self.next_level_button.place(relx=0.5, anchor="n")
                return



            self.main_menu_button = Button(
                self.canvas,
                text="Close",
                command=self.go_to_main_menu,
                background="black",
                borderwidth=0,
                highlightthickness=0,
                highlightbackground="white",
                highlightcolor="white",
                height=3,
                width=10,
                font=("Helvetica", 20))
            #Create the close button
            self.main_menu_button.place(x=0, y=0, anchor='nw')
            self.main_menu_button.lift() #Raise the close button to the top
            with open("leaderboard.txt", "a",encoding="utf-8") as myfile:
                myfile.write(f"{self.player_name} {self.score}\n")
            return

        if self.check_collisions_ball_on_screen(): #Check if the ball is on the screen
            self.remove_progress() #Remove the progress of the game
            self.canvas.unbind(self.pausekey) #Unbind the pause key from the toggle pause function
            self.canvas.create_text(
                WIDTH // 2,
                HEIGHT // 2,
                text="Game Over",
                font=("Helvetica", 30),
                fill="red",
                anchor="center"
            )
            #Create the game over text
            self.main_menu_button = Button(
                self.canvas,
                text="Close",
                command=self.go_to_main_menu,
                background="black",
                borderwidth=0,
                highlightthickness=0,
                highlightbackground="white",
                highlightcolor="white",
                height=3,
                width=10,
                font=("Helvetica", 20))
            #Create the close button
            self.main_menu_button.place(x=0, y=0, anchor='nw')
            self.canvas.delete(self.ball) #Delete the ball
            self.canvas.delete(self.paddle) #Delete the paddle
            for brick in self.bricks: #Delete the bricks
                self.canvas.delete(brick)


            self.window.unbind("<Left>")
            self.window.unbind("<Right>")
            self.window.unbind("<KeyRelease-Left>")
            self.window.unbind("<KeyRelease-Right>")
            self.window.unbind(self.pausekey)
            self.canvas.delete(self.currentpowerup)
            self.paddle_width = 100

            self.paddle_speed = PADDLE_SPEED
            self.ball_speed = BALL_SPEED
            return


        self.check_collision_powerup() #Check if the paddle is on a powerup
        self.window.after(5, self.game_loop)  # Call this function again after 5 ms


    def handlecanvas(self):
        """
        This method removes the canvas.
        """
        self.canvas.pack_forget() #Forget the canvas
        self.go_to_next_level() #Go to the next level

    def go_to_main_menu(self):
        """
        This method goes back to the main menu.
        """
        if self.main_menu_button is not None:
            self.main_menu_button.pack_forget()
        self.canvas.pack_forget() #Forget the canvas
        main_menu.menu() #Go back to the main menu








BALL_COLOR = "Red"
PADDLE_COLOR = "Blue"
WIDTH = 1280
HEIGHT = 720
PADDLE_WIDTH= 100
PADDLE_HEIGHT = 25
BRICK_HEIGHT = 30
CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 720
PADDLE_SPEED= 8
BALL_SPEED = 4
BALL_RADIUS = 8

BRICK_COLORS = ["blue","white"]

window = tk.Tk() #Create the window
window.title("Blast Breaker") #Set the title of the window
window.geometry("1280x720") #Set the size of the window
window.configure(bg="black") #Set the background colour of the window
window.resizable(False, False)  #Make the window not resizable

main_menu = MainMenu(window,BALL_COLOR,PADDLE_COLOR) #Create the main menu

window.mainloop() #Run the window
