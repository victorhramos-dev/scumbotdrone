import time

import pyautogui

import ocr
import window


class Drone:
    sw = window.ScumWindow()

    def go_home(self):
        # {X=-278811.062 Y=308753.781 Z=83165.383|P=0.000000 Y=0.000000 R=0.000000}
        self.send_message(
            '#teleport {X=-278811.062 Y=308753.781 Z=83165.383|P=0.000000 Y=0.000000 R=0.000000}')

    def send_message(self, message, scope=None):
        self.sw.focus_game()
        time.sleep(0.3)

        loc = pyautogui.locateOnScreen(ocr.resource_path(
            'assets/mute.png'), grayscale=True, confidence=0.7, region=(self.sw.x0 + 23, self.sw.y0 + 348, 40, 25))

        if loc is None:
            pyautogui.press('t')
            time.sleep(0.1)

        if scope is not None:
            current_scope = ocr.ocr(
                {'x': self.sw.x0 + 265, 'y': self.sw.y0 + 350, 'w': 42, 'h': 23}).lower()
            scope = scope.lower()

            if current_scope != scope:
                if current_scope == "admin" and scope == "local":
                    pyautogui.press('TAB')
                elif current_scope == "local" and scope == "global":
                    pyautogui.press('TAB')
                elif current_scope == "global" and scope == "admin":
                    pyautogui.press('TAB')
                elif current_scope == "local" and scope == "admin":
                    pyautogui.press('TAB')
                    pyautogui.press('TAB')
                elif current_scope == "admin" and scope == "global":
                    pyautogui.press('TAB')
                    pyautogui.press('TAB')
                elif current_scope == "global" and scope == "local":
                    pyautogui.press('TAB')
                    pyautogui.press('TAB')

        pyautogui.typewrite(message)
        time.sleep(0.1)
        pyautogui.press('enter')
        pyautogui.press('enter')


if __name__ == "__main__":
    drone = Drone()
    drone.sw.open_game()
