# BayesianWebPageClassifier

The main idea of this project is to create a multicore algorithm that can classify web pages between sports and technology.

Some of the libraries we are going to use for this project are:

threading (This one is for the multicore calls).
urllib (This one is going to be used to read the text inside the webpage).
bs4 (Beautiful soup, this one is going to be used to parse between the html items of the webpage)
Tkinter (This one is going to be used to create the graphic interphase of the project)
matplotlib (This one is going to be used to create the graphic in the graphic interphase)
This project is divided in different functions or steps:

First of all we need to read the data from the files and save them into arrays, for this we have the following files: commonwords.txt (common words that will be skipped once we analyze the words from the webpages), keywords_soccer.txt (key words related to soccer), keywords_technology.txt (key words related to technology), urls.txt (dataset of the urls that we are going to analyze) and urls2.txt (analyzed urls will be saved here so we only need to run the code once to show all the information of the websites).
Once we have all the data in our arrays, the project is going to call the function analyzeUrls(urlList,arrayLenght), that receives a list of urls and the lenght of it. In this function the project gets all the text from the website and parses it word by word comparing it to all the words related to soccer and technology, avoiding the common words, once its done it gives it a bayesian qualification, it depends on how much words related to X category it found and how many of this X category words exist on our dataset. Once its done, the code saves the qualification and the words related to it on an array. If a word is repeated too much on a link and its related to a category, the program saves the word on the keywords (its an intelligent algorythm that learns by itself).
Once all the websites are rated and categorized, the project is going to call the function printUrls(), this function is going to create the visual interfase wich we will be able to interact with, showing us a graphic with all the information to the links we used, showing the category, score and keywords related to each link. The categories are Soccer, Technology, Cant access this website and Cant be determined.
The call of the functions and the main, in this part we are going to use the multicore to call the analyzeUrls(urlList,arrayLenght) in order to do that, we have to split the array of the urls to analyze, and then call the function.
