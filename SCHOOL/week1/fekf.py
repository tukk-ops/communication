import pygame
import pygame_gui
import random
from pygame_gui.elements import UIPanel, UIButton, UILabel
from pygame_gui.windows import UIConfirmationDialog, UIMessageWindow

# --- 常數定義 ---
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 650
BG_COLOR = (240, 240, 240)
BLACK = (30, 30, 30)
GRAY_HOLE = (200, 200, 200)
WHITE = (255, 255, 255)

# 遊戲顏色清單
COLOR_PALETTE = [
    (255, 50, 50),   # 紅
    (50, 50, 255),   # 藍
    (50, 200, 50),   # 綠
    (255, 215, 0),   # 黃
    (255, 165, 0),   # 橘
    (160, 32, 240)   # 紫
]

class MastermindPro:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mastermind Professional Edition")
        
        # Pygame GUI 管理器
        self.manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # 遊戲邏輯變數
        self.max_attempts = 8
        self.secret = [random.choice(COLOR_PALETTE) for _ in range(4)]
        self.guesses = []   # 已提交的歷史紀錄
        self.feedback = []  # 已提交的 T/F 結果
        self.current_guess = [] # 目前正在輸入的顏色
        self.game_over = False
        
        self.setup_ui()
        self.clock = pygame.time.Clock()
        self.running = True

    def setup_ui(self):
        """建立右側控制面板與按鈕"""
        panel_width = 250
        self.right_panel = UIPanel(
            relative_rect=pygame.Rect((SCREEN_WIDTH - panel_width, 0), (panel_width, SCREEN_HEIGHT)),
            manager=self.manager,
            starting_height=0
        )

        UILabel(relative_rect=pygame.Rect((10, 20), (230, 40)), 
                text="CONTROL PANEL", manager=self.manager, container=self.right_panel)

        # 建立 6 個色彩按鈕
        self.color_buttons = []
        for i in range(6):
            btn = UIButton(
                relative_rect=pygame.Rect((25 + (i%2)*100, 80 + (i//2)*70), (80, 60)),
                text=f"Color {i+1}",
                manager=self.manager,
                container=self.right_panel,
                tool_tip_text=f"Pick color {i+1}"
            )
            self.color_buttons.append(btn)

        # 提交按鈕
        self.submit_btn = UIButton(
            relative_rect=pygame.Rect((25, 320), (200, 50)),
            text="SUBMIT ANSWER",
            manager=self.manager,
            container=self.right_panel
        )
        
        # 重置按鈕
        self.reset_btn = UIButton(
            relative_rect=pygame.Rect((25, 580), (200, 40)),
            text="RESTART GAME",
            manager=self.manager,
            container=self.right_panel
        )

    def check_logic(self):
        """計算 T (位置顏色皆對) 與 F (僅顏色對)"""
        if len(self.current_guess) < 4: return

        t_count = 0
        f_count = 0
        temp_secret = list(self.secret)
        temp_guess = list(self.current_guess)

        # 第一輪：找 T
        for i in range(3, -1, -1):
            if temp_guess[i] == temp_secret[i]:
                t_count += 1
                temp_secret.pop(i)
                temp_guess.pop(i)
        
        # 第二輪：找 F
        for g in temp_guess:
            if g in temp_secret:
                f_count += 1
                temp_secret.remove(g)

        self.feedback.append((t_count, f_count))
        self.guesses.append(list(self.current_guess))
        
        # 判斷勝負
        if t_count == 4:
            self.trigger_end_game(True)
        elif len(self.guesses) >= self.max_attempts:
            self.trigger_end_game(False)
        
        self.current_guess = []

    def trigger_end_game(self, win):
        self.game_over = True
        if win:
            title = "Victory!"
            msg = f"Congratulations! You solved it in {len(self.guesses)} tries."
            # 成就彈窗
            if len(self.guesses) <= 5:
                UIMessageWindow(
                    rect=pygame.Rect((250, 200), (300, 200)),
                    html_message="<br><b>ACHIEVEMENT UNLOCKED:</b><br>Mastermind Guru (Solved in ≤ 5)",
                    manager=self.manager,
                    window_title="Achievement"
                )
        else:
            title = "Game Over"
            msg = "You've run out of attempts!"
        
        UIConfirmationDialog(
            rect=pygame.Rect((250, 200), (300, 200)),
            manager=self.manager,
            window_title=title,
            action_long_desc=msg,
            blocking=False
        )

    def handle_events(self):
        time_delta = self.clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # 處理鍵盤退格
            if event.type == pygame.KEYDOWN and not self.game_over:
                if event.key == pygame.K_BACKSPACE and self.current_guess:
                    self.current_guess.pop()

            # 將事件傳遞給 GUI 管理器
            self.manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if not self.game_over:
                    # 顏色按鈕點擊
                    for i, btn in enumerate(self.color_buttons):
                        if event.ui_element == btn and len(self.current_guess) < 4:
                            self.current_guess.append(COLOR_PALETTE[i])
                    
                    # 提交按鈕點擊
                    if event.ui_element == self.submit_btn:
                        self.check_logic()
                
                # 重置按鈕
                if event.ui_element == self.reset_btn:
                    self.__init__()

        self.manager.update(time_delta)

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # --- 繪製左側遊戲區 ---
        start_x, start_y = 80, 40
        row_w, row_h = 350, 65
        
        for i in range(self.max_attempts):
            rect_y = start_y + i * row_h
            is_active = (i == len(self.guesses)) and not self.game_over
            
            # 1. 繪製矩形框 (當前行加粗)
            thickness = 4 if is_active else 1
            pygame.draw.rect(self.screen, BLACK, (start_x, rect_y, row_w, row_h - 10), thickness)
            
            # 2. 繪製框框內的 4 個球位
            for j in range(4):
                circle_pos = (start_x + 50 + j*60, rect_y + 27)
                
                # 決定顏色：已提交的顏色 > 正在輸入的顏色 > 預設灰色空心
                draw_color = None
                if i < len(self.guesses):
                    draw_color = self.guesses[i][j]
                elif is_active and j < len(self.current_guess):
                    draw_color = self.current_guess[j]
                
                if draw_color:
                    pygame.draw.circle(self.screen, draw_color, circle_pos, 20)
                else:
                    pygame.draw.circle(self.screen, GRAY_HOLE, circle_pos, 20, 2)

            # 3. 繪製回饋 T / F
            if i < len(self.feedback):
                t, f = self.feedback[i]
                font = pygame.font.SysFont("Arial", 20, bold=True)
                txt = font.render(f"T:{t} F:{f}", True, BLACK)
                self.screen.blit(txt, (start_x + 270, rect_y + 15))

        # --- 失敗時顯示答案 ---
        if self.game_over and len(self.feedback) == self.max_attempts and self.feedback[-1][0] != 4:
            font = pygame.font.SysFont("Arial", 24, bold=True)
            self.screen.blit(font.render("Correct Answer:", True, (200, 0, 0)), (start_x, 570))
            for j, color in enumerate(self.secret):
                pygame.draw.circle(self.screen, color, (start_x + 200 + j*50, 580), 18)

        # 繪製 GUI
        self.manager.draw_ui(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
        pygame.quit()

if __name__ == "__main__":
    game = MastermindPro()
    game.run()