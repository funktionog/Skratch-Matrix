-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
   ___________                   __         .__         _____          __         .__        
  /   _____/  | ______________ _/  |_  ____ |  |__     /     \ _____ _/  |________|__|__  ___
  \_____  \|  |/ /\_  __ \__  \\   __\/ ___\|  |  \   /  \ /  \\__  \\   __\_  __ \  \  \/  /
  /        \    <  |  | \// __ \|  | \  \___|   Y  \ /    Y    \/ __ \|  |  |  | \/  |>    < 
 /_______  /__|_ \ |__|  (____  /__|  \___  >___|  / \____|__  (____  /__|  |__|  |__/__/\_ \
         \/     \/            \/          \/     \/          \/     \/                     \/
                                                                                        by funktion_og
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------------
## Overview
-----------------------------------------------------------------------------------------------------------------------------
Skratch Matrix is a Python-based desktop tool designed for DJs and enthusiasts to manage and access their favorite Loopers and Flash Loopers. These looped beats are essential for scratch DJs, providing endless grooves to scratch over during practice or live performances. Skratch Matrix integrates local file support and links to Tablist.net, a platform offering a rich library of web-based loopers.

-----------------------------------------------------------------------------------------------------------------------------
## Features
-----------------------------------------------------------------------------------------------------------------------------

- Create and manage a personalized playlist of Flash Loopers.
- Add loopers via local file paths or URLs.
- Direct access to the Tablist.net web looper library.
- Launch loopers directly from the app.
- Save and load playlists for convenience.


-----------------------------------------------------------------------------------------------------------------------------
##  Libraries:
-----------------------------------------------------------------------------------------------------------------------------

- tkinter: Creates the graphical user interface (GUI).
- messagebox: Provides popup dialogs for warnings/errors.
- webbrowser: Opens URLs in a web browser.
- json: Reads and writes playlist data to a JSON file.
- os: Handles file paths and system-level interactions.
- sys: Provides system-specific parameters and functions.
- colorama: Adds colored terminal text, enhancing text-based visuals.
- termcolor and pyfiglet: Generate stylized ASCII art for the terminal.


-----------------------------------------------------------------------------------------------------------------------------
### Background: Flash Apps and Their Deprecation
-----------------------------------------------------------------------------------------------------------------------------

**Flash Apps** were interactive web applications created using Adobe Flash, a multimedia software platform renowned for its ability to produce animations, games, and interactive content. Flash was widely adopted during the early 2000s, providing a platform for creative and engaging experiences on the web, including DJ tools like Flash Loopers. Flash-based apps allowed developers to embed dynamic and rich content directly into web pages, making them a cornerstone of early web interactivity.

However, Flash faced significant challenges over time, such as performance issues, security vulnerabilities, and the rise of modern alternatives like HTML5, CSS3, and JavaScript. Adobe officially deprecated Flash on **December 31, 2020**, ceasing support and distribution for the platform. This move marked the end of an era and prompted many developers to transition to more robust, secure, and future-proof technologies for building interactive web applications.

-----------------------------------------------------------------------------------------------------------------------------
## What Are Flash Loopers?
-----------------------------------------------------------------------------------------------------------------------------

Flash Loopers are short audio loops tailored for DJs to scratch over. These loops provide consistent beats and rhythms, allowing scratch DJs to hone their skills or perform extended sets. Often used in combination with turntables or controllers, Flash Loopers are indispensable tools for modern DJs.

Despite the official deprecation of Adobe Flash in 2020, which rendered many Flash-based applications obsolete, some scratch DJs still maintain a collection of Flash loopers. They often run these loopers locally on their devices, preserving a nostalgic and functional part of their creative process. These legacy tools continue to hold sentimental and practical value, allowing DJs to keep practicing and performing with the loops they have grown accustomed to.

-----------------------------------------------------------------------------------------------------------------------------
## What is Tablist.net?
-----------------------------------------------------------------------------------------------------------------------------

Tablist.net is a popular online resource for scratch DJs. It hosts a vast collection of web loopers and resources, making it a go-to platform for DJs seeking fresh beats and creative inspiration. Skratch Matrix integrates this platform, enabling users to directly browse and use these web loopers.
Use the Tablist.net button to launch the Tablist.net weblooper. Once there you can locate a looper you like and copy the url to add 


-----------------------------------------------------------------------------------------------------------------------------
## How Does Skratch Matrix Fit Into This Discussion?
-----------------------------------------------------------------------------------------------------------------------------

Skratch Matrix provides a single location to create and edit a playlist to launch a user's favorite webloopers stored on Tablist.net and a user's favorite Flashloopers that are locally stored on their device.

-----------------------------------------------------------------------------------------------------------------------------
## How to Use Skratch Matrix
-----------------------------------------------------------------------------------------------------------------------------


1. **Add a Looper**:
   - Enter the looper's name in the "Looper Name" field.
   - Provide the file path or URL in the "URL or File Path" field.
   - To add a Flashlooper that is already on your harddrive you will need to copy the file path of the .exe and paste it in the "URL or File Path" field.
   - Click "Add to Playlist" to save it.
2. **Access Tablist.net**:
   - Click the "Tablist.net" button to open the tablist.net web looper library.
3. **Manage Your Playlist**:
   - Use "Remove Looper" to delete items from your playlist.
   - Click "Open Looper" to launch a selected item.
4. **Save and Load**:
   - Your playlist is automatically saved to a JSON file and loaded upon reopening the app.

 
-----------------------------------------------------------------------------------------------------------------------------
## Contributing
-----------------------------------------------------------------------------------------------------------------------------

Contributions to Skratch Matrix are welcome! Feel free to submit issues or pull requests to enhance the functionality or improve the user experience.




