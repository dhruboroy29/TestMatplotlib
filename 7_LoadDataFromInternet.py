import matplotlib.pyplot as plt
import numpy as np
import urllib
from matplotlib.dates import bytespdate2num

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'  # TESLA stock data
source_code = urllib.request.urlopen(stock_price_url).read().decode()

stock_data = []
split_source = source_code.split('\n')  # Split data into lines

# Split each line into tokens (fields)
for line in split_source[1:]:
        # [1:] ignores the header line "Date,Open,High,Low,Close,Adjusted_close,Volume" in list split_source
    split_line = line.split(',')
    if len(split_line) == 7:
        if 'values' not in line and 'labels' not in line:
            stock_data.append(line)

# Process variables
date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                                  delimiter=',',
                                                                  unpack=True,
                                                                  # %Y = full year. 2015
                                                                  # %y = partial year 15
                                                                  # %m = number month
                                                                  # %d = number day
                                                                  # %H = hours
                                                                  # %M = minutes
                                                                  # %S = seconds
                                                                  # E.g.: 12-06-2014 -> %m-%d-%Y
                                                                  converters={0: bytespdate2num('%Y-%m-%d')})
# Using mdates.strpdate2num('%Y-%m-%d') directly on Python3 returns:
# "TypeError: strptime() argument 0 must be str, not <class 'bytes'>"

plt.plot_date(date, closep, '-', label='Price')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('TESLA Stock prices')
plt.legend()
plt.show()
