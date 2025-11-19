# idlemation-ASCII

A simple code that runs an animation as a part of the desktop (technically its on top of the desktop, but below all other programs). $${\color{red}PRECAUTION}$$ : Only works on Windows currently.

## Features
1. Through animation modules present in the *Animations* folder, users can modify or create their own ASCII animations.
2. The animation can start playing on startup
3. Users can configure the animation settings via the *config* csv file created after running the code once. They can:
     1. Choose whether or not to automatically play an animation on startup,
     2. Choose which animation module to use,
     3. Configure the actual animation player (speed, background colour, font colour etc.)
   
## How to get On-Startup to get working
1. Press Win+R to open the run command window
2. Type or paste *shell:startup*. This opens the folder where all startup programs go.
3. Hover over a blank space and *right click > new > shortcut*
4. In the space provided paste something like
     1. *"C:\Path\To\pythonw.exe" "C:\Path\To\idlemation.pyw"*
     2. Example: *"C:\Users\Blaziken\AppData\Local\Programs\Python\Python312\pythonw.exe" "C:\Users\Blaziken\Desktop\PythonCodes\idlemation.pyw"*
     3. PRECAUTION : Make sure you link to *pythonw.exe* path and not *python.exe*
6. Click Next, name it anything (e.g., ASCII-Animation), and finish.

## How to configure the animation player settings
1. Run the program once, you should see the default animation play (counting numbers)
2. Go to the folder where *idlemation.pyw* is saved, there you should see a new *config.csv* file
3. Open it and you can configure the settings
4. PRECAUTION : Use hexadecimal codes for their respective colours; do not include the *.py* extension when choosing animation modules

## How to create an animation module
1. Open *ANIM_template.py* module and make each individual frame inside the *frames* list
2. The box provided in the template is optional
3. Optimally, each frame should be 33 spaces across and 23 spaces deep
4. PRECAUTION : The list should be named *frames*

   
