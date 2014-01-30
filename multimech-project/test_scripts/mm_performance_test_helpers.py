import mechanize
import time
import threading
from urlparse import urlparse
import cookielib
import urllib2


class RequestThread(threading.Thread):
    def __init__(self,performance_request):
        threading.Thread.__init__(self)
        self.performance_request = performance_request

    def run(self):
        return self.performance_request.getTimeForRequest()

class PerformanceRequest:
	def __init__(self,site,user,passwd):
		self.user = user
		self.passwd = passwd
		self.request = site
		self.site = site
		self.latency = 0
		self.browser = self.getBrowserInstance()
		
	def getBrowserInstance(self):
		browser = mechanize.Browser(factory=mechanize.RobustFactory())
		browser.set_handle_robots(False)
		browser.addheaders = [('User-agent', 'Load/Performance Tests')]
		browser.set_handle_redirect(True)
		browser.add_password(self.site, self.user, self.passwd)
		return browser

	def turnBrowserInstanceLogable(self):
		cookie_jar = cookielib.LWPCookieJar()
		self.browser.set_cookiejar(cookie_jar)

	def loginWithTime(self,user,password):
		"""
                TODO: put non generic code outside this block
		"""
		start_timer = time.time()
		self.browser.select_form(nr=0)
		self.browser["j_username"] = user
		self.browser["j_password"] = password  
		self.browser.submit()
		return time.time() - start_timer

	def logoutWithTime(self,url):
		self.request = url
		return self.getTimeForRequest()

	def getTimeForRequest(self):
		start_time = time.time()
		try:
			resp = self.browser.open(self.request)
			resp.read()
		except urllib2.HTTPError as e:
			print str(e.code) + ": " + self.request

		self.latency = time.time() - start_time
		return self.latency

        def performParallelRequests(self):
        		
		for url in requests_array:
			threads = []
			performance_request = PerformanceRequest(url,self.user,self.passwd)
			t = RequestThread(performance_request)	
			t.start()
			threads.append(t)
		for t in threads:
			t.join()

	def getTimeForParallelRequests(self, requests_array):
		#mainThread = threading.currentThread()
		start_time = time.time()

                performParallelRequests()

		self.latency = time.time() - start_time
		return self.latency
