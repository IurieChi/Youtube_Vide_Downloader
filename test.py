# pip install multiprocess
# pip install selenium
# pip install webdriver_manager
# piip install time
import multiprocessing
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# A Service class is responsible
# for the starting and stopping of chromedriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# An explicit wait is a code you define
# to wait for a certain condition to occur
# before proceeding further in the code
from selenium.webdriver.support import expected_conditions as EC

# Selenium Python binding provides some convenience methods
# so you don’t have to code an expected_condition class yourself
# An expectation for checking an element is visible
# and enabled such that you can click it.
from selenium.common.exceptions import NoSuchElementException

# Thrown when element could not be found.
import time


homepage = "https://www.youtube.com/@danielchigai"
consent_button_xpath_homepage = "//button[@aria-label='Accept all']"
video_links_class_name = "yt-simple-endpoint style-scope ytd-grid-video-renderer"
consent_button_xpath = "//button[@aria-label='Accept the use of cookies and other data for the purposes described']"
ads_button_selector = "button.ytp-ad-skip-button"
mute_button_class = "ytp-mute-button"
like_button_selector = 'segmented-like-button'
replay_xpath = '//*[@title="Replay"]'
# // -> Selects nodes in the document from the current node
# that match the selection no matter where they are
# * -> Matches any element node


def get_channel_links(homepage,video_links_class_name):
    # homepage = input("Please provide channel url: ")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(homepage)
    consent_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, consent_button_xpath_homepage))
    )
    consent_button.click()
    time.sleep(3)

    #scroll page for all 
    height = driver.execute_script("return document.documentElement.scrollHeight")
    previousHeight = -1

    while previousHeight < height:
        previousHeight = height
        driver.execute_script(f'window.scrollTo(0,{height + 10000})')
        time.sleep(1)
        height = driver.execute_script("return document.documentElement.scrollHeight")
        #open page and find elements by class name.
        vidElements = driver.find_elements(By.CLASS_NAME, video_links_class_name)
        vid_urls = []
        # extract all href from the list 
        for v in vidElements:
            vid_urls.append(v.get_attribute('href'))
            time.sleep(1)
            print(v)



    # links = driver.find_elements(By.CLASS_NAME, video_links_class_name )#'//*[@id="video-title"]'
    # # print(links)
    # for link in links:
    #     print(link.get_attribute("href"))

    # link_lst = driver.find_elements(By.CLASS_NAME, video_links_class_name)
    # link_lst = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, video_links_class_name)))
    # print(link_lst)
    # links = [ link.get_attribute("href") for link in link_lst if link.get_attribute("href")]
    # print(links)
    # for link in link_lst:
    #     print(link.get_attribute('href'))
    
    # driver.close()
    # driver.quit()
    # return links



def click_skip_adds(driver):
    try:
        skip_adds_button = driver.find_element(By.CSS_SELECTOR, ads_button_selector)
        skip_adds_button.click()
    except NoSuchElementException as e:
        print("No adds button found")
        pass

def like_video(driver):
    try:
        like_video = driver.find_element(By.ID, like_button_selector)
        like_video.click()
    except NoSuchElementException as e:
        print("No Like button found")
        pass

def click_mute_button(driver):
    try:
        mute_button = driver.find_element(By.CLASS_NAME, mute_button_class)
        mute_button.click()
    except NoSuchElementException as e:
        print("Mute button not found")
        pass


def replay(driver):
    # while True:
    try:
        replay_button = driver.find_element(By.XPATH, replay_xpath)
        replay_button.click()
    except NoSuchElementException as e:
        pass #continue
    else:
        print("Replay")
        driver.execute_script(
            """document.querySelector("video").playbackRate=16;"""
        )


def run_video(link):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(link)
    time.sleep(10)
    try:
        consent = driver.find_element(By.XPATH, consent_button_xpath)
        consent.click()
        time.sleep(10)
        click_skip_adds(driver)
        time.sleep(5)
        driver.execute_script("""document.querySelector("video").playbackRate=16;""")
        time.sleep(5)
        click_mute_button(driver)
        replay(driver)
        time.sleep(30)
    except Exception as e:
        print("Exception is ", e)
        driver.close()
        driver.quit()


links = [
   
]
if __name__ == "__main__":
    links = get_channel_links(homepage, video_links_class_name)
    
    # run_video("https://www.youtube.com/watch?v=dNq0H2zkn3E&t=3s")
    # for link in links:
    #     run_video(link)
    #     print(link)
        
    # processes = []
    # for link in links[:1]:
    #     p = multiprocessing.Process(target=run_video, args=(link,))
    #     p.start()
    #     processes.append(p)

    # for p in processes:
    #     p.join()
