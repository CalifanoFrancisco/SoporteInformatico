import cv2
import detector as dt
import numpy as np
import random

puntos_jugador = 0
puntos_pc      = 0

def pc_choose() -> str:
    return random.choice(["rock", "paper", "scissors"])

def calculatePoints(player_choice, pc_choice):
    global puntos_jugador, puntos_pc;
    if   player_choice == pc_choice:                                print("Empate");
    elif player_choice == "rock"     and pc_choice == "scissors":   puntos_jugador += 1;
    elif player_choice == "paper"    and pc_choice == "rock":       puntos_jugador += 1;
    elif player_choice == "scissors" and pc_choice == "paper":      puntos_jugador += 1;
    else:                                                           puntos_pc      += 1;

def render(pc_choice, videoFrame):
    
    screen = np.concatenate(
        (
            videoFrame, 
            cv2.imread('reactions/' + pc_choice + '.jpeg')
        ), 
        axis=1);

    cv2.putText(
        screen, 
        'Player: ' + str(puntos_jugador) + ' | PC: ' + str(puntos_pc),
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
        cv2.LINE_AA
    );
    cv2.imshow('Rock Paper Scissors', screen);

while True:
    data          = dt.detectHandGesture();
    player_choice = data[0];
    frame         = data[1];

    # player_choice, frame = ("rock", cv2.imread('reactions/rock.jpeg'));
    
    pc_choice     = pc_choose();
    
    print('Plyr: ' + player_choice + '| PC: ' + pc_choice + ' | ' + str(puntos_jugador) + ' | ' + str(puntos_pc));

    calculatePoints(player_choice, pc_choice);

    render(pc_choice, frame);

    cv2.waitKey(3000);
