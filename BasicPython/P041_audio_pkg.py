#!/bin/python3

import time
import pyglet


##---Main Execution;;
def main():
   pyglet.play('resources/pop.wav')


if __name__ == '__main__':
   print("#------------ Code Start ---------------#")
   startTime = time.time()
   main()
   endTime = time.time()
   print("Run Time:",endTime-startTime,"ms")
   print("#------------ Code Stop ----------------#")