# concatenate_files.py

# This script combines ERA5 .nc files by variable (i.e. All air temperature files from 2022, 2023, and 2024) would go into one file. 
# Optional modification on this script: file name in line XX. 

# Import packages
import glob
from collections import defaultdict
import xarray as xr
import os

### Combine the files, if you had to download them into chunks ###

def detect_variable_name(dataset):
    for var in dataset.data_vars:
        return var  # Return the first variable found

# Make a directory to hold the combined files 
path = os.path.dirname(os.path.abspath(__file__))  
output_folder = os.path.join(path, 'combined_files')
os.makedirs(output_folder, exist_ok=True)

# Group files by variable
var_groups = defaultdict(list)

all_files = sorted(glob.glob(os.path.join(path, "*.nc")))
for file in all_files:
    try:
        ds = xr.open_dataset(os.path.join(path, file))
        var = detect_variable_name(ds)
        var_groups[var].append(ds)
    except Exception as e:
        print(f"Skipping {file}: {e}")

print(f"\nFound variables: {list(var_groups.keys())}")

for var, files in var_groups.items():
    if len(files) == 1:
        print(f"Only one file for '{var}', no need to combine.")
        continue

# Combine and save each group
    print(f"\nCombining {len(files)} files for variable '{var}'...")
    try:
        combined = xr.concat(files, dim='valid_time')
        output_path = os.path.join(output_folder, f"ERA5_1994-2025_{var}.nc") # Change output file name
        combined.to_netcdf(output_path)
        print(f"Saved to {output_path}")
    except Exception as e:
        print(f"Error combining {var}: {e}")