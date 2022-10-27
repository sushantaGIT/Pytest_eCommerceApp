pytest -v -m "sanity" --html=./Reports/report_sanity.html testCases/
rem pytest -v -m "regression" --html=./Reports/report_sanity.html testCases/
rem pytest -v -m "sanity and regression" --html=./Reports/report_sanity.html testCases/
rem pytest -v -m "sanity or regression" --html=./Reports/report_sanity.html testCases/
