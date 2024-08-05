import requests
from pathlib import Path

if Path("helper_functions.py").is_file():
    print("Downloading helper_functions.py")
    request = requests.get("https://raw.githubusercontent.com/tonyzamyatin/learning-pytorch/master/fcc-course/helper_functions.py")
    with open("helper_functions.py", "wb") as f:
        f.write(request.content)