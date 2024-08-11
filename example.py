from progress import progress
import time

# Simple Progress Bar
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a)):
    time.sleep(1)

# Simple Progress Bar with Title
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, titles=a)):
    time.sleep(0.5)

# Progress Bar with Actioned Titles
a = [('Proccessing', '1'), ('Downloading', '2')]
for idx, num in enumerate(progress(a, titles=a)):
    time.sleep(2)

# Progress Bar with Names
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, name="Download Progress")):
    time.sleep(1)

# Progress Bar with Names with Rich Styling
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, name="[bold magenta]Download Progress[/bold magenta]")):
    time.sleep(0.5)

# Colored Progress Bar
a = [5, 6, 7, 8, 9]
for idx, num in enumerate(progress(a, percentagestyle='bold blue', barstyle='red', etastyle="bold green", progressstyle="italic magenta", speedstyle='underline yellow')):
    time.sleep(2)