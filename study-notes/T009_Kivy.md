````
-------------------------------------------------------------------------------------
-> Title : Python Kivy
-> Author: @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 20/02/2023
-> Updated : 20/02/2024
-> Summary : Notes indices are as follows (*** pending)
-------------------------------------------------------------------------------------
***Q006 : Layouting in Kivy App;;
***Q005 : Images Class in Kivy;
***Q004 : Label Class in Kivy;
-> Q003 : Kivy Installation;;
-> Q002 : Kivy Architecture;;
-> Q001 : What is Kivy;;
-------------------------------------------------------------------------------------
````

### PYTHON KIVY NOTES : BEGINNING 

-------------------------------------------------------------------------------------
***Q006 : Layouting in Kivy App;;


-------------------------------------------------------------------------------------
***Q005 : Images Class in Kivy;;


-------------------------------------------------------------------------------------
***Q004 : Label Class in Kivy;;


-------------------------------------------------------------------------------------
### Q003 : Kivy Installation;;
 
NOTE : Make sure to install python compatabile version in your system before hand.

Step 1 : Install or upgrade pip

	`$ pip install -U pip` 
then,

	`$ pip install --upgrade pip wheel setuptools` 

Step 2 : Install dependencies

	`$ pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew`

then 
	
    `$ pip install kivy.deps.gstreamer`  
then,
	
    `$ pip install kivy.deps.angle` 

Step 3 : Install Kivy
	
    `$ pip install kivy`


-------------------------------------------------------------------------------------
### Q002 : Kivy Architecture;;

#### Kivy Archietecture core components ...

````
 ------------------------------------------- -------------------------------
| 	                    Widget   	|	Kv Language                         | 	 
|---------------------------------------------------------------------------| 
| Cache, Clock, Gesture, Event Loop, Properties                             | 
------------------------------------------------------------------------------> High Level Top
| - Core Providers(Windows, Text, Image, Video, Audio)                      |
| - Graphics(vertex buffer, frame buffer, texture, shader, instructions)    |	 
| - Inputs(Motion events,Post Processing,double tap, dejitter...)           |
|-----------------------------------------------------------------------------> Low Level Below
| Pygame, Pil , GStreamer, GLES API, GLEW, Mouse, TUIO                      |	
|---------------------------------------------------------------------------|
|	 FFMpeg, SDL, Cairo, VM_Touch(MTDev), Mac Touch(HIDInput)               | 
----------------------------------------------------------------------------
````

#### Description of Components :-

1) Core Providers and Input Providers :- 

- Kivy Providers mainly abstract the various core tasks like - opening a
  window, displaying images and text, playing audio, spelling correction,
  fetching images from a camera, and so on.
- An input provider is a piece of code that helps us to add support for a
  specific input device such as TUIO, mouse emulator, or Apple's trackpads.
- We can also add support for new input devices by providing a new class that
  reads our input data from our device and transform them into Kivy events.

2) Graphics :-

- Kivy Graphics APIs have the ability to automatically optimize the drawing
  commands.

3) Core :-

~ Cache :  Cache is used to store python objects. We can control the cache in
the following two ways -
	1) Object limit
	2) Timeout

~ Clock : Clock is used to schedule the timer events. Clock supported both
one-shot timers and periodic timers.

~ Gesture : Kivy uses a simple gesture detection, which is used to detect
various types of strokes, circles, rectangles, or squares.

~ Kivy Language : Kivy language is used to describe user interfaces more
quickly and easily.

~ Properties : In Kivy, properties classes are used to link our widget code to
the user interface description.

4) UIX :-

The UIX module commonly contains Widgets and Layouts to quickly create a user
interface.

~ Widget : Widgets are the user interface components that we add to our
program to provide some kind of functionality.

Example: file browser, buttons, lists, sliders, and more.

~ Layouts : Layouts are used to arrange widgets.

5) Modules :-

Modules are the classes that can be loaded on the Kivy when we start the Kivy
application. The config file is used to manage the loading of modules.

6) Input Events :-

- Kivy Input events are an essential part of the kivy Architecture. Kivy
  contains different input events such as - touchs, Mouse, HIDInput, mice, 
  MTDev, TUIO (mutiple touch protocol).

- All input types are characterized by an instance of the touch () class. A
  touch () class instance can be one of the following three states.
  1) Down 
  2) Move 
  3) Up

7) Widgets and Input Dispatching :-

- The term Widgets are most frequently used in GUI programming to describe
  that part of the program which interacts with a user.
- In kivy, widgets are works as an object that receives input events. All
  widgets are arranged in the form of a widget tree. One widget may contain
  any number of child or none child.
- Whenever new data is available, Kivy sends one per touch. Every event is
  first received by the root widget of the widget tree.


-------------------------------------------------------------------------------------
### Q001 : What is Kivy;;

#### Introduction :

- Kivy is an open-source and Graphical User Interface (GUI) development
  platform for Python.
- It helps us to develop mobile applications and multi-touch application
  software with a NUI (Natural User Interface).
- It allows developers to build an application once and use it across all
  devices.
- It can also access mobile APIs to manipulate things such as the camera on a
  phone, GPS tracking, vibrator, and so on.
- It contains various components for creating an application such as,
	1) A graphical library for openGL ES2.
	2) An extensive range of widgets that support multi-touch.
	3) An intermediate Kv language to design custom widgets.
	4) An extensive support for input devices such as a mouse, keyboard, TUIO,
		as well as OS-specific multi touches events.

#### Featured :-

1) Video :- Kivy includes various modules to play video files and streams.
Kivy Video player also supports some common requirements related to videos
such as play, pause, stop buttons, text that can be used as a subtitle,
display messages to the user on videos, and more.

Example: pygame video provider supports MPEG1 on Linux.

2) Multi Touch Support :- Kivy uses a wide range of widgets that support
multi-touch and gestures. Kivy developers provide a gesture library to record
the user's gesture.

There are the following three gestures that we can record -
	+ Left to right horizontal line
	+ Right to left horizontal line
	+ Bottom to top vertical line

3) UI features :- Kivy comes with a number of widgets and controls to make our
mobile interface more attractive and beautiful. It is also used to improve
one-handed usability, navigate gestures, create new icons or design elements,
dark mode, and new animations.

4) Visual effects and OpenGL :- Kivy uses PyGame for easily creating new
games. PyGame comes with various modules to drawing shapes, dealing with
colors, and playing music.

5) Flexible :- Kivy is more flexible because it can run on a variety of
devices, including Linux, mobile phones, windows, tablets, iOS, and Raspberry
Pi. Kivy is flexible so it can adapt to new technologies quickly.

6) Free :- Kivy framework is completely free to use. To work with Kivy, you
must have 1 GHz 32 bit (x86), or 64 bit (x64) CPU, 1 GB of RAM, 128 MB of
graphical memory, and Python installed on your system.

#### Advantage and Dis-Advantage :- 

// Advantage :

1) Kivy helps us to design innovative user interfaces with multi-touch
functionalities.
2) It can smoothly work with various platforms such as Windows, Android,
Linux, ios, macOS, and Raspberry Pi.
3) It helps us to run code on all supported platforms.
4) It provides well-documented APIs.
5) It performs better than HTML 5.
6) It offers a better representation of programs, including classes, widget
configuration, and inherited classes.

// Disadvantage :

1) It is not always up-to-date with the latest Android APIs.
2) Kivy uses kV language, which is not suitable for us to compile our code alone.
3) The sizes of the package are unnecessarily huge.
4) It has a lack of community support.
5) It takes a lot of time for building and compiling mobile applications.


-------------------------------------------------------------------------------------