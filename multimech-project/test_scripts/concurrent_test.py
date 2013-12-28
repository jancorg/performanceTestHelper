import mm_performance_test_helpers
from mm_performance_test_helpers import  PerformanceRequest
import time
import mechanize
from configobj import ConfigObj


class Transaction(object):
    def run(self):
    	tittle = "Concurrent load test"
        config = ConfigObj('config.ini')
        request = PerformanceRequest(config['site'],
                                    config['http_user'],
                                    config['http_passwd'])
        request.request = config['site']
        latency_home =request.getTimeForRequest()
        self.custom_timers['Load_Home'] = latency_home
        time.sleep(2) 
  
        request.turnBrowserInstanceLogable()
        latency_logon = request.loginWithTime(config['user'],
                                            config['password']) 
        self.custom_timers['Logon'] = latency_logon
        time.sleep(2) 

        # Load a page and all its ajax calls
        request.request = config['site'] + '/that_page'
        latency_page_main = request.getTimeForRequest()

        requests_array = [
            config['site'] + '/ajax_call_1',
            config['site'] + '/ajax_call_2',
            config['site'] + '/ajax_call_3',                                 
            config['site'] + '/ajax_call_4'
            ]

        latency_ajax_parallel = request.getTimeForParallelRequests(requests_array)        

        self.custom_timers[tittle] = latency_home + latency_logon + latency_page_main + latency_ajax_parallel 

        request.logoutWithTime(config['site'] + '/logout')


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers



