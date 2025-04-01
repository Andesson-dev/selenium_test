# Selenium Web Automation Script

## Overview

This script uses Selenium WebDriver to automate a web browser. It connects to a remote Selenium Grid server, navigates to a specified website, finds input fields, and then closes the browser.

## Prerequisites

- Ensure you have the following installed and set up before running this script:

- Python (>=3.6)

- Selenium (pip install selenium)

- A running Selenium Grid Hub at http://selenium:4444/wd/hub

- Chrome WebDriver (if running locally)

- A web application running at http://siteweb:8000/

## Installation

- Clone this repository or copy the script to your local machine.

- Install Selenium via pip:

- pip install selenium

- Ensure your Selenium Grid is up and running.

## Usage

Run the script using:

- python script.py

- Code Explanation
  
## Notes

The script assumes that there are at least two input fields with the class form_container_input.

If Selenium Grid is not running, the script will fail to initialize the WebDriver.

Modify the command_executor URL if the Selenium Grid hub is running on a different address.

License

This project is open-source and can be modified as needed.

Troubleshooting

If the script fails to locate elements, check if the class name has changed.

If the connection to Selenium Grid fails, ensure it is running and accessible.

For SSL errors, ensure that the --ignore-ssl-errors option is correctly set.
