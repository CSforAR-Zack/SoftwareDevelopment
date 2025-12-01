import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog



COLORS: dict = {
    "BACKGROUND": "black",
    "TEXT": "white",
    "BASE": "grey",
    "HOVER": "cyan",
    "TEXT_BASE": "white",
    "TEXT_HOVER": "black",
}


def copy_file() -> None:
    """Make a copy of a file."""

    try:
        file_path: str = filedialog.askopenfilename(title="Select a file to copy")
        dest_path: str = filedialog.asksaveasfilename(
            title="Select destination for copied file",
            initialfile=os.path.basename(file_path),
        )

        # Missing copy implementation

        messagebox.showinfo("Success", f"File copied to {dest_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy file: {e}")


def move_file() -> None:
    """Move a file to a new directory"""

    try:
        file_path: str = filedialog.askopenfilename(title="Select a file to move")
        dest_path: str = filedialog.asksaveasfilename(
            title="Select destination for moved file",
            initialfile=os.path.basename(file_path),
        )
        
        # Missing move implementation

        messagebox.showinfo("Success", f"File moved to {dest_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to move file: {e}")


def rename_file() -> None:
    """Rename a file to a different name."""

    try:
        file_path: str = filedialog.askopenfilename(title="Select a file to rename")
        new_name: str = simpledialog.askstring("Rename File", "Enter new file name (with ext):")
        new_path: str = os.path.join(os.path.dirname(file_path), new_name)

        # Missing rename implementation

        messagebox.showinfo("Success", f"File renamed to {new_name}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to rename file: {e}")


def delete_file() -> None:
    """Delete a file. This action is permanent."""

    try:
        file_path: str = filedialog.askopenfilename(title="Select a file to delete")
        confirm: bool = messagebox.askyesno("Confirm", f"Permanently delete {os.path.basename(file_path)}?")
        if confirm:
            
            # Missing delete implementation

            messagebox.showinfo("Success", "File deleted successfully.")
        else:
            messagebox.showinfo("Cancelled", "File deletion cancelled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete file: {e}")


class HoverButton(tk.Button):
    """A custom button that changes color when hovered over."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.config(bg=COLORS["BASE"], fg=COLORS["TEXT_BASE"])
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def on_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse is over it."""

        event.widget.config(bg=COLORS["HOVER"], fg=COLORS["TEXT_HOVER"])

    def off_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse leaves it."""

        event.widget.config(bg=COLORS["BASE"], fg=COLORS["TEXT_BASE"])