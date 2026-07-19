import pandas as pd
import numpy as np
import re
from openpyxl import load_workbook



point_s = pd.read_excel('config/Major_brands_PS.xlsx', sheet_name='PS')

point_s_allowed_brand = list(point_s['PS_allowed'])

mb = pd.read_excel('config/Major_brands_PS.xlsx', sheet_name='MB')

mb_allowed_brand = list(mb['MB_Allowed'])

