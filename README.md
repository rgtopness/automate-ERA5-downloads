[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19768645.svg)](https://doi.org/10.5281/zenodo.19768645)

# **automate-ERA5-downloads**
### **Need to download a bunch of climate variables from ERA5?** :earth_americas: :computer: :world_map:

##### This code automates the downloading of multiple ERA5 reanalysis climate variables using the Copernicus Data Store API. Run this code, go to sleep, and you can wake up with all the files you need for analysis, forcing models, making maps, etc.
---
### **How to use this code:**

(1) Register an account at ECMWF. This will allow you access to download data from the Copernicus Data Store. 
> https://cds.climate.copernicus.eu/

(2) Set-up the CDS API key. After loggging into your account, click your name at the upper right, click Your **Profile**, then scroll down to **API key**. <br> 
Copy the text and create your `.cdsapirc` file. <br> 

Example .cdsapirc file:
>url: https://cds.climate.copernicus.eu/api <br>
>key: YOUR_API_KEY

(3) Place this file in your home directory (example: `~/home/rgtopness/`).

(4) Install cdsapi Python library and Python, if not already installed. Here are the instructions for Windows, Mac, and Linux: 
> https://cds.climate.copernicus.eu/how-to-api <br> 
```py
$ pip install "cdsapi>=0.7.7"
```
(5) Open the Python script `fetch_era5_data.py`. This is the API request. Edit the `area` bounding box for latitudes and longitudes North, West, South, and East in line 42 to select where on the globe you want to download data from. <br> 
```py
'area': [42.250, -79.000, 42.000, -78.750] # North, West, South, East for your site.
```
> ℹ️ *Note that this code was built for **ERA5 hourly data on single levels from 1940 to present**, but could likely easily be modified for other datasets!*
>```py
>dataset = "reanalysis-era5-single-levels"
>```

(6) Open the Python script `automate_fetch.py`. This code loops over the API requests, telling the CDS to get and download your requests one by one until they are completed. <br> 

In this script, you may wish to edit line 31, which lists the variables you want to download.
```py
variables = ['2d', '2t', '10u', '10v', 'sp', 'ssrd', 'strd', 'tp']
```
> ℹ️ *Note: You can look up variable abbreviations at the documentation for the dataset here: https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=overview*

Each file downloaded will include one variable and one year at a time (due to download file size restrictions) in batches. This might change based on the size of your request (spatially and/or temporally). 

You can change which years you download in lines 38 and 73 of `automate-fetch.py`.
```py
year_batches = [
    ['1994', '1995'],
    ['1996', '1997'],
    ['1998', '1999'],
    ['2000', '2001'],
    ...
```

> ℹ️ *Note: As written, this code downloads accumulated variables (total precipitation, longwave radiation, as shortwave radiation) every hour. All other variables (i.e. air temperature, wind speed, surface pressure) are downloaded at a 6-hourly time step.*

(7) Once the file settings are changed how you want, run the `automate-fetch.py` script in your terminal. 
```py
>>> python ./automate-fetch.py
```
(8) Updates will print out as the code runs so you can keep track of what's downloading. Each file will be saved in the same directory the Python scripts are located in as follows: 
> Example file download name: ERA5_2024_2025_hourly_sp.nc

## **References:**
Hersbach, H., Bell, B., Berrisford, P., Biavati, G., Horányi, A., Muñoz Sabater, J., Nicolas, J., Peubey, C., Radu, R., Rozum, I., Schepers, D., Simmons, A., Soci, C., Dee, D., Thépaut, J-N. (2023): ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS), DOI: 10.24381/cds.adbb2d47 (Accessed on 25-04-2026).

