import tkinter as tk
from random import randint
from time import sleep


COLORS: dict = {
    "BACKGROUND": "black",
    "UNSORTED": "grey",
    "SORTED": "lime green",
    "HIGHLIGHT": "yellow",
    "BEST": "red",
}


class _Bar:
    """Bar class with a height and color. Uses a Frame."""
    
    def __init__(
        self,
        height: int,
        width: int,
        color: str,
        wn: tk.Tk,
    ) -> None:
        
        self.height = height
        self._frame: tk.Frame = tk.Frame(wn, width=width, height=height, bg=color)

    def color(self, color: str) -> None:
        """Change the color of the bar."""

        self._frame.configure(bg=color)

    def __repr__(self) -> str:
        """How to show a bar."""

        return str(self.height)
    
    def __gt__(self, other: "_Bar") -> bool:
        """Return true if greater than other, false otherwise."""

        return self.height > other.height
    
    def __lt__(self, other: "_Bar") -> bool:
        """Return true if less than other, false otherwise."""

        return self.height < other.height


class _Sorter:
    """Class to manage multiple bars and sorting algorithms.
    Use the instance 'sorter' defined at the bottom.
    It should be treated as a singleton."""
    
    def __init__(self) -> None:
        """Create a bar manager."""
        
        self._wn: tk.Tk|None = None
        self._spacing: int = 0
        self._speed: float = 1.0

        self._bars: list[_Bar] = []

    def setup(
        self,
        wn: tk.Tk,
        spacing: int,
        speed: float,
    ) -> None:
        """Setup the bar manager."""

        self._wn = wn
        self._spacing = spacing
        self._speed = speed

    def create_bars(
        self,
        number_of_bars: int,
        width: int,
        max_height: int,
        color: str,
    ) -> None:
        
        for _ in range(number_of_bars):
            height: int = randint(1, max_height)
            bar: _Bar = _Bar(height, width, color, self._wn)
            self._bars.append(bar)
        self.pack_bars()
        self.update_bars()

    def pack_bars(self) -> None:
        """Pack the bars into the window."""

        for bar in self._bars:
            bar._frame.pack(side="left", anchor="s", padx=self._spacing)

    def update_bars(self) -> None:
        """Update the bars in the window."""

        for bar in self._bars:
            bar._frame.pack_forget()
        self.pack_bars()
        self._wn.update()
        sleep(self._speed)

    def swap_bars(self, first: int, second: int) -> None:
        """Swap bars at first and second index."""

        self._bars[first], self._bars[second] = self._bars[second], self._bars[first]

    def bubble_sort(self) -> None:
        """Perform bubble sort on bars."""

        for i in range(len(self._bars)):
            for j in range(len(self._bars)-1-i):
                if self._bars[j] > self._bars[j+1]:
                    self.swap_bars(j, j+1)
                self._bars[j].color(COLORS["UNSORTED"])
                self._bars[j+1].color(COLORS["HIGHLIGHT"])
                self.update_bars()
            self._bars[-1-i].color(COLORS["SORTED"])

    def __repr__(self) -> str:
        """How to show the bars."""

        return str(self._bars)
    

sorter: _Sorter = _Sorter()