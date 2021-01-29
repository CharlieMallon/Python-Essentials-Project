from scraper import JobScrape

mon = JobScrape("monster")

print("Working...")

mon_results = mon.get_jobs("Telford", "uk", "python,developer")

for result in mon_results:
    print(f"Job Title:   {result['title']}")
    print(f"Company:     {result['company']}")
    print(f"URL:         {result['url']}")

    if"description" in result:
        print(f"Description:")
        print(f"{result['description']}")
    
    print("----------")

print(f"{len(mon_results)} jobs found")

# print(mon_results)

""" How to work out what is being returned"""

# from requests_html import HTMLSession

# s = HTMLSession()

# r = s.get("url goes here")

# print(r.html.html)

# search through the given data for the bit you want form that site