from tkinter import Tk, BOTH, Canvas
from line import Line  # Import the Line class from line.py
from point import Point  # Import the Point class from point.py

class Window: 
    def __init__(self, width=1024, height=768):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Window")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False  # Indicates whether the window is running
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle window close event
    
    def draw_line(self, line, fill_color="black"):
        line.draw(self.canvas, fill_color)

    def run(self):
        self.is_running = True  # Set to True when the window starts running
        self.root.mainloop()
    
    def redraw(self):
        if self.is_running:
            self.canvas.update_idletasks()
            self.canvas.update()
        else:
            print("Window is not running. Cannot redraw.")
    
    def wait_on_close(self):
        if self.is_running:
            self.root.wait_window(self.root)
            self.redraw()
        else:
            print("Window is not running. Cannot wait on close.")
    
    def on_close(self):
        self.is_running = False
        self.root.destroy()
        self.root.quit()

def main():
    window = Window(800, 600)  # Create a window with specified dimensions
    line = Line(100, 100, 300, 300)  # Create a line from (100, 100) to (300, 300)
    window.draw_line(line, fill_color="red")  # Draw the line in red
    window.run()  # Start the window
    window.wait_on_close()  # Wait for the window to close

main()