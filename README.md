## MrWhoseTheBoss Adjectives
This repo was created to automate the video-making process for one of my YouTube videos titled *"Learn Adjectives with Arun"* which searches through the transcript of all of his videos and find the right keywords, then plays and screen-records the videos using ``Selenium`` bindings for Python and ``recordmydesktop``.
Same process can be reconfigured and repeated to search for a specific keyword/line and keep track of it for your favorite YouTube creator.

 - ### Install Dependencies
 `pip3 install youtube_transcript_api scrapetube selenium --user`
 `pacman -S recordmydesktop ffmpeg`
	
(Refer to your distribution's package manager)

 - ### Run script
Launch ``main.py`` first:

    python3 main.py
  This will create a new file ``url_list.txt`` which contains the next keyword of the search string and the video url which starts at that specific timestamp.
  
  Then:
  

    python3 record-screen.py

  This will use the installed `geckodriver` in your system and launch each URL one by one in *url_list.txt* file at the same time recording the screen and saving each file in the `downloads` folder.
  
*(Use `ffmpeg` to merge all video files into one which can be easily edited later)*
    

 

