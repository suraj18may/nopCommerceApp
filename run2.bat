pytest -v -s --html=Reports\report4.html testCases\test_SearchCustomerEmail.py --browser chrome
rem pytest -v -s --html=Reports\report5.html testCases\test_SearchCustomerByName.py --browser chrome
rem pytest -v -s -m "sanity" --html=Reports\report5.html testCases\test_SearchCustomerByName.py --browser chrome