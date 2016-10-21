# -*- coding: utf-8 -*-
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src import SandCage

sc = SandCage(api_key='<INSERT_API_KEY>')
result = sc.schedule_files({
    'jobs': [
        {
            "url": "http://cdn.sandcage.com/p/a/img/logo.jpg",
            "tasks": [
                {
                    "actions": "save"
                },
                {
                    "actions": "resize",
                    "filename": "hello_world.jpg",
                    "width": 200
                }
            ]
        },
        {
            "url": "http://cdn.sandcage.com/p/a/img/header_404.png",
            "tasks": [
                {
                    "actions": "resize",
                    "height": 30
                }
            ]
        }
    ],
    'callback_url': None  # optional
})

print(result.status_code)
print(result.json())
