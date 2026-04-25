#automate_fetch.py

# This script edits fetch_era5_data.py so that it cycles through the list of variables in line 48
# Only need to edit the list of variables (line 31) and year_batches (line 37) and years (line 55) in this script.

import subprocess
from datetime import datetime

def modify_script(variable, years, time_step):
    script_path = 'fetch_era5_data.py'
    
    with open(script_path, 'r') as file:
        lines = file.readlines()
    
    with open(script_path, 'w') as file:
        for line in lines:
            if "# RGT WAS HERE" in line:
                print(f"Modifying script to fetch data for: {variable}")
                file.write(f"    fetch_data('{variable}', {years}, '{time_step}')  # RGT WAS HERE\n")
            else:
                file.write(line)

def run_script():
    print("Running script...")
    result = subprocess.run(['python', 'fetch_era5_data.py'], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    # List of variables to fetch from the API
    variables = ['2d', '2t', '10u', '10v', 'sp', 'ssrd', 'strd', 'tp']

    for variable in variables:
        if variable in ['tp', 'strd', 'ssrd']: # Accumulated variables
            time_step = 'hourly'
            #################################################
            #### ADJUST THE YEAR BATCHES WITH YOUR YEARS ####
            year_batches = [
                ['1994', '1995'],
                ['1996', '1997'],
                ['1998', '1999'],
                ['2000', '2001'],
                ['2002', '2003'],
                ['2004', '2005'],
                ['2006', '2007'],
                ['2008', '2009'],
                ['2010', '2011'],
                ['2012', '2013'],
                ['2014', '2015'],
                ['2016', '2017'],
                ['2018', '2019'],
                ['2020', '2021'],
                ['2022', '2023'],
                ['2024', '2025']
            ]
            ##################################################
            
            for years in year_batches:
                start_time = datetime.now()
                print(f"Processing variable: {variable} for years {years[0]} to {years[1]}")
                print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
                modify_script(variable, years, time_step)
                run_script()
                end_time = datetime.now()
                print(f"End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Finished processing variable: {variable} for years {years[0]} to {years[1]}")
                print("-" * 40)

        else:
            time_step = '6-hourly'
            #################################################
            #### ADJUST THE YEAR BATCHES WITH YOUR YEARS ####
            year_batches = [
                ['1994', '1998'],
                ['1999', '2003'],
                ['2004', '2008'],
                ['2009', '2013'],
                ['2014', '2018'],
                ['2019', '2023'],
                ['2024', '2025']
            ]
            #################################################
            
            for years in year_batches:
                start_time = datetime.now()
                print(f"Processing variable: {variable} for years {years[0]} to {years[1]}")
                print(f"Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
                modify_script(variable, years, time_step)
                run_script()
                end_time = datetime.now()
                print(f"End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"Finished processing variable: {variable} for years {years[0]} to {years[1]}")
                print("-" * 40)