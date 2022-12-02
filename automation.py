from inspect import getframeinfo, stack
import requests
import sys
import os
import shutil
from datetime import datetime

# Session token used for authentication
from credlib import SESSION_TOKEN


# Method to exit script and print issue
def failed(issue=""):
    line = getframeinfo(stack()[1][0]).lineno
    print(f"automation.py:{line} Error: {issue}")
    exit()


# Day selection
args = sys.argv
if len(args) < 3:
    current_day = datetime.today()
    day, month, year = current_day.day, current_day.month, current_day.year
    if  month != 12 or day > 25:
        failed("No date provided and no challenge today")
else:
    year, day = args[1:3]
    if not (2015 <= int(year) <= datetime.today().year or 1 <= int(day) <= 25):
        failed(f"Invalid day (year-day): {year}-{day}")

year_path = f"{year}"
day_path = f"{year_path}/Day {day}"

# Check if already obtained
force_download = "-f" in args
year_exists = os.path.isdir(year_path)
day_exists = os.path.isdir(day_path)

# Create folders
if not year_exists:
    os.mkdir(year_path)

if not day_exists:
    os.mkdir(day_path)
elif not force_download:
    failed("Files are already present")


# Get input
response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session":SESSION_TOKEN, "User-Agent":"https://github.com/Rickerd1234/Advent-of-Code/blob/main/automation.py by Discord: Rickerd1234 hashtag 6169"})
if response.status_code != 200:
    failed(f"Failed to download {year}-{day}: "+ response.text)


# Store input
inp = response.text
with open(day_path+"/inp.txt", "w+") as file:
    file.write(inp[:-1])


# Create template
if not day_exists:
    shutil.copyfile("template.py", day_path+f"/{day}.py")

print(f"Finished preparing {year}-{day}")