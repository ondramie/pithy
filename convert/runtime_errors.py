#!/usr/bin/python3

''' This class captures command errors that were used to determine the 
    accuracy of queries used in elasticsearch database.  There are simple
    errors and more advanced errors that were used for comparison.  
'''
class StackErrors:
    def __init__(self): 
        
        # small errors
        self.runtime = "RuntimeError"
        self.value   = "ValueError"
        self.zero    = "ZeroDivisionError"

        # large errors
        self.large_trace_folders = """
        Traceback (most recent call last):
        File "/home/ubuntu/.local/lib/python3.6/site-packages/elasticsearch/connection/http_urllib3.py", line 172, in perform_request
        response = self.pool.urlopen(method, url, body, retries=Retry(False), headers=request_headers, **kw)
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 638, in urlopen
        _stacktrace=sys.exc_info()[2])
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/util/retry.py", line 343, in increment
        raise six.reraise(type(error), error, _stacktrace)
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/packages/six.py", line 686, in reraise
        raise value
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 600, in urlopenchunked=chunked)
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 354, in _make_request
        conn.request(method, url, **httplib_request_kw)
        File "/usr/lib/python3.6/http/client.py", line 1239, in request
        self._send_request(method, url, body, headers, encode_chunked)
        File "/usr/lib/python3.6/http/client.py", line 1285, in _send_request
        self.endheaders(body, encode_chunked=encode_chunked)
        File "/usr/lib/python3.6/http/client.py", line 1234, in endheaders
        self._send_output(message_body, encode_chunked=encode_chunked)
        File "/usr/lib/python3.6/http/client.py", line 1026, in _send_output
        self.send(msg)
        File "/usr/lib/python3.6/http/client.py", line 964, in send
        self.connect()
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/connection.py", line 196, in connect
        conn = self._new_conn()
        File "/home/ubuntu/.local/lib/python3.6/site-packages/urllib3/connection.py", line 176, in _new_conn
        (self.host, self.timeout))
        urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPConnection object at 0x7fd7e46a2fd0>, 'Connection to 54.209.55.117 timed out. (connect timeout=10)')
        Connection <Urllib3HttpConnection: http://54.209.55.117:9200> has failed for 1 times in a row, putting on 60 second timeout.
        """ 

        self.large_trace_nofolders = """
        Traceback (most recent call last):
        response = self.pool.urlopen(method, url, body, retries=Retry(False), headers=request_headers, **kw)
        _stacktrace=sys.exc_info()[2])
        raise six.reraise(type(error), error, _stacktrace)
        raise value
        conn.request(method, url, **httplib_request_kw)
        self._send_request(method, url, body, headers, encode_chunked)
        self.endheaders(body, encode_chunked=encode_chunked)
        self._send_output(message_body, encode_chunked=encode_chunked)
        self.send(msg)
        self.connect()
        conn = self._new_conn()
        (self.host, self.timeout))
        urllib3.exceptions.ConnectTimeoutError: (<urllib3.connection.HTTPConnection object at 0x7fd7e46a2fd0>, 'Connection to 54.209.55.117 timed out. (connect timeout=10)')
        Connection <Urllib3HttpConnection: http://54.209.55.117:9200> has failed for 1 times in a row, putting on 60 second timeout.
        """