import pyxel as pl
from objects import Objects as ob
import sys, json

class main :
    def __init__(self):
        pl.init(width=128, height=128, title="adventure", fps=60, display_scale=5)
        with open(f'music.json', 'rt') as fin:
            self.music = json.loads(fin.read())
        pl.load('grafic.pyxres')
        self.set_up()
        pl.run(self.update, self.draw)

    def def_charactor(self, size): # 大文字と小文字の定義群
        if size == 0:
            self.change_case = "Lowercase"
            self.A = "A"
            self.B = "B"
            self.C = "C"
            self.D = "D"
            self.E = "E"
            self.F = "F"
            self.G = "G"
            self.H = "H"
            self.I = "I"
            self.J = "J"
            self.K = "K"
            self.L = "L"
            self.M = "M"
            self.N = "N"
            self.O = "O"
            self.P = "P"
            self.Q = "Q"
            self.R = "R"
            self.S = "S"
            self.T = "T"
            self.U = "U"
            self.V = "V"
            self.W = "W"
            self.X = "X"
            self.Y = "Y"
            self.Z = "Z"
        elif size == 1:
            self.change_case = "Uppercase"
            self.A = "a"
            self.B = "b"
            self.C = "c"
            self.D = "d"
            self.E = "e"
            self.F = "f"
            self.G = "g"
            self.H = "h"
            self.I = "i"
            self.J = "j"
            self.K = "k"
            self.L = "l"
            self.M = "m"
            self.N = "n"
            self.O = "o"
            self.P = "p"
            self.Q = "q"
            self.R = "r"
            self.S = "s"
            self.T = "t"
            self.U = "u"
            self.V = "v"
            self.W = "w"
            self.X = "x"
            self.Y = "y"
            self.Z = "z"

    def set_up(self):
        global BGM_LIST
        BGM_LIST = [0]
        self.scene = 0
        self.logo = ob(-100, 48, 0, 16, 32, 32, True)
        self.arrow_place = 60
        self.arrow_place_high = 75
        self.option_language = 50
        self.language_txt = "English"
        self.language_color = pl.COLOR_WHITE
        self.arrow1_color = pl.COLOR_NAVY
        self.arrow2_color = pl.COLOR_WHITE
        self.back_color = pl.COLOR_WHITE
        self.control = 1
        self.change_case = "Lowercase"
        self.lst = ["", "", "", "", "", "", "", "", "", ""]
        self.def_charactor(0)

    def add_item(self, item): # namelist を 10 文字にする関数
        lis = []
        for i in self.lst:
            if i != "":
                lis.append(i)
        if len(lis) > 0 and item == "":
            lis.pop(-1)
        elif len(lis) != 10:
            lis.append(item)
        else:
            pl.play(3, 7)
        self.lst = lis
        for i in range(10 - len(self.lst)):
            self.lst.append("")

    def move(self): # 動作系の処理
        if self.scene == 1: # ゲーム初期画面
            if (pl.btnp(pl.KEY_W) or pl.btnp(pl.KEY_UP)): # arrow_up
                if self.arrow_place == 60:
                    self.arrow_place = 90
                    pl.play(3, 5)
                else:
                    self.arrow_place -= 10
                    pl.play(3, 5)
            elif(pl.btnp(pl.KEY_S) or pl.btnp(pl.KEY_DOWN)): # arrow_down
                if self.arrow_place == 90:
                    self.arrow_place = 60
                    pl.play(3, 5)
                else:
                    self.arrow_place += 10
                    pl.play(3, 5)
            elif pl.btnp(pl.KEY_RETURN):
                if self.arrow_place == 60:
                    pl.play(3, 6) # New Game
                    self.arrow_place = 15
                    self.arrow_place_high = 25
                    self.lst = ["", "", "", "", "", "", "", "", "", ""]
                    self.scene = 3
                elif self.arrow_place == 70:
                    pl.play(3, 6) # Continue
                    self.arrow_place = 15
                    self.arrow_place_high = 25
                    self.lst = ["", "", "", "", "", "", "", "", "", ""]
                    self.scene = 2.5
                elif self.arrow_place == 80: # Option
                    pl.play(3, 6)
                    self.arrow_place = 90
                    self.scene = 2
                elif self.arrow_place == 90:
                    pl.play(3, 6)
                    sys.exit() # Quit
        elif self.scene == 2: # ゲーム初期画面(option)
            if (pl.btnp(pl.KEY_A) or pl.btnp(pl.KEY_LEFT)): # arrow_left
                if self.control == 1:
                    pl.play(3, 7)
                else:
                    pl.play(3, 5)
                    self.language_txt = "English"
                    self.language_color = pl.COLOR_WHITE
                    self.arrow1_color = pl.COLOR_NAVY
                    self.arrow2_color = pl.COLOR_WHITE
                    self.back_color = pl.COLOR_WHITE
                    self.option_language = 50
                    self.control = 1
            elif (pl.btnp(pl.KEY_D) or pl.btnp(pl.KEY_RIGHT)): # arrow_right
                if self.control == 2:
                    pl.play(3, 7)
                else:
                    pl.play(3, 5)
                    self.language_txt = " Romaji"
                    self.arrow1_color = pl.COLOR_WHITE
                    self.arrow2_color = pl.COLOR_NAVY
                    self.back_color = pl.COLOR_NAVY
                    self.option_language = 49
                    self.control = 2
            elif pl.btnp(pl.KEY_RETURN):
                if self.arrow_place == 90 and self.back_color == pl.COLOR_WHITE:
                    pl.play(3, 6)
                    self.scene = 1
                    self.arrow_place = 60
                    self.arrow_ok = False
                else:
                    pl.play(3, 7)
        elif self.scene == 2.5: # continue
            if (pl.btnp(pl.KEY_A) or pl.btnp(pl.KEY_LEFT)): # arrow_left
                if self.arrow_place == 15: # 上段、下段において左にいけなくする
                    pl.play(3, 7)
                elif self.arrow_place_high == 75 or self.arrow_place_high == 90: # 下段での左移動
                    self.arrow_place -= 55
                    pl.play(3, 5)
                else:
                    self.arrow_place -= 15 # 上段での左移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_D) or pl.btnp(pl.KEY_RIGHT)): # arrow_right
                if self.arrow_place == 105 or (self.arrow_place_high == 55 and self.arrow_place == 75) or (self.arrow_place == 70 and (self.arrow_place_high == 75 or self.arrow_place_high == 90)): # 上段、下段において右にいけなくする
                    pl.play(3, 7)
                elif self.arrow_place_high == 75 or self.arrow_place_high == 90: # 下段での右移動
                    self.arrow_place += 55
                    pl.play(3, 5)
                else:
                    self.arrow_place += 15 # 上段での左移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_W) or pl.btnp(pl.KEY_UP)): # arrow_up
                if  self.arrow_place_high == 25: # 上段での上移動の規制
                    pl.play(3, 7)
                elif self.arrow_place_high == 75: # 下段->上段の動作
                    self.arrow_place = 15
                    self.arrow_place_high = 55
                    pl.play(3, 5)
                elif self.arrow_place_high == 90: # 下段->下段の動作
                    self.arrow_place_high = 75
                    pl.play(3, 5)
                else:
                    self.arrow_place_high -= 10 # 上段における上移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_S) or pl.btnp(pl.KEY_DOWN)): # arrow_down
                if self.arrow_place_high == 90:# 下段での下移動の規制
                    pl.play(3, 7)
                elif self.arrow_place_high == 75: # 下段->下段の動作
                    self.arrow_place_high = 90
                    pl.play(3, 5)
                elif self.arrow_place_high == 45 and (self.arrow_place == 105 or self.arrow_place == 90): # T, U から Z に降りる動作
                    self.arrow_place = 75
                    self.arrow_place_high = 55
                    pl.play(3, 5)
                elif self.arrow_place_high == 55: # 上段->下段の動作
                    self.arrow_place = 15
                    self.arrow_place_high = 75
                    pl.play(3, 5)
                else:
                    self.arrow_place_high += 10 # 上段における下移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_BACKSPACE)):
                self.add_item("")
                pl.play(3, 5)
            elif (pl.btnp(pl.KEY_RETURN)): # 文字入力処理
                if (self.arrow_place == 15 and self.arrow_place_high == 25):
                    self.add_item(self.A)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 25):
                    self.add_item(self.B)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 25):
                    self.add_item(self.C)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 25):
                    self.add_item(self.D)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 25):
                    self.add_item(self.E)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 25):
                    self.add_item(self.F)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 25):
                    self.add_item(self.G)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 35):
                    self.add_item(self.H)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 35):
                    self.add_item(self.I)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 35):
                    self.add_item(self.J)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 35):
                    self.add_item(self.K)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 35):
                    self.add_item(self.L)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 35):
                    self.add_item(self.M)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 35):
                    self.add_item(self.N)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 45):
                    self.add_item(self.O)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 45):
                    self.add_item(self.P)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 45):
                    self.add_item(self.Q)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 45):
                    self.add_item(self.R)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 45):
                    self.add_item(self.S)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 45):
                    self.add_item(self.T)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 45):
                    self.add_item(self.U)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 55):
                    self.add_item(self.V)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 55):
                    self.add_item(self.W)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 55):
                    self.add_item(self.X)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 55):
                    self.add_item(self.Y)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 55):
                    self.add_item(self.Z)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 75): # backspce
                    self.add_item("")
                    pl.play(3, 5)
                elif (self.arrow_place == 70 and self.arrow_place_high == 75): # 変換
                    if self.change_case == "Lowercase" :
                        self.def_charactor(1)
                        pl.play(3, 6)
                    else:
                        self.def_charactor(0)
                        pl.play(3, 6)
                elif (self.arrow_place == 70 and self.arrow_place_high == 90): # decide
                    if "".join(self.lst) == "":
                        pl.play(3, 7)
                    if len("".join(self.lst)) <= 1:
                        self.name_place = 64
                    elif len("".join(self.lst)) <= 3:
                        self.name_place = 60
                    elif len("".join(self.lst)) <= 5:
                        self.name_place = 56
                    elif len("".join(self.lst)) <= 7:
                        self.name_place = 52
                    elif len("".join(self.lst)) <= 9:
                        self.name_place = 48
                    else:
                        self.name_place = 44
                    if  "".join(self.lst) == "Apple": # Code: Apple
                        self.check_name_txt = "Is this code okay?"
                        self.check_name_place = 28
                        pl.play(3, 6)
                        self.arrow_place = 30
                        self.arrow_place_high = 70
                        self.scene = 2.51
                    else:
                        pl.play(3, 7)
                elif (self.arrow_place == 15 and self.arrow_place_high == 90): # back
                    pl.play(3, 6)
                    self.arrow_place = 60
                    self.scene = 1
        elif self.scene == 2.51: # Code確認画面
            if (pl.btnp(pl.KEY_A) or pl.btnp(pl.KEY_LEFT)): # arrow_left
                if self.arrow_place == 30:
                    pl.play(3, 7)
                else:
                    self.arrow_place -= 50
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_D) or pl.btnp(pl.KEY_RIGHT)): # arrow_right
                if self.arrow_place == 80:
                    pl.play(3, 7)
                else:
                    self.arrow_place += 50
                    pl.play(3, 5)
            elif pl.btnp(pl.KEY_RETURN):
                if self.arrow_place == 30: # no
                    pl.play(3, 6)
                    self.arrow_place = 15
                    self.arrow_place_high = 25
                    self.scene = 2.5
                elif self.arrow_place == 80: # ok
                    self.check_name_txt = "Sorry! Fanction of continue"
                    self.check_name_txt2 = "is not available yet!"
                    self.arrow_place = 55
                    pl.play(3, 6)
                    self.scene = 2.52
        elif self.scene == 2.52: # Codeないよ画面
            if pl.btnp(pl.KEY_RETURN):
                pl.play(3, 6)
                self.arrow_place = 15
                self.arrow_place_high = 25
                self.scene = 2.5
        elif self.scene == 3: # New Game
            if (pl.btnp(pl.KEY_A) or pl.btnp(pl.KEY_LEFT)): # arrow_left
                if self.arrow_place == 15: # 上段、下段において左にいけなくする
                    pl.play(3, 7)
                elif self.arrow_place_high == 75 or self.arrow_place_high == 90: # 下段での左移動
                    self.arrow_place -= 55
                    pl.play(3, 5)
                else:
                    self.arrow_place -= 15 # 上段での左移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_D) or pl.btnp(pl.KEY_RIGHT)): # arrow_right
                if self.arrow_place == 105 or (self.arrow_place_high == 55 and self.arrow_place == 75) or (self.arrow_place == 70 and (self.arrow_place_high == 75 or self.arrow_place_high == 90)): # 上段、下段において右にいけなくする
                    pl.play(3, 7)
                elif self.arrow_place_high == 75 or self.arrow_place_high == 90: # 下段での右移動
                    self.arrow_place += 55
                    pl.play(3, 5)
                else:
                    self.arrow_place += 15 # 上段での左移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_W) or pl.btnp(pl.KEY_UP)): # arrow_up
                if  self.arrow_place_high == 25: # 上段での上移動の規制
                    pl.play(3, 7)
                elif self.arrow_place_high == 75: # 下段->上段の動作
                    self.arrow_place = 15
                    self.arrow_place_high = 55
                    pl.play(3, 5)
                elif self.arrow_place_high == 90: # 下段->下段の動作
                    self.arrow_place_high = 75
                    pl.play(3, 5)
                else:
                    self.arrow_place_high -= 10 # 上段における上移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_S) or pl.btnp(pl.KEY_DOWN)): # arrow_down
                if self.arrow_place_high == 90:# 下段での下移動の規制
                    pl.play(3, 7)
                elif self.arrow_place_high == 75: # 下段->下段の動作
                    self.arrow_place_high = 90
                    pl.play(3, 5)
                elif self.arrow_place_high == 45 and (self.arrow_place == 105 or self.arrow_place == 90): # T, U から Z に降りる動作
                    self.arrow_place = 75
                    self.arrow_place_high = 55
                    pl.play(3, 5)
                elif self.arrow_place_high == 55: # 上段->下段の動作
                    self.arrow_place = 15
                    self.arrow_place_high = 75
                    pl.play(3, 5)
                else:
                    self.arrow_place_high += 10 # 上段における下移動
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_BACKSPACE)):
                self.add_item("")
                pl.play(3, 5)
            elif (pl.btnp(pl.KEY_RETURN)): # 文字入力処理
                if (self.arrow_place == 15 and self.arrow_place_high == 25):
                    self.add_item(self.A)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 25):
                    self.add_item(self.B)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 25):
                    self.add_item(self.C)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 25):
                    self.add_item(self.D)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 25):
                    self.add_item(self.E)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 25):
                    self.add_item(self.F)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 25):
                    self.add_item(self.G)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 35):
                    self.add_item(self.H)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 35):
                    self.add_item(self.I)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 35):
                    self.add_item(self.J)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 35):
                    self.add_item(self.K)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 35):
                    self.add_item(self.L)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 35):
                    self.add_item(self.M)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 35):
                    self.add_item(self.N)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 45):
                    self.add_item(self.O)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 45):
                    self.add_item(self.P)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 45):
                    self.add_item(self.Q)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 45):
                    self.add_item(self.R)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 45):
                    self.add_item(self.S)
                    pl.play(3, 5)
                elif (self.arrow_place == 90 and self.arrow_place_high == 45):
                    self.add_item(self.T)
                    pl.play(3, 5)
                elif (self.arrow_place == 105 and self.arrow_place_high == 45):
                    self.add_item(self.U)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 55):
                    self.add_item(self.V)
                    pl.play(3, 5)
                elif (self.arrow_place == 30 and self.arrow_place_high == 55):
                    self.add_item(self.W)
                    pl.play(3, 5)
                elif (self.arrow_place == 45 and self.arrow_place_high == 55):
                    self.add_item(self.X)
                    pl.play(3, 5)
                elif (self.arrow_place == 60 and self.arrow_place_high == 55):
                    self.add_item(self.Y)
                    pl.play(3, 5)
                elif (self.arrow_place == 75 and self.arrow_place_high == 55):
                    self.add_item(self.Z)
                    pl.play(3, 5)
                elif (self.arrow_place == 15 and self.arrow_place_high == 75): # backspce
                    self.add_item("")
                    pl.play(3, 5)
                elif (self.arrow_place == 70 and self.arrow_place_high == 75): # 変換
                    if self.change_case == "Lowercase" :
                        self.def_charactor(1)
                        pl.play(3, 6)
                    else:
                        self.def_charactor(0)
                        pl.play(3, 6)
                elif (self.arrow_place == 70 and self.arrow_place_high == 90): # decide
                    if "".join(self.lst) == "":
                        pl.play(3, 7)
                    if len("".join(self.lst)) <= 1:
                        self.name_place = 64
                    elif len("".join(self.lst)) <= 3:
                        self.name_place = 60
                    elif len("".join(self.lst)) <= 5:
                        self.name_place = 56
                    elif len("".join(self.lst)) <= 7:
                        self.name_place = 52
                    elif len("".join(self.lst)) <= 9:
                        self.name_place = 48
                    else:
                        self.name_place = 44
                    if "".join(self.lst) == "": # Empty name
                        self.check_name_txt = "Empty name..."
                        self.check_name_place = 40
                    elif "".join(self.lst) == "admin": # Admin
                        self.check_name_txt = "Do you want to run as admin?"
                        self.check_name_place = 8
                    elif "".join(self.lst) == "challenger": # challenger
                        self.check_name_txt = "You want a challenge?"
                        self.check_name_place = 24
                    else: # Nomal name
                        self.check_name_txt = "Is this name okay?"
                        self.check_name_place = 28
                    pl.play(3, 6)
                    self.arrow_place = 30
                    self.arrow_place_high = 70
                    self.scene = 3.5
                elif (self.arrow_place == 15 and self.arrow_place_high == 90): # back
                    pl.play(3, 6)
                    self.arrow_place = 60
                    self.scene = 1
        elif self.scene == 3.5: # 名前確認画面
            if (pl.btnp(pl.KEY_A) or pl.btnp(pl.KEY_LEFT)): # arrow_left
                if self.arrow_place == 30:
                    pl.play(3, 7)
                else:
                    self.arrow_place -= 50
                    pl.play(3, 5)
            elif (pl.btnp(pl.KEY_D) or pl.btnp(pl.KEY_RIGHT)): # arrow_right
                if self.arrow_place == 80:
                    pl.play(3, 7)
                else:
                    self.arrow_place += 50
                    pl.play(3, 5)
            elif pl.btnp(pl.KEY_RETURN):
                if self.arrow_place == 30: # no
                    pl.play(3, 6)
                    self.arrow_place = 15
                    self.arrow_place_high = 25
                    self.scene = 3
                elif self.arrow_place == 80: # ok
                    BGM_LIST[0] = 2
                    pl.play(3, 6)
                    self.scene = 4
        elif self.scene == 4:
            pass

    def play_bgm(self):
        if pl.frame_count == 175 and BGM_LIST[0] == 1:
            for ch, sound in enumerate(self.music):
                pl.sound(ch).set(*sound)
                pl.play(ch, ch, loop=True)
        elif BGM_LIST[0] == 2:
            pl.stop()

    def update(self):
        """ロゴの表示"""
        if pl.frame_count < 74 and self.scene == 0:
            self.logo.x += 2
        if pl.frame_count == 55 and self.scene == 0:
            pl.play(3, 4)
        if pl.frame_count == 160 and self.scene == 0:
            self.logo.plot = False
            BGM_LIST[0] = 1
        """初期画面の表示"""
        if pl.frame_count == 170 and self.scene == 0:
            self.scene = 1
        """動きの管理"""
        self.move()
        """BGM管理"""
        self.play_bgm()

    def draw(self):
        pl.cls(0)
        if self.logo.plot:
            pl.blt(self.logo.x, self.logo.y, 0,
                    self.logo.img_x, self.logo.img_y,
                    self.logo.img_w, self.logo.img_h,0)
        # pyxel.blt(x, y, img, u, v, w, h, [col])  (x, y)の位置にimage(img)の(u, v)から(u+w,v+h)まで[col]で貼り付ける
        elif self.scene == 1: # ゲーム初期画面
            pl.blt(15, 80, 0, 0, 0, 16, 16, pl.COLOR_GRAY) # 主人公
            pl.text(36, 35, "SUPER ADVENTURE", pl.COLOR_WHITE) # super adventure
            pl.text(50, 60, "New Game", pl.COLOR_WHITE)
            pl.text(50, 70, "Continue", pl.COLOR_WHITE)
            pl.text(50, 80, "Option", pl.COLOR_WHITE)
            pl.text(50, 90, "Quit", pl.COLOR_WHITE)
            pl.text(45, self.arrow_place, ">", pl.COLOR_WHITE)
        elif self.scene == 2: # ゲーム初期画面(option)
            pl.text(36, 35, "SUPER ADVENTURE", pl.COLOR_WHITE) # super adventure
            pl.text(50, 60, "Language", pl.COLOR_WHITE)
            pl.text(self.option_language, 70, self.language_txt, self.language_color)
            pl.text(55, 90, "Back", self.back_color)
            pl.text(42, 70, "<", self.arrow1_color)
            pl.text(79, 70, ">", self.arrow2_color)
            pl.text(50, self.arrow_place, ">", pl.COLOR_WHITE)
        elif self.scene == 2.5: # continue
            pl.text(self.arrow_place, self.arrow_place_high, ">", pl.COLOR_WHITE)
            pl.text(5, 10, "Code:", pl.COLOR_WHITE)
            pl.text(35, 10, self.lst[0], pl.COLOR_WHITE)
            pl.text(40, 10, self.lst[1], pl.COLOR_WHITE)
            pl.text(45, 10, self.lst[2], pl.COLOR_WHITE)
            pl.text(50, 10, self.lst[3], pl.COLOR_WHITE)
            pl.text(55, 10, self.lst[4], pl.COLOR_WHITE)
            pl.text(60, 10, self.lst[5], pl.COLOR_WHITE)
            pl.text(65, 10, self.lst[6], pl.COLOR_WHITE)
            pl.text(70, 10, self.lst[7], pl.COLOR_WHITE)
            pl.text(75, 10, self.lst[8], pl.COLOR_WHITE)
            pl.text(80, 10, self.lst[9], pl.COLOR_WHITE)
            pl.text(20, 25, self.A, pl.COLOR_WHITE)
            pl.text(35, 25, self.B, pl.COLOR_WHITE)
            pl.text(50, 25, self.C, pl.COLOR_WHITE)
            pl.text(65, 25, self.D, pl.COLOR_WHITE)
            pl.text(80, 25, self.E, pl.COLOR_WHITE)
            pl.text(95, 25, self.F, pl.COLOR_WHITE)
            pl.text(110, 25, self.G, pl.COLOR_WHITE)
            pl.text(20, 35, self.H, pl.COLOR_WHITE)
            pl.text(35, 35, self.I, pl.COLOR_WHITE)
            pl.text(50, 35, self.J, pl.COLOR_WHITE)
            pl.text(65, 35, self.K, pl.COLOR_WHITE)
            pl.text(80, 35, self.L, pl.COLOR_WHITE)
            pl.text(95, 35, self.M, pl.COLOR_WHITE)
            pl.text(110, 35, self.N, pl.COLOR_WHITE)
            pl.text(20, 45, self.O, pl.COLOR_WHITE)
            pl.text(35, 45, self.P, pl.COLOR_WHITE)
            pl.text(50, 45, self.Q, pl.COLOR_WHITE)
            pl.text(65, 45, self.R, pl.COLOR_WHITE)
            pl.text(80, 45, self.S, pl.COLOR_WHITE)
            pl.text(95, 45, self.T, pl.COLOR_WHITE)
            pl.text(110, 45, self.U, pl.COLOR_WHITE)
            pl.text(20, 55, self.V, pl.COLOR_WHITE)
            pl.text(35, 55, self.W, pl.COLOR_WHITE)
            pl.text(50, 55, self.X, pl.COLOR_WHITE)
            pl.text(65, 55, self.Y, pl.COLOR_WHITE)
            pl.text(80, 55, self.Z, pl.COLOR_WHITE)
            pl.text(20, 75, "BackSpace", pl.COLOR_WHITE)
            pl.text(75, 75, self.change_case, pl.COLOR_WHITE)
            pl.text(75, 90, "Decide", pl.COLOR_WHITE)
            pl.text(20, 90, "Back", pl.COLOR_WHITE)
#            pl.text(10, 25, str(self.arrow_place), pl.COLOR_WHITE)
#            pl.text(10, 35, str(self.arrow_place_high), pl.COLOR_WHITE)
        elif self.scene == 2.51: # Code確認画面
            pl.text(self.arrow_place, self.arrow_place_high, ">", pl.COLOR_WHITE)
            pl.text(self.check_name_place, 30, self.check_name_txt, pl.COLOR_WHITE)
            pl.text(self.name_place, 50, "".join(self.lst), pl.COLOR_WHITE)
            pl.text(35, 70, "NO", pl.COLOR_WHITE)
            pl.text(85, 70, "OK", pl.COLOR_WHITE)
        elif self.scene == 2.52: # Codeないよ画面
            pl.text(self.arrow_place, self.arrow_place_high, ">", pl.COLOR_WHITE)
            pl.text(12, 35, self.check_name_txt, pl.COLOR_WHITE)
            pl.text(24, 45, self.check_name_txt2, pl.COLOR_WHITE)
            pl.text(60, 70, "OK", pl.COLOR_WHITE)
        elif self.scene == 3: # continue
            pl.text(self.arrow_place, self.arrow_place_high, ">", pl.COLOR_WHITE)
            pl.text(5, 10, "Name:", pl.COLOR_WHITE)
            pl.text(35, 10, self.lst[0], pl.COLOR_WHITE)
            pl.text(40, 10, self.lst[1], pl.COLOR_WHITE)
            pl.text(45, 10, self.lst[2], pl.COLOR_WHITE)
            pl.text(50, 10, self.lst[3], pl.COLOR_WHITE)
            pl.text(55, 10, self.lst[4], pl.COLOR_WHITE)
            pl.text(60, 10, self.lst[5], pl.COLOR_WHITE)
            pl.text(65, 10, self.lst[6], pl.COLOR_WHITE)
            pl.text(70, 10, self.lst[7], pl.COLOR_WHITE)
            pl.text(75, 10, self.lst[8], pl.COLOR_WHITE)
            pl.text(80, 10, self.lst[9], pl.COLOR_WHITE)
            pl.text(20, 25, self.A, pl.COLOR_WHITE)
            pl.text(35, 25, self.B, pl.COLOR_WHITE)
            pl.text(50, 25, self.C, pl.COLOR_WHITE)
            pl.text(65, 25, self.D, pl.COLOR_WHITE)
            pl.text(80, 25, self.E, pl.COLOR_WHITE)
            pl.text(95, 25, self.F, pl.COLOR_WHITE)
            pl.text(110, 25, self.G, pl.COLOR_WHITE)
            pl.text(20, 35, self.H, pl.COLOR_WHITE)
            pl.text(35, 35, self.I, pl.COLOR_WHITE)
            pl.text(50, 35, self.J, pl.COLOR_WHITE)
            pl.text(65, 35, self.K, pl.COLOR_WHITE)
            pl.text(80, 35, self.L, pl.COLOR_WHITE)
            pl.text(95, 35, self.M, pl.COLOR_WHITE)
            pl.text(110, 35, self.N, pl.COLOR_WHITE)
            pl.text(20, 45, self.O, pl.COLOR_WHITE)
            pl.text(35, 45, self.P, pl.COLOR_WHITE)
            pl.text(50, 45, self.Q, pl.COLOR_WHITE)
            pl.text(65, 45, self.R, pl.COLOR_WHITE)
            pl.text(80, 45, self.S, pl.COLOR_WHITE)
            pl.text(95, 45, self.T, pl.COLOR_WHITE)
            pl.text(110, 45, self.U, pl.COLOR_WHITE)
            pl.text(20, 55, self.V, pl.COLOR_WHITE)
            pl.text(35, 55, self.W, pl.COLOR_WHITE)
            pl.text(50, 55, self.X, pl.COLOR_WHITE)
            pl.text(65, 55, self.Y, pl.COLOR_WHITE)
            pl.text(80, 55, self.Z, pl.COLOR_WHITE)
            pl.text(20, 75, "BackSpace", pl.COLOR_WHITE)
            pl.text(75, 75, self.change_case, pl.COLOR_WHITE)
            pl.text(75, 90, "Decide", pl.COLOR_WHITE)
            pl.text(20, 90, "Back", pl.COLOR_WHITE)
#            pl.text(10, 10, str(self.arrow_place), pl.COLOR_WHITE)
#            pl.text(10, 20, str(self.arrow_place_high), pl.COLOR_WHITE)
        elif self.scene == 3.5:
            pl.text(self.arrow_place, self.arrow_place_high, ">", pl.COLOR_WHITE)
            pl.text(self.check_name_place, 30, self.check_name_txt, pl.COLOR_WHITE)
            pl.text(self.name_place, 50, "".join(self.lst), pl.COLOR_WHITE)
            pl.text(35, 70, "NO", pl.COLOR_WHITE)
            pl.text(85, 70, "OK", pl.COLOR_WHITE)
#            pl.text(10, 10, str(self.arrow_place), pl.COLOR_WHITE)
#            pl.text(10, 20, str(self.arrow_place_high), pl.COLOR_WHITE)
        elif self.scene == 4:
            pl.bltm(0, 0, 0, 0, 0, 128, 128)
            # 初手城内部からのスタート(王室) あとでキングとクイーン、王兵も作る
            # 動作系は基本的に唯一の座標を参照する 家具系もちゃんと描画 object描画関数でも良い

main()
