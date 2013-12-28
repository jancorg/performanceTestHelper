import mm_performance_test_helpers
from mm_performance_test_helpers import  PerformanceRequest
import time
import mechanize
from configobj import ConfigObj


class Transaction(object):
    def run(self):
    	tittle = "Simple_Logon"
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
        self.custom_timers[tittle] = latency_logon + latency_home
		
        request.logoutWithTime(config['site'] + '/logout')

        time.sleep(1)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers

