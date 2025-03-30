from tkinter import Tk, BOTH, Canvas

class Window: 
    def __init__(self, width=800, height=600):
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Window")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.is_running = False  # Indicates whether the window is running
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle window close event
    
    def run(self):
        self.is_running = True  # Set to True when the window starts running
        self.root.mainloop()
    
    def redraw(self):
        if self.is_running:
            self.canvas.update_idletasks()
            self.canvas.update()
        else:
            print("Window is not running. Cannot redraw.")
        # Call the redraw method to update the canvas
    
    def wait_on_close(self):
        if self.is_running:
            self.root.wait_window(self.root)
            self.redraw()
        # Wait for the window to close
        else:
            print("Window is not running. Cannot wait on close.")
    
    def on_close(self):
        self.is_running = False
        self.root.destroy()
        self.root.quit()

def main():
    window = Window(800, 600) # Create a window with specified dimensions
    window.run()  # Start the window
    window.wait_on_close()  # Wait for the window to close

main()