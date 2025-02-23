

Re-Manga is a CLI program that can be used to install reddit posts of Mangas/Doujinshis.

# Pre-requisites

You might need the latest version of python for the rezip.py script to work. 

After getting python:

 1. Press `Win + S` and search for "Command Prompt"
 2. Change your working directory to your Re-Manga's
 3. Run `pip install -r requirements.py`


In Windows, I recommend you to use Git for Windows.



#  Installation

**Clone Via Git**

To use Re-Manga using git, run:
```
git clone https://github.com/RafaeloHQ/Re-Manga
```

**As a Zip**

Alternatively, you can download it as a zip by doing this:
 - Go to the Re-Manga repository at https://github.com/RafaeloHQ/Re-Manga
 - Click the green "Code" button
 - Click "Download Zip" button
 - Install it to your desired directory `i.e C:\Users\User\Desktop\Remanga`


# Reddit API Set Up

Re-Manga requires a Reddit API so that the title of the reddit post is retrieved and used. To set it up, do the following:

 - Go to [Reddit Apps](https://www.reddit.com/prefs/apps) (You need a reddit account)
 - Press "Create An App"
 - Set "Script" as the application type
 - Fill in the `name`, `redirect uri` (use http://localhost) and `description`
 - After creating the app, copy your `Client ID` and `Client Secret`
 - In your Re-Manga directory, open `API.env` and save the `Client ID` and `Client Secret` to their corresponding variable.
 - Save `API.env` 

# Re-Manga Set Up

To ensure that the package is working, follow the instructions below:

**On Linux:**
*if you cloned the repository:
```
cd ~/Re-Manga
```

```
chmod +x remanga
```

*if you installed it as a zip, and you decompressed it on directory:
```
cd <Re-Manga Directory>
```
```
chmod +x remanga
```

**On Windows:**

To use Re-Manga on windows, I recommend using [Git for Windows](https://git-scm.com/downloads/win)

And to also ensure that the package works, put the directory in the PATH environment variables:
  1. Press `win + S` and search for "Edit the system environment variables"
  2. Press the "Environment Variables..." button
  3. Under "System Variables" look for the PATH field and press "Edit..."
  4. Press the "New" button and paste the decompressed directory of Re-Manga `i.e C:\Users\User\Desktop\Re-Manga`
  5. Press "Okay" to save.

After putting the directory to the PATH system variables, you can start using it!

# Usage

To start using Re-manga:

```
remanga <Reddit URL>
```

# Features

**Destination Setup**

In your first run of Re-Manga, you will be prompted to set a destination directory for your downloads. Your manga/doujinshis will be compressed to Comic Book Zip Archive, otherwise known as CBZ, and will be placed under a directory named after the reddit post.
`i.e C:\Users\User\Desktop\Mangas\<Reddit Post Name>\ <Reddit Post Name>.cbz`

The purpose of this is to allow for manga readers like Komga and Kavita to organize them as separate series, instead of a book under a single series.

**URL Logging**

In each reddit post you install, a `source.txt` file will be included, which will include the reddit url of the post.

Re-manga will also create a `links.txt` file that will log all of the reddit urls you install. This is for the `-r` re-download feature that will basically install the lifetime collection of Reddit URLs that Re-Manga has collected.
You can copy this file anywhere for safe-keeping. 

**-r Parameter**

If you've used Re-Manga for a while, the `links.txt` file will be populated with all the Reddit URLs that you've downloaded. To redownload all the links inside `links.txt`, you can pass the `-r` parameter:
```
remanga -r
```
which will download all the URLs inside that file.

(Or you can replace `links.txt` with your own selection of reddit posts that you may want to download)


