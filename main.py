from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("Telford", "uk", "python,developer")

print(mon_results)