"""
PROBLEM 54
Write a program to print the output of the following poblem statement :-
http://forsk.in/images/Forsk_logo_bw.png"
Download the image from the url above and store in your workking diretory with the same
name as the image name.
Do not hardcode the name of the image?
"""

import requests
forsk = "http://forsk.in/images/Forsk_logo_bw.png"
source = requests.get(forsk)
file = open("Forsk_logo_bw.png",'wb')
file.write(source.content)
file.close()