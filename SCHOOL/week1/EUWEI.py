import pygame
import random

# --- 顏色定義 ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (220, 220, 220)
DARK_GRAY = (100, 100, 100)
RED = (255, 50, 50)
BLUE = (50, 50, 255)
GREEN = (50, 200, 50)
YELLOW = (255, 215, 0)
ORANGE = (255, 165, 0)
PURPLE = (160, 32, 240)

# --- 遊戲設定 ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
MAX_ATTEMPTS = 8
COLORS = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE]

class GameState:
    MENU = "MENU"
    MASTERMIND = "MASTERMIND"
    ACHIEVEMENTS = "ACHIEVEMENTS"

# --- 成就管理 ---
achievements = {
    "Mastermind Master": False  # 5次內猜出
}

def draw_text(surface, text, pos, font, color=BLACK, center=False):
    img = font.render(text, True, color)
    if center:
        rect = img.get_rect(center=pos)
        surface.blit(img, rect)
    else:
        surface.blit(img, pos)

# --- 珠璣妙算 類別 ---
class Mastermind:
    def __init__(self):
        self.secret = [random.choice(COLORS) for _ in range(4)]
        self.guesses = [] # 儲存格式: [color, color, color, color]
        self.feedback = [] # 儲存格式: (T, F)
        self.current_guess = []
        self.game_over = False
        self.won = False

    def check_guess(self):
        if len(self.current_guess) < 4 or self.game_over:
            return
        
        t_count = 0
        f_count = 0
        temp_secret = list(self.secret)
        temp_guess = list(self.current_guess)

        # 算 T (位置與顏色皆對)
        for i in range(3, -1, -1):
            if temp_guess[i] == temp_secret[i]:
                t_count += 1
                temp_secret.pop(i)
                temp_guess.pop(i)
        
        # 算 F (顏色對但位置錯)
        for g in temp_guess:
            if g in temp_secret:
                f_count += 1
                temp_secret.remove(g)
        
        self.feedback.append((t_count, f_count))
        self.guesses.append(list(self.current_guess))
        self.current_guess = []

        if t_count == 4:
            self.won = True
            self.game_over = True
            # 檢查成就
            if len(self.guesses) <= 5:
                achievements["Mastermind Master"] = True
        elif len(self.guesses) >= MAX_ATTEMPTS:
            self.game_over = True

    def draw(self, screen, font):
        screen.fill(WHITE)
        
        # --- 左側歷史區 (對稱排列) ---
        margin_left = 60
        row_h = 60
        row_w = 320
        for i in range(MAX_ATTEMPTS):
            y_pos = 60 + i * (row_h + 10)
            # 黑色矩形框框
            pygame.draw.rect(screen, BLACK, (margin_left, y_pos, row_w, row_h), 2)
            
            # 繪製已有的猜測
            if i < len(self.guesses):
                for j, color in enumerate(self.guesses[i]):
                    pygame.draw.circle(screen, color, (margin_left + 40 + j*50, y_pos + 30), 18)
                # 繪製 T/F 反饋
                t, f = self.feedback[i]
                draw_text(screen, f"T:{t} F:{f}", (margin_left + 240, y_pos + 18), font)

        # --- 右側參考區 (Peg Reference) ---
        ref_x = 450
        draw_text(screen, "[ Color Reference ]", (ref_x, 60), font, DARK_GRAY)
        for i, color in enumerate(COLORS):
            pygame.draw.circle(screen, color, (ref_x + 30 + i*45, 110), 15)
            draw_text(screen, str(i+1), (ref_x + 25 + i*45, 130), font, DARK_GRAY)

        # --- 右下角輸入區 ---
        input_box_rect = (450, 400, 280, 100)
        pygame.draw.rect(screen, GRAY, input_box_rect, border_radius=10)
        draw_text(screen, "Your Input:", (460, 410), font)
        for j, color in enumerate(self.current_guess):
            pygame.draw.circle(screen, color, (490 + j*50, 460), 18)

        # --- 遊戲結束處理 ---
        if self.game_over:
            msg = "VICTORY!" if self.won else "GAME OVER"
            color = GREEN if self.won else RED
            draw_text(screen, msg, (450, 250), font, color)
            
            # 公布答案
            draw_text(screen, "Secret was:", (450, 290), font)
            for j, color in enumerate(self.secret):
                pygame.draw.circle(screen, color, (490 + j*50, 335), 18)
            
            draw_text(screen, "Press R to Restart / M for Menu", (450, 530), font, DARK_GRAY)

# --- 主程式 ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("5-in-1 Game Collection")
    clock = pygame.time.Clock()
    font_main = pygame.font.SysFont("Arial", 28)
    font_small = pygame.font.SysFont("Arial", 22)

    state = GameState.MENU
    game = Mastermind()

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == GameState.MENU:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # 簡單按鈕偵測
                    if 300 < mouse_pos[0] < 500:
                        if 200 < mouse_pos[1] < 250:
                            game = Mastermind()
                            state = GameState.MASTERMIND
                        elif 280 < mouse_pos[1] < 330:
                            state = GameState.ACHIEVEMENTS
            
            elif state == GameState.ACHIEVEMENTS:
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    state = GameState.MENU

            elif state == GameState.MASTERMIND:
                if not game.game_over and event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_6:
                        idx = event.key - pygame.K_1
                        if len(game.current_guess) < 4:
                            game.current_guess.append(COLORS[idx])
                    elif event.key == pygame.K_BACKSPACE:
                        if game.current_guess: game.current_guess.pop()
                    elif event.key == pygame.K_RETURN:
                        game.check_guess()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: game = Mastermind()
                    if event.key == pygame.K_m: state = GameState.MENU

        # --- 繪製畫面 ---
        if state == GameState.MENU:
            screen.fill(WHITE)
            draw_text(screen, "5-in-1 GAME HUB", (SCREEN_WIDTH//2, 100), font_main, center=True)
            # 按鈕 UI
            btn_start = pygame.Rect(300, 200, 200, 50)
            btn_ach = pygame.Rect(300, 280, 200, 50)
            
            pygame.draw.rect(screen, BLACK, btn_start, 2)
            pygame.draw.rect(screen, BLACK, btn_ach, 2)
            
            draw_text(screen, "Start Game", (400, 225), font_main, center=True)
            draw_text(screen, "Achievements", (400, 305), font_main, center=True)

        elif state == GameState.ACHIEVEMENTS:
            screen.fill(WHITE)
            draw_text(screen, "ACHIEVEMENTS", (SCREEN_WIDTH//2, 100), font_main, center=True)
            
            y_offset = 200
            for name, unlocked in achievements.items():
                color = GREEN if unlocked else GRAY
                status = "[Unlocked]" if unlocked else "[Locked]"
                draw_text(screen, f"{name}: {status}", (SCREEN_WIDTH//2, y_offset), font_main, color, center=True)
                y_offset += 50
            
            draw_text(screen, "Press any key to return", (400, 500), font_small, DARK_GRAY, center=True)

        elif state == GameState.MASTERMIND:
            game.draw(screen, font_small)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()