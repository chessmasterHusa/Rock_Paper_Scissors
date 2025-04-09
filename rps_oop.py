import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path


class RockLabel(tk.Label):

    def __init__(
        self,
        window: tk.Misc,
        image_dir: Path,
        image_name: str
    ):
        self.image = ImageTk.PhotoImage(
            Image.open(image_dir / image_name)
        )

        super().__init__(
            master=window, image=self.image
        )

    def set_grid(
        self, row: int, column: int
    ):
        self.grid(row=row, column=column)



class RockPaperScissors(tk.Tk):

    def __init__(
        self, 
        image_dir: Path 
    ):
        super().__init__()

        self.lbl_computer = RockLabel(
            window=self, image_dir=image_dir, image_name="unknown.jpg"
        )
        self.lbl_computer.set_grid(row=2, column=1)

        self.lbl_player = RockLabel(
            window=self, image_dir=image_dir, image_name="unknown.jpg"
        )
        self.lbl_player.set_grid(row=3, column=1)

    def show(self):
        self.mainloop()
    

    def escape(self):
        self.bind("<Escape>", lambda x: self.quit())


if __name__ == "__main__":

    image_dir = Path(__file__).parent / "images"

    app = RockPaperScissors(
        image_dir=image_dir
    )
    
    app.escape()
    app.show()