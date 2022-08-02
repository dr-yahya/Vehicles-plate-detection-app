from anpr_app import app
from anpr_app import config
# from anpr_app.platenumber_player import PlatenumberPlayer
# from anpr_app.controllers import queue_processes
import json
if __name__ == '__main__':

    # init plate number solution
    # PlatenumberPlayer.run()

    # init dashborad process 
    # queue_processes.init_dashboard_proc()
    
    # print("run done")
    
    app.run(host= config.SERVER_IP, port= config.SERVER_PORT, debug=True)
    