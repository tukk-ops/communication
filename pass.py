import numpy as np
import pandas as pd

def simulate_comm_system(num_samples=8000, num_bits=10000):
    # 系統固定參數
    tx_power_dbm = 20.0     # 發射功率 (dBm)
    freq_mhz = 2400.0       # 載波頻率 (假設 2.4 GHz WiFi/藍牙頻段)
    
    # 自由空間路徑損耗公式的常數項 (Free Space Path Loss at 1m)
    # FSPL(dB) = 20*log10(d) + 20*log10(f_MHz) - 27.55
    fspl_constant = 20 * np.log10(freq_mhz) - 27.55
    
    # 障礙物衰減係數 (dB)
    attenuation_glass = 2.0
    attenuation_concrete = 10.0
    
    records = []
    
    print(f"開始進行模擬，預計生成 {num_samples} 筆組合，每組傳送 {num_bits} Bits...")
    
    # 使用隨機採樣來產生大規模的不同變數組合
    for i in range(num_samples):
        # 1. 隨機生成環境變數
        distance = np.random.uniform(10, 200)          # 距離: 10 到 200 公尺
        obs_count = np.random.randint(0, 5)            # 障礙物數量: 0 到 4 道牆
        obs_type = np.random.choice(['Glass', 'Concrete']) if obs_count > 0 else 'None'
        noise_power_dbm = np.random.uniform(-100, -60) # 背景雜訊功率: -100 到 -60 dBm
        
        # 2. 計算訊號路徑損耗 (Total Path Loss)
        fspl = 20 * np.log10(distance) + fspl_constant
        
        obs_loss = 0
        if obs_count > 0:
            if obs_type == 'Glass':
                obs_loss = obs_count * attenuation_glass
            else:
                obs_loss = obs_count * attenuation_concrete
                
        total_path_loss = fspl + obs_loss
        
        # 3. 計算接收端信噪比 (Received SNR)
        rx_power_dbm = tx_power_dbm - total_path_loss
        rx_snr_db = rx_power_dbm - noise_power_dbm
        
        # 將 SNR (dB) 轉為線性值，以便用於 AWGN 雜訊生成
        # SNR_linear = Signal_Power / Noise_Power
        snr_linear = 10 ** (rx_snr_db / 10.0)
        
        # 4. BPSK 通訊模擬
        # 生成隨機傳送的 0/1 位元
        tx_bits = np.random.randint(0, 2, num_bits)
        
        # BPSK 調變 (0 -> -1, 1 -> +1)
        tx_symbols = 2 * tx_bits - 1
        
        # 模擬高斯白雜訊 (AWGN)
        # 假設訊號功率為 1，則雜訊變異數 (Variance) N0 = 1 / SNR_linear
        noise_std = np.sqrt(1.0 / (2.0 * snr_linear)) if snr_linear > 0 else 1000.0
        noise = np.random.normal(0, noise_std, num_bits)
        
        # 接收到的訊號為發射訊號加上雜訊
        rx_symbols = tx_symbols + noise
        
        # 解調 (如果符號 > 0 判斷為 1，否則為 0)
        rx_bits = (rx_symbols > 0).astype(int)
        
        # 5. 計算統計結果標籤
        errors = np.sum(tx_bits != rx_bits)
        ber = errors / num_bits
        is_outage = bool(ber > 0.1) # 定義 BER > 10% 為通訊中斷
        
        # 6. 記錄該次模擬的特徵與結果
        records.append({
            'Distance_m': round(distance, 2),
            'Obstacle_Count': obs_count,
            'Obstacle_Type': obs_type,
            'Noise_Power_dBm': round(noise_power_dbm, 2),
            'Received_SNR_dB': round(rx_snr_db, 2),
            'Total_Path_Loss_dB': round(total_path_loss, 2),
            'BER': ber,
            'Is_Outage': is_outage
        })
        
        if (i + 1) % 1000 == 0:
            print(f"已完成 {i + 1} / {num_samples} 筆模擬...")
            
    # 轉換成 Pandas DataFrame
    df = pd.DataFrame(records)
    return df

if __name__ == "__main__":
    # 執行主程式 (模擬 8000 筆數據，這是一個適合機器學習的大小)
    dataset = simulate_comm_system(num_samples=8000, num_bits=10000)
    
    # 匯出資料集
    output_file = "telecom_simulation_dataset.csv"
    dataset.to_csv(output_file, index=False)
    
    print(f"\n模擬完成！檔案已儲存為：{output_file}")
    print("\n資料集預覽：")
    print(dataset.head())