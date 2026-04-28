import pygame
import pygame_gui
from pygame import gfxdraw
import random
import os

# ==========================================
# 核心常數與配置 (黃金比例排版)
# ==========================================
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 720

# 顏色定義與中文名稱映射
COLORS = {
    'R': (255, 82, 82),    # 紅
    'G': (76, 175, 80),    # 綠
    'B': (33, 150, 243),   # 藍
    'Y': (255, 235, 59),   # 黃
    'P': (156, 39, 176),   # 紫
    'O': (255, 152, 0)     # 橘
}
# 調整答案格式：代碼-中文
COLOR_NAMES = {
    'R': 'R-紅', 'G': 'G-綠', 'B': 'B-藍', 
    'Y': 'Y-黃', 'P': 'P-紫', 'O': 'O-橘'
}
COLOR_KEYS = list(COLORS.keys())

class MastermindLogic:
    """
    遊戲邏輯類別：嚴格管理 8 次嘗試限制
    """
    def __init__(self, code_length=4, max_attempts=8):
        self.code_length = code_length
        self.max_attempts = max_attempts
        self.secret_code = [random.choice(COLOR_KEYS) for _ in range(code_length)]
        self.history = []
        self.game_over = False

    def check_guess(self, guess):
        """
        T/F 演算法：
        T: 位置顏色皆對 | F: 僅顏色對
        """
        t_count = 0
        f_count = 0
        temp_secret = list(self.secret_code)
        temp_guess = list(guess)

        # 第一輪：檢查 T
        for i in range(self.code_length):
            if temp_guess[i] == temp_secret[i]:
                t_count += 1
                temp_secret[i] = None
                temp_guess[i] = None

        # 第二輪：檢查 F
        for i in range(self.code_length):
            if temp_guess[i] is not None:
                if temp_guess[i] in temp_secret:
                    f_count += 1
                    temp_secret.remove(temp_guess[i])

        return t_count, f_count

class MastermindGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mastermind - Professional Edition")
        
        # 1. 強制載入系統中文字體 (微軟正黑體)
        font_path = "C:\\Windows\\Fonts\\msjh.ttc"
        
        # 2. 初始化 UI 管理器並載入字體
        self.ui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), 'theme.json')
        self.ui_manager.add_font_paths("chinese_font", font_path)
        self.ui_manager.preload_fonts([
            {"name": "chinese_font", "point_size": 18, "style": "regular"},
            {"name": "chinese_font", "point_size": 18, "style": "bold"}
        ])
        
        self.logic = MastermindLogic()
        self.current_guess = []
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.end_window = None 
        
        self.setup_ui()

    def reset_game(self):
        """實作重玩一次的功能邏輯：重置所有遊戲狀態"""
        self.logic = MastermindLogic()
        self.current_guess = []
        self.end_window = None
        print("遊戲已重置，新的一局開始！")

    def setup_ui(self):
        """
        控制面板重設計：精確坐標計算，確保不重疊
        """
        # 1. 顏色按鈕區 (Y=580)
        btn_width = 50
        btn_spacing = 10
        total_btns_width = (btn_width * 6) + (btn_spacing * 5)
        start_x = (SCREEN_WIDTH - total_btns_width) // 2
        
        self.color_buttons = []
        for i, color_key in enumerate(COLOR_KEYS):
            btn = pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect((start_x + i * (btn_width + btn_spacing), 580), (btn_width, 50)),
                text=color_key,
                manager=self.ui_manager
            )
            self.color_buttons.append((btn, color_key))

        # 2. 功能按鈕區 (Y=640)：提交與刪除並排
        action_btn_width = 120
        action_start_x = (SCREEN_WIDTH - (action_btn_width * 2 + 20)) // 2
        
        self.submit_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((action_start_x, 640), (action_btn_width, 50)),
            text='SUBMIT',
            manager=self.ui_manager
        )
        
        self.delete_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((action_start_x + action_btn_width + 20, 640), (action_btn_width, 50)),
            text='DELETE',
            manager=self.ui_manager
        )

    def show_end_message(self, title, message):
        """
        使用 UIMessageWindow 顯示結果與答案
        """
        if self.end_window is not None:
            self.end_window.kill()

        self.end_window = pygame_gui.windows.UIMessageWindow(
            rect=pygame.Rect((SCREEN_WIDTH // 2 - 160, SCREEN_HEIGHT // 2 - 120), (320, 240)),
            manager=self.ui_manager,
            window_title=title,
            html_message=message
        )

    def draw_bead(self, surface, color, center, radius):
        """反鋸齒渲染 + 3D 高光珠子"""
        x, y = int(center[0]), int(center[1])
        gfxdraw.aacircle(surface, x, y, radius, color)
        gfxdraw.filled_circle(surface, x, y, radius, color)
        highlight_pos = (x - radius // 3, y - radius // 3)
        gfxdraw.aacircle(surface, highlight_pos[0], highlight_pos[1], radius // 4, (255, 255, 255))
        gfxdraw.filled_circle(surface, highlight_pos[0], highlight_pos[1], radius // 4, (255, 255, 255))

    def draw_history(self):
        """繪製 8 行歷史紀錄，確保與控制面板分離"""
        row_height = 60
        start_y = 30
        box_width = 440
        box_x = (SCREEN_WIDTH - box_width) // 2

        for i in range(8):
            current_y = start_y + i * row_height
            rect = pygame.Rect(box_x, current_y, box_width, 50)
            pygame.draw.rect(self.screen, (40, 40, 40), rect, border_radius=10)
            pygame.draw.rect(self.screen, (70, 70, 70), rect, 1, border_radius=10)

            if i < len(self.logic.history):
                guess, (t, f) = self.logic.history[i]
                for j, char in enumerate(guess):
                    self.draw_bead(self.screen, COLORS[char], (box_x + 40 + j * 60, current_y + 25), 18)
                
                # 歷史紀錄文字使用 Arial (通常系統內建支援中文，或僅顯示英文數字)
                font = pygame.font.SysFont("Arial", 22, bold=True)
                res_text = font.render(f"T: {t}  F: {f}", True, (220, 220, 220))
                self.screen.blit(res_text, (box_x + 300, current_y + 12))

    def run(self):
        while self.is_running:
            time_delta = self.clock.tick(60) / 1000.0
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                
                self.ui_manager.process_events(event)

                # 監聽彈窗關閉事件：當玩家點擊結束彈窗的「確定」或關閉時，自動呼叫 reset_game()
                if event.type == pygame_gui.UI_WINDOW_CLOSE:
                    if event.ui_element == self.end_window:
                        self.reset_game()

                if not self.logic.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if self.current_guess:
                                self.current_guess.pop()

                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        for btn, char in self.color_buttons:
                            if event.ui_element == btn and len(self.current_guess) < 4:
                                self.current_guess.append(char)
                        
                        if event.ui_element == self.delete_btn:
                            if self.current_guess:
                                self.current_guess.pop()

                        if event.ui_element == self.submit_btn:
                            if len(self.current_guess) == 4:
                                t, f = self.logic.check_guess(self.current_guess)
                                self.logic.history.insert(0, (list(self.current_guess), (t, f)))
                                attempts = len(self.logic.history)
                                
                                # 公布答案格式化：代碼-中文
                                answer_str = ", ".join([COLOR_NAMES[c] for c in self.logic.secret_code])
                                
                                if t == 4:
                                    self.logic.game_over = True
                                    self.show_end_message("勝利！", 
                                        f"恭喜你猜對了！<br>你只花了 {attempts} 次就解開了密碼！<br><br>"
                                        f"正確答案是：<br><b>{answer_str}</b><br><br>關閉此視窗即可重玩。")
                                elif attempts >= 8:
                                    self.logic.game_over = True
                                    self.show_end_message("遊戲結束", 
                                        f"很遺憾你輸了。<br><br>"
                                        f"正確答案是：<br><b>{answer_str}</b><br><br>關閉此視窗即可重玩。")
                                
                                self.current_guess = []

            self.screen.fill((30, 30, 30))
            self.draw_history()
            
            # 繪製當前輸入預覽 (Y=530)
            for i, char in enumerate(self.current_guess):
                self.draw_bead(self.screen, COLORS[char], (SCREEN_WIDTH // 2 - 90 + i * 60, 535), 18)

            self.ui_manager.update(time_delta)
            self.ui_manager.draw_ui(self.screen)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = MastermindGame()
    game.run()
