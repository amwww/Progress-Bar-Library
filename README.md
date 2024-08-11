# Progress Bar Library

A Simple Progress Bar Library in Python to track FOR loops.

- RichCLI Styles
- Custom Titles
- Percentage, ETA, Speed

# Instructions

1. Download the project as a ZIP
2. Extract the ZIP
3. Read the examples if you like
4. Copy the progress.py file into your project

# Examples

Simple Progress Bar
```
from progress import progress
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a)):
    time.sleep(1)
```

```
40.0%  | ██████████████████████████████████████████████████                                                 | (0:02<0:03) 2/5 1.02s/it
```

```
100.0% | ██████████████████████████████████████████████████████████████████████████████████████████████████ | (0:05<0:00) 5/5 1.01s/it  
==> Finished.
```

Simple Progress Bar with Titles
```
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, titles=a)):
    time.sleep(0.5)
```

```
60.0%  | ██████████████████████████████████████████████████████████                                       | (0:01<0:01) 3/5 1.98it/s 
==> Proccessing 7 
```

Progress Bar with Actioned Titles
```
a = [('Proccessing', '1'), ('Downloading', '2')]
for idx, num in enumerate(progress(a, titles=a)):
    time.sleep(2)
```

```
50.0%  | ████████████████████████████████████████████████                                                 | (0:02<0:02) 1/2 2.00s/it    
==> Downloading 2    
```

Progress Bar with Names with Rich Styling
```
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, name="[bold magenta]Download Progress[/bold magenta]")):
    time.sleep(0.5)
```

(not colored in the markdown)

```
Download Progress
100.0% | ██████████████████████████████████████████████████████████████████████████████████████████████████ | (0:02<0:00) 5/5 1.98it/s  
==> Finished.
```

Colored Progress Bar

```
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, percentagestyle='bold blue', barstyle='red', etastyle="bold green", progressstyle="italic magenta", speedstyle='underline yellow')):
    time.sleep(2)
```