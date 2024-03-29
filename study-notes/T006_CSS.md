````
-------------------------------------------------------------------------------------
-> Title : CSS Notes
-> Author: @neeraj-singh-jr
-> Status : Completed
-> Created : 03/02/2023
-> Updated : 11/02/2023
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q028 : Flexbox in CSS;
-> Q027 : Media Query in CSS;
-> Q026 : CSS Page Layout;
-> Q025 : Cascade in CSS;
-> Q024 : Pseudo-Elements in CSS;
-> Q023 : Pseudo-Class in CSS;
-> Q022 : Combinators in CSS;
-> Q021 : Float in CSS;
-> Q020 : Position in CSS;
-> Q019 : Display none vs Visibility Hidden in CSS;
-> Q018 : Display in CSS;;
-> Q017 : CSS Box Model;;
-> Q016 : Styling Forms in CSS;;
-> Q015 : Styling Tables in CSS;;
-> Q014 : Styling Un/Ordered List in CSS 
-> Q013 : Styling Anchor Links in CSS;
-> Q012 : Opacity in CSS;
-> Q011 : Borders in CSS;
-> Q010 : Backgrounds in CSS;;
-> Q009 : Text Formatting in CSS;;
-> Q008 : Spacing With Padding in CSS;;
-> Q007 : Spacing With Margin in CSS;;
-> Q006 : Min Width and Min Height;;
-> Q005 : Max Width and Max Height;;
-> Q004 : CSS Sizing;;
-> Q003 : CSS Color;;
-> Q002 : Selectors Brief;;
-> Q001 : CSS Core;;
-------------------------------------------------------------------------------------
````

### CSS NOTES : BEGINNING 

-------------------------------------------------------------------------------------
-> Q028 : Flexbox in CSS;

Display Properties - static, relative, absolute, fixed, float, flex 

#### Flexbox Display Property :-

The float property has been used a lot in the past to create web layouts. We
can agree that it helps us stack elements next to each other.

But, there are so many limitations with float. Not only that, our code gets
complex for large layouts too

for eg,
<!-- HTML -->
<section>
  <div class="col">
    <h2>Solar System</h2>
    <p>First Paragraph</p>
  </div>
  <div class="col">
    <h2>The Sun</h2>
    <p>Second Paragraph</p>
  </div>
  <div class="col">
    <h2>Earth</h2>
    <p>Third Paragraph</p>
  </div>
</section>

<!-- CSS -->
.section {
  display: flex;
}
.col {
  margin: 10px
  padding: 5px 15px;
  background-color: #F1F5F9;
}

#### Flex Container :-

When you set the display property of an element to flex, that element becomes
a flex container and all its immediate child elements become flex items.

for eg,
<!-- HTML -->
<div class="container">
  <div class="pink"> 1 </div>
  <div class="green"> 2 </div>
  <div class="orange"> 3 </div>
  <div class="grey"> 4 </div>
  <div class="black"> 5 </div>
  <div class="white"> 6 </div>
</div>

<!-- CSS -->
div {
  color: #fff;
}
.container {
  display: flex;
}
.pink, .orange, .green, 
.grey, .black, .white {
  padding: 30px;
}
.pink {
  background-color: lightpink;
}
.orange {
  background-color: orange;
}
.green {
  background-color: lightgreen;
}
.grey {
  background-color: grey;
}
.black {
  background-color: black;
}
.white {
  background-color: lightgrey;
}

#### Flex Direction :-

By default, the elements within a flex container are stacked next to each
other in a single row. The stacking happens left to right.

Direction for Flex Direction - 
row, row-reverse, column and column-reverse for the flex-direction property

for eg,
<h3>Flex Direction: Row</h3>
<div class="container row">
  <div class = "inner-div">1</div>
  <div class = "inner-div">2</div>
  <div class = "inner-div">3</div>
</div>

<h3>Flex Direction: Row Reverse</h3>
<div class="container row-rev">
  <div class = "inner-div">1</div>
  <div class = "inner-div">2</div>
  <div class = "inner-div">3</div>
</div>

<h3>Flex Direction: Column</h3>
<div class="container col">
  <div class = "inner-div">1</div>
  <div class = "inner-div">2</div>
  <div class = "inner-div">3</div>
</div>

<h3>Flex Direction: Column Reverse</h3>
<div class="container col-rev">
  <div class = "inner-div">1</div>
  <div class = "inner-div">2</div>
  <div class = "inner-div">3</div>
</div>

<!-- CSS -->
.container {
  display: flex:
  margin: 10px 10px;
}
.container > div {
  margin: 5px;
  padding: 10px 10px;
  background-color: orange;
}
.row {
  flex-direction: row;
}
.row-rev {
  flex-direction: row-reverse;
}
.col {
  flex-direction: column;
}
.col-rev {
  flex-direction: column-reverse;
}

#### Flex Wraps :-

By default, flexbox tries to fit all the child elements in a single row or a
single column depending on the flex-direction.

If the width of the flex items exceeds the width of the parent element, we
will see a horizontal scrollbar.

To avoid this, we can choose to wrap the elements pushing them to the next
row / column using the flex-wrap property.

Default Columns for flex-wrap - wrap, wrap-reverse.

for eg,
<!-- HTML -->
<div class="container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div>4</div>
  <div>5</div>
</div>

<!-- CSS -->
.container {
  display: flex;
  flex-wrap: wrap;
}
.container > div {
  background-color: orange;
  padding: 30px 90px;
  margin: 5px;
}

#### Flex Justify Content :-

By default, we saw that the flex items are placed at the beginning of the
container depending on the flex direction, with least spacing between the
items.

In case of row-reverse, the items begin from right. With column, from the top
and with column-reverse, from the bottom

The justify-content property is used to change this behaviour. We can use the
values 'flex-start', 'flex-end', 'center', 'space-between', 'space-around' and
'space-evenly'.

-> flex-start : Items are placed at the beginning of the container, which is
   the default value.

-> flex-end : Items are placed at the end of the container.

-> center : Items are placed in the center.

-> space-between : There is as much space between the items as can be evenly
   distributed.

-> space-around : The spaces between the items are double the space on both
   ends of the container.

-> space-evenly : There is equal space between the items and at both the
   ends.

for eg, 
<!-- HTML -->
<h3>Flex Start - Default</h3>
<div class="container flex-start">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Flex End</h3>
<div class="container flex-end">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Center</h3>
<div class="container center">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Space Between</h3>
<div class="container between">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Space Around</h3>
<div class="container around">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Space Evenly</h3>
<div class="container evenly">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- CSS -->
.container {
  display: flex;
  padding: 10px;
  background-color: beige;
}
.container > div {
  background-color: orange;
  padding: 20px;
  margin: 5px;
}
.flex-start {
  justify-content: flex-start;
}
.flex-end {
  justify-content: flex-end;
}
.center {
  justify-content: center;
}
.between {
  justify-content: space-between;
}
.around {
  justify-content: space-around;
}
.evenly {
  justify-content: space-evenly;
}

#### Align Items :-

While justify-content allows us to change the placement and spacing of the
items in one direction, we would also want to align the items in the other
direction.

Align items Property Values :-

-> flex-start : Items are aligned at the beginning of the container.

-> flex-end : Items are aligned at the end of the container.

-> center : Items are aligned in the center.

-> baseline : Items are aligned such that the bottom of all elements are in a line.

-> stretch : Items are stretched full width in case of the column direction,
   and full height in case of the row direction.

for eg,
<!-- HTML -->
<h3>Flex Start</h3>
<div class="container flex-start">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Flex End</h3>
<div class="container flex-end">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Center</h3>
<div class="container center">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Baseline</h3>
<div class="container baseline">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<h3>Stretch</h3>
<div class="container stretch">
  <div>1</div>
  <div>2</div>
  <div>3</div>
</div>

<!-- CSS -->
.container {
  display: flex;
  padding: 10px;
  background-color: beige;
  min-height: 150px;
}
.container > div {
  background-color: orange;
  padding: 20px;
  margin: 5px;
}
.container > div:nth-child(2) {
  font-size: 2em;
}
.flex-start {
  align-items: flex-start;
}
.flex-end {
  align-items: flex-end;
}
.center {
  align-items: center;
}
.baseline {
  align-items: baseline;
}
.stretch {
  align-items: stretch; /* Default */
}


#### Align Self :-

When you want only one flex item to be aligned differently from the rest, you
can use the align-self property.

for eg,
<!-- HTML -->
<div class="container">
  <div>1</div>
  <div>2</div>
  <div>3</div>
  <div class="last">4</div>
</div>

<!-- CSS -->
.container {
  background-color: darkgrey;
  display: flex;
  height: 200px;
}
.container > div {
  padding: 20px;
  margin: 5px;
  background-color: orange;
  align-items: baseline;
}
.last {
  align-self: end;
}

#### Flex Grow :-

Sometimes, you might want one or all of the items to occupy the full space
available. That's when you can use the flex-grow property on individual flex
items to specify a number.

The default value is 0, which is why the items occupy only as much space as
required. When the value is more than 0 for some items, the extra space is
divided proportionally among those items.

for eg,
<!-- HTML -->
<div class="container">
  <p class="p1">Sun</p>
  <p class="p2">The Sun is the star at the center of the Solar System.</p>
</div>

<!-- CSS -->
.container {
  display: flex;
}
p {
  background-color: #f1f1f8;
  padding: 10px;
  border: 1px solid #a1a1a1;
}
.p1 {
  flex-grow: 2;
}
.p2 {
  flex-grow: 0;
}

#### Flex Shrink :-

When the flex items don't wrap, they try to shrink as much as possible to fit
into the available space.

Using the flex-shrink property, we can control how much each item shrinks. The 
value can be any number. 

Value 0 means no shrink. Higher the value, more the item shrink

for eg, 
<!-- HTML -->
<div class="container">
  <div class="shrink"></div>
  <div class="shrink-more"></div>
  <div class="shrink"></div>
</div>

<!-- CSS -->
.container {
  display: flex
}
.container > div {
  padding: 30px;
  margin: 10px;
  width: 33%;
  bachground-color: orange;
}
.shrink {
  flex-shrink: 1;
}
.shrink-more {
  flex-shrink: 5;
}

#### Flex Basis :-

With the flex-basis property, we can set the initial size of the item. It's
possible to set this with the width property too, but flex-basis is a better
way to do the same, for flex items.

The default is auto.

for eg,
<!-- HTML -->
<div class="container">
  <div id="one">
  </div>
  <div id="two">
  </div>
  <div id="three">
  </div>
</div>


<!-- CSS -->
.container {
  display: flex;
}
.container > div {
  padding: 30px;
  margin: 10px;
  background-color: orange;
}
#one {
  flex-basis: 50px;
}
#two {
  flex-basis: 50%;
}
#three {
  flex-basis: 50%;
}

#### Flex Shorthand Property :- 

-> You can set flex-grow, flex-shrink and flex-basis with one single shorthand
   flex property.

-> This can take one, two or three values separated by spaces:

flex: <flex-grow> <flex-shrink> <flex-basis>


//--- Three values
flex: 1 1 auto;

flex-grow is 1
flex-shrink is 1
flex-basis is auto


//--- Two values - Both without units
flex: 0 1;

flex-grow is 0
flex-shrink is 1
flex-basis not specified

//--- Two values - One without units and another with units
flex: 0 100px;

flex-grow is 0
flex-shrink is not specified
flex-basis is 100px

#### Flex Order :-

-> By default, flex items are displayed in the same order they appear in the
   HTML code.

-> We can change the order using the order property for the flex item, without
   even changing the HTML.

-> The value can be any number. The default is 0. Higher the number, later the
   element appears in the layout or The lower the value, the earlier the
   element appears.

for eg,
<!-- HTML -->
<div class="container">
  <div id="one">1<br>(Order: 2)</div>
  <div id="two">2<br>(Order: 1)</div>
  <div>3<br>(Order: 0)</div>
  <div>4<br>(Order: 0)</div>
</div>

<!-- CSS -->
.container {
  display: flex;
  flex-wrap: wrap;
}
.container > div {
  background-color: orange;
  padding: 30px;
  margin: 5px;
  text-align: center;
}
#one {
  order: 2;
}
#two {
  order: 1;
}


-------------------------------------------------------------------------------------
-> Q027 : Media Query in CSS;

#### Responsive without Media Query :- 

With CSS flexbox, we can create blocks which automatically adjust their sizes
for small and large screens

for eg,
<!-- HTML -->
<section>
  <div class="col">
    <h2>Solar System</h2>
    <p> FIRST PARAGRAPH </p>
  </div>
  <div class="col">
    <h2>The Sun</h2>
    <p>SECOND PARAGRAPH</p>
  </div>
  <div class="col">
    <h2>Earth</h2>
    <p>THIRD PARAGRAPH</p>
  </div>
</section>

<!-- CSS -->
section {
  display: flex;
}
.col {
  margin: 10px;
  padding: 5px 15px;
  background-color: #F1F5F9;
}
@media screen and (max-width: 630px) {
  section {
    flex-direction: column;
  }
}

Mobile first and Desktop first Approaches The Media Rule :-

CSS @media rule which is used to apply different styles for different device
types or sizes.

@media screen and (max-width: 630px) {
  ...
}

//--- Media Type and Media Feature :-

-> This rule contains a media type screen and a media feature max-width: 630px.
-> Except screen, other media type are all, print and speech can also be used.
-> A media feature expression tests for a condition. The styles within the
   media query are applied if this condition is true.

for eg,
<!-- HTML -->
<div> </div>

<!-- CSS -->
div {
  width : 1200px;
  height: 200px;
  background-color: green
}

@media screen and (max-width: 600px) {
  background-color: orange;
}

NOTE : 
-> Width > 600 green bg shown and smaller then 600 orange bg will be shown.

#### Mobile first and Desktop first Approaches :-

-> Desktop First Approaches : Usually, We started with layouts suitable for
   desktops. Then we worked our way towards smaller screen sizes by adding
   breakpoints to change the styles for widths lower than that of the
   breakpoint. This approach is known as the Desktop First approach

-> Mobile First Approaches : We can start with a layout suitable for the
   mobile screens. Usually, this would be a simpler design choice. This
   approach known as the Mobile First approach is the recommended one.

-> Keep in mind that we used max-width media feature for desktop-first
   approach and min-width for mobile-first approach.

#### Media Queries for Orientation :-

We can also change some styles based on whether our web page is being viewed
in portrait or landscape orientation

for eg,
<!-- HTML -->
<p> The Solar System is the gravitationally bound system of the Sun and the
objects that orbit it, either directly or indirectly. Of the objects that
orbit the Sun directly, the largest are the eight planets, with the remainder
being smaller objects, the dwarf planets and small Solar System bodies. </p>

<!-- CSS -->
p {
  width: 50%;
}
@media screen and (orientation: portrait) {
  p {
    width: 100%;
  }
}

#### Responsive Images :-

When we specify the width of an image in pixels or em, on larger screens there
might be a lot of empty space next to image and on smaller screens, a
horizontal scrollbar might appear.

BEST APPROACH : To making the images responsive, without the need for media
queries, is to set their max-width as 100%

for eg,
<!-- HTML -->
<img src="path-to-image.jpg" alt="" />

<!-- CSS -->
img {
  max-width: 100%
}

#### Responsive Text :-

Just like any other style, we can change the text size too, based on screen
width using media queries

for eg,
<!-- HTML -->
<h1>Large heading on desktop</h1>
<h2>Relatively smaller one</h2> 

<!-- CSS -->
h1 {
  font-size: 2rem;
}
h2 {
  font-size: 1.5rem;
}
@media screen and (min-width: 767px) {
  h1 {
    font-size: 2.6rem;
  }
  h2 {
    font-size: 2rem;
  }
}

#### Responsive Blocks :-

One of the earliest methods of creating responsive layouts is to set the width
of blocks in percentages and stack them one below the other for mobile
devices. With the help of media queries, we can use float to stack them next
to each other on larger screens

for eg,
<!-- HTMl -->
<header></header>
<div class="content">
  <div class="left"></div>
  <div class="right"></div>
</div>

<!-- CSS -->
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  padding: 10px;
  margin: auto;
}

header, .left, .right {
  padding: 10px;
  margin-top: 10px;
}

header {
  height: 80px;
  background-color: #f1f5ff;
}

.left {
  height: 250px;
  background-color: #d4d7ff;
}

.right {
  height: 250px;
  background-color: #ffd4d7;
}

@media (min-width: 767px) {
  .left {
    width: 29%;
    float: left;
  }
  .right {
    width: 69%;
    float: right;
  }


-------------------------------------------------------------------------------------
-> Q026 : CSS Page Layout;

#### Most common web page structure

Key Points :-
- The header, navigation bar and footer occupy 100% width of the page.
- The sidebars and main content are placed next to each other using the float
  property. Individual blocks are styled using width, height, margin, padding
  and background-color
- The line-height property is used to vertically center the text in each block.

for eg,
<!-- HTML -->
<header> Header </header>
<nav> Navigation bar </nav>

<div class="content">
  <div class="left"> Left Sidebar </div>
  <div class="main"> Main Content </div>
  <div class="right"> Right Sidebar </div>
</div>

<footer> Footer </footer>

<!-- CSS -->
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  padding: 10px;
  font-family: sans-serif;
  font-size: 1em;
  text-align: center;
}
header, nav, .left, .main, .right, footer {
  padding: 10px;
  background-color: #f1f2f3;
}
header {
  height: 80px;
  line-height: 60px;
}
nav, footer {
  margin-top: 10px;
  height: 50px;
  line-height: 30px;
}
.left, .right {
  width: 25%;
  float: left;
  margin-top: 10px;
  height: 250px;
  line-height: 230px;
}
.main {
  width: 46%;
  float: left;
  margin: 10px 2% 0;
  height: 250px;
  line-height: 230px;
}
.content::after {
  content: "";
  display: block;
  clear: both;
}

#### Fluid Layout :-

Instead of setting the width in pixels, if we use percentages, all the
elements auto adjust their width based on the screen size.

for eg,
<!-- HTML -->
<header> Header </header>
<div class="content">
  <div class="left"> Left Sidebar </div>
  <div class="main"> Main Content </div>
  <div class="right"> Right Sidebar </div>
</div>

<!-- CSS -->
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  padding: 10px;
}
header, .left, .main, .right {
  padding: 10px;
  background-color: #f1f5ff;
}
header {
  height: 80px;
}
.left, .right {
  width: 25%; /* Width in percentage */
  float: left;
  margin-top: 10px;
  height: 250px;
}
.main {
  width: 46%; /* Width in percentage */
  float: left;
  margin: 10px 2% 0;
  height: 250px;
}

This is a fluid layout because all the elements adjust according to the size
of the screen just like a liquid put inside a container.

#### Adaptive Layout :-

If we can change the appearance of elements based on screen size, our problem
is solved. We can use media queries to set different styles for different
sizes.

These are media queries:
  @media (min-width: 768px) and (max-width: 1200px) { ... }

The styles specified within this block are applied when the screen width is a
minimum of 768px and a maximum of 1200px.

Such a layout is called an adaptive layout.

//--- Limitation of Adaptive Layout :-

- Adaptive layouts are great, but with them, you need to design multiple fixed
  layouts and take care of each element's width. Also, you might have noticed
  a lot of empty space on both sides of the content for some screen sizes.

- To Avoid these Responsive Layouts are used.

for eg,
<!-- HTML -->
<header></header>
<div class="content">
  <div class="left"> </div>
  <div class="main"> </div>
</div>

<!-- CSS -->
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
body {
  margin: auto;
  width: 1200px;
}
header, .left, .main {
  padding: 10px;
  margin-top: 10px;
}
header {
  height: 80px;
  background-color: #f1f5ff;
}
.left {
  width: 348px;
  float: left;
  height: 250px;
  background-color: #d4d7ff;
}
.main {
  width: 828px;
  float: right;
  height: 250px;
  background-color: #ffd4d7;
}
@media (min-width: 768px) and (max-width: 1200px) {
  body {
    width: 768px;
  }
  .left {
    width: 222px;
  }
  .main {
    width: 530px;
  }
}
@media (min-width: 480px) and (max-width: 767px) {
  body {
    width: 480px;
  }
  .left, .main {
    float: none;
    width: 480px;
  }
}
@media (max-width: 479px) {
  body, .left, .main {
    width: 300px;
  }
}

#### Responsive Layout :-

Responsive layouts use a mix of fluid and adaptive layouts. That is, we can
specify the widths in percentages and use media queries to change them as
needed

for eg,
<!-- HTML -->
<header></header>
<div class="content">
  <div class="left">
  </div>
  <div class="main">
  </div>
</div>

<!-- CSS -->

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  padding: 10px;
  margin: auto;
}

header,
.left,
.main {
  padding: 10px;
  margin-top: 10px;
}

header {
  height: 80px;
  background-color: #f1f5ff;
}

.left {
  width: 29%;
  float: left;
  height: 250px;
  background-color: #d4d7ff;
}

.main {
  width: 69%;
  float: right;
  height: 250px;
  background-color: #ffd4d7;
}

@media (max-width: 767px) {
  .left,
  .main {
    float: none;
    width: 100%;
  }
}



-------------------------------------------------------------------------------------
-> Q025 : Cascade in CSS;

#### Cascade : Basic :-

When you have multiple CSS rules that apply to the same HTML, these rules
conflict with each other and one of them wins

There are three rules that try to apply different colors to the same p element, and two rules that try to apply different background colors

for eg,
<!-- HTML -->
<p> CSS is Cascading Style Sheets, and the cascading is important </p>

<!-- CSS -->
p {
  color: orange;
  background-color: black;
}
p {
  color: blue;
  background-color: yellow;
}
p {
  color: green;
}

In such a case, where all the selectors are identical, the rule that appears
last in the code always wins. The last color value is green and the last
background-color is yellow

#### Cascade : Specificity Hierarchy :-

When the selectors are identical, or have the same importance, the rule that
comes later wins. 

But what happens with different selectors like in the example given below

//--- CASE 1 : 
<!-- HTML -->
<p id="p1" class="para">
  CSS is Cascading Style Sheets, and the cascading is important.
</p>

<!-- CSS -->
#p1 {
  color: purple;
}
.para {
  color: red;
}

NOTE : Purple Wins, Id selector > class & html-element.

//--- CASE 2 :
<!-- HTML -->
<p class="para">
  CSS is Cascading Style Sheets, and the cascading is important.
</p>

<!-- CSS -->
.para {
  color: red;
}
p {
  color: blue;
}

NOTE : Red Wins, Class selector > html-element.

#### Cascade : Specificity Value :-

There is a specificity value attached to each of the selectors or combination
of selectors. Higher the specificity value, more specific is the selector.

Specificity Value Cheatsheet :-
1) ID Selector (#menu) with Value - 100
2) Class Selector (.nav) with Value - 10
3) Element Selector (ul) with Value - 1
4) Element Selector (li) with Value - 1

the specificity value of this selector is 100 + 10 + 1 + 1 = 112

for eg,
<!-- HTML -->
<div>
  <p class="para" id="p1">
    This is a paragraph with a <span class="sp">span</span> element
  </p>
</div>

<!-- CSS -->
#p1 > span {
  color: red;
}
div .para .sp {
  color: blue;
}

Calculate Specificity Value :-
# CASE 1 :- (div .para .sp)
Specificity value = 1 + 10 + 10 = 21

# CASE 2 :- (#p1 > span)
Specificity value = 100 + 1 = 101

#### Cascade : The !important Rule :-

Sometimes you might need to override the styles of a more specific selector.
The only way to do that is by adding !important to the CSS rule, to which you
want to give more importance

for eg,
<!-- HTML -->
<p id="p1" class="para">
  !important overrides any specificity discussion.
</p>

<!-- CSS -->
#p1 {
  background-color: orange;
}
.para {
  background-color: gray !important;
}


-------------------------------------------------------------------------------------
-> Q024 : Pseudo-Elements in CSS;

#### Pesudo Elements : Styling First Line and First Letter :-

::first-line :- When you want to style only the first line of a paragraph or
  the first line of each paragraph differently, you can use the ::first-line
  pseudo-element

::first-letter :- When you want to style only the first letter of a paragraph or
  first letter of each paragraph differently, you can use the ::first-letter
  pseudo-element

NOTE:
::first-line will be considered on the basis of width of the element. Try changing
the width of the whole div box.


for eg,
<!-- HTML -->
<div>
  <p> Albert Einstein was a German-born theoretical physicist, widely
  acknowledged to be one of the greatest physicists of all time. </p>
  
  <p> Einstein is known for developing the theory of relativity, but he also
  made important contributions to the development of the theory of quantum
  mechanics. </p>
</div>

<!-- CSS -->
div {
  max-width: 450px;
}
p::first-line {
  font-size: 1.2rem;
  line-height: 1.2rem;
  color: brown;
}
p::first-letter {
  font-size: 2rem;
  color: brown;
}

you can combine the :first-child pseudo-class with :first-letter like this:

p:first-child::first-letter

#### Pesudo Elements : Before Element :-

When you want to add something at the beginning of an element without actually
adding it in HTML, you can use the ::before pseudo-element to do so, with the
help of the content property.

for eg,
<!-- HTML -->
<h2>Frequently asked questions</h2>
<p class="question"> What are FAQs </p>
<p class="answer"> FAQs are frequently asked questions by customers of a product or students of a course.</p>

<!-- CSS -->
.question::before {
  content: "Q";
}
.answer::before {
  content: "A";
}
.question::before, .answer::before {
  margin-right: 5px;
  font-size: 1.5rem;
  font-weight: bold;
  line-height: 0;
  color: tomato;
}

#### Pesudo Elements : After Element :-

When you want to add something at the end of an element without actually
adding it in the HTML, you can use the ::after pseudo-element to do so, with
the help of the content property.

for eg,
<!-- HTML -->
<h2>A Styled Heading</h2>


<!-- CSS -->
h2::before, h2::after {
  content: '';
  display: inline-block;
  width: 100px;
  border-top: 3px solid lightgray;
  margin: 6px 10px;
}


-------------------------------------------------------------------------------------
-> Q023 : Pseudo-Class in CSS;

#### Pseudo Class: Hover :-

When a user takes the mouse pointer over an element, you can style it
differently by appending :hover to the selector

for eg,
<!-- HTML -->
<div> Hover over me to see the paragraph element </div>
<p> You can see me </p>

<!-- CSS -->
p {
  position: absolute;
  display: none;
  background-color: orange;
  padding: 8px;
}
div:hover + p {
  display: block;
}

#### Pseudo Class : Focus :-

When you click or tap on an element, or when you use the tab key on keyboard
to move to it, an element gets focus

By default, the browser adds a blue outline to an element that is focused.
This can be changed using the :focus pseudo-clas

for eg,
<!-- HTML -->
<form>
  <h3>Register:</h3>
  <input type="text" id="name" placeholder="Full name" />
  <button type="button">Submit</button>
</form>

<!-- CSS -->
input[type="text"] {
  border: 1px solid lightgray;
  padding: 4px 8px;
  font-size: 1em;
}
button {
  border: none;
  padding: 4px 8px;
  background-color: purple;
  color: white;
  font-size: 1em;
}
#name:focus {
  outline: 1px solid black;
}
button:focus {
  outline: 1px solid darkblue;
}

#### Pseudo Class : Links :-

Along with :hover, we can change the appearance of links depending on other
user actions. We can change the link styling for when the user clicks the
link or based on whether the link was previously visited or not:

:visited - Used if the link was previously visited

:active - Applied when the link is just clicked

for eg,
<!-- HTML -->
<p>
  First, take the cursor on the link to see the hover styles take effect.
  Next click on it to see the active styles take effect.
  Notice that the visited styles take effect after you have clicked it once.
</p>
<a href="#1">
  Hover and click
</a>

<!-- CSS -->
a {
  color: tomato;
}
a:visited {
  color: darkgrey;
}
a:hover {
  color: orange;
  text-decoration: none;
}
a:active {
  color: darkred;
}

#### Pseudo Class : First and Last Child :-

We can select first child or the last child of its parent element, we can
use - 

-> First Element (:first-child) 
-> Last Element (:last-child)

for eg,
<!-- HTML -->
<ul>
  <li>Home</li>
  <li>About</li>
  <li>Services</li>
  <li>Contact</li>
</ul>

<!-- CSS -->
ul > li:first-child {
  list-style-type : lower-roman;
  font-weight: bolder;
}
ul > li:nth-child(2) {
  list-style-type : upper-roman;
  font-weight: lighter;
}
ul > li:nth-child(3) {
  list-style-type : disc;
  font-style: italic;
}
ul > li:last-child {
  list-style-type : cirlce;
  color: yellow;
}

#### Pseudo Class : Nth Child :-

You can also select a specific child element using the :nth-child
pseudo-class

:nth-child(n+3) - Selects all matching child elements starting from 3rd one

:nth-child(3n) - Selects every 3rd matching child element

:nth-child(3n-2) - Selects every 3rd matching child element starting from the first

for eg,
<!-- HTML -->
<div>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
  <span></span>
</div>

<!-- CSS -->
span {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-color: lightgray;
  margin-right: 5px;
}
span:nth-child(n+3) {
  background-color: teal;
}

#### Pseudo Class : First and Last of Type :-

With the :first-child pseudo-class, you can select a particular type of
element if its the first child of its parent. 

For example, span:first-child selects a span element, only if its the first
child of its parent

you want to select the first span element within its parent, whether or not it
is the first child, you can use span:first-of-type instead.

:last-child and :last-of-type work in the same manner as :first-child and 
:first-of-type.

for eg,
<!-- HTML -->
<div>
  <p>This is a beginning paragraph</p>
  <span>Span 1</span>
  <span>Span 2</span>
  <span>Span 3</span>
  <p>This is an ending paragraph</p>
</div>

<!-- CSS -->
span {
  padding: 5px 8px;
  background-color: lightgray;
  border-radius: 3px;
}
span:first-of-type {
  background-color: orange;
}

#### Pseudo Class : nth of Type :-

When you want to select the 7th element of its type within its parent, or
select the first 15 elements or every 3rd element and so on, you can use
the :nth-of-type pseudo-clas

for eg,
<!-- HTML -->
<div>
  <p>
    Albert Einstein was a German-born theoretical physicist, widely
    acknowledged to be one of the greatest physicists of all time. <a
    href="#">Read full story now</a>
  </p>
</div>
<span>
  <a href="#">Like</a>
  <a href="#">Comments</a>
  <a href="#">Read Story</a>
</span>

<!-- CSS -->
span a {
  text-decoration: none;
  display: inline-block;
  background-color: black;
  padding: 5px;
  color: #ffffff;
}
a, span a:nth-child(2) {
  margin: 0px 5px;
}


-------------------------------------------------------------------------------------
-> Q022 : Combinators in CSS;

#### Combinators : Selecting Direct Child Elements :-

We can select an element directly using its class, or id, or the tag name. 

But sometimes, we need to select elements based on their relationship with
other elements.

Here, > is a combinator. Notice that the styles were only applied to the p
elements within a div.

for eg,
<!-- HTML -->
<div>
  <p>First Paragraph</p>
  <p>Second Paragraph</p>
</div>

<!-- CSS -->
div > p {
  color: darkgrey;
  background-color: lightgrey;
}

#### Combinator : Selecting all child elements :-

When we need to select a particular set of child elements, we use the space
character like this - div a

Here, div a will select all a elements that are the children of a div element,
even when those a elements are nested deeper within the div

for eg,
<!-- HTML -->
<div> <a href="#" >Link 1 </a> </div>

a href="#" alt="">Link 2</a>

<ul> <li>Summer</li> </ul>


<!-- CSS -->
div a {
  font-weight: bolder;
  color: red;
}
a {
  color: green;
}
ul li {
  display:inline-block;
  padding-right: 10px
}

#### Combinators : Selecting Immediate Next Element :-

When we need to select the immediate next element, we use the + character.

for eg,
````
<!-- HT :--->
<h1>Lotus</h1>
<p>
  Binomial name: Nelumbo nucifera
  <p> GREEN COLOUR NOT SHOWN FOR THIS PARAGRAPH! </p>
</p>
````

<!-- CSS -->
h1 + p {
  font-weight: bold;
  font-size: 1.1em;
  color: green;
}

#### Combinators : Selecting any Next Element :-

When we need to select any sibling element that follow a particular element,
we use the ~ character to combine two selectors like this, h2 ~ p

for eg,
````
<div>
  <p>BROWN COLOR NEGATI76VE</p>
  <h2>Hello World</h2>
  <a href="#">LINK COLOR WILL CHANGE</a>
  <p>BROWN COLOR POSITIVE</p>
</div>
<p class="outer">BROWN COLOR NEGATIVE
  <p>BROWN COLOR NEGATIVE</p>
</p>
````

<!-- CSS -->
h2 ~ p {
  color: brown;
  font-weight: bolder;
}
h2 ~ a {
  color: red;
  font-weight: bolder;
}


-------------------------------------------------------------------------------------
-> Q021 : Float in CSS;

#### Float Property :-

We can use the float property to put an element on the right or left side
inside its parent element

The commonly used values for this property are ...
1) left
2) right
3) none

for eg,
<!-- HTML -->
<div>
  <img src="har-ki-doon-valley-uttarakhand.jpg" alt="Har ki Doon Valley Uttarakhand"/>
  <h1>Har Ki Doon</h1>
  <p>
    Har Ki Doon or Har Ki Dun is a cradle-shaped hanging valley in the Garhwal Himalayas of Uttarakhand, India. The region is surrounded with green Bugyals (High Altitude Meadows). It is surrounded by snow-covered peaks and alpine vegetation. It is connected to Baspa Valley by the Borasu Pass. (Credits: Wikipedia)
  </p>
</div>

<!-- CSS -->
img {
  float:left;
  padding-right: 15px;
  width: 300px;
}

#### Float Clear Property :-

Float's clear property is used to clear the left or right alignment.

The value of clear should be similar to that of float specified previously. Or
you can also use the value both to simply clear both right as well as the
left direction.

for eg,
<!-- HTML -->
<body>
  <div class="intro">
    <img src="url-to-image.jpg" alt=""/>
    <h2>Header shift to right </h2>
    <p>Long description shifted to right </p>
  </div>

  <div class="another-block">
    <h2>Another block header </h2>
    <p>Another Block Description </p>
  </div>
</body>

<!-- CSS -->
img {
  float: left;
  padding-right: 15px;
  width: 150px;
}
.another-block {
  clear: left
}

#### Clearfix :-

The clear property on the next element to clear the effect of the float property. 

If the floating element is taller than its parent, it overflows the parent's
boundaries.

for eg,
<!-- HTML -->
<div class="clearfix">
  <img src="aliyar-dam-pollachi.jpg" alt="Aliyar Dam Pollachi"/>
  <p> FIRST PARAGRAPH  </p>
</div>
<div>
  <p>SECOND PARAGRAPH.</p>
</div>

<!-- CSS -->
img {
  float:left;
  padding-right: 15px;
  width: 150px;
}
div {
  background-color: lightgreen;
  padding: 15px;
}
.clearfix::after {
  content: "";
  clear: both;
  display: block;
}


-------------------------------------------------------------------------------------
-> Q020 : Position in CSS;

#### Position Property;

By default, all the HTML elements appear on the web page one after another in
the same order as specified in the HTML markup. 

for eg,
<!-- HTML -->
<body>
	<div id="relative"> Relative </div>
	<div id="absolute"> Absolute </div>
	<div id="fixed"> Fixed </div>
	<div id="sticky"> Sticky </div>
</body>

<!-- CSS -->
body {
  height: 150vh;
}
div {
  background-color: orange;
  width: 100px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  border: 3px solid darkorange;
}
#relative {
  position: relative;
  left: 50px;
  top: 50px;
}
#absolute {
  position: absolute;
  right: 0px;
  top: 0px;
}
#fixed {
  position: fixed;
  right: 0px;
  top: 50px;
}
#sticky {
  position: sticky;
  margin-top: 50px;
  top: 50px;
}

#### Position Relative :-

The default value for the position property is static. It makes the elements
follow the normal flow.

When you set an element's position to relative, you can move the element to a
new location. The top, right, bottom and left properties are used to note the
distance of the new location from the original default location.

When you set the element position to relative then element start moving from 
top, left, right, bottom as per the hierarch index of that element.

for eg, 
<body>
  <div id="div1"> Static </div>
  <div id="div2"> Relative, but not moved </div>
  <div id="div3"> Relative & moved </div>
</body>

<!-- CSS -->
div {
  border: solid 1px lightgray;
  width: 210px;
  padding: 20px;
}
#div1 {
  position: static; /* Default */
}
#div2 {
  position: relative;
}
#div3 {
  position: relative;
  left: 100px;
  top: 100px;
}

In the above example, div3's original position is directly below div2. But by
setting the position value to relative and using left and top values, we have
pushed it from the left and top by 100px from its original position.

The top and left properties wouldn't work if you remove the position property.
These properties don't work with the static position elements.

#### Difference between offsets and margins :-

//--- Top vs Margin-top :-

The top and left properties appear to work similar to the margin-top and the
margin-left properties. But there is a big difference between them.

When you set the top property of a relative element to 50px, only that element
is shifted by 50px from the top. 

But if you set the margin-top property to 50px, all the elements below this
particular element are also shifted down by 50px

//--- Left vs Margin-Left :-

When you set the left property of a relative element, only that element is
shifted from the left of its original position.

//--- Right and Bottom Offsets :-

When you set the right property of a relative element, the element actually
moves to the left. That is because the element is pushed from the right side.

for eg,
<!-- HTML -->
<body>
  <div> Relative Element </div>
</body>

<!-- CSS -->
div {
  padding: 10px;
  background-color: orange;
  position: relative;
  right: 50px;
  border: 5px solid darkorange;
}

Similarly, when you set the bottom property of a relative element, it moves
upwards, because it is pushed from the bottom

for eg,
<!-- HTML -->
<body>
  <div> Relative Element </div>
</body>

<!-- CSS -->
body {
  margin: 0;
}
div {
  width: 150px;
  padding: 10px;
  background-color: orange;
  position: relative;
  bottom: 20px;
  border: 5px solid darkorange;
}

#### Negative Offset Values :-

The top, right, bottom and left properties can also have negative values.

for eg,
<body>
  <div id="static"></div>
  <div id="relative"></div>
</body>

<!-- CSS -->
div {
  width : 80px;
  height: 80px;
}
#static {
  background-color: teal;
}
#relative {
  position: relative;
  background-color : orange;
  top: -15px;
  left: 40px;
}

#### Z-Index :-

Sometimes, we want to overlap one element over another. We can achieve this
with position:relative, but which element appears in front or at the back can
be difficult to manage. This is why, we have the z-index property.

The element with a lower z-index value goes behind the one with a higher z-index.

for eg,
<!-- HTML -->
<body>
  <div id="one"> </div>
  <div id="two"> </div>
  <div id="three"> </div>
</body>

<!-- CSS -->
div {
  width: 80px;
  height: 80px;
  position: relative;
}
#one {
  background-color: indigo;
  z-index: 3;
}
#two {
  background-color: orange;
  bottom: 50px;
  left: 30px;
  z-index: 1;
}
#three {
  background-color: teal;
  bottom: 100px;
  left: 60px;
  z-index: 2;
}

#### Position Absolute :-

When you set an element's position to absolute, you can use the top, right,
bottom and left properties to change the its position inside its parent
element.

When you set the item's position to absolete then that item start moving from top,
left, right, bottom as per the web page.

for eg,
<!-- HTML -->
<body>
    <div id="static">
      Static
    </div>
    <div id="relative">
      Relative
    </div>
    <div id="absolute">
      Absolute
    </div>  
</body>  

<!-- CSS -->
body {
  background-color: steelblue;
}
div {
  border: 2px solid white;
  padding: 20px;
  width: 200px;
  color: white;
  font-size: 1.2rem;
}
#relative {
  position: relative;
  top: 20px;
  right: 20px;
}
#absolute {
  position: absolute;
  top: 20px;
  right: 20px;
}

#### Parent Element For Absolute Position;

An absolute element's location changes with respect to its parent element.
This works only if the parent element has its own position set to a value
other than static.

If this is not so, the absolute element looks for the nearest parent whose
position is set to a value other than static. 

If no such parent element is found, it's location changes with respect to the
body itself:

for eg,
<!-- HTML -->
<div class="outer">
    <div class="box1"></div>
</div>

<!-- CSS -->
body {
  background-color: lightgrey;
  width: 500px;
  height: 500px;
}
div {
  width: 220px;
  height: 200px;
  background-color: darkgrey;
}
.outer { 
  /* Case 1, Case 2, Case 3 : Try Commenting below position, result are same */
  /*position: absolute;*/
  /*position: relative;*/
  position: static;

}
.box1 {
  width: 100px;
  height: 100px;
  background-color: yellow;
  position: absolute;
  top: 0px;
  left: 0px;
}

#### Absolute Element's Width & Height;

If an absolute element has no height specified, we can make the element fill
up the available vertical space by specifying both top and bottom values.

Similarly, we can make the absolute element fill up the available horizontal
space by specifying both left and right values when width is not specified.

NOTE : 
- Top and Bottom Veritical Spacing will work only when width is not specified.
- Left and Right Horizontal Spacing will work only when height is not specified.

for eg,
<!-- HTML -->
<div id="parent">
  <div id="absolute">
  </div>
</div>

<!-- CSS -->
#parent {
  position: relative;
  background-color: teal;
  width: 200px;
  height: 200px;
}
#absolute {
  /* No width & height */
  position: absolute;
  background-color: orange;
  left: 10px;
  right: 10px;
  top: 10px;
  bottom: 10px;
}

//--- Exception for Width and Height :-

If both top and bottom values are specified for an element and the element is
also provided a height value, the element takes up the specified height, and
ignores the bottom property value. 

Similarly, when both left and right values are provided along with a width
value, the element takes up the specified width and ignores the right
property value.

for eg,
<!-- HTML -->
<div id="parent">
  <div id="absolute">
  </div>
</div>

<!-- CSS -->
#parent {
  position: relative;
  background-color: teal;
  width: 200px;
  height: 200px;
}
#absolute {
  /* Width & height specified */
  position: absolute;
  background-color: orange;
  width: 100px;
  height: 100px;
  top: 20px;
  right: 0px; /* right ignored */
  bottom: 20px; /* bottom ignored */
  left: 0px;
}

#### Position Fixed :-

When you set an element's position to fixed, the element stays at the same
position even when you scroll away.

The top, right, bottom, and left properties are used to position the element
relative to the browser window itself.

for eg,
<!-- HTML -->
<div></div>

<!-- CSS -->
body {
  min-height: 120vh;
}
div {
  background-color: orange;
  width: 50px;
  height: 50px;
  position: fixed;
  left: 0px;
  bottom: 0px;
}

#### Position Sticky

The orange coloured div is positioned sticky in the example given below. Try
to scroll inside the example window.

A position:sticky element has a relative position until the user scrolls to
it, and then it behaves in place like a fixed element

for eg,
<!-- HTML -->
<div id="div1"></div>
<div id="sticky"></div>

<!-- CSS -->
body {
  margin: 0;
  min-height: 200vh;
}
#div1 {
  width: 100px;
  height: 100px;
  background-color: teal;
}
#sticky {
  background-color: orange;
  width: 50px;
  height: 50px;
  position: sticky;
  top: 100px;
  left: 50px;
}

//--- Position Sticky within Parent :-

The sticky element stops being sticky once the page is scrolled such that the
element reaches the bottom of its parent element.

for eg,
<!-- HTML -->
<body>
  <div id="parent">
    <div id="sticky"></div>
  </div>
</body>

<!-- CSS -->
body {
  margin: 0;
  min-height: 200vh;
}

#parent {
  width: 250px;
  height: 250px;
  background-color: teal;
  margin-top: 50px;
}

#sticky {
  background-color: orange;
  width: 100px;
  height: 100px;
  position: sticky;
  top: 0px;
}

#### Position Inset Property :-

Instead of using the individual top, right, bottom and left properties, a
single inset property can be used to specify all the four values.

->  Four values :-
- If this property has four different values separated by spaces:
- Values get assigned in the clockwise direction starting from the top.

inset: 10px 20px 30px 40px;

10px is top
20px is right
30px is bottom
40px is left

-> Three values:-
inset: 10px 20px 30px;
10px is top
20px is right as well as left
30px is bottom

-> Two values :-
inset: 10px 20px;
10px is top and bottom
20px is right and left

-> One value :-
inset: 10px;

for eg,
<!-- HTML -->
<body>
  <div class="parent">
    <div class="child" id="child1">
    </div>
  </div>
  <div class="parent">
    <div class="child" id="child2">
    </div>
  </div>
  <div class="parent">
    <div class="child" id="child3">
    </div>
  </div>
  <div class="parent">
    <div class="child" id="child4">
    </div>
  </div>
</body>

<!-- CSS -->
.parent {
  width: 100px;
  height: 100px;
  background-color: teal;
  margin-bottom: 10px;
  position: relative;
}
.child {
  position: absolute;
  background-color: orange;
}
#child1 {
  inset: 10px 20px 30px 0px;
  /* top right bottom left - clockwise direction starting from top */
}
#child2 {
  inset: 10px 20px 30px;
  /* top right&left bottom */
}
#child3 {
  inset: 10px 20px;
  /* top&bottom right&left */
}
#child4 {
  inset: 10px;
  /* all four */
}

//--- Inset Property Auto Values :-

For inset property, you can use the value auto to automatically calculate one
or more offset values

for eg,
<!-- HTML -->
<div id='absolute'></div>

<!-- CSS -->
div {
  background-color: orange;
  width: 50px;
  height: 50px;
  position: absolute;
  inset: auto 10px 0 auto;
}


-------------------------------------------------------------------------------------
-> Q019 : Display none vs Visibility Hidden in CSS;

It remove the element from page and DOM.
for eg, Display:none;

It remove only from page.
for eg, Visibility:hidden;


-------------------------------------------------------------------------------------
-> Q018 : Display in CSS;;

#### Display Block :-

The div and p elements have their default display set to block. Some more
block-level elements are the heading elements - h1 to h6, header, footer,
section and form.

Block elements start on a new line, occupy 100% width by default, and can have
height, width properties and also have functional margin on all four sides.

We can make elements like span, a and img behave like block-level elements by
setting their display property to block

for eg,
<!-- HTML-->
Example 1: <span>Now span also starts on a new line</span><br>
Example 2: <p>Paragraph starts on a new line and occupies 100% width</p>
<a href="#">Link 1</a>
<a href="#">Link 2 in the next line</a>

<!-- CSS -->
p {
  background-color: yellow;
  margin-top: 30px;
}
span, a {
  display: block;
  background-color: orange;
  margin-top: 30px;
}

#### Display Inline :-

The span, a and img elements have their display set to inline by default.
These elements do not start on a new line and take up only as much space as
required.

ul - block level element 

for eg,
<!-- HTML -->
<ul>
  <li><a href="#">Home</a></li>
  <li><a href="#">About</a></li>
  <li><a href="#">Contact</a></li>
</ul>

<!-- CSS -->
ul {
	display: inline;
	margin: 10px;
}

#### Display Inline Block :-

Sometimes it's helpful to have elements display in the same line but also
behave like block-level elements with specified height and width.

This can be achieved with the display value of inline-block

for eg,
<!-- HTML -->
<p>Some links for your reference:</p>
<a href="#">Link 1</a>
<a href="#">Link 2</a>

<!-- CSS -->
a {
  display: inline-block;
  background-color: orange;
  width: 150px;
  height: 50px;
  border-radius: 10px;
  text-align: center;
  font-size: 16px;
  text-decoration: none;
  line-height: 3rem;
  margin-top: 50px;
}

#### Display None :-

The display property has another value none which makes the element completely disappear.

for eg,
<!-- HTML -->
<span id="span1">You cannot see me</span>
<span id="span2">You can see me</span>

<!-- CSS -->
#span1 {
  display: none;
}


-------------------------------------------------------------------------------------
-> Q017 : CSS Box Model;;

#### CSS Box Model or content-box :-

In CSS, all elements are represented as rectangular boxes in the browser. 

The width and height specified for an element in CSS are not the final width
and height occupied by the element on the web page. 

The actual dimensions include the collective size of padding, borders and
margins along with the content area. Like, 

Final width = content width + left padding + right Padding + left Border 
							+ right Border + left Margin + right Margin

Final height = content height + top padding + bottom Padding + top Border 
							+ bottom Border + top Margin + bottom Margin

#### Box Sizing Model :-

The calculations for the width or height in the box model tend to become complex. 
This is why, CSS has an alternative box model, where the padding and border sizes 
are included within the specified width. The margin is excluded. 
This makes the calculation of the width simpler.

The property box-sizing is used to determine how these calculations will be done. 
By default, the value is content-box because of which the original box model is used. 
When we set this to border-box, the alternate model is followed.


<!--- 
	Example of content-box and box-sizing border box model
-->
<!-- HTML -->
<body>
	<div id="standard"> Standard box model </div>
	<div id="alternate"> Alternate box model </div>
</body>

<!-- CSS -->
div {
  background-color: lightgreen;
  width: 250px;
  height: 80px;
  padding: 20px;
  border: solid 10px darkgreen;
  margin: 30px;
}
#standard {
  box-sizing: content-box; /* Default */
}
#alternate {
  box-sizing: border-box;
}


-------------------------------------------------------------------------------------
-> Q016 : Styling Forms in CSS;;

#### Styling Width & Height for Text Inputs :-

The text fields and textareas in forms can be styled in multiple ways using
width, height, padding, border, color, background-color and fonts. 

for eg,
<!-- 
	!! Refer HTML !!
-->
<!-- HTML -->
<body>
	<form>
		<input type="text" placeholder="Your Name" /><br>
		<input type="radio" id="male" name="gender" value="male">
		<label for="male">Male</label>
		<input type="radio" id="female" name="gender" value="female">
		<label for="female">Female</label>
		<input type="radio" id="other" name="gender" value="other">
		<label for="other">Other</label><br>
		<input type="button" value="Submit">
	</form>
</body>

<!-- CSS -->
form {
  width: 300px;
  border: 3px solid black;
}
input {
  width: 200px;
  height: 25px;
}
textarea {
  width: 100%;
  height: 100px;
}

#### Style Input by type :-

Select each input type differently, we can use it like this -

input[type="value"]

for eg,
<!-- CSS -->
input[type="text"] {
  width: 300px;
  height: 25px;
  margin-bottom: 20px;
}
input[type="radio"] {
  width: 50px;
  height: 10px;
}
input[type="button"] {
  margin-top: 20px;
  width: 200px;
  height: 25px;
}

#### Padding & Margin for text inputs :-

Padding and Margin can be used inside the text inputs. 

for eg,
<!-- CSS -->
input[type="text"], textarea {
  padding: 15px;
  margin: 10px 0;
  width: 300px;
}

#### Styling with Borders and Colors :-

Text input fields and textareas have a border by default. But we can change
their look using the border property.

for eg,
<!-- CSS -->
input[type="text"], textarea {
  width: 300px;
  padding: 15px;
  margin: 10px 0;
  color: indigo;	
  background-color: lavender;
}
input[type="text"] {
  border: none;
  border-bottom: 1px solid lightgray;
   border-radius: 10px;
}
textarea {
  border: 1px solid lightgray;
}

#### Styling Font-Family and Font-Size :-

By default, the text field has a sans-serif font and the textarea has a serif
font. The font sizes are different too.

Most of the HTML elements inherit the font family and font size from body, but
the text input fields don't. They use their default values. 

TO customize, we need to specify these properties separately

for eg,
input[type="text"], textarea {
  width: 300px;
  padding: 15px;
  margin: 5px 0;
  width: 20em;
  border: 1px solid lightgray;
  font-family: 'Helvetica', sans-serif;
  font-size: 1em;
}

#### Textarea resize :-

The textarea field can be resized when you drag the resizer at the bottom
right corner in any direction. To prevent resizing horizontally, vertically
or in both directions, we can use the resize property.

Default value for this property is both which allows resizing in both vertical
and horizontal direction. 

Other accepted values are horizontal, vertical, and none.

for eg,
<!-- HTML -->
<form>
  <p>Try dragging the resizer and notice that you can resize it only vertically:</p>
  <textarea id = "vertical-resizer" rows="4" placeholder="Vertical Slider"></textarea>

  <p>Try dragging the resizer and notice that you can resize it only horizontally:</p>
  <textarea id = "horizontal-resizer" rows="4" placeholder="Horizonal Slider"></textarea>
</form>

<!-- CSS -->
textarea {
  width: 70%;
  padding: 15px;
  border: 1px solid lightgray;
}
#horizontal-resizer {
    resize: horizontal;
}
#vertical-resizer {
    resize: vertical;
}

#### Styling Select Inputs :-

The select input can be styled in the standard manner much like any other HTML
element or a form element

for eg,
<!-- HTML -->
<form>
  <fieldset>
    <legend>Styling Select</legend>
    <p>Are you happy with our service?</p>
	  <select name="review">
	    <option value="5">Very Happy</option>
	    <option value="4">Satisfied</option>
	    <option value="3">Neutral</option>
	    <option value="2">Unhappy</option>
	    <option value="1">Disappointed</option>
	  </select>  
  </fieldset>
</form>

<!-- CSS -->
select {
  width: 300px;
  padding: 15px;
  margin: 5px 0;
  width: 20em;
  border: 1px solid lightgray;
  background-color: beige;
  font-family: 'Helvetica', sans-serif;
  font-size: 1em;
}
select > option {
  font-size: 1.5em;
  line-height: 1px;
}

#### Styling Border :-

Buttons can be styled in various ways using the standard properties - width,
height, padding, background-color, color, border, border-radius, font-family,
font-size.

for eg,
<!-- HTML -->
````
<form
	<input type="button" value="Next"/>
	<input type="reset" value="Reset"/>
	<input type="submit" value="Submit"/>
</form>
````

<!-- CSS -->
input[type="button"] {
  width: 100px;
  padding: 12px 16px;
  background-color: #4568bb;
  color: white;
  font-family: sans-serif;
  font-size: 0.9em;
  border: none;
  border-radius: 5px;
}
input[type="reset"] {
  width: 100px;
  padding: 12px 16px;
  margin-left: 10px;
  background-color: white;
  color: #4568bb;
  font-family: sans-serif;
  font-size: 0.9em;
  border: 1px solid #4568bb;
  border-radius: 5px;
}
input[type="submit"] {
  width: 100%;
  padding: 15px 0;
  margin-top: 10px;
  background-color: green;
  color: white;
  font-family: sans-serif;
  font-size: 1em;
  border: none;
}

#### Hover & Focus Styles

When you take your mouse over a text input or a button, the background or
border colour can be changed using the :hover pseudo-class selector.

when you tap on an input field or move focus to it using the tab key on your
keyboard, a blue outline appears around the input field. This style can be
changed using the :focus pseudo-class selector.

for eg,
<!-- HTML -->
````
<input type="text" id="email" placeholder="Email ID" />
<input type="button" id="subscribe" value="Subscribe" /
````

<!-- CSS -->
#email {
  border: solid 1px #dddddd;
  padding: 10px;
}
#subscribe {
  padding: 10px;
  border: none;
  background-color: #6789ff;
  color: white;
}
/* Same hover & focus styles */
#email:hover, #email:focus {
  border: solid 1px #888888;
  outline: none;
}
#subscribe:hover, #subscribe:focus {
  background-color: #4567de;
  cursor: pointer;
}


-------------------------------------------------------------------------------------
-> Q015 : Styling Tables in CSS;;

#### Table Border :-

The border property for the table element adds a border around the table:

for eg, 
<!-- 
Refer This table for Every example
-->
<!-- HTML -->
<body>
	<table>
	  <tr>
	    <th>Name</th>
	    <th>Age</th>
	    <th>Gender</th>
	  </tr>
	  <tr>
	    <td>Oliver</td>
	    <td>25</td>
	    <td>Male</td>
	  </tr>
	  <tr>
	    <td>Eve</td>
	    <td>30</td>
	    <td>Female</td>
	  </tr>
	</table>
</body>

<!-- CSS -->
table, th, td {
  border: 1px solid darkgray;
}

#### Table Collapse :-

When we add borders around cells, we get double borders. We can use the
property border-collapse to change this behavior.

Default value for this property is separate.

for eg,
<!-- CSS -->
table, th, td {
  border: 1px solid darkgray;
  border-collapse: collapse;
}

#### Table Width and Height :-

By default, the table occupies only as much width as required by the content.
But we can manually set the width for a table too.

If the specified width is smaller than the content width, the columns will
occupy the minimum width required to display the content properly.

If the specified width is larger than required, the additional width is added
to all the columns proportionately.

for eg,
<!-- CSS -->
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
table {
  width: 400px;
  height: 200px;
}
th {
  height: 55px;
}
td {
  height: 35px;
}

#### Table Text Alignment - Horizontally :-

By default, the text in the header row is center aligned and the text in all
other rows is left aligned. The text-align property can be used to change
this alignment using the values left, right, center or justify

for eg,
<!-- CSS -->
table {
	width: 100%;
	text-align: center;
}
table > tr {
	height : 50px
}

#### Table Text Alignment - Vertically :-

When you set a height for the entire table or for individual rows, the text is
vertically aligned to the middle by default. The vertical-align property can
be used to change this alignment using the values top, middle or bottom.

for eg,
<!-- CSS -->
table, th, td {
	width : 100%;
	border: 1px solid dark;
	border-collapse: collapse;
}
th, td {
	/** Text Alignments **/
	text-align: center;
	veritical-align: center;

	/** Padding Space **/
	padding : 10px 15px 10px 15px;
}
th {
	/* backgroud colors */
	background-color : blue;
}
td {
	/* background colors */
	background-color : lightgrey;
}

NOTE: The vertical-align property has no effect on the table selector.

#### Styling Specific Rows (tr:tag):-

We can style specific rows of a table using pseudo classes like 

-> Select First Child, tr:first-child, 
	for eg, td:first-child 

-> Select Last Child, tr:last-child
	for eg, td:last-child 

-> Select nth child, tr:nth-child pseudo class 
	for eg, tr:nth-child(1)

-> Select Even or Odd child, 
	for eg, tr:nth-child(even), tr:nth-child(odd)

#### Styling Specific Columns (td:tag):-

We can style specific columns of a table using pseudo classes like 

-> Select first child using, 
	for eg, td:first-child 

-> select the last child using, 
	for eg, td:last-child 

-> Select the nth-child using,
	for eg, td:nth-child(1)

-> Select the even or odd child,
	for eg, td:nth-child(even), td:nth-child(odd)


-------------------------------------------------------------------------------------
-> Q014 : Styling Un/Ordered List in CSS 

#### Styling : Ordered and Unordered List :-

//--- List Style Type as decimal, alpha, roman, shapes :-

Unordered list, each item has a little circular disc as marker type by default. 

We can change this marker using the property 'list-style-type'.

Available Values for 'list-style-type' property :-
-> disc, circle
-> decimal
-> lower-alpha, upper-alpha
-> lower-roman, upper-roman

for eg,
<!-- HTML -->
<body>
	<h3> Styling Unordered List </h3>
	<ul>
	  <li>English</li>
	</ul>
</body>

<!-- CSS -->
ul {
	list-style-type: lower-alpha
}

//--- List Style Type as Image :-

The property 'list-style-image' can be used to display an image 
in place of the list item marker.

for eg,
<!-- HTML -->
<body>
	<ul>
		<li> Apple </li>
		<li> Mango </li>
		<li> Banana </li>
	</ul>
</body>

<!-- CSS -->
ul {
	list-style-image : url('new-marker.png');
}

//-- List Style Type Position :-

The list-style-position property is used to specify whether the list marker is
placed within the list text or outside the list text.

Default value for "list-style-position" : outer;

for eg,
<!-- HTML -->
<body>
	<h3>Un/Ordered List</h3>
	<ul id="inner-marker-pointer">
		<li>Inner Item #1</li>
		<li>Inner Item #2</li>
		<li>Inner Item #3</li>
	</ul>
	<ul id="outer-marker-pointer">
		<li>Outer Item #1</li>
		<li>Outer Item #2</li>
		<li>Outer Item #3</li>
	</ul>
</body>

<!-- CSS -->
#inner-marker-pointer {
	list-style-type : lower-alpha;
	list-style-position : inner;
}
#outer-marker-position {
	list-style-type: lower-alpha;
	list-style-position : outer;
}


-------------------------------------------------------------------------------------
-> Q013 : Styling Text in CSS;

#### Styling : Anchor Links :-

Links can be styled in many different ways using properties like color,
background-color, border, padding, text-decoration and so on:

<body>
	<a href="#" id="first">
	  Colored link
	</a>
</body>

<!-- CSS -->
a {
	text-decoration: none;
}

#### Styling : Anchor Links With States :-

We can change the appearance of links not only like the normal elements, but
also depending on some user actions. Like when the user takes their cursor
over the link, or just when the user clicks the link or based on whether the
link was previously visited or not.

we use the following link states:

a:visited - Applies if the link was visited previously

a:hover - Applies when the user takes the cursor over the link

a:active - Applies when the link is just clicked

for eg,
<!-- HTML -->
<body>
	<p> PARAGRAPH	</p>
	<a href="#"> Hover and click </a>
</body>

<!--CSS -->
a {
  color: tomato;
}
a:visited {
  color: darkgrey;
}
a:hover {
  color: orange;
  text-decoration: none;
}
a:active {
  color: darkred;
}

Here, a:visited, a:hover and a:active are called Pseudo-class selectors.

a:active must be specified after a:hover and a:hover must be specified after
a:visited for the styles to take effect.


-------------------------------------------------------------------------------------
-> Q012 : Opacity in CSS;

#### Opacity :-

The opacity property is used to define transparency for elements.

You can specify any value between 0.0 and 1.0.

Here, 0 is fully transparent, 0.5 is semi-transparent and 1 is fully opaque.

for eg,
<!-- HTML -->
<body>
	<button id="first">
	  Click me first
	</button>
	<button id="second">
	  Click me later
	</button>
</body>

<!-- CSS -->
#first {
	/* 
	Default value ~ 1  
	Full Opaque;
	*/
  opacity: 1;
}
#second {
  opacity: 0.3;
}

#### Opacity using RGBA :-

When we set the opacity for a parent element, all the child elements also
inherit the same value:

Opacity of the div is set to 0.5, but the child elements h1 and p also become
semi-transparent. This makes it hard to read the text.

If we want the opacity to apply only to the background, we can specify the
background color value using rgba instead of using rgb.

rgba(red, green, blue, alpha)

The alpha parameter sets the opacity. It takes in any value ranging from 0.0
to 1.0

for eg,
<!-- HTML -->
<body>
	<div>
	  <h1>Autumn</h1>
	  <p>
	    Autumn, also known as fall, is one of the four temperate seasons. Outside the tropics, autumn marks the transition from summer to winter, in September (Northern Hemisphere) or March (Southern Hemisphere), when the duration of daylight becomes noticeably shorter and the temperature cools considerably.
	  </p>
	</div>
<body>

<!-- CSS -->
div {
  margin: 20px;
  padding: 30px;
  background-color: rgba(253,186,116,0.5);
}

-------------------------------------------------------------------------------------
-> Q011 : Borders in CSS;

#### Border Color :-

The border-color property is used to specify the colour of the borders using
color names or RGB or HEX values.

When this property is not set, the border takes the value of the color
property of the element. The default value for color is black.

Border colour can also be set to transparent

for eg,
<!-- HTML -->
<body>
	<div id="first"> First </div>
</body>

<!-- CSS -->
#first {
	border-color : grey;
	border-width : 2px 3px 4px 1px;
	border-style : dashed;
}

#### Border Style :-

The border-style property is used to identify the type of border:

for eg,
<!-- HTML -->
<body>
	<div id="first"> Border on all sides </div>
	<div id="second"> Green dotted border at the bottom </div>
	<button> Button with 3D effect </button>	
</body>

<!-- CSS -->
div {
  padding: 10px;
  margin: 10px;
}
#first {
  border-style: solid;
}
#second {
  border-style: dashed;
}
#third {
  border-style: double;
}

Border Style can be of different types :- 
solid, dashed, double, dotted, groove, ridge, inset, outset and none.

//--- Border Style With Multiple Values :-

For the four sides of an element, we can provide different border styles.

When this property has only one value specified, the same style is applied to
all four sides.

When it has two values, the first value is applied to the top and bottom
borders, and the second value is applied to the right and left borders:

for eg,
<!-- HTML -->
<body>
	<div id="first"> Border on all sides </div>
</body>

<!-- CSS -->
#first {
	/* 
	For 2 side here have different styles
	border-style: dashed dotted;
	*/

	/* For 2 side here have different styles */

  border-style: dashed solid dotted outset;
}

#### Border Width :-

The border-width property is used to specify the thickness of the borders.

For specifying values, we can use the standard absolute or relative units or
we can use values like thin, medium or thick.

When this property is not set, a medium border appears by default.

for eg,
<!-- HTML -->
<body>
	<div id="first"> Thin border </div>
</body>

<!-- CSS -->
#first {
  border-style: solid;
  border-width: 2px;
}

//--- Border Width With Multiple Values:-

We can specify one, two, three or four values for border-width for defining
different border thickness on different sides:

When it has two values, the first value is applied to the top and bottom
borders, and the second value is applied to the right and left borders

for eg,
<!-- HTML -->
<body>
	<div id="first">
  	Thin borders on top and bottom, 4px width on right and left.
	</div>
</body>

<!-- CSS : 2 Values Width -->
#first {
  border-style: solid;
  border-width: thin 4px;
}

<!-- CSS : 3 Values Width -->
#first {
  border-style: solid;
  border-width: 1px 2px 4px;
}

#### Border Shorthand :-

The border properties in CSS are used to create borders around an HTML
element. We can control the width, color and the general styling of the
border using these properties.

Popular Border can be of different types :-
1) Dashed 
2) Dotted
3) Solid
4) Ridge 
5) Outset

for eg,
<!-- HTML -->
<body>
	<div id="first"> Border on all sides </div>
	<div id="second"> Green dotted border at the bottom </div>
	<button> Button with 3D effect </button>	
</body>

<!-- CSS -->
div {
	border : 2px solid dashed;
}
#first {
	border : 2px dashed darkgrey;
}
#second {
	border : 2px dotted organge;
}

#### Border Sides :-

We can set different styles, widths and colours for the borders of the
different sides of an element. We do this by specifying multiple values for
the same property, like border-width: 3px 3px 4px 5px.

However, there are individual properties such as border-top-style,
border-right-width, border-bottom-color among others, for styling borders for
the specific sides.

for eg,
<!-- HTML -->
<body>
	<div id="first">
	  Left and right color properties
	</div>
	<div id="second">
	  Top and bottom style properties
	</div>
</body>

<!-- CSS -->
div {
  padding: 10px;
  margin: 10px;
}
#first {
  border-style: solid;
  border-left-color: red;
  border-right-color: green;
}
#second {
  border-top-style: dashed;
  border-bottom-style: dashed;
  border-color: #cccccc;
}

#### Borders Corners :-

When you need rounded corners instead of the default sharp corners, you can
use the border-radius property.

for eg,
<!-- HTML -->
<div id="first"> </div>

<!-- CSS -->
#first {
  background-color: red;
  border: 5px solid darkred;
  border-radius: 50%;
}

//--- Border Corners With Multiple Values;

You can specify border radius for each corner individually using the properties:

border-top-left-radius
border-top-right-radius
border-bottom-left-radius
border-bottom-right-radius

for eg,
<div id="first"> Border Corner </div>

<!-- CSS -->
#first {
	border-top-left-radius : 10,
	border-top-right-radius : 10, 
	border-bottom-left-radius : 10, 
	border-bottom-right-radius : 10
}


-------------------------------------------------------------------------------------
-> Q010 : Backgrounds in CSS;;

#### Background Color :-

We can add a background color to an HTML element using the background-color
property. Color can be specified using color names, HEX values or RGB values.

for eg,
<!-- HTML -->
<p>	Paragraph </p>

<!-- CSS -->
p {
	background-color: lightgrey;
	color: darkgrey;
}

#### Background Image :-

An image can be added to the background of any element using the
background-image property.

for eg,
<!-- HTML -->
<body>
	<h1>Monsoon</h1>
	<p>
	  A monsoon is traditionally a seasonal reversing wind accompanied by corresponding changes in precipitation, but is now used to describe seasonal changes in atmospheric circulation and precipitation associated with the asymmetric heating of land and sea.
	</p>
</body>

<!-- CSS -->
body {
  background-image: url('https://images.pexels.com/photos/4913167/pexels-photo-4913167.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=600');
  padding: 30px;
  color: white;
}

#### Background Repeat :-

By default, the background image repeats itself horizontally and vertically,
if it's smaller than the element. This can be changed using the
background-repeat property.

Required Values : 
repeat(default), no-repeat, repeat-x (horizontally), repeat-y (Vertically)

for eg,
<!-- HTML -->
<body>
	<h1>Monsoon</h1>
	<p>
	  A monsoon is traditionally a seasonal reversing wind accompanied by
	  corresponding changes in precipitation, but is now used to describe
	  seasonal changes in atmospheric circulation and precipitation associated
	  with the asymmetric heating of land and sea.
	</p>
</body>

<!-- CSS -->
body {
  padding: 60px;
  background-image: url('https://images.pexels.com/photos/2512387/pexels-photo-2512387.jpeg?auto=compress&cs=tinysrgb&w=150');
  background-repeat: repeat-x;
}

#### Background Size :-

The background image for any element retains its original size. To adjust the
image size, we need to use the background-size property.

When this property is set to cover, the image stretches or scales down in size
to fill the entire container

We can also specify the exact width and height in pixels or percentage.

If only one value is specified, then width is set to that value and height is 
auto-adjusted 

If we want the image to be fully visible, then background size property can be
set to contain.

for eg,
<!-- HTML -->
<body>
	<div>
		<h1>Monsoon</h1>
		<p> A monsoon is traditionally a seasonal reversing wind accompanied by
		corresponding changes in precipitation, but is now used to describe
		seasonal changes in atmospheric circulation and precipitation associated
		with the asymmetric heating of land and sea.</p>
	</div>
</body>

<!-- CSS -->
div {
  padding: 60px;
  background-image: url('https://images.pexels.com/photos/2512387/pexels-photo-2512387.jpeg?auto=compress&cs=tinysrgb&w=400');
  /* Image stretches to occupy full space */
  background-size: cover;
}

#### Background Position :-

By default, the background image starts at the top left corner of its HTML
element. This can be changed using the background-position property.

This property takes in two values like this: background-position: left center.
The first value is for the horizontal and the second one is for the vertical
position.

Required Values :- Top, Left, Right, Bottom 

for eg,
<!-- HTML -->
<body>
	<div> </div>
</body>

<!-- CSS -->
body {
	background-color: cyan	;
}
div {
	background-image : url('url-to-image');
	background-size : 250px 250px;
	background-position: center center;
	background-repeat: no-repeat;
}


-------------------------------------------------------------------------------------
-> Q009 : Text Formatting in CSS;;

#### Text Color :-

We can set the colour of the text in any element on the web page using its color property.

The values can be color names, HEX values, or RGB values.

for eg,
<!-- HTML -->
<body>
	<h2>Hello World</h2>
	<p>Paragraph</p>
	<ul>
		<li>Item</li>
	</ul>
</body>

<!-- CSS -->
h2 {
  color: purple;
}
p {
  /* Crimson */
  color: #dc143c;
}
ul {
  /* DarkCyan */
  color: rgb(0, 139, 139);
}

#### Text Alignments :-

We can make our text align the way we want, using the text-align property.
We can use the values left, right, center or justify to align the text
accordingly.

for eg,
<!-- HTML -->
<body>
	<h2>Hello World</h2>
	<p>Paragraph</p>
	<ul>
		<li>Item</li>
	</ul>
</body>

<!-- CSS -->
h2 {
  text-align: center;
}
p {
  text-align: justify;
}
ul {
  text-align: left;
  /* This is the default value */
}

#### Text Decoration :-

We can underline text, strike through it or remove an underline using the
text-decoration property.

for eg,
<!-- HTML -->
<body>
	<h2>Hello World</h2>
	<p>Paragraph</p>
	<ul>
		<li>Item</li>
	</ul>
</body>

<!-- CSS -->
h2 {
  text-decoration: underline;
}
p {
  text-decoration: line-through;
}
ul {
  text-decoration: none;
  /* Removes default underline */
  color: purple;
}
ul > li {
  color: green;
}

#### Text Line Height :-

We can control the space between lines of text using the line-height
property.

The value can be given as a unitless number like 1.5, 2 etc or in px, em, % or
even the keyword normal.

The number value or percentage is used as a multiplier. line-height: 1.5 means
the space between the lines will be 1.5 times the font size of the element.

The value of line-height: normal is set based on the browser's default value.

for eg,
<!-- HTML -->
<body>
	<h2>Hello World</h2>
	<p>Paragraph</p>
	<ul>
		<li>Item</li>
	</ul>
</body>

<!-- CSS -->
h2 {
  line-height: 1em;
}
p {
  line-height: 140%;
}
ul > li {
  line-height: 2;
}

#### Text Letter Space :-

We can control the spacing between letters of the text using the
letter-spacing property.

A positive value increases the space between the letters in a word, while a
negative value decreases it.

for eg,
<!-- HTML -->
<body>
	<h2>Hello World</h2>
</body>

<!-- CSS -->
h2 {
  letter-spacing: 1em;
}

#### Text Font Space :-

We can modify the size of any text using the font-size property.

for eg,
<!-- HTML -->
<body>
	<h1>The Solar System</h1>
	<p>
	  The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly.
	</p>
</body>

<!-- CSS -->
h1 {
  font-size: 2.4em;
}
p {
  font-size: 120%;
}

#### Text Font Weight :-

The font-weight property is used to make text bolder or lighter.

We can use values such as normal, bold, lighter, bolder for this. We can also
use numbers in the multiples of 100 such as 100, 200 and so on up to 900.
Here 100 is the lightest and 900 is the boldest

for eg,
<!-- HTML -->
<body>
	<p id="first">Hello World</p>
	<p id="second">Second Paragraph</p>
</body>

<!-- CSS -->
#first {
	/* Bold */
  font-weight: bold;
}
#second {
	/* Normal */
  font-weight: 400; 
}

#### Text Font Family :-

The font-family property can help us choose which font we want for our text.

By default, this value is serif. The other generic font families available are
sans-serif, monospace, cursive and fantasy

for eg,
<!-- HTML -->
<p id="serif">
  This is a serif font.
</p>

<!-- CSS -->
#serif {
   font-family: 'Times New Roman', serif;
}
p {
	font-size: 1.2em;
  margin-top: 10px;
}

Here, Serif is the fallback font for #serif id based element.


-------------------------------------------------------------------------------------
-> Q008 : Spacing With Padding in CSS;;

#### Padding :-

The padding property defines the spacing within an element. It controls the
space between the content in the element and the element's boundaries.

for eg,
<!-- HTML -->
<body>
	<p> A paragraph with 2em padding on all four side </p>
</body>

<!-- CSS -->
p {
  background-color: tan;
  padding: 2em;
}

#### Padding Shorthand Property :-

Instead of using individual properties for top, bottom, right and left
padding, the single padding property can be used to specify different values
for each direction.

-> Padding With Four values :-

If this property has four different values separated by spaces:

padding: 10px 20px 30px 40px;


10px is top padding
20px is right padding
30px is bottom padding
40px is left padding

The values get assigned in clockwise direction starting from the top.

-> Padding With Three values :-

If this property has three values:

padding: 10px 20px 30px;
10px is top padding
20px is right and left padding
30px is bottom padding

-> Padding With Two Values :-

If this property has two values:

padding: 10px 20px;

Top padding and bottom padding are both 10px.
Right padding and left padding are both 20px.

-> Padding With One value :-

If this property has only one value:

padding: 10px;

All four padding values are 10px

for eg,
<!-- HTML -->
<body> 
	<p>PARAGRAPH</p>
</body>

<!-- CSS -->
p {
	background-color: lightgray;
	padding: 50px 100px 80px 20px; /* top right bottom left */
}


-------------------------------------------------------------------------------------
-> Q007 : Spacing With Margin in CSS;;

#### Margins :-

The margin property defines the spacing around an element.

for eg,
<!-- HTML -->
<body>
	<p>A paragraph with 2em margin on all four sides</p>
	<span>Another element here</span>
</body>

<!-- CSS -->
body {
  background-color: orange;
}
p {
  background-color: yellow;
  margin: 2em;
}

#### Side Margin :-

We can separately set margin properties for each side of an element using
margin-top, margin-bottom, margin-left and margin-right.

for eg,
<!-- HTML -->
<body>
	<p id="first">
	  A paragraph with 50px margin at the top and 100px margin on the left
	</p>
	<p id="second">
	  Another paragraph with 80px margin on the right
	</p>
</body>

<!-- CSS -->
#first {
  background-color: yellow;
  margin-top: 50px;
  margin-left: 100px;
}
#second {
  background-color: orange;
  margin-right: 80px;
}

#### Margin Shorthand Property :-

Instead of using individual properties for top, bottom, right and left
margins, the single margin property can be used to specify different values
for each direction.

-> Margin with Four values :-

If this property has four different values separated by spaces:

margin: 10px 20px 30px 40px;

10px is top margin
20px is right margin
30px is bottom margin
40px is left margin

for eg,
<!-- HTML -->
<body>
	<p id="first">A paragraph with four margin values</p>
	<p>Web design encompasses many different skills and disciplines in the
	production and maintenance of websites.</p>
</body>

<!-- CSS -->
#first {
  background-color: yellow;
  /* top right bottom left */
  margin: 50px 100px 80px 20px; 
}

-> Margin With Three Values :-

If this property has three values:

margin: 10px 20px 30px;

10px is top margin
20px is right margin as well as the left margin
30px is bottom margin

for eg,
<!-- HTML -->
<body>
	<p id="first">A paragraph with four margin values</p>
	<p>Web design encompasses many different skills and disciplines in the
	production and maintenance of websites.</p>
</body>

<!-- CSS -->
#first {
  background-color: yellow;
  /* top right-left bottom */
  margin: 50px 0px 80px; 
}

-> Margin With Two values :-
If this property has two values:

margin: 10px 20px;

10px is top and bottom margin
20px is right and left margin

for eg,
<!-- HTML -->
<body>
	<p id="first">A paragraph with four margin values</p>
	<p>Web design encompasses many different skills and disciplines in the
	production and maintenance of websites.</p>
</body>

<!-- CSS -->
#first {
  background-color: yellow;
  /* top-bottom right-left */
  margin: 50px 100px; 
}

-> Margin With One value
If this property has only one single value:

margin: 10px;

All four margins are 10px in size.

for eg,
<!-- HTML -->
<body>
	<p id="first">A paragraph with four margin values</p>
	<p>Web design encompasses many different skills and disciplines in the
	production and maintenance of websites.</p>
</body>

<!-- CSS -->
#first {
  background-color: yellow;
  margin: 50px;
}

#### Margin With Negative Values :-

The margin properties can also accept negative values. This reduces the
spacing around elements.

for eg,
<!-- HTML -->
<body>
	<div id="first"></div>
	<div id="second"></div>
</body>

<!-- CSS -->
#first {
  background-color: orange;
  height: 100px;
}
#second {
  background-color: green;
  width: 50%;
  height: 100px;
  margin-top: -2em;
}

#### Marign with Auto Alignments :-

The margin property can be set to auto value. This horizontally centers an
element.

The left and right margins are auto calculated by equally splitting the
remaining space.

for eg,
<!-- HTML -->
````
<body>
	<div id="auto-align">Check Alignment
</body>
````

<!-- CSS -->
.auto-align {
  width: 75%;
  margin: auto;
}

REMARK : 
- If margin-left is set to auto, the remaining space is assigned to left
  margin and hence the element aligns to the right.

- If margin-right is set to auto, the element aligns to the left.


-------------------------------------------------------------------------------------
-> Q006 : Min Width and Min Height;;

#### Minimum Height (~ min-height) :-

The min-height property is used to define the minimum height of an element.

If the content is larger than the value given to the min-height, this property
has no effect. But, if it is smaller than the min-height value, the minimum
height is applied.

When both min-height and height are defined, the larger of the two values is
applied, as can be seen in the code examples given below:

for eg,
<!-- HTML -->
<body>
	<div>
		<p id="first"> FIRST PARAGRAPH </p>
		<p id="second"> SECOND PARAGRAPH </p>
	</div>
</body>

<!-- CSS -->
#first {
  /*Minimum height has no effect */
  min-height: 10px;
  background-color: yellow;
}
#second {
  height: 50px;
  min-height: 100px;
  /* Greatest value is applied */
  background-color: orange;
}

#### Minimum Width (~ min-width) :-

The min-width property is used to define the minimum width of an element.

If the content is larger than the min-width value, this property has no
effect. But if the content is smaller than the min-width value, the minimum
width is applied.

When both min-width and width are defined, the larger of the two values is
applied.

View the editor in full screen mode and change the width of the output panel
to feel the difference.

for eg,
<!-- HTML -->
<body>
	<div>
		<p id="first"> FIRST PARAGRAPH </p>
		<p id="second"> SECOND PARAGRAPH </p>
	</div>
</body>

<!-- CSS -->
#first {
  width: 50%;
  min-width: 250px;
  /* Greatest value is applied */
  background-color: yellow;
}
#second {
  width: 50%;
  min-width: 500px;
  /* Greatest value is applied */
  background-color: orange;
}


-------------------------------------------------------------------------------------
-> Q005 : Max Width and Max Height;;

#### Maximum Height (~ max-height) :-

The max-height property is used to define the maximum height of an element.

If the content is smaller than the value of the max-height, this property has
no effect. But, if the content is larger than the max-height value, the
content overflows.

When both max-height and height are defined, the smaller of the two values is
applied, as can be seen in the code example given below:

for eg,
<!-- HTML -->
<body>
	<p id="first">FIRST PARAGRAPH</p>
	<p id="second">SECOND PARAGRAPH</p>
</body>

<!-- CSS -->
#first {
  height: 100px;
  max-height: 200px;
  /* Least value is applied */
  background-color: yellow;
}
#second {
  height: 100px;
  max-height: 25px;
  /* Least value is applied */
  background-color: orange;
}

#### Maximum Width (~ max-width) :-

The max-width property is used to define the maximum width of an element.

If the content is larger than the defined value, the height of the element
increases to make space.

When both max-width and width are defined, the least of the two values is
applied, as can be seen in the code examples given below:

for eg,
<!-- HTML -->
<body>
	<p id="first">Web Design</p>
	<p id="second">PARAGRAPH</p>
</body>

<!-- CSS -->
#first {
  /* Width is 100% by default */
  max-width: 200px;
  /* Least value is applied */
  background-color: yellow;
}
#second {
  width: 200px;
  max-width: 100px;
  /* Least value is applied */
  background-color: orange;
}


-------------------------------------------------------------------------------------
-> Q004 : CSS Sizing;;

#### CSS : Heights;;

The height property is used to set the height of an element. Height can be
defined in percentage % or pixels px.

Percentage height is calculated based on the height of the immediate parent element.

for eg,
<!-- HTML -->
<body>
	<p>PARAGRAPH HERE...</p>
	<div>
	  <img src="fort-kochi-beach.jpg" alt="Fort Kochi Beach">
	</div>
</body>

<!-- CSS -->
p {
	font-size: 24px;
}
div {
	width : 250px;
	height : 250px;
	background-color: red;
}
img {
	width: 100%
}

#### CSS : Width;;

The width property is used to set the width of an element. Width can be
defined in percentage % or pixels px.

for eg,
<!-- HTML -->
<body>
	<div id="parent">
		<div id="first">This div is set to 300px width</div>
		<div id="second">This div is set to 50% width</div>
	</div>
</body>

<!-- CSS -->
#parent {
  border: 3px solid darkcyan;
}
#first {
  width: 300px;
  height: 100px;
  background-color: yellow;
  border: 2px solid orange;
}
#second {
  width: 50%;
  height: 100px;
  background-color: orange;
  border : 2px solid yellow;
}

#### CSS : Relative Units;;

When we use relative units to specify a length, it depends on the size of
other elements.

Let us look at some commonly used relative units

//--- Percentage '%' :- 

When width, height or font size of an element is specified in %, it is
relative to the parent element's width, height or font-size

for eg,
<!-- HTML -->
<body>
	<div>Width, height and font size in %</div>
	<p>Normal font size</p>
</body>

<!-- CSS -->
html, body {
  width: 100%;
  height: 100%;
  background-color: yellow;
}
div {
  width: 50%;
  height: 50%;
  background-color: orange;
  font-size: 200%;
}

//--- Reative Unit 'em' :-

When length of an element is specified using em, it is calculated based on the
font size of the element.

If this element has no font-size specified, the length is calculated based on
the font size of its nearest parent element.

Default, 1em = 16px

for eg, #1
<!-- HTML -->
<body>
	<div>Relative unit 'em'</div>
</body>

<!-- CSS -->
div {
	/* 10em = 10*font-size = 10*20px = 200px */
	/* width : 10*20px : 200px*/
	width: 10em;  
	/*height : 10*20px : 200px*/
	height: 10em;
	background-color: orange;
	font-size: 20px;
}

Example Note #1 : Here, the width and height of the div were calculated based
on the div's font-size.

for eg, #2 
<!-- HTML -->
<body>
	<div id="parent"><h1 id="child"> Relative unit 'em' </h1></div>
</body>

<!-- CSS -->
#parent {
  font-size: 20px;
}
#child {
  width: 5em;
  height: 5em;
  /* 
  font-size = 1 em = 1*20px = 20px
  width & height = 5em = 5*font-size = 5*20px = 100px
  */
  font-size: 1em;
  background-color: peachpuff;
}

Example Note #2 : The width and height of h1 was calculated based on h1's font
size. Though one thing different here is that, the font-size itself is given
in em. So the font-size value of h1 now depends on the font-size of its
parent element.


//--- Relative Unit 'rem' :-

When length is specified using rem, it is calculated based on the font size of
the root element of the page, which is the <html> element

for eg,
<!-- HTML -->
<html>
	<body>
 		<div id="first"></div>
		<div id="second"></div>
 </body>
</html>

<!-- CSS -->
html {
  font-size: 10px;
}
#first {
  width: 10rem;
  height: 10rem;
  background-color: beige;
  font-size: 1em;
}
#second {
  width: 10rem;
  height: 10rem;
  background-color: orange;
  font-size: 24px;
}

Example Note : The width and height of both the <div> depend on the font-size
of the html element. The sizes are not linked to the font-sizes of the
respective elements.

The width of the div is calculated as:
10rem = 10*font-size-of-html = 10*10px = 100px

//--- Relative Units 'vh' :-

When length is specified using vh, it is calculated based on the window
height, also known as viewport height.

1vh is 1% of the window height. So, 100vh is equivalent to the window height.

for eg,
<!-- HTML -->
<body>
	<div>Occupies 100% height of the window.</div>
</body>

<!-- CSS -->
div {
  height: 100vh;
  background-color: beige;
}

Example Remark : Viewport is the visible part of a screen. In the example
given above, the viewport is the rectangular window given below the code
editor and the div covers it completely with a height of 100vh.

//--- Relative Unit 'vw' :-

When length is specified using vw, it is calculated based on the window width,
also known as viewport width.

1vw is 1% of the window width. So, 100vw is equivalent to the window width.

for eg,
<!-- HTML -->
<body>
	<div>Occupies 50% width of the window, with same height.</div>
</body>

<!-- CSS -->
div {
  width: 50vw;
  height: 50vw;
  background-color: beige;
}

//--- Absolute Units :-

+ When we use absolute units to specify a length, the size is fixed and does not
	depend on the size of other elements.

+ Some absolute units are:
	1) Pixels, px
	2) Centimeters, cm
	3) Inches, in 

for eg,
<!-- HTML -->
<body>
	<div id="inches">
	  <div id="centi">
	    <div id="pixels">
	    </div>
	  </div>
	</div>
</body>

<!-- CSS -->
#inches {
  width: 2in;
  height: 2.5in;
  background-color: tomato;
}
#centi {
  width: 4cm;
  height: 4cm;
  background-color: orange;
}
#pixels {
  width: 100px;
  height: 50px;
  background-color: teal;
}

Example Remark : The size of these elements do not change when you change
their font size or parent element's size.


-------------------------------------------------------------------------------------
-> Q003 : CSS Color;;

#### CSS : Color Names;;

Color names such as blue, yellow, black, white, gray, darkgreen in your CSS.

for eg,
<!-- HTML -->
<body>
	<h1>Light gray heading on a black background</h1>
</body>

<!-- CSS -->
body {
  background-color: black;
}
h1 {
  color: lightgray;
}

#### CSS : RGB Colurs;;

RGB mix the 3 primary colours Red, Green and Blue in different proportions.
This way, we can create any colour that we require.

The <h1> has a text color of Orange because we mixed red with an intensity of
255, green with an intensity of 165 and blue with an intensity of 0.

The <p> element with id one has text color gray because in the rgb code, we
have all three colors with an intensity of 128.

Each parameter takes a value ranging from 0 to 255, 0 being least intensity
and 255 being highest intensity

for eg,
<!-- HTML -->
<body>
	<h1>Web Design</h1>
	<p id="one">First Paragraph</p>
	<p id="two">Second Paragraph</p>
</body>

<!-- CSS -->
h1 {
  /* Orange */
  color: rgb(255, 165, 0);
}
#one {
  /* Gray */
  color: rgb(128, 128, 128);
}
#two {
  /* Black background */
  background-color: rgb(0, 0, 0);
  /* White text */
  color: rgb(255, 255, 255);
}

#### CSS : HEX Colurs;;

HEX color value is a mix of Red, Green, Blue color values. The colour code
uses the hexadecimal number range from 00 to ff to represent the different
intensities

for eg,
<!-- HTML -->
<body>
	<h1>Web Design</h1>
	<p id="one">First Paragraph</p>
	<p id="two">Second Paragraph</p>
</body>

<!-- CSS -->
h1 {
  /* Orange */
  color: #ffa500;
}
#one {
  /* Gray */
  color: #808080;
}
#two {
  /* Black background */
  background-color: #000000;
  /* White text */
  color: #ffffff;
}


-------------------------------------------------------------------------------------
### Q002 : Selectors Brief;;

#### CSS : Element Selectors;;

Selectors like h2 and p are Element Selectors. They select elements using
their HTML tag name.

for eg,
<!-- HTML -->
<body>
	<h2>The Sun</h2>
	<p>
	  The Sun is the Solar System's star and by far its most massive component.
	</p>
</body>

<!-- CSS -->
h2 {
  text-decoration: underline;
}
p {
  color: darkblue;
}

#### CSS : Class Selectors;;

An element selector selects all the elements with that tag. But what if we
need to give a different color only to the second and third headings

In such case we can use class attribute to select elements. The . symbol is
used before the class name to select the element

for eg,
<!-- body -->
<body>
	<h2> Solar System </h2>
	<p>
	  The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly.
	</p>
	<h2 class="heading">The Sun</h2>
	<p class="brief">The Sun is the Solar System's star and by far its most massive component.</p>
</body>

<!-- CSS -->
body {
	background-color: lightgrey;
}
.heading {
	font-size : 24rem;
}
.brief {
	color : darkgrey;
}

#### CSS : ID Selectors;;

When we need to style only one element on the page differently, using a class
selector is not the best way.

We can use the HTML id attribute to select that single element. The # symbol
is used before the id name to select it

for eg,
<body>
	<h2 id="title">Solar System</h2>
	<p>The Solar System is the gravitationally bound system of the Sun and the 
	objects that orbit it, either directly or indirectly.</p>
</body>

<!-- CSS -->
#title {
  font-size: 36px;
}
p {
  color: darkblue;
}

#### CSS : Universal Selectors;;

Sometimes, we need to apply some common styles to all elements on a web page.
For this, we can use the universal selector *. 

This applies the specified styles to all the elements.

for eg,
<!-- HTML -->
<body>
	<h2>Solar System</h2>
	<p>The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly.</p>
	<a href="#">Read more</a>
</body>

<!-- CSS -->
* {
  color: darkgreen;
}


-------------------------------------------------------------------------------------
### Q001 : CSS Core;;

#### CSS : Selectors

Selector are used to select the HTML elements that we want to style. 

for eg.
<!-- HTML -->
<body>
	<h1>
	  Solar System
	</h1>
	<p>
	  The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly.
	</p>
</body>

<!-- CSS -->
body {
	background-color: yellow;
}
h1 {
	color : darkgreen;
}
p {
	font-size : 18px;
}

#### CSS : Properties and Values;

Properties that we want to change like background-color, color and font-size etc

Values are that we provide to the properties like beige, darkgreen, blue, 18px etc

for eg,
<!-- HTML -->
<body>
	<h1>Solar System</h1>
	<p>The Solar System is the gravitationally bound system of the Sun and the objects that orbit it, either directly or indirectly.</p>
</body>

<!-- CSS -->
body {
  background-color: beige;
}
  color: darkgreen;
}
p {
  font-size: 18px;
}

#### CSS : Comments;

CSS comments start with /* and end with */. They can be single line or span
across multiple lines.

for eg,
/* This is a comment */

/* Here is a
multi-line comment */

body {
  /* background-color: yellow; */
}


-------------------------------------------------------------------------------------