# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 12:18:08 2023

@author: jkris
"""

import snipsearch as ss

def test():
    """test."""
    search = [
        "search",
        "pyfile",
        "pandas",
        "sphinx",
        "database",
    ]
    genpath = R"C:\Users\jkris\OneDrive\2022_onward\2023\python\myrepo\generic"
    all_results = ss.search_all_pyfiles(genpath, search)
    return all_results


def main():
    """main."""
    numprint = 6
    results = test()
    resultstr = ss.get_result_str(results, number=numprint)
    print(resultstr)
    #run("test()", sort="tottime")
    #time1 = timeit(test, number=10)
    #time2 = timeit(test2, number=10)
    #print(f"\ntime1: {time1}\ntime2: {time2}\n")


if __name__ == "__main__":
    main()