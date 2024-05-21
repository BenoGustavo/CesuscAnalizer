<p align="center">
  <a href="https://cesusc.edu.br/">
    <img src="assets/images/logo-cesusc.png" alt="Cesusc Logo" width=72 height=72>
  </a>

  <h3 align="Center">Cesusc Personal Analizer</h3>

  <p align="center">
    Your personal performance analizer
    <br>
    <a href="https://reponame/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://reponame/issues/new?template=feature.md&labels=feature">Request feature</a>
  </p>
</p>

## Table of contents

-   [Quick start linux](#quickstart-for-linux)
-   [Quick start windows](#quickstart-for-windows)
-   [Status](#status)
-   [What's included](#whats-included)
-   [Contributing](#contributing)
-   [Creator](#creator)
-   [Thanks](#thanks)
-   [Copyright and license](#copyright-and-license)

## Requirements

-   Google Chrome
-   Python >= 3.10

If you don't have the Google Chrome installed it will freeze the application.

## Quickstart-for-linux

Setup on Linux🐧(Tested on Ubuntu 22.04.03 LTS)

-   Download the project from the GitHUB

-   Extract the file

-   Open the dir on your terminal (Bash,ZSH or others)

-   Create a Python .env on the root of the project

    `python3 -m venv .env` OR `python3.10 -m venv .env`

-   Enter on you Python .env

    `source "your_env"/bin/activate` OR `. "your_env"/bin/activate`

-   Install the modules and libs

    `pip install -r requirements.txt` OR `pip3 install -r requirements.txt`

-   Run the application

    `python3 src/app.py` OR `python3.10 src/app.py`

-   If it won't work right away you will need some extra system libs for it to work fine so...

-  This is the error you will probably get:

    ```t.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found. This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.```

-  Fix it with:

    ```sudo apt-get install libxcb-xinerama0 libxcb-xinerama0-dev libxcb1 libxcb1-dev libx11-xcb1 libx11-xcb-dev libxcb-render0-dev libxcb-shape0-dev libxcb-xfixes0-dev libxcb-cursor0```

-   Now your application may be working 😃

## Quickstart-for-windows

_Work in progress_

## Status

It's already finished (I think), but can have some bugs. Feel free notify me if you see any.

## What's included

Project structure. If you wan't to know more about each module check-out his inside documentation.

```text
master/
├── assets/
│       ├──Images/
│       │        └── (all kinds of images)
│       └── UI/
 |                └── (Project interfaces from qtdzn)
├── out/
 |        └── (Your reports)
└── src/
    ├── database/
    │   ├── connection/
    │   │       └── StudantController.py
    │   ├── studants.db
    │   └── studantModel.py
    ├── scraping/
    │  ├── browserInstance/
    │  │       ├── bin/
    │  │       │       └── (YourChromeDriver)
    │  │       └── makeChromeInstance.py
    │  ├── dataMining.py
    │  ├── scrapper.py
    │  ├──utils.py
    │  └──xlsxWriter.py
    ├─ screens/
    │     ├──controllers/
    │     │      ├── registerUserController.py
    │     │      ├── selectUserController.py
    │     │      └── workers.py
    │     ├──registerScreen.py
    │     ├──resourcePath.py
    │     └──selectUserScreen.py
    └── app.py
```

## Creator

**Gustavo Leandro Gorges**

-   <https://github.com/BenoGustavo>

## Thanks

I want to thank you for your attention =)

## Copyright and license

Code and documentation copyright 2011-2018 the authors.

Enjoy
