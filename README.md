# CS411Group2

For our web application, we have decided to come up with two ideas of either devleoping a music streaming app and a educational website. For the music streaming app, we were thinking of this app generating a list of music options for the users based on their search history and user preferences. For the tech stack, we were thinking of going with MySql, Flask, Node.js for the backend. We'll be using Javascript and HTML/CSS for the frontend. For the APIs, we were thinking of using a Spotify API to get the music options and maybe a searching API to list the details of each song. We'll also be using the Ticketmaster API to generate a list events through the users artist input. We'll also create a login page so it can store the users login infos in a database.

Final Project

Functionality
Our project has finally been finished! When you first launch the application on the web, it will first prompt you to the registration page. If we don't have your login credentials stored locally in our database, you will first need to register an account first. However, if you already have a login credential stored in our database, you can log in locally to access our mainpage. We also provided another option for 3rd party Oauth login through Spotify so we can verify your login with your Spotify account and log you in to access the mainpage. After you have successfully login, there will be a search bar for you to search youre favorite music artist. It may take a while depending how many songs it generated when the user types in a artist making a call to the Spotify API and Ticketmaster API. After a few seconds, we will generate a list of songs by that artist you just typed in and the upcoming events the artist may have. It may not generate any events if there are none upcoming. You will also be provided with another input bar for you to add your favorite song by that artist to your playlist. You can drag to copy and paste the song onto the input bar and press Add so the song is added to your playlist. After that, you can press View my playlist and it will redirect you to another page with the list of songs that you just added. This is the overall functionality of our app. Hope you enjoy it!

Techstack: 
Frontend: HTML, CSS, Javascript
Backend: Python/Flask MySQL
