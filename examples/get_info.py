# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import SandCage

sc = SandCage(api_key='<INSERT_API_KEY>')
# option 1
res1 = sc.get_info({
    'request_id': '<INSERT_REQ_ID>'  # conditional
})

print(res1.status_code)
print(res1.json())

# option 2
res2 = sc.get_info({
    'files': [{'file_token': '<INSERT_FILE_TOKEN>'}]  # conditional
})

print(res2.status_code)
print(res2.json())
