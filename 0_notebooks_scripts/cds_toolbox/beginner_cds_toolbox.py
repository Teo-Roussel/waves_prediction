import cdsapi
import xarray as xr
from urllib.request import urlopen

# import urllib3
# import certifi # Would be nice to understand this

# start the client
cds = cdsapi.Client()

# dataset you want to read
dataset = "reanalysis-era5-pressure-levels-monthly-means"

# flag to download data
download_flag = False

# api parameters
params = {
    "format": "netcdf",
    "product_type": "monthly_averaged_reanalysis",
    "variable": "temperature",
    "pressure_level": '1000',
    'year': ['2019', '2020'],
    'month': ['01', '02', '03'],
    "time": "00:00",
    "grid": [1.0, 1.0],
    "area": [90, -180, -90, 180],
}

# retrieves the path to the file
fl = cds.retrieve(dataset, params)

# download the file
if download_flag:
    fl.download("./output.nc")

# load into memory
with urlopen(fl.location) as f:
    ds = xr.open_dataset(f.read())
    print(ds)

del fl
