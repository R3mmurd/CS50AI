# Minesweeper

## Background

### The game

Minesweeper is a puzzle game that consists of a grid of cells, where some of the cells contain hidden “mines.”
Clicking on a cell that contains a mine detonates the mine, and causes the user to lose the game. Clicking on a
“safe” cell (i.e., a cell that does not contain a mine) reveals a number that indicates how many neighboring
cells – where a neighbor is a cell that is one square to the left, right, up, down, or diagonal from the given
cell – contain a mine.

Given this information, a logical player could conclude that there must be a mine in the lower-right cell and
that there is no mine in the upper-left cell, for only in that case would the numerical labels on each of the other
cells be accurate.

The goal of the game is to flag (i.e., identify) each of the mines. In many implementations of the game,
including the one in this project, the player can flag a mine by right-clicking on a cell (or two-finger clicking,
depending on the computer).

### Knowledge Representation

Each sentence of our AI’s knowledge, is represented like the below.

$$\{A, B, C, D, E, F, G, H\} = 1$$

Every logical sentence in this representation has two parts: a set of cells on the board that are involved in the sentence,
and a number count, representing the count of how many of those cells are mines. The above logical sentence says that
out of cells $A$, $B$, $C$, $D$, $E$, $F$, $G$, and $H$, exactly $1$ of them is a mine.

## Getting Started

Run the following command to install the required Python package (pygame) for this project:

```bash
pip3 install -r requirements.txt
```

## Usage

```bash
python3 runner.py
```
