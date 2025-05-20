import os
import pandas as pd

def rename_and_record_files(folder_path):
   
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx') or f.endswith('.xls')]

    
    records = []

    for i, file in enumerate(files, start=1):
        new_name = f"G{i}.xlsx"
        original_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        os.rename(original_path, new_path)
        records.append({'Original Name': file, 'New Name': new_name})

    
    df = pd.DataFrame(records)
    df.to_excel(os.path.join(folder_path, 'renaming_record.xlsx'), index=False)


folder_path = 'Renamed_output'  
rename_and_record_files(folder_path)
