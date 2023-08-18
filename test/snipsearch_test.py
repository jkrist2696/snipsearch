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
    genpath = R"./../../"
    all_results = ss.search_all_pyfiles(genpath, search)
    return all_results


def main():
    """main."""
    numprint = 6
    results = test()
    resultstr = ss.get_result_str(results, number=numprint)
    print(resultstr)


if __name__ == "__main__":
    main()
