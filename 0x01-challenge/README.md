# 0x01-challenge

## Tasks

### 0. Server status


I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).

But I don’t know why it’s not working…

Could you look at it and fix it please?

My code is [here](https://github.com/holbertonschool/0x01-Fix_My_Code_Challenge/tree/master/status_server/)


```
$ python -m api.v1.app 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
```
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```
**Files** - status_server/



### 1. My square
I love geometry!

Look [my square](https://github.com/holbertonschool/0x01-Fix_My_Code_Challenge/blob/master/square.py), it’s perfect? No? Should I change something?

**File** - square.py
