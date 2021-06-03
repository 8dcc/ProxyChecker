# ProxyTester. https://github.com/r4v10l1

try:
    import requests, time
except Exception:
    print(" Could not import the necesary modules: requests, time")
    exit(1)

#####  EDIT ME  #####
Delay = False       #  Will change the delay between requests if the var type is int
MakeLog = True      #  Will make a proxyTester.log file if the var is set to True
#####################

Try_count = 1
while True:
    r = requests.get("https://api.ipify.org", allow_redirects=True)
    IP_address = r.text  # Store the requests content (the ip address) into a variable
    print(f" [{Try_count}] Returned: {IP_address}")
    if MakeLog == True:  #  Will make a proxyTester.log file if the var is set to True
        with open("proxyTester.log", "a") as LogFile:  # Append to the log file
            LogFile.write("[%s] %s" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), IP_address))  # Append the time and IP into a log
            LogFile.write("\n")
    if type(Delay) == int:  #  Will change the delay between requests if the var type is int
        time.sleep(Delay)
    Try_count += 1  # Add a number to the Try_count var
