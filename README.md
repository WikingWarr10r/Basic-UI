**A Basic UI Implementation for PyGame**

This is a basic, general implementation in PyGame to create UI for future projects inspired by ImGUI.

**Installing**

Download the repo, place the ```ui``` folder and ```ui_system.py``` in your project.

First add these imports:
```
from ui.ui_container import UIContainer
from ui.math import vec2
```

Then create a UI Container:
```
ctr1 = UIContainer("Hello", vec2(0, 0), 100, 500)
```

Initialise the UI System and add a UI Container:
```
ui_system = UISystem()
ui_system.add_container(ctr1)
```
Finally in the main loop:
Run ```ui_system.handle_events()``` to handle mouse clicks 

After clearing the screen run ```ui_system.update()``` to be able to move and render the container
