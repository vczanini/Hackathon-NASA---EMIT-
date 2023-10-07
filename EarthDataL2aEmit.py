# in a terminal, virtual machine or application that runs Python 
# you must install the netCDF4 library used in data science for information about geographic location
# if you want a model of NASA coordinates already tested in NetCDF (NC) format, you can in google:
# intitle:index.of + "emit" + "nasa" or "jpl" 
# rebember to use a VPN, because there are crawlers!!

pip install netCDF4 as nc
pip install pandas as pd
pip install os 
pip install osgeo 
from spectral.io import envi
from osgeo import gdal
import netCDF4 as nc
import csv
import numpy as np
import math
import pandas as pd
import xarray as xr
import rasterio as rio
import s3fs
from fsspec.implementations.http import HTTPFile

# https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/EMITL2ARFL.001/EMIT_L2A_RFL_001_20220903T163129_2224611_012/EMIT_L2A_RFL_001_20220903T163129_2224611_012.nc
# https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/EMITL2ARFL.001/EMIT_L2A_RFL_001_20220903T163129_2224611_012/EMIT_L2A_MASK_001_20220903T163129_2224611_012.nc
