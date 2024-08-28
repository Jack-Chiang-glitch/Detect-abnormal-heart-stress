import pandas as pd
import numpy as np
from scipy.signal import firwin,filtfilt
import matplotlib.pyplot as plt
import os

i,j=1,1
main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"


def Get_ppg_sequence(i,j):
    folder_name = f"{str(i).zfill(2)}-{str(j).zfill(2)}"
    file_path = os.path.join(main_directory, folder_name, "PPG_processed.csv")
    ppg_data_frame = pd.read_csv(file_path)
    ppg_sequence = ppg_data_frame["FR2"]
    return ppg_sequence.to_numpy()

def Save_ppg_dataframe(four_stage_ppg_df, i):  # R : Remove outliers F : Filtering 1 : intitial 2 : final
    serial_number = f"{str(i).zfill(2)}"
    main_directory = "C:\\Jack\\Rppg_acquire_8.18\\The-rPPG-Acquiring-System-main\\TriAnswer_Records(processed)"
    output_file_path = os.path.join(main_directory, serial_number + "_PPG.csv")
    four_stage_ppg_df.to_csv(output_file_path, index=False)

for i in range(51, 59):
    if i == 7 or i == 10: continue
    first_rest, psycho_pressure, second_rest, physic_pressure = \
        Get_ppg_sequence(i, 1), Get_ppg_sequence(i, 2), Get_ppg_sequence(i, 3), Get_ppg_sequence(i, 4)
    if i%2==0: 
        psycho_pressure, physic_pressure = physic_pressure, psycho_pressure
        
    print("i="+str(i))
    print(len(first_rest))
    print(len(psycho_pressure))
    print(len(second_rest))
    print(len(physic_pressure))
    
    four_stage_ppg_df = pd.DataFrame({
        "First_rest": first_rest,
        "Psycho": psycho_pressure,
        "Second_rest": second_rest,
        "Physic": physic_pressure
    })
    
    
    Save_ppg_dataframe(four_stage_ppg_df, i)
    print(f"{str(i).zfill(2)}")
    
        