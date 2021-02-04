# MBSim

**Portuguese ATM Simulator** for school project

![multibanco](main_menu.png)

## List of contents

1. [Info](#Info)
1. [Development](#Development)
1. [Features](#Features)
1. [Get Started](#Get-Started)

## Info

The current version of the program is only optimised for Windows 10.

*Default admin password is* `3579`

## Development

This project was made and is maintained by @goncrust, @teravyte18 and @KingKatana09:

[![](https://github.com/goncrust.png?size=50)](https://github.com/goncrust) [![](https://github.com/teravyte18.png?size=50)](https://github.com/teravyte18) [![](https://github.com/KingKatana09.png?size=50)](https://github.com/KingKatana09)

## Features

### Real Banks

The application has a list of real Portuguese banks, with iban generation similar to reality.

![banks](banks_register.png)

### Admin Menu

With an admin menu you can change any user data you want.

![admin](admin_menu.png)

### Local Database

SQLite3 is used so that all data relating to users and account movements is stored locally.

## Get Started

### Requirements

- python (3 or above)
- pillow
- tkcalendar

### Step by step

1. Install [python 3.9](https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe)
1. Install the required python librarys:
    - `pip install pillow`
    - `pip install tkcalendar`
1. Clone the repo
1. Go to the folder created by cloning the repo and run `py main.py`
