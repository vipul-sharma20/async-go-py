async-go-py
===========

Comparing Go's goroutines and Python's coroutines.

Checkout analysis at: [http://vipul.xyz/2017/09/performance-analysis-goroutine-pythons-coroutine.html](http://vipul.xyz/2017/09/performance-analysis-goroutine-pythons-coroutine.html)


Golang
------

Using `net/http` package

Python3
-------

Using `urllib3`, `requests` and `aiohttp` libraries

Analysis
--------

### Async/Sync HEAD requests (time in seconds) ###

[![oh no](http://i.imgur.com/pI2SV5J.png)](http://i.imgur.com/pI2SV5J.png)

### Async/Sync GET requests (time in seconds) ###

[![oh no](http://i.imgur.com/QoQ9o2R.png)](http://i.imgur.com/QoQ9o2R.png)

### Async/Sync HEAD requests (memory in MB) ###

[![oh no](http://i.imgur.com/hPffv48.png)](http://i.imgur.com/hPffv48.png)

### Async/Sync GET requests (memory in MB) ###

[![oh no](https://i.imgur.com/vTTn4JZ.png)](https://i.imgur.com/vTTn4JZ.png)

Thanks to
---------
People who helped me understand important concepts

* Brett Cannon: [How the heck async/await works](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/)
* Abu Ashraf Masnun: [Concurrency in Python](http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/)
* Nathan Leclaire: [Go channels](https://nathanleclaire.com/blog/2014/02/21/how-to-wait-for-all-goroutines-to-finish-executing-before-continuing-part-two-fixing-my-ooops/)
* People on Reddit :')

LICENSE
-------

This project is licensed under MIT License:

Copyright (c) 2017-2018: Vipul Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

