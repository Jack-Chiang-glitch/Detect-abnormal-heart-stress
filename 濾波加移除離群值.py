import pandas as pd
import numpy as np
from scipy.signal import firwin,filtfilt
import matplotlib.pyplot as plt
import os

def Remove_outliers(ppg_sequence):
    Q1 = np.quantile(ppg_sequence, 0.25)
    # 計算第 3 四分位數 (Q3, 0.75 分位數)
    Q3 = np.quantile(ppg_sequence, 0.75)
    IQR = Q3 - Q1
    # 定義離群值範圍
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = (ppg_sequence < lower_bound) | (ppg_sequence > upper_bound)
    for i in range(len(outliers)):
        if outliers[i] == True:
            ppg_sequence[i] = ppg_sequence[i-1]      
    return ppg_sequence

def Filtering(ppg_sequence):
    fs=100
    taps = firwin(300, [0.5 / (fs / 2), 5 / (fs / 2)], pass_zero=False)
    ppg_sequence = filtfilt(taps,1, np.double(ppg_sequence))
    return ppg_sequence

def PPG_FR_processing(ppg_sequence):
    ppg_sequence = Filtering(ppg_sequence)
    ppg_sequence = Remove_outliers(ppg_sequence)
    return ppg_sequence

def PPG_RF_processing(ppg_sequence):
    ppg_sequence = Remove_outliers(ppg_sequence)
    ppg_sequence = Filtering(ppg_sequence)
    return ppg_sequence

def Get_raw_ppg(i,j):
    # 設定主資料夾路徑
    main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(unprocessed)"
    folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
    file_path = os.path.join(main_directory, folder_name, "PPG_R.csv")
    # 讀取 CSV 檔案
    ppg_data_frame = pd.read_csv(file_path, header=None)
    # 取得第一個欄位並轉為 numpy 陣列
    raw_ppg = ppg_data_frame.iloc[:, 0].to_numpy() # get first 
    raw_ppg = raw_ppg[:30000]
    
    return raw_ppg

def Save_ppg_dataframe(ppg_dataframe, i, j):  # R : Remove outliers F : Filtering 1 : intitial 2 : final
    main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
    folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
    output_file_path = os.path.join(main_directory, folder_name, "PPG_processed.csv")
    ppg_dataframe.to_csv(output_file_path, index=False)
    #np.savetxt(output_file_path, ppg_dataframe, delimiter=',', header='PPG Data', comments='', fmt='%.6f')


# 建立 01-01 到 15-04 的資料夾
for i in range(51, 59):
    for j in range(1, 5):
        if i == 7 and j == 1:
            continue
        raw_ppg = Get_raw_ppg(i,j)
        
        FR1_ppg = PPG_FR_processing(np.copy(raw_ppg))
        FR2_ppg = PPG_FR_processing(np.copy(FR1_ppg))
        
        RF1_ppg = PPG_RF_processing(np.copy(raw_ppg))
        RF2_ppg = PPG_RF_processing(np.copy(RF1_ppg))
        
        
        # 將這四個陣列組合成一個 DataFrame，並指定欄位名稱
        ppg_dataframe = pd.DataFrame({
            "FR1": FR1_ppg,
            "FR2": FR2_ppg,
            "RF1": RF1_ppg,
            "RF2": RF2_ppg
        })
        Save_ppg_dataframe(ppg_dataframe, i, j)
        print(f"{str(i).zfill(2)}-{str(j).zfill(2)}")







"""
############################ THIRD
i = 1
j = 4
raw_ppg = Get_raw_ppg(i,j)
ppg_raw_filtered  = PPG_processing(raw_ppg)
ppg_corrected_filtered = PPG_processing(np.copy(ppg_raw_filtered))
third_ppg = PPG_processing(np.copy(ppg_corrected_filtered))



low = 20000
up =  25000
plt.plot(third_ppg - ppg_corrected_filtered, label='Processed', color='red', marker='o', markersize=0.1)
plt.figure(figsize=(12, 6))

# 繪製未處理的資料
plt.plot(third_ppg[low:up], label='Third processing', color='red', linestyle='-', linewidth=1)

# 繪製處理後的資料
plt.plot(ppg_corrected_filtered[low:up], label='Second processing', color='blue', linestyle='-', linewidth=1)



# 添加圖例
plt.legend()

# 顯示圖形
plt.show()
###########################
"""




"""

i = 1
j = 4
raw_ppg = Get_raw_ppg(i,j)
ppg_raw_filtered  = PPG_processing(raw_ppg)
ppg_corrected_filtered = PPG_processing(np.copy(ppg_raw_filtered))
third_ppg = PPG_processing(np.copy(ppg_corrected_filtered))



low = 20000
up =  25000
plt.plot(ppg_corrected_filtered - ppg_raw_filtered, label='Processed', color='red', marker='o', markersize=0.1)
plt.figure(figsize=(12, 6))

# 繪製未處理的資料
plt.plot(ppg_raw_filtered[low:up], label='First processing', color='red', linestyle='-', linewidth=1)

# 繪製處理後的資料
plt.plot(ppg_corrected_filtered[low:up], label='Second processing', color='blue', linestyle='-', linewidth=1)



# 添加圖例
plt.legend()

# 顯示圖形
plt.show()

"""








"""
plt.plot(ppg_processed, label='Processed', color='blue', marker='o', markersize=0.1)



def plot_comparison(ppg_processed, second_ppg_processed):
    plt.figure(figsize=(12, 6))

    # 繪製未處理的資料
    plt.plot(ppg_processed[:1000], label='processed Data', color='red', linestyle='-', linewidth=1)

    # 繪製處理後的資料
    plt.plot(second_ppg_processed[:1000], label='second processed Data', color='blue', linestyle='-', linewidth=1)

    # 設置圖形標題和標籤
    plt.title('Unprocessed Data vs Processed Data')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')

    # 設置 Y 軸上下限（根據數據範圍調整）
    #plt.ylim([min(min(ppg_unprocessed), min(second_ppg_processed)), 
    #          max(max(ppg_unprocessed), max(second_ppg_processed))])
    plt.ylim([-700,800])
    # 顯示圖例
    plt.legend()

    # 顯示網格
    plt.grid(True)

    # 顯示圖形
    plt.show()

# 繪製比較圖
plot_comparison(ppg_processed, second_ppg_processed)
plt.plot(second_ppg_processed - ppg_processed, label='Processed', color='blue', marker='o', markersize=0.1)

"""



