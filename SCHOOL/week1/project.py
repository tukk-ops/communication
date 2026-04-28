import pygame
import random
import math

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# 初始化
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("5-in-1 遊戲大集合")

# 這裡改用系統預設字體，避免路徑問題
font = pygame.font.SysFont(None, 32) 

class GameState:
    MENU = 0
    MASTERMIND = 1

# --- 遊戲 1: 珠璣妙算 (Mastermind) ---
class Mastermind:
    def __init__(self):
        self.colors = [RED, BLUE, GREEN, YELLOW, (255, 165, 0), (128, 0, 128)]
        self.secret = [random.choice(self.colors) for _ in range(4)]
        self.guesses = []
        self.current_guess = []
        self.feedback = [] 
        self.game_over = False

    def check_guess(self):
        if len(self.current_guess) != 4: return # 沒填滿不能檢查
        
        black = 0
        white = 0
        temp_secret = list(self.secret)
        temp_guess = list(self.current_guess)

        # 算黑點 (位置對且顏色對)
        for i in range(3, -1, -1):
            if temp_guess[i] == temp_secret[i]:
                black += 1
                temp_secret.pop(i)
                temp_guess.pop(i)
        
        # 算白點 (顏色對但位置錯)
        for g in temp_guess:
            if g in temp_secret:
                white += 1
                temp_secret.remove(g)
        
        self.feedback.append((black, white))
        self.guesses.append(list(self.current_guess))
        self.current_guess = []
        if black == 4: self.game_over = True

    def draw(self, screen):
        screen.fill(WHITE)
        # 繪製標題
        title = font.render("Mastermind - Press 1-6 to Pick, Enter to Submit", True, BLACK)
        screen.blit(title, (50, 10))

        # 繪製歷史紀錄
        for i, guess in enumerate(self.guesses):
            for j, color in enumerate(guess):
                pygame.draw.circle(screen, color, (100 + j*50, 60 + i*50), 20)
            b, w = self.feedback[i]
            fb_text = font.render(f"B:{b} W:{w}", True, BLACK)
            screen.blit(fb_text, (300, 45 + i*50))
        
        # 繪製當前輸入區
        pygame.draw.rect(screen, GRAY, (50, 480, 300, 60))
        for j, color in enumerate(self.current_guess):
            pygame.draw.circle(screen, color, (100 + j*50, 510), 20)
        
        if self.game_over:
            win_text = font.render("YOU WIN! Press R to Restart", True, GREEN)
            screen.blit(win_text, (100, 550))

# --- 主程式執行區 ---
def main():
    current_state = GameState.MASTERMIND # 先直接進遊戲測試
    game = Mastermind()
    clock = pygame.time.Clock()
    running = True

    while running:
        # 1. 偵測玩家動作 (Events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 按下視窗叉叉
                running = False
            
            if not game.game_over and event.type == pygame.KEYDOWN:
                # 偵測數字鍵 1-6 (對應 0-5 索引)
                if pygame.K_1 <= event.key <= pygame.K_6:
                    idx = event.key - pygame.K_1
                    if len(game.current_guess) < 4:
                        game.current_guess.append(game.colors[idx])
                
                # 退格鍵 (刪除上一個選的顏色)
                if event.key == pygame.K_BACKSPACE:
                    if game.current_guess:
                        game.current_guess.pop()

                # Enter 提交
                if event.key == pygame.K_RETURN:
                    game.check_guess()
            
            # 贏了之後按 R 重新開始
            if game.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game = Mastermind()

        # 2. 繪製畫面
        if current_state == GameState.MASTERMIND:
            game.draw(screen)
        
        # 3. 更新螢幕
        pygame.display.flip()
        
        # 4. 控制每秒跑 60 次 (FPS)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()