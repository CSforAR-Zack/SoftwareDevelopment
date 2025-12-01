import tkinter as tk
from tkinter.font import Font

import helper_lib as hl


def main():
    # Custom Variables
    padding: int = 20
    button_size_x: int = 40
    button_size_y: int = 3

    # Window setup
    root: tk.Tk = tk.Tk()
    root.title("File Manager")

    # Fonts
    font: Font = Font(size=30)

    # Main Frame
    main_frame: tk.Frame = tk.Frame(
        root,
        bg=hl.COLORS["BACKGROUND"],
        padx=padding,
        pady=padding,
    )
    main_frame.pack(fill="both", expand=True)
    
    # Label
    label: tk.Label = tk.Label(
        main_frame,
        text="File Manager",
        bg=hl.COLORS["BACKGROUND"],
        fg=hl.COLORS["TEXT"],
        font=font,
    )
    label.pack()

    # Button
    copy_button: hl.HoverButton = hl.HoverButton(
        master=main_frame,
        text="Copy File",
        command=hl.copy_file,
        width=button_size_x,
        height=button_size_y,
    )
    copy_button.pack()

    move_button: hl.HoverButton = hl.HoverButton(
        master=main_frame,
        text="Move File",
        command=hl.move_file,
        width=button_size_x,
        height=button_size_y,
    )
    move_button.pack()
    
    rename_button: hl.HoverButton = hl.HoverButton(
        master=main_frame,
        text="Rename File",
        command=hl.rename_file,
        width=button_size_x,
        height=button_size_y,
    )
    rename_button.pack()
    
    delete_button: hl.HoverButton = hl.HoverButton(
        master=main_frame,
        text="Delete File",
        command=hl.delete_file,
        width=button_size_x,
        height=button_size_y,
    )
    delete_button.pack()

    # Mainloop
    root.mainloop()


if __name__ == "__main__":
    main()