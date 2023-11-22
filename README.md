# Tic Tac Toe Játék

## Hallgató: Sárosi Tibor Márk

Ez a projekt a Tic Tac Toe játékot valósítja meg a Tkinter GUI modullal Python nyelven.

## Feladat leírása

A program célja egy interaktív és felhasználóbarát Tic Tac Toe játék létrehozása, amely lehetővé teszi két játékosnak, hogy kölcsönösen egymás ellen játszhassanak.

## Modulok és függvények

### TicTacToe osztály (main.py):

#### Metódusok:
- `__init__(self, master)`: A játék inicializálása, létrehozza a GUI-t, beállítja az alapértelmezett értékeket.

- `next_turn(self, row, column)`: Ellenőrzi a következő lépést, frissíti a játékállást és a GUI-t.

- `check_winner(self)`: Ellenőrzi, hogy van-e nyertes a játékban.

- `empty_spaces(self)`: Ellenőrzi, hogy van-e üres hely a játéktáblán.

- `new_game(self)`: Új játék indítása, inicializálja a táblát és a játékosokat.

### TicTacToeLogic osztály (logic.py):

#### Metódusok:
- `__init__(self)`: A játéklogika inicializálása, beállítja az alapértelmezett értékeket.

- `next_turn(self, row, column)`: Ellenőrzi a következő lépést, frissíti a játékállást.

- `check_winner(self)`: Ellenőrzi, hogy van-e nyertes a játékban.

- `empty_spaces(self)`: Ellenőrzi, hogy van-e üres hely a játéktáblán.


Jó szórakozást a Tic Tac Toe játékhoz!
