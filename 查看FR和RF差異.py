import pandas as pd
import numpy as np
from scipy.signal import firwin,filtfilt
import matplotlib.pyplot as plt
import os

i, j = 1, 4
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
file_path = os.path.join(main_directory, folder_name, "PPG_processed.csv")

PPG_df = pd.read_csv(file_path)
FR2 = PPG_df["FR2"].to_numpy()
RF2 = PPG_df["FR1"].to_numpy()



plt.plot(FR2 - RF2 , label='Difference', color='red', marker='o', markersize=0.1)
plt.figure(figsize=(12, 6))


low = 11500
up =  12500
# 繪製未處理的資料
plt.plot(FR2[low:up], label='Filter Remove', color='red', linestyle='-', linewidth=1)

# 繪製處理後的資料
plt.plot(RF2[low:up], label='Remove Filter', color='blue', linestyle='-', linewidth=1)



# 添加圖例
plt.legend()

# 顯示圖形
plt.show()