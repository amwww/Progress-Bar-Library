import time, math, os
from rich import print as print_rich
from typing import Iterable

class progress:
    def __init__(self, iter:Iterable, *, titles:Iterable[tuple[str, str]]|Iterable[str]|None=None, name:str|None=None, percentagestyle:str='white', barstyle:str='white', etastyle:str='white', progressstyle:str='white', speedstyle:str='white') -> None:
        self.iter = iter
        self.barchar = u" " + u''.join(map(chr, range(0x258F, 0x2587, -1)))
        self.iterlen = len(iter)
        self.iteridx = 0
        self.iterpref = []
        self.complete = False
        self.titles=titles
        self.name=name
        self.running = False
        self.lastupdate = time.perf_counter()
        self.percentagestyle = percentagestyle
        self.barstyle = barstyle
        self.etastyle = etastyle
        self.progressstyle = progressstyle
        self.speedstyle = speedstyle

    def clear(self) -> None:
        tersize = (os.get_terminal_size().columns, os.get_terminal_size().lines)
        returnchar = '\033[F' if self.titles else '\r'
        print(tersize[0]*" "*(2 if self.titles else 1), end=returnchar)

    def display(self, write:bool=True, returnchar:str='\r') -> str:
        self.lastupdate = time.perf_counter()
        self.clear() if self.iteridx > 0 else ""
        returnchar = '\033[F' if self.titles else returnchar
        percentage = progress.toFixed(self.iteridx/self.iterlen*100, 1)
        elapsed = progress.toClock(int(time.perf_counter() - self.starttime))
        avg = sum(self.iterpref)/len(self.iterpref) if self.iteridx > 0 else "??"
        avgstr = (f'{progress.toFixed(avg, 2)}s/it' if avg >= 1 else f'{progress.toFixed(1/avg, 2)}it/s') if self.iteridx > 0 else "??s/it"
        remaining = (progress.toClock(avg * (self.iterlen - self.iteridx))) if self.iteridx > 0 else "??"
        tersize = (os.get_terminal_size().columns, os.get_terminal_size().lines)
        display = f'100.0% |  | [{elapsed}<{remaining}] {self.iteridx}/{self.iterlen} {avgstr} {returnchar}'
        maxbarsize = tersize[0] - len(display)
        barsize = int(maxbarsize * (self.iteridx/self.iterlen))
        display = f'[{self.percentagestyle}]{percentage}%{(5-len(str(percentage)))*" "}[/{self.percentagestyle}] | [{self.barstyle}]{barsize * self.barchar[-1]}{(maxbarsize-barsize)*" "}[/{self.barstyle}] | [{self.etastyle}]({elapsed}<{remaining})[/{self.etastyle}] [{self.progressstyle}]{self.iteridx}/{self.iterlen}[/{self.progressstyle}] [{self.speedstyle}]{avgstr}[/{self.speedstyle}]'
        title = ''
        if self.titles and self.iterlen != self.iteridx:
            if type(self.titles[self.iteridx]) == tuple:
                title = f'\n[green]==>[/green] [bold]{self.titles[self.iteridx][0]}[/bold] [bold green]{self.titles[self.iteridx][1]}[/bold green]'
            else:
                title = f'\n[green]==>[/green] [bold]Proccessing[/bold] [bold green]{self.titles[self.iteridx]}[/bold green]'
        if write:
            print_rich(display, end='')
            print_rich(f'{title}' if self.iterlen != self.iteridx else f'\n[blue]==>[/blue] [bold]Finished.[/bold]', end=returnchar if self.iterlen != self.iteridx else '\n')
        return display

    @staticmethod
    def toClock(secs:int) -> str:
        hr = math.floor(secs / (60*60))
        mins = math.floor(secs / 60)
        secs = int(secs % 60)
        return f'{str(hr) + ":" if hr > 0 else ""}{mins if len(str(mins)) == 2 or hr == 0 else "0" + str(mins)}:{secs if len(str(secs)) == 2 else "0" + str(secs)}'

    @staticmethod
    def toFixed(num:float, deci:int) -> float:
        num = str(num)
        newnum = ''
        aft = False
        deci = deci
        for digit in num:
            if aft:
                if deci > 0:
                    newnum += digit
                    deci -= 1
                    continue
                continue
            if digit != '.':
                newnum += digit
                continue
            newnum += '.'
            aft = True
        return newnum

    def __iter__(self):
        self.starttime = time.perf_counter()
        print_rich(self.name) if self.name else ""
        for obj in self.iter:
            self.display()
            self.running = True
            yield obj
            sumprev = sum(self.iterpref[0:(self.iteridx)])
            self.iterpref.append(time.perf_counter() - self.starttime - sumprev)
            self.iteridx += 1
        self.endtime = time.perf_counter()
        self.complete = True
        self.display(returnchar='\n')
        self.running = False
        return