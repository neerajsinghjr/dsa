#!/bin/python3

import os
import re
import sys
import time
import math
import random
import asyncio, functools
from aiohttp import ClientSession

### example 1: asyncio module;;
async def cor1():
   print("cor1 start...")
   for x in range(10):
      await asyncio.sleep(2)
      cor2()
      print(f"cor1: {x}")
   print("cor1 -> end")

async def cor2():
   print("cor2 start ...")
   for y in range(5):
      await asyncio.sleep(1)
      print(f"cor2: {y}")
   print("cor2 -> end")

async def ex1main():
   loop = asyncio.get_event_loop()
   loop.run_until_complete(cor1())
   loop.run_until_complete(cor2())
   
   
### //example 1;;
   
### example 2: asyncio module;;
def trigger(event):
   # event trigger function
   print('EVENT SET')
   event.set() # wake up coroutines waiting

# event consumers
async def consumer_a(event):
   consumer_name = 'Consumer A'
   print('{} waiting'.format(consumer_name))
   await event.wait()
   print('{} triggered'.format(consumer_name))
   
async def consumer_b(event):
   consumer_name = 'Consumer B'
   print('{} waiting'.format(consumer_name))
   await event.wait()
   print('{} triggered'.format(consumer_name))

# event
event = asyncio.Event()

async def ex2main():
   # wrap coroutines in one future
   main_future = asyncio.wait([consumer_a(event), consumer_b(event)])
   # event loop
   event_loop = asyncio.get_event_loop()
   event_loop.call_later(0.1, functools.partial(trigger, event))
   # trigger event in 0.1 sec
   # complete main_future
   done, pending = event_loop.run_until_complete(main_future)
   print(f"done -> {done}")
   print(f"pending -> {pending}")
   
### //example 2;;


### example 3: Web Socket connection;
session = ClientSession()

class WebSocket:
   
   async def __init__(self):
      self.websocket = await session.ws_connect("wss:echo.websocket.org")
   
   async def send(self, message):
      self.websocket.send_str(message)
      
   async def receive(self):
      result = (await self.websocket.receive())
      return result.data      

async def ex3main():
   socket = WebSocket()
   await socket.connect()
   await socket.send("Hello World!!!")
   print(await socket.receive())

##---Main Execution;;
def main():
   ### exmaple3: websocket;;
   ex3main()
   
   ### example2:
   ex2main()
   
   ### example 1;;
   ex1main()

if __name__ == '__main__':
    print("#------------ Code Start --------------#")
    startTime = time.time()
    main()
    endTime = time.time()
    print("Run Time:",endTime-startTime,"ms")
    print("#------------ Code Stop ----------------#")