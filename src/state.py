import pygame

from board import Board, BoardDisplay, Cell
from player import Human, PlayerManager, MinimaxAI

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

    def processEvent(self, event):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

class GameState(State):
    def __init__(self):
        self.board = Board()
        self.boardDisplay = BoardDisplay(self.board, 120, 5)
        self.playerManager = PlayerManager(Human(self.boardDisplay), MinimaxAI())

    def processEvent(self, event):
        pass

    def update(self):
        if not self.board.isGameOver():
            self.playerManager.play(self.board)

    def render(self, screen):
        self.boardDisplay.render(screen)