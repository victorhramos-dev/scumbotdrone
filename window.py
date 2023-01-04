import time
import webbrowser
import pyautogui
import pywinauto
import ocr


class ScumWindow:
    x0, y0, x1, y1 = 0, 0, 0, 0

    def open_game(self):
        webbrowser.open("steam://rungameid/513710//")

        while (True):
            try:
                self.focus_game()
                time.sleep(0.1)
                if (pyautogui.locateOnScreen(ocr.resource_path('assets/exit_game.png'), confidence=0.6, region=(self.x0, self.y0, self.x1-self.x0, self.y1-self.y0))):
                    break
            except:
                pass
        return

    def connect_server(self):
        return
    
    
    def find_game(self):
        try:
            app = pywinauto.application.Application()
            app.connect(title="SCUM  ")
            appwindow = app.top_window()
            rect = appwindow.rectangle()
            self.x0, self.y0, self.x1, self.y1 = rect.left, rect.top, rect.right, rect.bottom
            return True
        except:
            return False
    
    def focus_game(self):
        try:
            app = pywinauto.application.Application()
            app.connect(title="SCUM  ")
            appwindow = app.top_window()
            appwindow.set_focus()
            rect = appwindow.rectangle()
            self.x0, self.y0, self.x1, self.y1 = rect.left, rect.top, rect.right, rect.bottom
            appwindow.move_window(x=self.x0, y=self.y0, width=1024, height=768, repaint=True)
            rect = appwindow.rectangle()
            self.x0, self.y0, self.x1, self.y1 = rect.left, rect.top, rect.right, rect.bottom
                     
            return True
        except:
            return False
    
if __name__ == "__main__":
    #app = pywinauto.application.Application()
    #app.connect(title="SCUM  ")
    #appwindow = app.top_window()
    #appwindow.set_focus()
    #print(appwindow.rectangle())
    sw = ScumWindow().focus_game()