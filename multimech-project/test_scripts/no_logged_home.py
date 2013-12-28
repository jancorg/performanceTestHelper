import time
import mechanize
from mm_performance_test_helpers import  PerformanceRequest
from configobj import ConfigObj

class Transaction(object):
    def run(self):

        tittle = "NOT_LOGGED_HOME"
        config = ConfigObj('config.ini')
        request = PerformanceRequest(config['site'],config['http_user'],config['http_passwd'])
        request.request = config['site'] 
        latency_main = request.getTimeForRequest()

        self.custom_timers[tittle + '_main'] = latency_main

        self.custom_timers[tittle] = latency_main

        time.sleep(1)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers

