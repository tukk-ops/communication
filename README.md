# 基于機器學習之無線通訊斷訊預測與通道特徵量化分析
# (Wireless Signal Outage Prediction and Feature Importance Analysis via Machine Learning)

本專題透過 Python 獨立建構無線通訊通道模擬系統，大量生成 BPSK 數位訊號在不同物理環境下的衰減數據，並進一步運用 **隨機森林（Random Forest）分類演算法**，實現對智慧場域通訊盲點與斷訊風險（Is_Outage）的動態預測與特徵權重量化。

---

## 📌 研究背景與痛點
在智慧校園無人載具導航、自駕車及室內盲人導航等應用中，無線通訊訊號（如 5G 毫米波、Wi-Fi）極易受到距離延伸與水泥、玻璃等建築物阻隔影響，導致訊號嚴重衰減甚至斷訊。
傳統優化多依賴高成本的現地量測，本研究旨在透過**軟體模擬結合 AI 演算法**，在不增加硬體成本的前提下，建構一低成本、高效率的智慧場域服務質量（QoS）動態預測機制。

---

## 🛠️ 系統架構與實作步驟

### 1. 通道動態數學模擬 (Data Generation)
* 透過 Python 數學公式模擬訊號發射與傳輸。
* 考慮變數（Features）：傳輸距離（Distance）、障礙物數量（Obstacle Count）、障礙物材質（Obstacle Type）及環境高斯白雜訊（AWGN）。
* 生成包含「路徑損耗（Path Loss）」、「接收信噪比（SNR）」與「是否斷訊（Is_Outage, 定義為 BER > 0.1）」之標準 CSV 數據集。

### 2. 獨立重構與資料清理 (Data Preprocessing)
* 針對 Python 3.13 最新環境進行環境解耦，捨棄相容性欠佳的套裝軟體，純手工使用底層 `scikit-learn` 與 `pandas` 進行重構。
* 內建「自動大小寫相容」與「動態欄位清理」防呆演算法，全面杜絕 `KeyError`，並完成特徵標準化（Standardization）。

### 3. 隨機森林模型訓練 (Model Training)
* 將數據集切分為 80% 訓練集與 20% 測試集。
* 導入隨機森林分類器（Random Forest Classifier），透過多棵決策樹進行非線性環境特徵抓取，並針對測試集進行二元預測。

---

## 📊 研究結果與數據分析 (Results)

執行 `putup.py` 後，模型在測試集（共 1,600 筆通訊資料）上跑出了極其優異的表現，並自動將視覺化成果儲存為 `ML_Analysis_Results.png`：

### 1. 混淆矩陣 (Confusion Matrix) 評估 —— 準確率 100%
* **精準命中：** 成功完全識別出 1,150 筆正常訊號（Normal）與 450 筆中斷訊號（Outage）。
* **零誤判表現：** 模型在測試集上的 **Accuracy、Precision、Recall 及 F1-Score 皆達到了 1.00 (100%)**，充分驗證了透過環境物理特徵預測斷訊風險的技術可行性。

### 2. 特徵重要性 (Feature Importance) 權重量化
模型自動剖析並導出影響通訊斷訊的核心物理指標排序：
1. **接收信噪比 (received_snr_db)：** 權重高達 **70%**，為斷訊與否的最關鍵因素。
2. **總路徑損耗 (total_path_loss_db)：** 權重約 **18%**，為第二大主因。
3. **背景雜訊功率 (noise_power_dbm)：** 權重約 **8%**。
4. **障礙物數量與材質：** 呈現微弱隨機分佈，其直接影響
