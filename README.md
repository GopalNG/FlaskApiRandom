# FlaskApiRandom
Flask Based API For Generating Random File with size of downloadable

### Steps to Start App

clone the repo
```
$ python3 -m venv randomvenv
```
### For activing created virtual environment
```
$ source bin/activate   
```
### Now install all the required packages
```
$ pip install -r requirements.txt
```
### Start App
```
$ python app.py
```

## About API Endpoints
### There are Three API for the application
```
# To Generate the Random Data For File Processing
```
"/api/generate/" To Generate The File
```

# To Download The File 
```
'/api/download/<int:file_id>' file_id is generated file_id (will be return on generate api)
```

# To Get The Report
```
'/api/download/<int:file_id>' file_id is generated file_id (will be return on generate api)
```

```
## To Know Packages in requirements.txt
