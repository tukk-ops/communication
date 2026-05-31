import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 載入 Scikit-Learn 的核心模組 (完美支援 Python 3.13)
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, confusion_matrix, classification_report

def main():
    print("📥 1. 載入資料集中...")
    try:
        df = pd.read_csv('telecom_simulation_dataset.csv')
    except Exception as e:
        print("❌ 找不到檔案，嘗試使用絕對路徑...")
        df = pd.read_csv(r'C:\Users\user\Desktop\海大\telecom_simulation_dataset.csv')
    
    # === 【大絕招：全自動清理欄位名稱】 ===
    # 去除前後空格，並將所有欄位名稱轉成英文小寫，澈底解決 KeyError 問題
    df.columns = [str(col).strip().lower() for col in df.columns]
    
    print("\n📋 偵測到你的 CSV 內真實存在的欄位（已自動轉小寫）：")
    print(list(df.columns))
    print("===================================================\n")
    
    # 建立大小寫相容的映射別名
    # 判斷哪些是我們要預測的目標（Label），哪些是拿來訓練的特徵（Features）
    target_loss_cols = ['path_loss', 'pathloss', 'path_loss_db', 'loss']
    target_outage_cols = ['is_outage', 'outage', 'isoutage']
    ignore_cols = ['received_snr', 'snr', 'ber', 'unnamed: 0'] + target_loss_cols + target_outage_cols
    
    # 自動找出對應的欄位名稱
    path_loss_col = next((c for c in df.columns if c in target_loss_cols), None)
    is_outage_col = next((c for c in df.columns if c in target_outage_cols), None)
    obstacle_type_col = next((c for c in df.columns if 'obstacle_type' in c or 'type' in c), None)

    # 【資料預處理】：將文字標籤（如類別型態）轉為數字
    if obstacle_type_col and df[obstacle_type_col].dtype == 'object':
        df = pd.get_dummies(df, columns=[obstacle_type_col], drop_first=True)
        
    # 動態定義特徵欄位 X
    features = [col for col in df.columns if col not in ignore_cols]
    X = df[features]
    
    print(f"💡 用於訓練模型的特徵欄位 (X): {features}")

    # ==========================================
    # 任務 A：迴歸模型 (預測 Path_Loss 路徑損耗)
    # ==========================================
    reg_success = False
    if path_loss_col:
        print(f"\n🤖 2. 開始訓練【迴歸模型】(正在預測欄位: {path_loss_col})...")
        y_reg = df[path_loss_col]
        
        X_train_R, X_test_R, y_train_R, y_test_R = train_test_split(X, y_reg, test_size=0.2, random_state=42)
        
        reg_model = RandomForestRegressor(n_estimators=100, random_state=42)
        reg_model.fit(X_train_R, y_train_R)
        
        y_pred_R = reg_model.predict(X_test_R)
        print("✅ 迴歸模型評估結果：")
        print(f"   - R² Score: {r2_score(y_test_R, y_pred_R):.4f} (越接近 1 表示預測越準確)")
        print(f"   - 均方誤差 (MSE): {mean_squared_error(y_test_R, y_pred_R):.4f}")
        reg_success = True
    else:
        print("\n⚠️ 警告：找不到路徑損耗相關欄位，跳過迴歸任務！")

    # ==========================================
    # 任務 B：分類模型 (預測 Is_Outage 是否斷訊)
    # ==========================================
    clf_success = False
    if is_outage_col:
        print(f"\n🤖 3. 開始訓練【分類模型】(正在預測欄位: {is_outage_col})...")
        y_clf = df[is_outage_col]
        
        X_train_C, X_test_C, y_train_C, y_test_C = train_test_split(X, y_clf, test_size=0.2, random_state=42)
        
        clf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        clf_model.fit(X_train_C, y_train_C)
        
        y_pred_C = clf_model.predict(X_test_C)
        print("✅ 分類模型評估結果：")
        print(classification_report(y_test_C, y_pred_C, target_names=['正常 (False)', '中斷 (True)']))
        clf_success = True
    else:
        print("\n⚠️ 警告：找不到斷訊中斷相關欄位，跳過分類任務！")

    # ==========================================
    # 繪製並儲存圖表
    # ==========================================
    print("\n📊 4. 產生視覺化圖表中...")
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # 左圖：混淆矩陣
    if clf_success:
        cm = confusion_matrix(y_test_C, y_pred_C)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                    xticklabels=['Normal', 'Outage'], yticklabels=['Normal', 'Outage'])
        axes[0].set_title("Confusion Matrix (Is_Outage Prediction)")
        axes[0].set_xlabel("Predicted Label")
        axes[0].set_ylabel("Actual Label")
    else:
        axes[0].text(0.5, 0.5, 'No Classification Model Data', ha='center', va='center', fontsize=14)
    
    # 右圖：特徵重要性
    if 'clf_model' in locals() or 'clf_model' in globals():
        importances = clf_model.feature_importances_
        feature_names = list(X.columns)
        
        # 建立一個 DataFrame 並排序
        imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
        imp_df = imp_df.sort_values(by='Importance', ascending=False)
        
        # 繪圖
        sns.barplot(x='Importance', y='Feature', data=imp_df, ax=axes[1], palette="viridis")
        axes[1].set_title("Feature Importance (What affects Outage most?)")
        axes[1].set_xlabel("Importance Score")
        axes[1].set_ylabel("Features")
    else:
        axes[1].text(0.5, 0.5, 'No Feature Importance Data', ha='center', va='center', fontsize=14)
    
    # 自動排版並儲存成圖片
    plt.tight_layout()
    plt.savefig("ML_Analysis_Results.png")
    print("\n🎉 【大功告成】分析圖表已儲存為同資料夾下的 'ML_Analysis_Results.png'！")

if __name__ == '__main__':
    main()