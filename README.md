# Mark McClean

## Milestone Project 3 – Data Centric Development

## Lego Minifigures Catalogue – Python Flask application using MongoDB

### Table of Contents
* [Why make a Lego Minifigures Catalogue?](#Why-make-a-Lego-Minifigures-Catalogue)
* [How the website works](#How-the-website-works)
* [UX: Strategy](#UX-Strategy)
* [Scope](#Scope)
* [Structure](#Structure)
* [Sketelon](#Sketelon)
* [Surface](#Surface)
* [Technologies Used](#Technologies-Used)
* [Testing](#Testing)

### View the live project
The live website hosted by Heroku can be viewed [here](https://lego-minifigure-catalogue.herokuapp.com/).

### Why make a Lego Minifigures Catalogue?
For the third milestone project I decided to build an application where users can add pictures and information of their own Lego Minifigures for others to view and admire, therefore buiding up a community of users that create the catalogue themselves.

Since I was young I was a Lego fanatic. That craze died down in my teens but now that I have children of my own, the love of Lego has returned. What better way to celebrate that than to create a Lego Minifigure Catalogue where people can come together and share their love of Lego.

Lego has come a log way since it began and now there are many themes and types of lego for small children and adults. This has resulted in a vast array of different minifigures for all themes, some of which have since been discontinued. I invite users to upload their own minifigues, unique or common so that others can enjoy the amazing collection.

### How the website works
The users will be directed to the home page initially where there will be an introduction to the site with some explanation on what the site is about and how the users can use it. There will also be several clear buttons to direct the users to either view the catalogue or add their own minifigure. A navigation bar will also be available to help user to navigate around the site.

If a user clicks on ‘View Catalogue’ they will be directed to the full catalogue page where they can view all other minifigures that have currently been added to the database by other users. Here there will also be a function for the users to filter the minifigures by name, theme or age so they can see a specific group of minifigures. There will also be an option to like a minifigure.

Each minifigure in the catalogue can be clicked on to view the additional information that was uploaded by the user. Here there will be an option to edit this information if, for example, something was left out by the user or there is incorrect information uploaded. There will also be a delete option here if a user wishes to delete a minifigure. This will however just hide the minifigure from users and not delete it totally from the database.

When the user goes to the ‘Add a minifigure’ page they will be presented with a form to fill out to upload their own minifigure including photo. After completion they will be redirected to the catalogue where they can view their own minifigure.

Users will also be given the option of adding extra Lego themes that may not yet exist in the database. There will also be options to edit and delete existing themes.

The overall idea is that a community of users will be built up and they will create the catalogue for their own and others enjoyment.

[↥ Back to top](#Mark-McClean)

## UX: Strategy

### Primary Target Audience

This website can be enjoyed by anyone who is old enough to use a computer or smartphone. This is a place where lovers of Lego, or people who would like to know more, can come together and share their knowledge and photos.

### Appropriate Content
The Lego world is a predominantly bright and vibrant one and I want my website to reflect that so there will be a few bright colours but also some white background to offset the brightness of the colours. There will be clear separations between different sections of each page with different colours of backgrounds, text and photos with a minimal feel so that there is not too much reading for the user. Clear buttons and text are very important so the user can understand and navigate the site.

### Why this website?
I wanted to create a website with a sense of community where the users have the power and are relied upon to create the catalogue themselves and keep it up to date with accurate information. The theme of Lego is a bonus for me as I am a big fan of Lego.

[↥ Back to top](#Mark-McClean)

## Scope

### User Stories
As a potential user I would like to:

- View an amazing Lego Minifigure catalogue and discover minfigs I’ve never seen before
- Add my own photo and minifig info for others to enjoy
- Edit info of other minifigs if something is missing or incorrect
- Delete my minifig if I no longer want others to view it
- Feel part of a community of Lego minifigure lovers by helping to build up the catalogue and keep it up to date with accurate info on all minifigs
- Add new Lego themes, if they are not yet available on the site
- Delete or modify Lego themes if they need updating or have been discontinued
- To view minfigs of a certain theme, age or name
- Be able to view the site on my phone, tablet or laptop
- Have a simple design and clear instructions so I know how the site works
- Have appropriate content for all users, young and old
- Use a website that’s easy on the eye and makes me want to come back to see the latest uploaded minifigs.

As a developer I would like:

- To create a beautiful and user friendly website for fellow Lego lovers.
- For users to enjoy the website and encourage them to upload their own minifigs and help build and maintain the catalogue.
- Show my current knowledge of HTML, CSS, JS, Python, Flask and use of MongoDB with useful functionality built into the website.
- To enjoy using the site myself just like any other user

### Goal
My goal for this project was to create a fun, user friendly and interactive experience for lovers of Lego minifigures. The website will be clear and minimal to provide users with the best experience whilst learning how to use the catalogue. My aim is to make the users feel like they’re part of a community of fellow Lego fans that buildup the catalogue together and help to keep it maintained.

[↥ Back to top](#Mark-McClean)

## Structure

### Features
1.	A Lego minifigure head is used as my website logo along with the name of the website in the top left corner of the navigation bar. This is directly imported from a URL on the internet. I think it is a very appropriate logo for the content of the site. The icon and name are together also a link to the home page from anywhere on the site, which a is fairly standard feature of modern websites.
2.  A collapsible navbar element has been implemented for medium and smaller screens. The menu is hidden inside the 'hamburger' icon and the navbar sweeps in from the right when clicked.
3.	A Lego minifigures photo is used as the backdrop of the callout section of the home page. I imported this photo on to the development environment this time as I modified it before upload so that it was cropped a little more. On large screens this appears on the right side of the callout section and moves to the top of the callout section on medium sized (tablet) screens so that the image doesn’t appear too small on this medium screens.
4.	A different photo was used on the callout section for mobile devices. The original photo appears too small at mobile screen size to have the desired effect and experience for the user. This photo is more square in shape, to fit the long mobile screen shape better and shows different minifigures but closer again.
5.	Callout section shows the title of the website along with 2 buttons to either view the catalogue or add a minifig. I think this is a very important part of modern websites that users have buttons to draw them in, when they first arrive, and direct them to other parts of the website, other than using the navbar. In larger screens this section of the callout appears on the left side of the screen and moves under the main photo for medium sized screens, with the website name to the left and the buttons to the right. For mobile devices the elements are all stack on top of one another with the photo at the top, the website name under and the buttons under that. All of this still fits inside a modern standard phone screen size so the user doesn’t have to scroll down to see the whole callout section.
6.	Under the callout section is another section in a different colour to provide some short explanation to the user as to what the site is about and how to use it.
7.	At the bottom of the page is the footer, again in a different colour to clearly differentiate a different section of the website. This contains links and info about the site.
8.	On the ‘View Catalogue’ page the user can view all the current minifigs that have been uploaded onto the site. This initially appears as just a photo and minifig name under with a down arrow beside the name to indicate that more information is available. When you click on the name an additional element appears showing the information associated with that minifig along with 2 other functions, an edit minifig button and a delete minifig button. The arrow beside the name now points up, indicating the associated info can be collapsed again.
9.	When the user clicks on a minifig to reveal the associated info and then clicks on ‘Edit Minifigure’, they are brought to a form to fill in where all the current info for that minifigure is already filled in, therefore if the user only wants to change one field they do not need to fill in the rest of the form. When the user clicks ‘Edit Minifigure ’ at the bottom of the form, the information will be updated and the user will be return to the catalogue where they can view the minifig again and see the updated info.
10.	When the user clicks on a minifig to reveal the associated info and then clicks on ‘Delete Minifigure’ the minifigure will then disappear from view for all users however it will not be completely deleted from the database so that the administrator (myself) can always retrieve the deleted minifigure in the event that it was deleted by accident.
11.	When the user wants to add their own minifig they can click on the ‘Add Minifigure’ button on the homepage callout or navbar and they will be directed to a form to fill out, similar to the edit minifigure form. In this case though they also have the option to upload a photo of their own minifig. Only the photo field will be required and all other fields can be filled if the user knows the information. If not they can leave it blank and that gives other users the opportunity to edit the minifig at a later time and keep the catalogue up to date. Most of the form fields are drop down menus, provided by the database, giving the users a range of options to choose from. This gives consistency as to how the info is presented on the website. When the form is filled out and submitted the user will be redirected back to the catalogue to see their uploaded minifigure.
12.	On the ‘Theme Management’ page the user will have the option to add new Lego themes to the website, should some new ones become available or if existing themes do not yet appear on the website. Once new themes are added they will also appear in the drop down list within the add minifg and edit minfig forms enabling new minifig uploads to use the new themes if necessary.
13.	Users will also have the opportunity to edit and delete existing themes, in the event that the theme is not correct or has been discontinued in the Lego world. To do this users must click on a theme on the ‘Theme Management’ page and a collapsible element will appear showing 2 options, one for edit and one for delete.

[↥ Back to top](#Mark-McClean)

### User Authentication
User authentication is something we have not yet covered in the course however my mentor advised me to look into it as it would enhance my project and help to prevent anyone from just editing or deleting records.
I did some research on the internet and found a very useful [video](https://www.youtube.com/watch?v=vVx1737auSE) on YouTube on how to set up a basic user authentication system for a flask application using sessions. I used most of the code in the video for my own system, changing a few lines.
The functionality in the user system includes allowing new users create an account with a username and password. The password has some hash and encoding functionality added so even I, as administrator of the database, cannot see the actual password in the Mongo collection. If the user tries to use a username that already exists, they receive a message that the username is already taken and to try another. Once the user successfully registers a new account, they are immediately logged in and they can see that on the home page, where they are redirected to, with a text message in to the top right corner under the navbar.
If an already registered user is returning to the site they have the option to log in. If the username and or password they enter are incorrect, they receive a warning and to try again. Again when they are logged in they can see this with a message in to the top right corner of the home page.
I have also added further functionality to the buttons and navbar options, which change depending on whether a user is logged in or not. If a user is not logged in they can only view the home page or catalogue but not edit any records. Links to the add minifig and themes pages are not even visible. If they try to edit or delete any of the records in the catalogue they will be prompted to login or sign up. If a user is logged on then all functionality will be open to that user, the navbar will have more options and the homepage buttons will be different.

### Features left to implement
1. I think a more extensive login and account system would be a good feature for the future. One which takes a user’s email address and notifies them if their record has been modified or deleted. 
2. Tracking which users are doing which activities may be useful so you can see which users are modifying or deleting which records.
3. An account page would also be useful for users so they can see their own profile and the records that they have added to the database.
4. A chat feature so users can interact with one another if they want to discuss a particular record.

### Overall Structure
For the structure of the site I wanted to start off with a large Lego minifigures image on the homepage to capture the users attention and give them a big clue as to what the website is about. Alongside the image will be a callout section with the title of the website and some links to the main sections of the website. 
Along the top of the website will be the navbar with the same links as the callout and some additional ones on the right side. The navbar will have a yellow colour, which is synonymous with Lego, and the title and logo of the site will be in the left side of the navbar. 
A footer which sticks to the bottom of the page will be used as there are a few pages with minimal content so the navbar will always be pushed to the bottom and bot below the final element of the main section.
Most of the pages will also have a blue section somewhere with some explanation of what can be done or needs to be done on that page. This will provide a consistent design so that users will know that this section contains information about this page of the site.
Throughout the site I have also added some single minifigure pictures, within the blue sections, to remind the users that this is what the site is about.

[↥ Back to top](#Mark-McClean)

## Main Database Collections
Below are the 2 main database collections used to post and retrieve information to and from the front end to the back end.

### Users
| Title       | Identifier Key | Type     | Method                |
|-------------|----------------|----------|-----------------------|
| User ID     | _id            | ObjectId | Automatic             |
| User Name   | username       | string   | User Input            |
| Password    | password       | string   | User Input  + hashing |
| Liked Items | liked_items    | set      | User Input            |

### Minifigures
| Title                 | Identifier Key  | Type     | Method                         |
|-----------------------|-----------------|----------|--------------------------------|
| Minifigire ID         | _id             | ObjectId | Automatic                      |
| Photo                 | photo           | file     | User Input                     |
| Minifigure Name       | minifigure_name | string   | User Input                     |
| Theme                 | theme_name      | string   | User Input,<br>dropdown select |
| Minifigure Age        | age_range       | string   | User Input,<br>dropdown select |
| Feature               | feature         | string   | User Input                     |
| Number of parts       | number_of_parts | string   | User Input,<br>dropdown select |
| Rarity                | rarity_name     | string   | User Input,<br>dropdown select |
| Uploaded By           | uploaded_by     | string   | session username               |
| Is minifigure deleted | minifig_deleted | Boolean  | User Input,<br>delete option   |
| Liked Counter         | liked_counter   | integer  | User Input                     |

[↥ Back to top](#Mark-McClean)

## Sketelon
I used the Balsamiq program for the wireframes and attached them to the directory. The original idea is still recognizable from the finished application. There have obviously been some design changes along the way but the wireframe is useful to have to put the idea in your head down on paper before you start coding. The wireframes can also be view her below.<br/>
[Wireframe 1 - Home page callout Desktop](wireframes/1.LegoMinifiguresCatalogueHome.png)<br/>
[Wireframe 2 - View Catalogue Desktop](wireframes/2.ViewCatalogue.png)<br/>
[Wireframe 3 - Add Minifig Desktop](wireframes/3.Addaminifig.png)<br/>
[Wireframe 4 - Manage Themes Desktop](wireframes/4.ManageThemes.png)<br/>
[Wireframe 5 - Home Page Mobile](wireframes/5.MobileHome.png)<br/>
[Wireframe 6 - View Catalogue Mobile](wireframes/6.MobileViewCatalogue.png)<br/>
[Wireframe 7 - Add Minifig Mobile](wireframes/7.MobileAddMinifig.png)<br/>
[Wireframe 8 - Manage Themes Mobile](wireframes/8.MobileThemes.png)

## Surface

### Colours and icons
For the colours of the site, I wanted to go with something bright and fun. Something that reflects the Lego world. The colour that is most synonymous with Lego is of course yellow. I decided to go with yellow as the colour of my navbar but a brighter version than the traditional Lego yellow colour. This is because I also wanted to have a Lego minifigure head as the logo of the site and I think it works well against the brighter yellow of the navbar.
Along with the yellow I’ve chosen a bright but rich blue colour as the background for the information sections of each page. Blue and yellow is obviously a classic combination of colours and I think it works well on the site. The yellow and blue are broken up with a few white spaces so the site is not saturated with colour.
I’ve also used the same 2 colours for all the buttons of the site to keep it consistent. Each button also changes to a darker version when hovered over so the user has a visual indicator that the button will do something.
Within most buttons on the site I have also added icons to provide the user with some additional visual indicators as to what the button does. For example a plus icon if you click the ‘Add Minifigure’ button or a downward arrow to indicate that the button will drop down with additional information or links. Icons are also visible in the forms beside each input field as a reference of the content required for that filed.

### Font
For the font I wanted to go with something fun, modern and clear. I searched through Google fonts and decided upon ‘Ubuntu’. I took the link provided by Google and pasted it directly into my CSS file to become the default font for the whole site. There is a backup of San-Serif provided in the event that the browser being used is unable to access Google fonts.

[↥ Back to top](#Mark-McClean)

## Technologies Used
* Gitpod – used as my IDE for the development of the website.
* HTML – used to write the code for the structure and layout of all templates in the site
* CSS – used for custom styling of many HTML elements. 
* Materialize – Materialize was used to provide the navbar, footer, forms, collapsible elements for each database record and the use of a grid system. Most of these imported elements have then been custom styled to suit this project.
* Javascript – Used to provide some simple interactive features of the website.
* jQuery – Used to initialize some Materialize components.
* Popper.JS – Used to aid the responsiveness of the website.
* Python – Used for the main functionality of the site. All CRUD (Create, Read, Update, Delete) functionality is provided by Python through flask and other imported technologies in the ‘app.py’ Python file such as PyMongo, flask PyMongo, bson.objectid and bcrypt. These are all listed at the top of the app.py file.
* Flask - Flask framework was used to create the routes for the CRUD functionality.
* Jinja - Jinja templating language was used to project some of the Flask functionality onto the frontend to make only certain features arrpear when a user is logged on for example.
* MongoDB – MongoDVB was used as the backend database where collections were stored, created, updated and retrieved through the Flask routes.
* Font Awesome - Font Awesome was used to display the social media icons in the footer.
* Google Font - 1 Font was imported from Google Fonts and the URL can be found in the base template.
* Balsamiq - This was used to build the wireframes that were then uploaded to the Gitpod IDE.
* Tables Generator - Used to create the tables inserted here in the README file.

[↥ Back to top](#Mark-McClean)

## Testing

### General Testing
I am not currently very knowledgeable about automated testing and was short of time so I decided to do all the testing manually via the browser and Chrome Developer tools. How I achieved this was after almost every line of code that I wrote, I opened up the browser to view the live website. Viewing it in Google Chrome I am then able to right click on the website and select inspect from the menu. Chrome Developer tools opens up which allows me to view the elements, styles and console log to see JavaScript errors.
I tried to work with small tasks in the beginning, setting up the navbar, creating some links. During this process I would view the website in the browser many times, select elements to see what default styles had been attached to them and change if necessary. Chrome Developer tools also allows you to add styles to elements and change the website as you view it. If I was happy with the changes I could copy the styles from Chrome and paste them into my CSS file. This can be useful to cut down the amout of times you view the developer tools to see what differences your styling makes and speed up the developing process. Within the Chrome developer tools there is also the console, which I monitored to find bugs in the JavaScript functions.
After spending some time on the HTML, Materialize and CSS to set up the look, styles and responsiveness of the website, I moved on to writing the Python code. I used the same manual tests as above using Chrome Developer tools. However I learned throughout the course to also print certain variables and functions during the writing to see if the Command Line Interface was printing the desired outcome when I run the app and clicked on certain routes. This helps to see if the program reaches parts of your function and if there are any bugs, at which point it is going wrong.
When the basic functionality of the game was in place, I shared by the website with friends and family to get their feeback of usablity and first impressions of the game and functionality.
Through continual monitoring and with the feedback of friends and family, I have fixed a few design faults in the HTML and CSS and bugs in my Flask code.

### Code Validation
Several times during the development process I tested my code in various online validation programs.

* **HTML** - For HTML I used [W3 Markup Validation Service](https://validator.w3.org/#validate_by_input). I pasted my entire HTML pages one at a time into the input field and the code was checked. I received several warnings about my code. Warnings are things that can be changed in the code but it's also not necessary.
* **CSS** - For CSS I used [W3 CSS Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input). Again I pasted my CSS file into the input field and the code was checked.
* **JavaScript** - For JavaScript validation, within the Gitpod environment there is a 'Problems' tab which I checked often during the development. Any errors in the code would appear immediately so I was able to address any issue in the JavaScript right away. For external validation I used [JS Hint](https://jshint.com/).
* **Python** - Like JavaScript, within the Gitpod environment I used the 'Problems' tab which I checked often during the development. For external validation I used [PEP8](http://pep8online.com/).

### Testing in different browsers
I used Google Chrome as my main browser test as I was constantly using the Chrome developer tools to view and adjust my code. I also regularly tested the website on my phone, also using Google Chrome. I occasionally checked Firefox on the laptop. I sent the URL to friends and family to test on ipads(5th generation or younger) and iphones(8 or younger) along with Samsung Galaxy(S9 or younger) and Saumsung Galaxy Tab(S3 or younger). Any issues I found have been documented below in the section: [Issues still to be resolved](#Issues-still-to-be-resolved).

[↥ Back to top](#Mark-McClean)

### Issued found and solved throughout the development

1.	* **Issue** – App not running in Heroku
    * **Fix** – I needed to add the environment variables in Heroku and Gitpod but I had only added them in Gitpod. I also needed to update my requirements file as I had added more dependencies since I first created the file.
    * **Result** – The app can now be run and viewed in Heroku

2.	* **Issue** – For loop not working in page that displays all records from the database.
    * **Fix** – I originally had the for loop, to display all records, outside a list item that contained all the information about the record. However the records was not displaying correctly the way I wanted it. I first tried moving the for loop outside the unordered list tag but eventually realized it needed to be outside the div tag so that a new div was created for each record and that for each div, it would take up the specified amount of horizontal space depending on the screen size.
    * **Result** – The records now display clearly and horizontally the way I wanted them to.

3.	* **Issue** – The photo that was uploaded by the user, from the add minifig form, was not rendering on the page displaying the records.
    * **Fix** – To resolve this I had to rewrite the insert_minifig function so that the image was saved using a save_file method. The image along with all the other data from the form had to be manually created as a dictionary in the same function so that Mongo could interpret all the data together.
                A separate function also had to be written to create a URL for each image, which is then retrieved within the HTML of the main display records page.
    * **Result** – The image uploaded by the user can now be viewed on the main catalogue page along with all the associated data from the form.

4.	* **Issue** – The function to update existing records was not working
    * **Fix** – The original data populated the update form however when the data was changed and the update button was clicked to confirm the changes, the new data was not displayed on the record. This was a simple fix that I had overlooked when first writing the route. I needed to define the methods=[‘POST’] as like the add minifig function we are changing the database which requires a POST method.
    * **Result** – When the update minifig form is filled in and the changes are confirmed the new data can now be viewed within the record on the main catalogue page.

5.	* **Issue** – After a record was updated with extra or amended data, the image file disappeared from view on the updated record
    * **Fix** – In the update records function I needed to use the $set keyword which is used to only update the key/value pairs defined on the function. All data from the undefined key/value pairs, for example the image,  would then remain the same. This $set key word is placed in the function before the dictionary of key/value pairs that are to be updated.
    * **Result** – The update function now works as expected and the data can be changed whilst the image remains part of the record.

6.	* **Issue** – I needed to create a delete function for the project but wanted to make it like a soft delete function where the record does not get deleted from the database.
    * **Fix** – I added an extra key/value pair for every new record of ‘minifig-deleted’ and the value by default set to ‘False’.  This is something that the user cannot see. When the user clicks on delete minifig then instead of deleting completely the ‘minifig_deleted’ value changes to True.
                The get_minifigure route then had to be modified to specify that only records with a key/value pair of ‘minifig_deleted’ that equals to False, would be displayed in the catalogue, otherwise they don’t appear but also don’t get deleted completely. That way I can always reinstate records that may have been deleted by accident as the data is still in the database.
    * **Result** – When a user deletes the minfig records, it no longer appears in the catalogue but is still available in the Mongo database.

7.	* **Issue** – Materialize navbar aligning in the middle of the screen on small and medium devices.
    * **Fix** – When reviewing the site through Google Chrome development tools with the responsive view displayed the navbar items all aligned to the centre when the screen size was set to tablet or smaller. This was a relatively simple fix. I just needed to remove some of the materialize default classes from this element for smaller devices.
    * **Result** – The navbar, when viewed on a smaller device, kept the layout of the large screen with the logo and site title on the left side and the menu or in this case the dropdown menu button, appeared on the right side of the navbar.

8.	* **Issue** – Dropdown select filter function not working. When a theme is chosen from the dropdown menu, nothing happens.
    * **Fix** – When trying to figure out this problem with a Code Institute tutor, we discovered that the href that I had specified inside the select options of the dropdown list, was not visible in the Chrome developer tools. This led me to discover that Materialize select options cannot contain <a> tags and therefore the reason that the function was not being called when a select option was chosen. I was advised by a Code institute mentor on slack to try a dropdown button instead of a dropdown select option. The dropdown button contains list items, which in turn can contain an <a> tag. This appeared to be the solution as the href was now visible on the Chrome developer tools.
                Although the desired href was appearing in developer tools the function was still not filtering the results per theme or age. I was advised through slack to make sure I was looping through the filtered records on the page displaying the records and I had not done that yet. I copied the code block used to display all records and pasted it below wrapped in a new loop that looped through and displayed only the results of the selected theme or age.
                The final sub issue within this general filter issue was that when the filter was finally working and the records for a single theme were only displayed the dropdown button menu was no longer populating to choose a different filter. This was a simple fix as I had not yet added the collections to the new filter routes and therefore they didn’t appear after the first filter was run.
    * **Result** – The filter was working, only showing results from the theme or age range selected and another filter could be applied after the first to filter different options.

9.	* **Issue** – Name filter function not working
    * **Fix** – When I initially started writing this function I was passing a name parameter into the function like I had done with the dropdown menu parameters but I was advised on slack that this was not necessary as I would extract the name from the input form in the form of a request just like in the add minifig route. So I took the paramaters out and added a POST method to my route. On the next test the app was rendering a new page but with no results so the last advce I got was to check in the route if request.method = POST and then search on mongo, passing in the request form input. I also added some further functionality to this route by adding a lower method to the request form input so that all text entered is converted to lowercase to check the database where it is also lowercase. Results are then displayed capitalized.
    * **Result** – After entering a name I know to be in the database the app returned that record. 

10. * **Issue** - First time I tried to log in as a user I received an error message
    * **Fix** – When I tried to log in using an account that I had successfully created through the registration form, I received an error message that the object had no encode attribute. After some searching on the internet and speaking with a fellow student on slack it became evident that some of the code I had copied from the video was not applicable. I had encoded the password that was stored in the database and compared it to the password passed through in the login form. However I only needed to encode the password passed through in the login form and compare it to the password in the database, which was of course already encoded from the registration form, so I didn’t need to encode it a second time.
    * **Result** – The login system now allows existing users to log in.

[↥ Back to top](#Mark-McClean)

### Issues still to be resolved

1.	* **Issue** – Items in grid layout on medium screens not always aligning.
    * **Description** – During the development I've had some issues with the alignment of the records on medium and large screens. Due to the possibility of users uploading photos of varying heights, the records will automatically align from the top and some will hang lower than others. I addressed this by adding some styles to make the records align from the bottom and there may be differences along the top of the records. I thought this was a visually more appealing than the records having different bottom alignment. The problem was this affected the responsivness of the website. I fixed that removing the float: none style for smaller screens. So on large screens the records are lining up as desired along the bottom but on medium screens there sometimes appears gaps between or beside records in the grid if the images uploaded are different heights. At the moment the problem is not visible because all the photos uploaded by myself and family members are all the same resolution and therefore all the same size.
    * **Potential Resolution** – On the add minifigure page I have advised users to upload photos with a 4:3 resolution so that all images will be the same size. This is only a partial resolution though as not all users will adhere to this advice. I will have to dig deeper to find a more permanent resolution to this problem for future releases.

2.	* **Issue** – Responsiveness of images on description sections.
    * **Description** – On several pages of the application I have images overlapping to give a visually appealing way to demonstrate a photo of a minifigure so the users can take inspiration from these photo when uploading their own photos. The overlapping of the photos and to keep them responsive required a lot of amendments to relative and absolute positioning and media queries and even then they are still not perfectly aligned on different screen widths. There's probably an easier way to achieve what I want and with cleaner code. This is something I would like to rectify for future versions of this application.
    * **Potential Resolution** - A potential solution might be to make a single image of how I would like the overlapping images to appear and use that one image and let it respond naturally to the different screen sizes instead of modifying both photos individually for each different scrren size.

3.	* **Issue** – Like feature not fully implemented yet.
    * **Description** – As you can see on the minifigures page below each minifigure there is a grey heart that can be click and it turns red. The frontend of the feature is working ok but I was working on the backend but ran out of time.
    * **Potential Resolution** - What I was trying to do was create a function where the minifigure_id is passed into the function and I check if that minifigure_id exists in a list of liked_items inside the users own document. If it exists in the list then it is removed and a liked_counter(which exists in the minifigure document) decreases by one and if it doesn't yet exist in the list it is added and the liked_counter increases by one. The liked_counter would then appear beside the heart to tell users how many times the record is liked. This way users can only like each record one time. A further part of the function would be to include JavaScript and Ajax to make this function run without refreshing the page.

## Deployment
The code environment was taken from a code institute [Gitpod template](https://github.com/Code-Institute-Org/gitpod-full-template) that is stored on Github. 
This is then cloned and saved onto my own Github account as a new repository. From there I use the built in 'Gitpod' button to open up the new repository on my own Gitpod account. 
The template then opens with a boiler plate to start coding including links for Bootstrap, jQuery, Popper and Font Awesome so I didn’t need to look for the CDN’s myself. 
After every session of coding I committed my work using the Git terminal in Gitpod. Every commit has a message attached to clearly explain the changes that were made since the last commit. After the commit, the code is also then pushed to my Github account, also using the Git terminal.

### How to run this project locally
To run this project on your own IDE follow the instructions below.
Ensure you have an IDE such as GitPod and the following installed:
* PIP
* Git
* Python3
* If you are using the Code Institute Full template the above will already be installed
* A MongoDB account

### Instructions
* After installing all required modules to make your functions work you need to run the command `pip3 freeze -r requirements.txt` in the CLI. This will create a requirements file, which later in the project, can be updated with the same command if you were to add more modules.
* In your local IDE create a file called `env.py`
* Inside the `env.py` file, create a SECRET_KEY variable and a MONGO_URI to link to your own database.
* Make sure to immediately add `env.py` to a `.gitignore` file so it's not committed and pushed to the repository where anyone can then see the SECRET_KEY and MONGO_URI
* You can now run the application with the command `python app.py`

### Heroku Deployment
* Create a requirements.txt file using the terminal command `pip freeze > requirements.txt`
* Create a Procfile with the terminal command `echo web: python app.py > Procfile`
* git add and git commit the new requirements and Procfile and then git push the project to GitHub.
* Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.
* From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
* Confirm the linking of the heroku app to the correct GitHub repository.
* In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
* Set the following config vars:
    * DEBUG: False
    * IP: 0.0.0.0
    * MONGO_URI: `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
    * PORT: 5000
    * SECRET_KEY: `<your_secret_key>`
* The MONGO_URI will have to be retrieved from your own MongoDB account. The URI will include information relative to your own account: username, password, database_name and so on.
* In the heroku dashboard, click "Deploy"
* In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch"
* The site should now be successfully deployed.

## Credits
* All content was written by myself
* All photos from the catalogue page were taken and uploaded by myself along with family and friends
* Other photos on the site come from various sources found through Google image search
* Log in with sessions functionality came from a [YouTube video](https://www.youtube.com/watch?v=vVx1737auSE)
* Uploading photos into Mongo also came from a [YouTube video](https://www.youtube.com/watch?v=DsgAuceHha4)
* Code institute tudors helped me throughout the project on functions for search filters, saving and displaying photos.

### Special thanks
* Special thanks to my mentor Anthony Ngene who talked me through several pieces of code and advised me on how to improve my code
* Many thanks to the Code Institute tudors, who also helped me out with some small and larger issues I had during the development process
* Thanks to all the friends and family who tested the game on various devides and gave me feedback to improve the game
