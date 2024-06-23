import pyxel
import json

MUSIC_FILE = "music"

class Test:
    def __init__(self):
        pyxel.init(width=160, height=100, title="TestWegit")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

Test()
