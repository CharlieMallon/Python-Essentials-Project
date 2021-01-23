# from requests_html import HTMLSession
# session = HTMLSession()

from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("telford", "England", "html,css,js,python")