from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options

server = Server('./browsermob-proxy-2.1.4/bin/browsermob-proxy')
server.start()
proxy = server.create_proxy()
print('proxy', proxy.proxy)

firefox_options = Options()
firefox_options.add_argument('--ignore-certificate-errors')
firefox_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

url = "https://www.nmpa.gov.cn/datasearch/home-index.html"


browser = webdriver.Firefox(executable_path="./geckodriver",options=firefox_options)
proxy.new_har(options={
    'captureContent': True,
    'captureHeaders': True
})


browser.get(url)
browser.get("https://www.nmpa.gov.cn/datasearch/search-result.html")

en_sub = browser.find_element_by_xpath("/html/body/div[2]/main/div[1]/div[6]/ul/li[2]/a")
en_sub.click()
ch_sub = browser.find_element_by_xpath("/html/body/div[2]/main/div[1]/div[7]/div/div[2]/input")
ch_sub.send_keys("高频切开刀")
sd_sub = browser.find_element_by_xpath("/html/body/div[2]/main/div[1]/div[7]/div/div[2]/div/button")
sd_sub.click()

result = proxy.har
for entry in result['log']['entries']:
    print(entry['request']['url'])
    print(entry['response']['content'])