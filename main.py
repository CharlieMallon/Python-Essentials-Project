from scraper import JobScrape

mon = JobScrape("monster")

mon_results = mon.get_jobs("telford", "England", "python,django")