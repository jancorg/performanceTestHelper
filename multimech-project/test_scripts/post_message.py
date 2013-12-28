import mm_performance_test_helpers
from mm_performance_test_helpers import  PerformanceRequest
import time
import mechanize
from configobj import ConfigObj


class Transaction(object):
    def run(self):
    	title = "Post_Test"
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

        request.request = request.browser.geturl() + "/blog/performanceTests.test1"
        latency_edit_post = request.getTimeForRequest()
        request.request = request.browser.geturl() + "/blog/editPost"
        latency_edit_post = request.getTimeForRequest()

        start_time=time.time()
        request.browser.select_form(nr=2)
        request.browser["title"] = "Performance test at " + time.time()
        request.browser["body"] = "Performace test message"
        request.browser.submit()
        lantency_publish_post = time.time() - start_time

        self.custom_timers[title] = latency_logon + latency_home + latency_edit_post + lantency_publish_post
		
        request.logoutWithTime(config['site'] + '/logout')

        time.sleep(2)




if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers


