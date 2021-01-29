from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("Telford", "uk", "python,developer")

print(mon_results)

""" How to work out what is being returned"""

# from requests_html import HTMLSession

# s = HTMLSession()

# r = s.get("url goes here")

# print(r.html.html)

# search through the given data for the bit you want form that site