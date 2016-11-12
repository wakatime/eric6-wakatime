eric6-wakatime
==============

Metrics, insights, and time tracking automatically generated from your programming activity.


Installation
------------

1. Run `install.py`:

  **Mac and Linux**

  `curl -fsSL https://raw.githubusercontent.com/wakatime/eric6-wakatime/master/install.py | python`

  **Windows**

  Download and extract [eric6-wakatime-master.zip](https://github.com/wakatime/eric6-wakatime/archive/master.zip), then double click `install.py`.

2. Restart Eric6/Pymakr.

3. Enter your [api key](https://wakatime.com/settings), then press `enter`. If not prompted, select File -> WakaTime.

4. Use Eric6/Pymakr and your time will be tracked for you automatically.

5. Visit https://wakatime.com/dashboard to see your logged time.


Screen Shots
------------

![Project Overview](https://wakatime.com/static/img/ScreenShots/Screen-Shot-2016-03-21.png)


Troubleshooting
---------------

First, turn on debug mode in your `~/.wakatime.cfg` file by adding this line:

`debug = true`

Second, in Pymakr/Eric6 go to Settings -> Enable expert mode, then add this line to your `~/.config/Pycom/pymakr.ini` file under the `UI` section:

`AdvancedBottomSidebar=true`

Then, restart Eric6/Pymakr and look for error messages in the Log-Viewer tab at the bottom.

Also, tail your `$HOME/.wakatime.log` file to debug wakatime cli problems.

For more general troubleshooting information, see [wakatime/wakatime#troubleshooting](https://github.com/wakatime/wakatime#troubleshooting).
