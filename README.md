# idlemation-ASCII

A simple code that runs an animation as a part of the desktop (technically its on top of the desktop, but below all other programs). $${\color{red}PRECAUTION}$$ : Only works on Windows currently.

## Features
1. Through animation modules present in the *Animations* folder, users can modify or create their own ASCII animations.
2. The animation can be set to run automatically on system startup.
3. Users can configure the animation settings via the *config.csv* file created after running the code once. They can:
     1. Choose whether or not to automatically play an animation on startup,
     2. Choose which animation module to load,
     3. Configure animation behaviour (speed, background colour, font, font colour etc.)
   
## How to get On-Startup to get working
1. Press Win+R to open the run command window
2. Type or paste *shell:startup*. This opens the folder where all startup programs go.
3. Hover over a blank space and *right click > new > shortcut*
4. In the space provided paste something like
     1. *"C:\Path\To\pythonw.exe" "C:\Path\To\idlemation.pyw"*
     2. Example: *"C:\Users\Blaziken\AppData\Local\Programs\Python\Python312\pythonw.exe" "C:\Users\Blaziken\Desktop\PythonCodes\idlemation.pyw"*
     3. $${\color{red}PRECAUTION}$$ : Make sure you link to *pythonw.exe* path and not *python.exe*
6. Click Next, name the shortcut anything (e.g., ASCII-Animation), and finish.

## How to configure the animation player settings
1. Run the program once; the default animation play (counting numbers) should play
2. In the same folder where *idlemation.pyw* is saved, you should see a new *config.csv* file
3. Open it (through text editor or a spreadsheet program) and configure the settings according to your need
4. $${\color{red}PRECAUTION}$$ : Use hexadecimal codes for their respective colours; do not include the *.py* extension when selecting animation modules

## How to create an animation module
1. Open *ANIM_template.py* module (inside the *Animations* folder) and add each individual frame inside the *frames* list
2. The provided ASCII “box” in the template is optional
3. For consistency, each frame should be roughly 25 characters wide and 33 lines tall (recommended)
4. $${\color{red}PRECAUTION}$$ : The list should be named *frames* and each element should be a string

   
