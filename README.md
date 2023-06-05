# extracting-data-from-JSON
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data

<h2>Assignment 01</h2>
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1806432.json (Sum ends with 10)
You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

Sample Execution

$ python3 solution.py <br>
Enter location: http://py4e-data.dr-chuck.net/comments_42.json <br>
Retrieving http://py4e-data.dr-chuck.net/comments_42.json <br>
Retrieved 2733 characters <br>
Count: 50 <br>
Sum: 2... <br>

<h2>Assignmen 02</h2>

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py <br>
Enter location: South Federal University <br>
Retrieving http://... <br>
Retrieved 2453 characters <br>
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8 <br>

Turn In <br>

Please run your program to find the place_id for this location:

IT College of Estonia
