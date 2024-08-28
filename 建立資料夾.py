import os

# 設定主資料夾路徑
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"

# 建立 01-01 到 15-04 的資料夾
for i in range(51, 59):
    for j in range(1, 5):
        folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
        folder_path = os.path.join(main_directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"資料夾已建立: {folder_path}")
