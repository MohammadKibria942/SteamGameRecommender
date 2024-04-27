::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::
:: ____   _____     _     ____   __  __  _____  ::
::|  _ \ | ____|   / \   |  _ \ |  \/  || ____| ::
::| |_) ||  _|    / _ \  | | | || |\/| ||  _|   ::
::|  _ < | |___  / ___ \ | |_| || |  | || |___  ::
::|_| \_\|_____|/_/   \_\|____/ |_|  |_||_____| ::
::                                              ::
::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::

My name is Mohammad Yusef Ahmod Kibria and i thank you for looking at my project.


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ___              _          _  _                                   ::
::|_ _| _ __   ___ | |_  __ _ | || |                                  ::
:: | | | '_ \ / __|| __|/ _` || || |                                  ::
:: | | | | | |\__ \| |_| (_| || || |                                  ::
::|___||_| |_||___/ \__|\__,_||_||_|                                  ::
::                                                                    ::
:: ___              _                       _    _                    ::
::|_ _| _ __   ___ | |_  _ __  _   _   ___ | |_ (_)  ___   _ __   ___ ::
:: | | | '_ \ / __|| __|| '__|| | | | / __|| __|| | / _ \ | '_ \ / __|::
:: | | | | | |\__ \| |_ | |   | |_| || (__ | |_ | || (_) || | | |\__ \::
::|___||_| |_||___/ \__||_|    \__,_| \___| \__||_| \___/ |_| |_||___/::
::                                                                    ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


To run the program please have VScode along with Anaconda and Python installed
For installation instructions please refer to this video:

https://www.youtube.com/watch?v=h1sAzPojKMg

Once installed please open the folder in VSCode and open the following files in order:

1) DataDownloader.ipynb
2) SteamApiCleaner.ipynb
3) SteamSpyCleaner.ipynb
4) RecommendationEngine.py
5) gui.py


::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: ____          _                                                    ::
::|  _ \   __ _ | |_  __ _                                            ::
::| | | | / _` || __|/ _` |                                           ::
::| |_| || (_| || |_| (_| |                                           ::
::|____/  \__,_| \__|\__,_|                                           ::
::                                                                    ::
:: ___              _                       _    _                    ::
::|_ _| _ __   ___ | |_  _ __  _   _   ___ | |_ (_)  ___   _ __   ___ ::
:: | | | '_ \ / __|| __|| '__|| | | | / __|| __|| | / _ \ | '_ \ / __|::
:: | | | | | |\__ \| |_ | |   | |_| || (__ | |_ | || (_) || | | |\__ \::
::|___||_| |_||___/ \__||_|    \__,_| \___| \__||_| \___/ |_| |_||___/::
::                                                                    ::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

There is a specific order needed to run the programs in. 

1)First you should run the DataDownloader.ipynb

1a) The program specifically DataDownloader.ipynb, has the ability to download the entire steam library, this means that downloading the data can take a large amount of time. Therefore extra code has been added to limit the amount of data that the program downloads. This code is done added In cell 7 (lines 56 and 57) and cell 9 (line 35 and 36). it is recommended when running DataDownloader.ipynb you click run all, however you can also run each cell one after the other.

1b) Please do note that some time the API can give an SSLError, this is unfortunatley something out of my control and is to do with the APIs themselves. If you do receive such errors. it is recommended to extract the AllData.zip file into the projects folder and overwrite/replace any files. 

2) After Downloading the data you can move onto running SteamApiCleaner.ipynb. It is recommended to click run all, however you can also run each cell one after the other.

3) Then you can move on to running SteamSpyCleaner.ipynb. It is recommended to click run all, however you can also run each cell one after the other.

4) Before running the RecommendationEngine.py it is recommended to extract the  AllData.zip file into the projects folder and overwrite/replace any files.

5) gui.py does not need to be run by itself.

Thank you for reading and if ther are any problems you are experiencing please refer to the demo video below:

https://www.youtube.com/watch?v=DGVO_5SeEts


