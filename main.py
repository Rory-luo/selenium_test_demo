from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# 初始化Chrome浏览器
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # 无头模式，不弹出浏览器窗口

# 使用WebDriverManager来自动下载并获取ChromeDriver路径
chrome_driver_path = ChromeDriverManager().install()
chrome_service = ChromeService(chrome_driver_path)
browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

# 打开指定网页
url = "https://blog.csdn.net/CSDN_430422/article/details/130871320?ops_request_misc=&request_id=&biz_id=102&utm_term=%E7%88%AC%E8%99%AB&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~sobaiduweb~default-0-130871320.pc_edu_default&spm=1018.2226.3001.4450"
browser.get(url)

# 等待页面加载，可以根据实际情况调整等待时间
browser.implicitly_wait(5)

# 获取页面的所有文字内容
all_text_elements = browser.find_elements(By.XPATH, "//body//text()")

# 输出文字内容
for element in all_text_elements:
    print(element.text)

# 关闭浏览器
browser.quit()

