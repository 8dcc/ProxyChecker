## Proxy checker
Simple python script to monitor your current IP.

You can edit the script to:
* Add a delay by setting the `Delay` variable to an integer
* Enable the log function by setting the `MakeLog` variable to `True`. This will create a file called **proxyTester.log** this file will contain the ips the program logged and the time the request was made.

### Instalation

`git clone https://github.com/r4v10l1/ProxyChecker`

`cd ProxyChecker`

`python -m pip install requests`  The script uses requests and time.

`python proxyTester.py`
