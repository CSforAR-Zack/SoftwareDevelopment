import tkinter as tk

import sort_lib as sl


def main():
    # These are the variables we can change
    number_of_bars: int = 40
    width: int = 20
    max_height: int = 500
    spacing: int = 1
    speed: float = .01
    
    
    # Setup Window
    root: tk.Tk = tk.Tk()
    root.title("Visual Sort")
    root.configure(bg=sl.COLORS["BACKGROUND"])

    bars: sl._Sorter = sl.sorter
    bars.setup(root, spacing, speed)
    bars.create_bars(number_of_bars, width, max_height, sl.COLORS["UNSORTED"])

    bars.bubble_sort()

    root.mainloop()


if __name__ == "__main__":
    main()