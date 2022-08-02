import json
import time
from datetime import datetime

from anpr_app.db_helper.vehicle import vehicle_db_helper
import mqtt_publish

partial_result = vehicle_db_helper.get_vehicles()

client = mqtt_publish.connect_mqtt()
client.loop_start()

# print("result", result)
# result_json = json.loads(partial_result)
# print("result_json", result_json)
for data in partial_result:
    # print("data", data)
    time.sleep(10)
    topic = "mqtt/top_vehicles"
    timestamp = datetime.now()
    print(timestamp)
    dt_object = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    data["time_stamp"] = str(dt_object)
    print(data)
    result = client.publish(topic, json.dumps(data))
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Lane {data['lane_id']} vehicle {data['plate_no']} to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")
