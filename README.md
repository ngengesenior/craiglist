# Craiglist Job scraper

The project makes use of for spiders build in stages using scrapy python library to scrape
http://craiglist.org. The first spider (in [job-titles.py](craiglist/spiders/jobs-titles.py)) starts
by scraping just the job titles while the last and more advanced [jobs_all_and_details.py](craiglist/spiders/jobs_all_and_details.py)
detail description of the jobs as well.  
