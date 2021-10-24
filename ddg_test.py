# CSC256-0002

# initial imports

import pytest
import requests

# create a list of presidents for later, excluding duplicate last names

presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Jackson', 'Van Buren',
                'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
                'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'McKinley',
                'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman',
                'Eisenhower', 'Kennedy', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
                'Clinton', 'Obama', 'Trump', 'Biden']
# constant DDG url

url_ddg = "https://api.duckduckgo.com"

# example test to verify the data is coming from DDG

def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

# main criteria of this lesson, that all the presidents appear in the response

def test_presidents():

    # request with the presidents in the query
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    # separate the RelatedTopics section into a new list for easier iteration
    topics = rsp_data['RelatedTopics']
    # create a list of successful matches to compare to the original list in the final assertion
    successes = []

    # iterate over the entire list of presidents to see if they appear in the RelatedTopics text field
    for p in presidents:
        # counter variable since you need to slice the list by integers at first
        counter = 0
        # iterate over the list of entries in RelatedTopics to see if the president appears
        for t in topics:

            # president matches, append their name to the success list
            if p in topics[counter]['Text']:
                successes.append(p)
                break # end loop execution and move to the next president

            # assuming the counter hasn't exceeded the total topics available (which shouldn't happen),
            # increment the counter and search the next RelatedTopics entry
            elif counter < len(topics):
                counter += 1

            # worst-case scenario, the president was not found in the entire list (counter > len(topics))
            else:
                print('An error occurred.')
                break

    # if all presidents were found, the list of successes should match the original list of presidents, making this test valid
    assert successes == presidents