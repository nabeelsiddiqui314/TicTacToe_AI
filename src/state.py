import pygame

from board import Board, BoardDisplay, Cell

class StateManager:
    def __init__(self, state):
        self.state = None
        self.setState(state)

    def setState(self, state):
        state.stateManager = self
        self.state = state

    def processEvent(self, event):
        self.state.processEvent(event)

    def update(self):
        self.state.update()

    def render(self, screen):
        self.state.render(screen)

class State:
    def __init__(self):
        self.stateManager = None

    def update(self):
        pass

    def render(self, screen):
        pass

class GameState(State):
    def __init__(self):
        self.board = Board()
        self.boardDisplay = BoardDisplay(self.board, 120)

    def processEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            cellIndex = self.boardDisplay.getCellIndexFromPoint(event.pos)
            if not self.board.isGameOver() and cellIndex is not None:
                self.board.playNext(cellIndex)

    def update(self):
        pass

    def render(self, screen):
        self.boardDisplay.render(screen)