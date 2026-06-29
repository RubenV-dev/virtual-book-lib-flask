In order to run this backend we must do the following:

Create a virtual environment:

```
python -m venv venv (windows)
python3 -m venv venv (mac)
```

Activate the environment:

```
source venv/bin/activate (MacOS/Linux)
.\venv\Scripts\activate.ps1 (Windows Powershell)
venv\Scripts\activate.bat (WIndows COmmand Prompt)
```

Install project requirements:

```
pip install -r requirements.txt
```

Run project:

```
python app.py (windows)
python3 app.py (MacOs)
```

The API will be running at:
http://localhost:5000
