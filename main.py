#############################################################################
# 만든이 : Kain7f1 (Hansol Lee)
# 생성일 : 2025-02-24
# 사용 전제 조건 : C:\Users 폴더에 현재 크롬 버전에 맞는 chromedriver.exe를 다운받아주세요

from tourney_crawler import crawl_tourney_result, crawl_tourney_meta

import crawling_tool as cr
import utility_module as util

# --------------
url_0 = "https://www.dbpia.co.kr/?language=ko_KR&hasTopBanner=true"
url_00 = "https://nooo1.tv/"
url_000 = "https://btoon82.com/webtoon?sca=%EC%97%B0%EC%9E%AC+%EC%9B%B9%ED%88%B0"

url_1 = "https://hero-7733.com/"
url_2 = "https://pan-1010.com/"
url_3 = "https://lula.sc/Main?agentCode=9966"
url_4 = "https://cms-0815.com/?ref=8823"    # 캡챠

driver = cr.get_driver()  # 크롬 웹드라이버. 드라이버 옵션 미리 설정해 두었음


driver.get(url_000)  # 타겟 url

html_source = driver.page_source
# print(html_source)
cleansed_html = util.extract_korean(html_source)
print(cleansed_html)

driver.quit()


