#!/usr/local/bin/python3 -tt
"""
Program to scrape NBA player data from https://www.basketball-reference.com/.

Author: Gordon Lim
Last Edit: 2 May 2018 
"""

import NBAanalysissetup
import sys

def main():

    firstyear = 1980
    if (len(sys.argv) > 1):
        firstyear_str = sys.argv[1]
        firstyear = int(firstyear_str)    
    
    lastyear = 2019
    if (len(sys.argv) > 2):
        lastyear_str = sys.argv[2]
        lastyear = int(lastyear_str)    
    
    for year in range(firstyear, lastyear):
        NBAanalysissetup.NBA_totals_scraper(year)
        NBAanalysissetup.NBA_advanced_scraper(year)
        if (year != 1999):
            NBAanalysissetup.NBA_AllStar_scraper(year)
        NBAanalysissetup.NBA_teamstats_scraper(year)
        NBAanalysissetup.NBA_teammisc_scraper(year)
        NBAanalysissetup.NBA_rookies_scraper(year)
        NBAanalysissetup.NBA_MVP_scraper(year)
        NBAanalysissetup.NBA_ROY_scraper(year)
        if (year >= 1983):
            NBAanalysissetup.NBA_DPOY_scraper(year)
        if (year >= 1984):
            NBAanalysissetup.NBA_SMOY_scraper(year)

    return 0

if __name__ == '__main__':
    main()
