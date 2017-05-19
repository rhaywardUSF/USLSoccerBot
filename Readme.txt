# SoccerBot 0.1 by Randy Hayward 										#
# RandyHayward.com												#
#---------------------------------------------------------------------------------------------------------------#
# This program automates user flair assignment. A bot user is set up and reads incoming mailbox messages.	#
# The bot user receives a flair request, and assigns said flair to the user.					#
# If the subreddit has the matching flair image and flair code, the user will see the team crest appear next to #
# their name.													#
#														#
# Ultimately, this bot will update flairsheets and subreddit styling, assign flair, update sidebar scores, 	#
#and update news banners at the top of the subreddit								#					
#														#
# See Photos Folder for Illustrations on how this program actually works					#
#---------------------------------------------------------------------------------------------------------------#
# Installation													#
# ************													#
#														#
# 1) Create an account for the bot and reddit App to run on (ex: MySoccerBot) on http://www.reddit.com. 	#
# 	Save the username and password somewhere Safe!								#					
#														#
# 2) If you have not created and moderated a subreddit before, go to reddit.com and create one:			#
#	http:reddit.com/r/<yoursubredditnamehere>								#
# 	(Tip: If the subreddit doesn't already exist, you will see a "Create your own subreddit" button		#
# 	on the top right)											#
#														#
# 3) Go to your subreddits' stylesheet page:									#
#	https://www.reddit.com/r/<yoursubredditnamehere>/about/stylesheet/					#
#	(Tip: You can click on the sidebar link in your subreddit to access this page in the future)		#
#														#
# 4) On the Stylesheet page, Upload the images located in the SubredditStyling folder to your subreddit. 	#
#    Be sure to click save!											#
#														#
# 5) Copy the css code located in SubredditStyling/Stylesheet.css and paste it below any css 			#
#    in the stylesheet textarea.										#
#														#
# 6) Go to https://www.reddit.com/prefs/apps/ and create an app:						#
# 	a) Enter a name for your bot (Ex:MySoccerBot)								#
#	b) Select 'script' as the type of application								#
#	c) Enter a Description of what your bot will do:							#
#	Ex: "MySoccerBot assigns custom user flair based on messages received by PM."				#
#	d) Enter about url: You can point this to the test subreddit if you'd like				#
#	e) Redirect Uri: Enter a uri and port that are accessible locally 					#
#	(ex: http://localhost:65010/autorize_callback - remember this url later because it's important!)	#
#	f) Click create app											#
#														#
# 7) Your app has been created! Click the small "edit" button located underneath your app name (under the <?>	#
# Logo). You will notice a few codes:										#				
#	- Underneath  your app name, there is a 14-character code. This is  your client_id			#
#	- There is a secret field with a 27-character code. This is your client_secret				#
# 														#
# 8) In Helpers/AuthHelper.py, replace <YourSoccerBotAgent>, <YourAppKey>, <YourAppSecret>, 	#
#    and <YourCallbackUri> with a Bot Agent Name (ex:MySoccerBot v1.0), your client_id, client_secret, 		#
#    and callback uri												#
#														#
# 9) In Auth.ini, replace <YourUrl>, <YourPort>, <YourRedirectPath>, <YourAppKey>, <YourAppSecret>		#
#    with the uri portion before the port, your selected port number, any redirect path after your port number  #
#    (ex:authorize_callback) (Note:your url must match the url in your http://www.reddit.com/prefs/apps config) #
#    the client_id, and the client_secret respectively								#

# 10) Run the Program! If the program asks you redirects you to a your callback uri, and displays a token,	#
#     enter it in Auth.ini under refresh token									#