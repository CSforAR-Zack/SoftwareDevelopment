import pygame as pg

from snake_enums import FontFiles, State


class GameManager:
    """Manages the game and state."""

    # Make GameManager a singleton
    _instance: "GameManager" = None

    def __new__(cls) -> "GameManager":
        """Singleton pattern to ensure only one instance of GameManager exists."""

        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self) -> None:
        """Initializes the game manager."""
        
        self.width: int = 800
        self.height: int = self.width
        self.screen: pg.Surface = pg.display.set_mode((self.width, self.height))
        self.size: int = self.width // 20
        self.speed: int = 10
        self.clock: pg.time.Clock = pg.time.Clock()

        self.state: int = State.menu
        self.score: int = 0
        self.high_score: int = 0

        self.large_font: pg.font.Font = pg.font.Font(FontFiles.large, 48)
        self.small_font: pg.font.Font = pg.font.Font(FontFiles.small, 24)
        
    def center(self) -> tuple:
        """Returns the center of the screen."""

        return (self.width // 2, self.height // 2)
    
    def tick(self) -> None:
        """Controls the frame rate of the game."""

        self.clock.tick(self.speed)