# JSONPlaceholder testing

## Setup
Requires Python 3.6+ (for f-strings) and requests module (requirements.txt file included for ease of installation).

To run, should just be able to execute form the command line (e.g. > python .\Tests.py).

## Notes

* Chose to use python and the unittest and requests modules for ease of setup and because I was already familiar with them.
* Ideally, would use api client generation code such as swagger such tool to facilitate testing amongst other benefits. Wrote some basic helper functions to try and get some of the way there.
* In terms of coverage, tried to cover every endpoint (with just a basic get request, check expected count), and tried to exercise all the verbs (though just against posts endpoint). Get basic CRUD (create/update/delete) cycle for that purpose.
* Variations from RESTfulness all to do with data being static (i.e. impossible to actually create/update/delete anything.)
* Though individual call should mimic expected responses as per the docs, I found I was getting errors with my PUT/Patch methods, probably for data input reasons of some kind I didn't have time to debug.
