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

