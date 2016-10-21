# Sandcage API python
sandcage-api-python is a python library for interfacing with SandCage's API. The API documentation can be found at https://www.sandcage.com/docs/0.2/

# Requirements
- certifi 2016.9.26
- requests 2.7.0

```
pip install -r requirements.txt
```

# Usage
```
import SandCage

sc = SandCage(api_key='<INSERT_API_KEY>')
sc.list_files()
```

more examples [here](examples/)
