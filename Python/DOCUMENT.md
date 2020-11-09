[toc]

# DOCUMENT

it's document of 2048 game

## How to play

input `w s a d` in console denote `up down left right` four different direction to move number in board

## Game logic

- target: earn most likely score.

  when you merge number, your score will add this merge number , a case is you merge `2` and `2` in board than you can see your score will add `4` which is sum of `2` plus `2`

- every **effective** move will generate a new number which is `2` or `4` , `2` number occur possibility is greater than `4` number

  a move seen effective mean the number in board moved, when the number not move, will not new number generate

- end condition: when the board is filled and not direction move can move the number in the board, the game end

## Class design

this program has five classes as list:

- Game

  `Game` class take charge the game start, run and end. It import `InputFlow` , `Board` and `Score`. 

- InputFlow

  get keyboard input

- Score

  1. read history score
  2. update current score
  3. when the game end, Score will rewrite history score if current score higher than history score

- Board

  1. Board is a 4x4 square that fill by number
  2. we can move number at appointed direction, all number in board will remove



