````
-------------------------------------------------------------------------------------
-> Title : Celery Notes
-> Author: @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 04/12/2022
-> Updated : 05/12/2022
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q005 : Setup redis for celery;;
-> Q004 : Celery steup project;;
-> Q003 : Why use Celery;;
-> Q002 : Celery real life applications;;
-> Q001 : What is Celery;;
-------------------------------------------------------------------------------------
````

### CELERY NOTES : BEGINNING 

-------------------------------------------------------------------------------------
### Q005 : Setup redis for celery;;

Install redis-server, like

````
---------------------------------------------------------------------------------
Shell
---------------------------------------------------------------------------------
(venv) $ sudo apt update
(venv) $ sudo apt install redis-server
(venv) $ redis-server
---------------------------------------------------------------------------------
````

This window will be your dedicated terminal window for Redis. Keep it open for
the rest of this tutorial.

````
---------------------------------------------------------------------------------
Note															            
---------------------------------------------------------------------------------
 Note: Running redis-server starts the Redis server. You run Redis as a 		
process that’s independent of Python, so you don’t need to have your virtual	
environment activated when you start it.										
---------------------------------------------------------------------------------
````

To test whether communicating with the Redis server works, start the Redis CLI
in another new terminal window:
````
---------------------------------------------------------------------------------
Shell															            
---------------------------------------------------------------------------------
 127.0.0.1:6379> ping 															
 PONG 																			
 127.0.0.1:6379>																
---------------------------------------------------------------------------------
````

After starting the Redis CLI with redis-cli, you sent the word ping to the
Redis server, which responded with an authoritative PONG. If you got this
response, then your Redis installation was successful, and Celery will be
able to communicate with Redis.

Quit the Redis CLI by pressing Ctrl+C before moving on to the next step.

Next, you’ll need a Python client to interface with Redis. Confirm that you’re
in a terminal window where your virtual environment is still active, and then
install redis-py:

````
---------------------------------------------------------------------------------
Shell															            
---------------------------------------------------------------------------------
 (venv) $ python -m pip install redis 											
---------------------------------------------------------------------------------
````

This command doesn’t install Redis on your system but only provides a Python
interface for connecting to Redis.


-------------------------------------------------------------------------------------
### Q004 : Celery steup project;;

Your first step in integrating Celery into your Django app is to install the
Celery package into your virtual environment:

> (venv) $ python -m pip install celery

Just installing Celery, however, isn’t enough. If you attempt to run the task
queue, you’ll notice that Celery first seems to start up fine but then
displays an error message that indicates that Celery can’t find a message
broker:

````
Shell															            
---------------------------------------------------------------------------------
(venv) $ python -m celery worker 									            
[ERROR/MainProcess] consumer: Cannot connect to 					            
⮑ amqp://guest:**@127.0.0.1:5672//: [Errno 61] Connection refused.            
Trying again in 2.00 seconds... (1/100)							            
---------------------------------------------------------------------------------
````
Celery needs a message broker to communicate with programs that send tasks to
the task queue. Without a broker, Celery isn’t able to receive instructions,
which is why it keeps trying to reconnect.

````
# Note 																		
---------------------------------------------------------------------------------
Note: You may notice the URL-like syntax in the target that Celery attempts 
to 	connect to. The protocol name, amqp, stands for Advanced Message Queuing		
Protocol and is the messaging protocol that Celery uses. The best-known project 
that implements AMQP natively is RabbitMQ, but Redis can also communicate using 
the protocol.													
````

Before using Celery, you’ll need to install a message broker and define a
project as a message producer. In your case, the producer is your Django app,
and the message broker will be Redis.


-------------------------------------------------------------------------------------
### Q003 : Why use Celery;;

There are two main reasons why most developers want to start using Celery:

Offloading work from your app to distributed processes that can run
independently of your app Scheduling task execution at a specific time,
sometimes as recurring events Celery is an excellent choice for both of these
use cases. It defines itself as “a task queue with focus on real-time
processing, while also supporting task scheduling” (Source).

Even though both of these functionalities are part of Celery, they’re often
addressed separately:

`Celery workers` are worker processes that run tasks independently from one
another and outside the context of your main service. 

`Celery workers` are the backbone of Celery. Even if you aim to schedule
recurring tasks using Celery beat, a Celery worker will pick up your
instructions and handle them at the scheduled time. 

`Celery beat` is a scheduler that orchestrates when to run tasks. You can 
use it to schedule periodic tasks as well. 

What Celery beat adds to the mix is a time-based scheduler for Celery
workers.

-------------------------------------------------------------------------------------
### Q002 : Celery real life applications;;

Celery isn’t only useful for web applications, but it’s certainly popular in
that context. That’s because you can efficiently tackle some everyday
situations in web development by using a distributed task queue such as
Celery:

a) `Email sending`: You may want to send an email verification, a password reset
email, or a confirmation of a form submission. Sending emails can take a
while and slow down your app, especially if it has many users.

b) `Image processing`: You might want to resize avatar images that users upload
or apply some encoding on all images that users can share on your platform.
Image processing is often a resource-intensive task that can slow down your
web app, mainly if you’re serving a large community of users.

c) `Text processing`: If you allow users to add data to your app, then you might
want to monitor their input. For example, you may want to check for profanity
in comments or translate user-submitted text to a different language.
Handling all this work in the context of your web app can significantly
impair performance.

d) `API calls and other web requests`: If you need to make web requests to
provide the service that your app offers, then you can quickly run into
unexpected wait times. This is true for rate-limited API requests just as
much as other tasks, such as web scraping. It’s often better to hand off
these requests to a different process.

e) `Data analysis`: Crunching data is notoriously resource-intensive. If your
web app analyzes data for your users, you’ll quickly see your app become
unresponsive if you’re handling all the work right within Django.

f) `Machine learning model runs`: Just like with other data analysis, waiting
for the results of machine learning operations can take a moment. Instead of
letting your users wait for the calculations to complete, you can offload
that work to Celery so they can continue browsing your web app until the
results come back.

g) `Report generation`: If you’re serving an app that allows users to generate
reports from data they provided, you’ll notice that building PDF files
doesn’t happen instantaneously. It’ll be a better user experience if you let
Celery handle that in the background instead of freezing your web app until
the report is ready for download

-------------------------------------------------------------------------------------
### Q001 : What is Celery;;

- Celery is a distributed task queue for UNIX systems. It allows you to offload
work from your Python app. 
- Once you integrate Celery into your app, you can send time-intensive tasks to 
Celery’s task queue. 
- That way, your web app can continue to respond quickly to users while Celery 
completes expensive operations asynchronously in the background.

-------------------------------------------------------------------------------------