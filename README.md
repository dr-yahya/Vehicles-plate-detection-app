# anpr_backend
_____________________________________________________________

### Kill process at specific port 
```Python
sudo kill -9 `sudo lsof -t -i:9001`
```
_____________________________________________________________

### Download VS code

```Python
sudo snap install code --classic
```
_____________________________________________________________

### Download PyCharm

```Python
sudo snap install pycharm-community --classic
```
_____________________________________________________________

### Download VLC

```Python
sudo apt-get install vlc
```
_____________________________________________________________


### Download git

```Python
sudo apt install git-all
```

_____________________________________________________________

### Clone and install requirments (updated on 6-11-2021)

```Python

git clone https://github.com/karismasys/anpr_backend.git

apt install python3-pip

pip3 install -r requiremnets.txt

pip install flask
pip install flask_migrate
pip install base32_crockford
pip install psutil

pip install numpy
pip3 install paho-mqtt python-etcd

```
_____________________________________________________________

### Activate Licence (updated on 24-11-2021)

```Python
cp *.so /usr/lib/

./DTKLPRActivate

Lisense key: xxxx-xxxx-xxxx-xxxx-xxxxx
Channels: 4
Comments: ANPR-SERVER2
Expiration date: 2021-12-23
```
_____________________________________________________________

### Install postgres (updated on 6-11-2021)

```Python
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists:
sudo apt-get update

# Install the latest version of PostgreSQL.
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql':
sudo apt-get -y install postgresql

#
# Setup the repository
#

apt install curl

# Install the public key for the repository (if not done previously):
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add

# Create the repository configuration file:
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

#
# Install pgAdmin
#

# Install for both desktop and web modes:
sudo apt install pgadmin4

#changing password postgres
sudo -u postgres psql

ALTER USER postgres PASSWORD 'postgres';
```
_____________________________________________________________

### Intiating the database (updated on 6-11-2021)

```Python
export FLASK_APP=anpr_app/__init__.py

flask db init

sudo apt-get install libpq-dev
pip install psycopg2

#create database with name 'anpr'

flask db migrate
flask db upgrade


```
_____________________________________________________________

### For fun settings :)

Change Ubuntu screen resolution and aspect ration
```Python
xrandr --listactivemonitors

xrandr

xrandr --newmode "1680x1000_60.00"  139.25  1680 1784 1960 2240  1000 1003 1013 1038 -hsync +vsync

xrandr --addmode DP-1 "1680x1000_60.00"

xrandr --output VGA-1 --mode 1680x1000

```
_____________________________________________________________


## Backend documentations
_____________________________________________________________

### Requirements

Installing requirements for python project.
```Python
pip3 install -r requirements.txt
```
_____________________________________________________________

### Node js server
_____________________________________________________________

Node js server base url: http://10.224.82.101:8080
_____________________________________________________________

### Video streaming from file:

(updated on 8-9-2021)

Please use this url to connect to node js server "http://10.224.82.101:8080"
Then you can use this api tostart the video streaming:
url: "/<video_path>"

Example: http://10.224.82.101:8080/sam.mp4
_____________________________________________________________

### Flask app server

```Python
Flask app base url: http://10.224.82.101:5000
```

_____________________________________________________________

### How to install MQTT (updated on 5-11-2021)

Update Ubuntu's package list and install the latest Mosquitto Broker available from it
```Python
sudo apt-get update
sudo apt-get install mosquitto
```

Install MQTT clients
```Python
sudo apt-get install mosquitto-clients
```

Create a configuration file for Mosquitto pointing to the password file we have just created.
```Python
sudo nano /etc/mosquitto/conf.d/default.conf
```

This will open an empty file. Paste the following into it.
```Python
port 1883 0.0.0.0
protocol mqtt

# Websockets

listener 9001
protocol websockets
allow_anonymous true
```
Save and exit the text editor with "Ctrl+O", "Enter" and "Ctrl+X".

Now restart Mosquitto server and test our changes.
```Python
sudo systemctl restart mosquitto
```

Open ports in firewall
```Python
sudo ufw status
sudo ufw enable
sudo ufw allow 9001
sudo ufw allow 1883

```
_____________________________________________________________

### MQTT credentials (updated on 10-11-2021)

```Python
broker = '192.168.0.20'
port = 9001
```
_____________________________________________________________

### Top vehicle

(updated on 10-11-2021)

mqtt_topic = 'mqtt/top_vehicles'

Response:

```Python
{'time_stamp': '1631091581', 'plate_no': 'PPD9778', 'confidence': '100', 'direction': '153', 'plate_image_path': '2021-09-08/p_PPD9778_4_1_2021-09-08 16:59:41.png', 'frame_image_path': '2021-09-08/PPD9778_4_1_2021-09-08 16:59:41.png', 'lane_id': 4, 'plate_type': '1', 'vid_width': '1920', 'vid_height': '1080', 'vid_fps': '25', 'vid_four_cc': '875967080'}
```
Width of the video stream in pixels. If the video stream is not started, the return value is 0.

Height of the video stream in pixels. If the video stream is not started, the return value is 0.

Frames per second (FPS) of the video stream. If the video stream is not started, the return value is 0.

FOURCC code (32 bit integer) of the video stream. If the video stream is not started, the return value is 0.
____________________________________________________________

### Dashboard 

Get Dashboard stats . (updated on 10-11-2021)
```Python
mqtt_topic = 'mqtt/dashboard'
api_url = '/get_dashboard'
```
Response : List object that contains: 

1. CPU usage, RAM usage, and UP time
2. Bandwidth 
3. Average Confidence

```Python
[{'cpu_usage': 3.9, 'memory_usage': 5.8, 'memory_used': 3716.14453125, 'memory_total': 64369.38671875, 'up_time': '3:09:32.129885'}, {'upload_rate': 2.953277587890625, 'download_rate': 1.9584121704101562}, [{'avg': 95, 'lane_id': 6}, {'avg': 78, 'lane_id': 5}, {'avg': 93, 'lane_id': 4}], [{'lane_id': 1, 'lane_uid': 'K06', 'data': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, ...]]
```
Note 1: the memory is in MB.
Node 2: these data is sent every 1 second
_____________________________________________________________

Get statistics for the graph (GET). (updated on 6-9-2021) (format of the response updated upon a request from Amira)
```Python
url = '/get_statistics'
```
statistics about the current day only;
   
``` 

Response : JSON object that contains: 
```Python
[{"lane_id": 1, "lane_uid": "", "data": [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}]
``` 
______________________________________________________________

### Vehicle

Get vehicles data [GET](updated on 10-11-2021): 
```Python
/get_vehicles
```

Response : list of JSON objects that contains:

```Python
{"plate_no": "WYR733", "id": 10026, "uid": "480K159K5T5CS3M0", "time_stamp": "1630922928", "confidence": 95, "direction": -1, "plate_image_path": "http://10.224.82.62:5000/public/2021-09-06/p_WYR733_1_1_2021-09-06 18:08:48.png", "frame_image_path": "http://10.224.82.62:5000/public/2021-09-06/WYR733_1_1_2021-09-06 18:08:48.png", "lane_id": 1, "plate_type": "1"}
```
______________________________________________________________

Search function [GET](updated on 10-11-2021): 
```Python
/search_vehicles?lane_id=1&start=some&end=some
```
Example:
```Python
http://10.224.82.101:5000/search_vehicles?lane_id=1&start=2021-11-09 20:17:08&end=2021-11-09 22:50:21
```
Response : list of JSON objects that contains:
```Python
{"plate_no": "WYR733", "id": 10026, "uid": "480K159K5T5CS3M0", "time_stamp": "1630922928", "confidence": 95, "direction": -1, "plate_image_path": "http://10.224.82.62:5000/public/2021-09-06/p_WYR733_1_1_2021-09-06 18:08:48.png", "frame_image_path": "http://10.224.82.62:5000/public/2021-09-06/WYR733_1_1_2021-09-06 18:08:48.png", "lane_id": 1, "plate_type": "1"}
```
Search API takes 3 parameters:    
lane_id : int, example: 1
start : string, in this format '%Y-%m-%d %H:%M:%S', example: '2021-11-09 20:17:08'
end : string, in this format '%Y-%m-%d %H:%M:%S', example: '2021-11-09 22:50:21'
______________________________________________________________

### Zones

Get all zones data for a specific lane [GET] (for listing) (updated on 6-9-2021): 
```Python
/get_zones_by_lane/lane_id
```
Parameters: 
camera_id : serial

Response : List of JSON objects that contains:

```Python
[]
```
______________________________________________________________

Get all zones data [GET] (for listing) (updated on 6-9-2021): 
```Python
/get_zones
```
Response : List of JSON objects that contains:

```Python
[{"id": 1, "name": "zone 1", "time_stamp": null, "coordinates": "0.3, 0.2, 0.6, 0.1, 0.8, 0.5, 0.6, 0.9, 0.3, 0.8", "lane_id": 1}]
```
______________________________________________________________

Add new zone record [POST] (updated on 6-9-2021): 
```Python
'/add_zone'
```
Takes these POST request parameters:

```Python
JSON Object that contains:
    "name": string
    "coordinates": string
    "lane_id": serial
```

Returns: 

```Python
'success', 204 or 'error', 400
```
______________________________________________________________

Edit zones [PUT] (updated on 6-9-2021):

url '/edit_zone/<zone_id>'

url parameters: 
zone_id = serial

body parameter: 
```Python
JSON Object that conrains these members:
    "name": string
    "coordinates": string
    "lane_id": serial
```
returns:
```Python
'success' or 'error' 
```
____________________________________________________________

Delete zone [DELETE] (updated on 6-9-2021):

url '/delete_zone/<zone_id>'

url parameter: 
```Python
zone_id = serial
```
returns:
```Python
'success' or 'error' 
```
____________________________________________________________

### Get image

Get image [GET](updated on 29-8-2021): 
```Python
url: <image_path>
```
image_path : string

______________________________________________________________

### Plaza

Get all plaza records [GET] (updated on 6-9-2021):

url '/get_plazas'

returns: 
```Python
[{"id": 1, "name": "sepang", "uid": "480"}, {"id": 2, "name": "penang", "uid": "490"}]
```
______________________________________________________________

Add new paza record [POST] (updated on 6-9-2021):

url '/add_plaza'

parameter: 
```Python
JSON Object that conrains:
    "name" = string
    "uid" = string
```
returns:
```Python
'success' or 'error'
```
____________________________________________________________

Edit paza record [PUT] (updated on 6-9-2021):

url '/edit_plaza/<plaza_id>'

url parameters: 
id = serial

body parameters: 
```Python
JSON Object that conrains these members:
    "name" = string
    "uid" = string
```
returns:
```Python
'success' or 'error'
```
____________________________________________________________

Delete plaza record [DELETE] (updated on 6-9-2021):

url '/delete_plaza/<plaza_id>'

url parameter: 
```Python
id = serial
```
returns:
```Python
'success' or 'error'
```
____________________________________________________________

### Lanes
____________________________________________________________

Get All lanes [GET] (updated on 6-9-2021):

url '/get_lanes'

returns:
```Python
[{"id": 1, "name": "lane1", "source": 1, "video_path": null, "stream_link": null, "username": null, "password": null, "plaza_id": 1, "uid": "K15", "activated": 1}]
```
____________________________________________________________

Add lane [POST] (updated on 6-9-2021):

url '/add_lane'

parameter: 
```Python
form-data that conrains:
    "activated": "1" for active or "0" for inactive
    "name": string
    "password": string
    "plaza_id": int
    "source": "1" for rtsp or "0" for file
    "stream_link": string
    "uid": string
    "username": string
    "video_file": file
```
returns:
```Python
'success' or 'error' 
```
____________________________________________________________

Edit lane [PUT] (updated on 6-9-2021):

url '/edit_lane/<lane_id>'

url parameters: 
lane_id = serial

body parameter: 
```Python
JSON Object that conrains:
    "activated": 1 for active or 0 for inactive
    "name": string
    "password": string
    "plaza_id": int
    "source": 1 for rtsp or 0 for file
    "stream_link": string
    "uid": string
    "username": string
    "video_file": file
```
returns:
```Python
'success' or 'error' 
```
____________________________________________________________

Delete lane [DELETE] (updated on 6-9-2021):

url '/delete_lane/<lane_id>'

url parameter: 
```Python
lane_id = serial 
```
returns:
```Python
'success' or 'error' 
```
____________________________________________________________

End of Docs 

