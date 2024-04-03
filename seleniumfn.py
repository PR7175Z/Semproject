from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service 
import time

options = webdriver.FirefoxOptions() 
user_agent = '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
options.add_argument(user_agent) 
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

options.add_argument("--headless") 
options.add_argument("--log-level") 
options.add_argument('--disable-application-cache') 
driver = webdriver.Firefox(options=options) 

extension1 = "D://pythonlectures//semprojectraw//include//ublock_origin-1.55.0.xpi"
driver.install_addon(extension1, temporary=True) 

def stream(MusicName, driver=driver):
	driver.get(f"https://www.youtube.com/results?search_query={MusicName}") 
	driver.implicitly_wait(0.5)
	video = driver.find_element( 
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string") 
	video.click()
	return True

def pauseAndPlay(driver=driver): 
    pauseVideo = driver.find_element( 
        "xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[1]/video") 
    driver.implicitly_wait(1) 
    pauseVideo.click() 

def playnext(driver=driver):
	nextvid = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-radio-renderer/div[1]/div[1]/ytd-thumbnail/a")
	driver.implicitly_wait(1)
	print(nextvid.get_attribute("href"))
	if '&list' in nextvid.get_attribute("href"):
		print("playlist")

def get_name(driver=driver):
	vid_title = driver.find_element(
		"xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")
	time.sleep(2)
	return vid_title.text

def stop(driver=driver): 
	driver.quit() 

if __name__ == "__main__": 
	print("Enter the name of song") 
	while True: 
		try:
			uinput = str(input()) 
			if uinput.split(" ", 1)[0] == "st": 
				songName = uinput.split(" ", 1)[1] 
				print(songName)
				stream(songName)
			elif uinput == "play":
				pauseAndPlay()
			elif uinput == 'next':
				playnext()
			elif uinput == 'name':
				get_name()
			elif uinput == "stop": 
				stop() 

			else: 
				print("invalid command") 
		except:
			stop()
