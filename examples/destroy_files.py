# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import SandCage

sc = SandCage(api_key='<INSERT_API_KEY>')
result = sc.destroy_files({
    'files': [
        {'reference_id': '<INSERT_FILE_REF_ID>'},
        {'file_token': '<INSERT_FILE_TOKEN>'}
    ],
    'callback_url': None  # optional
})
