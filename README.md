# Have I Been Pwned Command Line Tool

This is a small Python script which was largely copied from a great Computerphile video. I watched the video and decided to try and make my own copy while peeking at the published code as little as possible as a little lunch break hack.

The point of this tool is to take in a password, encrypt it, and then to send only the first part of that encrypted password to the Have I Been Pwned password API. The API will return a dictionary of leaked hashes which start with the same digits. Then, your computer will attempt to match your hashed password to the one found in the response. *The benefit is that at no point is your full password leaving your computer.*

# Running the script
1. You will need to have Python installed. (The code examples below are for Python 3, but 2 would probably be fine)
2. Once you have downloaded the script, it has one dependency which you may need to install: Requests.
3. If you need to install Requests, you can do this from the command line:
  `pip3 install requests`
4. To run the script:
  `python3 passwordchecker.py <insert a password to check here>`
  
  # Examples
  
