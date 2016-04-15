This is a small Flask website which is only meant to reproduce <a href="https://github.com/benoitc/gunicorn/issues/1210#issuecomment-210466094">this error</a> by doing a ping from the browser to the server.

## Steps to reproduce error:

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt
    gunicorn --worker-class eventlet -b 127.0.0.1:5000 -w 1 app:app
    
Then open the browser at http://127.0.0.1:5000 and see the terminal output, which should show something like this:


    016-04-15 17:01:34 [31122] [ERROR] Error handling request
    Traceback (most recent call last):
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/workers/async.py", line 45, in handle
        self.handle_request(listener, req, client, addr)
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/workers/async.py", line 102, in handle_request
        resp.close()
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/http/wsgi.py", line 369, in close
        self.send_headers()
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/http/wsgi.py", line 284, in send_headers
        tosend = self.default_headers()
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/http/wsgi.py", line 265, in default_headers
        elif self.should_close():
      File "/Users/kramer65/repos/gunicorn-error/venv/lib/python2.7/site-packages/gunicorn/http/wsgi.py", line 198, in should_close
        if self.status_code < 200 or self.status_code in (204, 304):
    AttributeError: 'Response' object has no attribute 'status_code'
