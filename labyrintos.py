# -*- coding: utf-8 -*-
# LabyrinthOS - A Self-Solving Maze Simulation
# Author: A. Olgun

import os
import time
import random

# --- Ayarlar ---
WIDTH = 41  # Genişlik (tek sayı olmalı)
HEIGHT = 21 # Yükseklik (tek sayı olmalı)
DELAY = 0.03 # Animasyon hızı

# --- Karakterler ---
WALL = '█'
PATH = ' '
PLAYER = '☺'
VISITED = '·'
SOLUTION = '●'

def create_maze(width, height):
    """Rastgele bir labirent oluşturur (Recursive Backtracking algoritması)"""
    maze = [[WALL for _ in range(width)] for _ in range(height)]
    
    def carve(x, y):
        maze[y][x] = PATH
        directions = [(x-2, y), (x+2, y), (x, y-2), (x, y+2)]
        random.shuffle(directions)
        
        for new_x, new_y in directions:
            if 0 < new_x < width-1 and 0 < new_y < height-1 and maze[new_y][new_x] == WALL:
                maze[new_y - (new_y - y) // 2][new_x - (new_x - x) // 2] = PATH
                carve(new_x, new_y)

    carve(1, 1)
    maze[1][0] = PLAYER  # Başlangıç
    maze[height-2][width-1] = PATH  # Bitiş
    return maze

def print_maze(maze):
    """Labirenti ekrana basar"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- LabyrinthOS ---")
    print("Hedef: Çıkışı bul!")
    for row in maze:
        print("".join(row))
    print("-------------------")

def solve_maze(maze):
    """Labirenti çözer ve animasyonu gösterir (Depth-First Search)"""
    start_x, start_y = 1, 1
    end_x, end_y = WIDTH - 2, HEIGHT - 2
    
    stack = [(start_x, start_y)]
    path_taken = {}

    while stack:
        time.sleep(DELAY)
        x, y = stack[-1]

        if (x, y) == (end_x, end_y):
            break 
            
        maze[y][x] = PLAYER
        print_maze(maze)
        maze[y][x] = VISITED

        found_move = False
        directions = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)] # Aşağı, Yukarı, Sağ, Sol
        random.shuffle(directions)

        for next_x, next_y in directions:
            if maze[next_y][next_x] == PATH:
                path_taken[(next_x, next_y)] = (x, y)
                stack.append((next_x, next_y))
                found_move = True
                break
        
        if not found_move:
            stack.pop()

    # Çözüm yolunu renklendir
    solution_path = []
    curr = (end_x, end_y)
    while curr != (start_x, start_y):
        solution_path.append(curr)
        try:
            curr = path_taken[curr]
        except KeyError:
            print("Çözüm yolu bulunamadı!")
            return
            
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == VISITED:
                maze[y][x] = PATH
                
    for y, x in reversed(solution_path):
        time.sleep(DELAY)
        maze[x][y] = SOLUTION
        print_maze(maze)
    
    maze[start_y][start_x] = SOLUTION
    maze[end_y][end_x] = SOLUTION
    print_maze(maze)
    print("--- ÇIKIŞ BULUNDU! ---")


if __name__ == '__main__':
    maze_grid = create_maze(WIDTH, HEIGHT)
    solve_maze(maze_grid)
