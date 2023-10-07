# in a terminal, virtual machine or application that runs Python 
# you must install the netCDF4 library used in data science for information about geographic location
# if you want a model of NASA coordinates already tested in NetCDF (NC) format, you can in google:
# intitle:index.of + "emit" + "nasa" or "jpl" 
# rebember to use a VPN, because there are crawlers!!

pip install netCDF4
import netCDF4 as nc
import csv

# https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/EMITL2ARFL.001/EMIT_L2A_RFL_001_20220903T163129_2224611_012/EMIT_L2A_RFL_001_20220903T163129_2224611_012.nc
# https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/EMITL2ARFL.001/EMIT_L2A_RFL_001_20220903T163129_2224611_012/EMIT_L2A_MASK_001_20220903T163129_2224611_012.nc
