````
-------------------------------------------------------------------------------------
-> Title : HTML Notes
-> Author: @neeraj-singh-jr
-> Status : Completed
-> Created : 03/02/2023
-> Updated : 04/02/2023
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q008 : HTML Structure;;
-> Q007 : Input Element;;
-> Q006 : Form Element;;
-> Q005 : Tables Element;;
-> Q004 : Anchor Links to same Page;;
-> Q003 : HTML Tag with attributes;;
-> Q002 : HTML Attributes;;
-> Q001 : HTML Core;;
-------------------------------------------------------------------------------------
````

### HTML NOTES : BEGINNING 

-------------------------------------------------------------------------------------
-> Q008 : HTML Structure;;

#### Element : Doctype

`<!DOCTYPE>` is a special element that is added only at the top of the document.
It provides information about the type of HTML used in the document. 

For example, the following code is used for an HTML document:

for eg, 
````
<!DOCTYPE html>

#### Element : <html>

The <html> element is the main element, which acts as the container for all
the other elements, except the <!DOCTYPE> element. The <head> and <body>
elements are placed inside the <html> element.

for eg,
<!DOCTYPE html>
<html>
	<!-- Body -->
</html>
````

#### Element : <head>

The <head> element is used for specifying additional information about your
webpage. Information such as which fonts to use, which JavaScript or CSS
files to link to, what is the title of the page, etc.

The elements includes

- Title : <title> element, used to set the title of the web page.
- Link : <link> element, used to add external resources, such as CSS files.
- Script : <script> element, used to embed JavaScript code.

for eg,
````
<head>
	<title>Web Page Title</title>
</head>
````

#### Element : <body>

The <body> element contains the HTML elements that are used to display the
contents of the web page, such as headings, images, paragraphs, links etc.
There can be only one <body> tag within an HTML document.

for eg,
````
<body>
	<!-- Content here -->
</body>
````

#### Element : Comments

Comments are great! Comments can help explain your work to other coders and
even to your future self.

Comments do not get shown in the actual webpage. Although your comments can
contain anything you want, yet it is recommended that you keep them precise
and helpful.

For writing a comment use the syntax: <!-- text -->

#### Complete : Structure

- <!DOCTYPE> declaration
- <html> element, contains root HTML element that holds all the other elements.
- <head> element, contains information about the document.
- <body> element, contains the actual content displayed in the browser.

for eg,
````
<!DOCTYPE html>
<html>
	<!-- HEADERS -->
	<head>
		<title> <title>
	</head>

	<body>
		<!-- BODY -->
	</body>
</html>
````


-------------------------------------------------------------------------------------
-> Q007 : Input Element;;

###---------------- Input Type : Basic

The <input type="text"> is used for submitting a single line of text.

for eg,
<form>
	<label>Name:</label>
	<input type="text">
</form>

###---------------- Input Type : Password

The <input type="password"> is used for submitting a password. For security
purposes, it hides the text entered by the user by displaying symbols like
the dot in place of each character entered.

for eg,
<form>
	<label>Username:</label>
	<input type="text">
	<br />
	<label>Password:</label>
	<input type="password">
</form>

###---------------- Input Type : Submit

The <input type="submit"> creates a button for submitting the form data.

for eg,
<form>
	<label>Username:</label>
	<input type="text">
	<br />
	<label>Password:</label>
	<input type="password">
	<br />
	<input type="submit">
</form>

###---------------- Input Type : Reset

The <input type="reset"> resets all the form data to their default values.

for eg,
<form>
	<label>Username:</label>
	<input type="text">
	<br />
	<label>Password:</label>
	<input type="password">
	<br />
	<input type="submit">
	<input type="reset">
</form>

###---------------- Input Type : Reset

The <input type="radio"> is used to create a list from which the user can select one option.

for eg,
<form>
	<label>Can you vote?</label>
	<br />
	<input type="radio" id="vote1" value="no" name="vote">
	<label>No</label>
	<br />
	<input type="radio" id="vote2" value="yes" name="vote">
	<label>Yes</label>
	<br />
	<input type="radio" id="vote3" value="maybe" name="vote">
	<label>Maybe!</label>
</form>

The value attribute is important for the website to analyze the choice made by
the user. Also, it is required to have the name attribute be the same for all
the radio input types for them to be treated as a group.

###---------------- Input Type : Checkbox

The <input type="checkbox"> allows the user to select one or more options from
a list of choices. Attribute name is used as key and value is used as value
for the key and the output is shown like a hashmap

for eg,
<form>
	<label>Fruits you like:</label>
	<br />
	<input type="checkbox" name="fruit" value="apple">
	<label>Apple</label>
	<br />
	<input type="checkbox" name="fruit" value="banana">
	<label>Banana</label>
	<br />
	<input type="checkbox" name="fruit" value="orange">
	<label>Orange</label>
	<br />
</form>

###---------------- Input Type : Button

The <input type="button"> creates a clickable button.

for eg,
<form>
	<input type="button" value="Click Me!">
</form>


-------------------------------------------------------------------------------------
-> Q006 : Form Element;;

###---------------- Form : BASIC

An HTML form is used to collect information that the user submits. The HTML
<form> element can nest other elements like input, label, textarea, button,
etc. inside it to represent different parts of a form.

for eg,
<form>
  <input type="text" placeholder="Enter your name here">
  <button type="submit">Submit</button>
</form>

###---------------- Form : Attributes

There are many different attributes that we can specify for HTML forms. The following are some of the important ones:
1) action = "url-to-destination"
2) method = "GET / POST"

# ACTION :- The action attribute in the form element tells us where to send
  the form data after the form is submitted.

# METHOD : The method attribute specifies how to submit the form data. We use
  the GET and POST methods to submit form data. The default method is GET.

for eg,
<form action="/login" method="post">
	<!-- Form Fields Here -->
</form>

###----------------- Form : Elements

#--- ELEMENT : <input>
There are many HTML form elements. Let's look at some of the important ones:

The <input> element accepts data from the user. Its functioning depends on the
value of its type attribute.

eg,
<form action="path-to-url" method="POST">
	<input type="text">
	<input type="submit">
</form>

#--- ELEMENT : <label>
The <label> element puts a label on other form elements. 

In the example given below, <label> helps the user understand the purpose of
the <input> element.

eg,
<form>
	<label>Name: </label>
	<input type="text">
</form>

#--- ELEMENT : <textarea>
The <textarea> element is for submitting large textual content. To control its
size, the rows and cols attributes are utilized.

for eg,
<form>
	<textarea rows="3" cols="30" placeholder="Enter description here"></textarea>
</form>

#--- ELEMENT : <select>
For creating drop-down lists in our forms, we use the <select> element.

for eg,
<form>
	<select name="fruits">
		<option value="apple">Apple</option>
		<option value="orange">Orange</option>
		<option value="mango">Mango</option>
		<option value="papaya">Papaya</option>
	</select>
</form>

// Output -> "fruits" : "Apple"

#--- ELEMENT : <button>
The <button> element displays a button. 

for eg,
<form>
	<input type="text" />
	<button type="reset">Wipe it clean!</button>
</form>

#--- ELEMENT : <fieldset>
The <fieldset> element groups related form elements. Inside the <fieldset>, a
<legend> element sets the caption at the top.

for eg,
<fieldset>
	<legend>Location: </legend>
	<label>City: </label>
	<input type="text">
	<br>
	<label>State: </label>
	<input type="text">
	<br>
	<label>Country: </label>
	<input type="text">
</fieldset>

#--- FORM Structure :-
The basic structure of a form is as follows:

for eg,
<form>
	<label>Name: </label>
	<input type="text" />
	
  	<fieldset>
		<legend>Address:</legend>
		<label>City:</label>
		<input type="text" />
		<label>State: </label>
		<input type="text" />
		<label>Country: </label>
		<input type="text" />
  	</fieldset>
 
	<label>Review:</label>	
  	<textarea rows="3" cols="30"></textarea>
  
  	<label>Favorite color: </label>
	<select>
		<option value="apple">Red</option>
		<option value="orange">Green</option>
		<option value="mango">Blue</option>
	</select>
  
	<button type="reset">Reset</button>
	<input type="submit" />
</form>


-------------------------------------------------------------------------------------
-> Q005 : Tables Element;;

###---------------- TABLE Usage : Basic

The <table> element is used to display data in a table consisting of rows and
columns.

The following elements are used to arrange the data within a <table> element:
-> <caption> : It is used to add the title to the table.
-> <th> : It is used to add a table header.
-> <tr> : It is used to add a table row.
-> <td> : It is used to add information in a table row.

for eg,
<table>
	<!-- CAPTION -->
	<caption> 
		User Profile
	</caption>
	<!-- ROW : HEADER -->
	<tr>
		<th>Name</th>
		<th>Age</th>
		<th>Gender</th>
	</tr>
	<!-- ROW 1 : DATA -->
	<tr>
		<td>Oliver</td>
		<td>25</td>
		<td>Male</td>
	</tr>
	<!-- ROW 2 : DATA -->
	<tr>
		<td>Eve</td>
		<td>30</td>
		<td>Female</td>
	</tr>
</table>

###---------------- TABLE Usage : Advance

-> Table Head :- 
The <thead> element is used to organize the header row of a table.

It doesn't change anything in the table, but it can contain the whole header
row and gives your code a good structure.

-> Table Body :-
The <tbody> element is used to organize the body of a table.

It doesn't change anything in the table's layout. But, it is used to give the
table's HTML, a proper structure.

-> Table Footer :-
The <tfoot> element is used to organize the footer row of a table.

It doesn't change anything in the table, but it can contain the whole footer
row and gives your code a good structure.

for eg, 
<!-- Table -->
<table>
	<!-- Table : Head -->
	<thead>
		<tr>
			<td>Type<td>
			<td>Count</td>
		</tr>
	</thead>
	<!-- Table : Body -->
	<tbody>
		<tr>
			<td>Children</td>
			<td>20</td>
		</tr>
		<tr>
			<td>Nature</td>
			<td>15</td>
		</tr>
		<tr>
			<td>Fantasy</td>
			<td>15</td>
		</tr>
	</tbody>
	<!-- Table : Footer -->
	<tfoot>
		<tr>
			<td>Total</td>
			<td>50</td>
		</tr>
	</tfoot>
</table>


-------------------------------------------------------------------------------------
-> Q004 : Anchor Links to same Page;;

Suppose, we want to link to a section in the same page that we are on.

For an instance, imagine a long page where you have read a lot and scrolled to
the bottom. Now, wouldn't it be easy to go back to the top without having to
do all that scrolling again

For these purposes, we can use the a tag in the following manner:

for eg,
<!-- HTML PAGE -->

<h1 id="title">Geographical Concepts</h1>

<a href="#country">Countries</a>

<a href="#city-network">City Network</a>

<a href="#micronation">Micronation</a>

<h2 id="country">Countries</h2>
<p>LONG PARAGRAPH 1</p>

<h2 id="city-network">City Network</h2>
<p>LONG PARAGRAPH - 2</p>

<h2 id="micronation">Micronation</h2>
<p>LONG PARAGRAPH - 3</p>


<!-- CLICK HERE TO GOTO TOP -->
<a href="#title">Go to top</a>

<!-- /HTML PAGE -->

NOTE: For making these links work, we need to make them point to the "#id" of a
part of the same page. We need to use the # symbol before the id name in the
link's href. eg, <a href="#micronation">Link <a>


-------------------------------------------------------------------------------------
-> Q003 : HTML Tags with attributes;;

###---------------- Topics: Anchor tag

The <a> element is used to create a link to a web page. 

The <a> element contains href. When we click the link, the href identifies the
web page to which the browser will now take us

for eg,
<h1>Links HTML</h1>

<p>
  <a href="https://www.dictionary.com/">dictionary.com</a>
</p>

<p>
  <a href="https://en.wikipedia.org/wiki/Bear">Let's read about Bears!</a>
</p>

<p>
  <a href="https://en.wikipedia.org/wiki/Giant_panda">Giant Pandas are interesting too!</a>
</p>

###---------------- Topics: Images Attribute

The <img> element is used to display an image. The <img> element uses src to
specify the source of the image being displayed.

The <img> is a self-closing tag.

Although the general rule is that every HTML element must have an opening and
closing tag, there are some exceptions. Some elements are self-closing,

i.e. they don't need a closing tag and can optionally be closed in the opening
tag itself. <img />, <br />, <hr />, are some self-closing elements

for eg,
<div>
	<img src="path/to/your/image.jpg" />
</div>

# Image Tag with `alt` attribute :- The `alt` attribute in an img tag is to
provide a description of the image. This is particularly useful in
situations when our image is not properly loaded on the screen. Also, the
alt text is used by screen readers to explain the image to visually
impaired people

for eg,
<img src="view-from-a-balcony.jpg" alt="The view from a balcony" width="400px"/>
<img src="view-from-a-somewhere.jpg" alt="The view from a plane" width="235"/>

###---------------- Topics: Class Attribute

Class attribute is used when we want to group a few of our elements together
so that when we want to change them through CSS or JavaScript, we can access
all of them at one time

for eg,
<div>
	<h1>Let's Learn</h1>

	<p class = "brilliant-learning-resources">
		Google
		<a href="https://google.com" class = "link-to-the-resource">Click Here</a>
	</p>

	<p class = "brilliant-learning-resources">
		Wikipedia
		<a href="https://www.wikipedia.org/" class = "link-to-the-resource">Click Here</a>
	</p>

	<p class = "brilliant-learning-resources">
  		Dictionary
  		<a href="https://www.dictionary.com/" class = "link-to-the-resource">Click Here</a>
	</p>
</div>

In the example above, we have grouped all the p elements by giving their class
attributes the value 'brilliant-learning-resources'. Similarly, we have grouped
all the links by giving their class attributes the value
'link-to-the-resource'.


###---------------- Topics: ID Attribute

ID attribute is used when we want to select only a single element to be
changed with the use of CSS or JavaScript.

for eg,
<div>
	<h1>Countries</h1>

	<p class = "countries" id = "malaysia">
	  Malaysia <a href="https://www.malaysia.travel/">Travel</a>
	</p>

	<p class = "countries" id = "egypt">
	  Egypt <a href="http://egypt.travel/">Travel</a>
	</p>
</div>


-------------------------------------------------------------------------------------
-> Q002 : HTML Attributes;;

An HTML element can have optional attributes. An attribute is used to set the
behaviour of an HTML element. It has two parts, a name and a value, and is
added within the opening tag of an element.

###---------------- Topics: Title Attributes

The title attribute is used to set the text which is displayed when the mouse
is hovered over an HTML element.

for eg,
````
<h1 title="The web loves HTML">On the internet, HTML is everywhere</h1>
````

-------------------------------------------------------------------------------------
### Q001 : HTML Core Topics;;

#### Topic : Elements

An HTML document is made up of different HTML elements. 

Each HTML element typically has three parts:
1. Opening tag 
2. Content 
3. Closing tag

for eg, 
````
<h1>This is a heading</h1>
<br />
<h1>This is another heading</h1>
````

Here, <h1> at the beginning is called the opening tag, the 'Hello, World!' text 
is the content and the </h1> at the end is called the closing tag.


#### Topic : Headings

The elements <h1> through <h6> are used to display headings.
````
<div>
<h1> is the most important heading.</h1>
<h2> is less important than h1, but more important than any other text.</h2>
</div>
````

This way, we have six different types of headings, from <h1> to <h6>.

for eg,
````
<h1>Hello BigBinary Academy</h1>
<h2>Hello BigBinary Academy</h2>
<h3>Hello BigBinary Academy</h3>
<h6>Hello BigBinary Academy</h6>
````

#### Topic : Paragraph

The <p> element is used to display a paragraph.

for eg,
````
<h1>The Himalayas?</h1>
<p>Himalayas is a beautiful mountain range. It lies in the Indian subcontinent.</p>
<p>It is mostly made up of uplifted sedimentary and metamorphic rock.</p>
````

#### Topic : List

There are two types of list in the html section
1) Unordered list
2) Ordedered list

`Unordered List` : The <ul> element is used to display a bulleted list of items.
Each item, in turn, needs to be put inside an <li> element.

for eg,
````
<h1>Things I like</h1>

<ul>
  <li>Ice cream</li>
  <li>Chocolate</li>
  <li>Movies</li>
</ul>
````

`Ordered List` : The <ol> element is used to display an ordered list of items.
Each item, in turn, needs to be put inside an <li> element.

for eg,
````
<h1>Greek Alphabet</h1>

<ol>
  <li>Alpha</li>
  <li>Beta</li>
  <li>Gamma</li>
</ol>
````

#### Topic : Line Break

The br element is used to create a line break in your text. It is a
self-closing tag and so looks like this, <br/>.

A line break will force the text to start from a new line without creating a
new paragraph. br tags can be used to display text where we need to show the
information in different lines, but the lines are not contextually separate

for eg,
````
An old silent pond...<br/>
A frog jumps into the pond, <br/>
splash! Silence again.<br/>
- Matsuo Basho
````

#### Topic : Div Tag

The `<div>` element is used to create a section in an HTML document.

It is a box in which you can hold a certain part of your content. You can
group HTML tags, text, or any kind of content together in a div. Since, it is
simply holding your content, you'll see no change in the output, but your
code is now more organized.

The importance of div will be visible to you as you practice more.

for eg,
````
<!-- DIV 1 -->
<div>
  <h2>Administrator</h2>
  <p>Every administrator has an editor page</p>
</div>
<!-- DIV 2 -->
<div>
  <h2>User</h2>
  <p>Every user has a profile page</p>
</div>
<!-- DIV 2 -->
<div>
  <h2>Product</h2>
  <p>Every product has a product card</p>
</div>
````

-------------------------------------------------------------------------------------