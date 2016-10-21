# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import SandCage

sc = SandCage(api_key='<INSERT_API_KEY>')
result = sc.list_files({
    'directory': 'root',  # optional
    'page': 1,  # optional
    'results_per_page': 100  # optional
})

print(result.status_code)
print(result.json())
