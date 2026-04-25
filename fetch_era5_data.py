#fetch_era5_data.py

# This is the API request that tells CDS what ERA5 reanalysis data to download. Edit this script!

import cdsapi

def fetch_data(variable, years, time_step):
    
    dataset = "reanalysis-era5-single-levels"
    
    request = {
        'product_type': ['reanalysis'],
        'variable': [variable],
        'year': [str(year) for year in range(int(years[0]), int(years[1]) + 1)], # This allows for automation over different years, don't change! 
        'month': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
        ],
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00','01:00','02:00','03:00','04:00','05:00',
            '06:00','07:00','08:00','09:00','10:00','11:00',
            '12:00','13:00','14:00','15:00','16:00','17:00',
            '18:00','19:00','20:00','21:00','22:00','23:00'
        ] if time_step == 'hourly' else ['00:00', '06:00', '12:00', '18:00'], # 6-hourly timesteps
        'data_format': 'netcdf',
        'download_format': 'unarchived',
        'area': [42.250, -79.000, 42.000, -78.750] # North, West, South, East for your site.
    }

    filename = f'ERA5_{years[0]}-{years[1]}_{time_step}_{variable}.nc'

    client = cdsapi.Client()
    client.retrieve(dataset, request).download(filename)

    print(f"Data for {variable} ({time_step}) from {years[0]} to {years[1]} saved as {filename}")

if __name__ == "__main__":
    fetch_data('sp', ['2024', '2025'], '6-hourly')  # RGT WAS HERE