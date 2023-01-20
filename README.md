# Instagram Follower Bot
A simple Python script that uses Selenium to automate the process of following Instagram users.

## Requirements
- Chrome browser
- ChromeDriver
- Python 3
- Selenium
- config.py file with your Instagram account email and password

## Installation
1. Clone the repository
```sh
git clone https://github.com/your-username/ig-follower-bot.git

2. Install the required packages
```sh
pip install -r requirements.txt

3. Set the path of ChromeDriver in the script

## Usage

1. Run the script
```sh
python main.py

The script will open Chrome and navigate to the Instagram login page. It will then enter your email and password, log in, and navigate to the followers page of a similar account. Then it will follow all the followers of that account.

Please keep in mind that automation of following users on Instagram can be a violation of their terms of service. So you should make sure to read and understand the terms of service before interacting with any website using Selenium.

Also, as I mentioned before, you should be aware that Instagram can block your IP address after a certain number of requests are made within a short period of time. This is a common anti-scraping measure that websites use to prevent automation. So you should use a proxy server or a VPN to change your IP address and avoid getting blocked.

## Customization

You can customize the script by changing the SIMILAR_ACCOUNT variable in the script to the username of the account you want to follow the followers of.

## Note

This is for educational and testing purposes only. Do not use this script for any malicious activities.

## Created by:
Rafael Queiroz
