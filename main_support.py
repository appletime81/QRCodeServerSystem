import tkinter as tk
import main as m


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = m.Toplevel1(_top1)
    _w1.iniciar()
    root.mainloop()
