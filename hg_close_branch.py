#!/usr/bin/env python
#coding:utf-8
class _Getch:
    """Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            try:
                self.impl = _GetchMacCarbon()
            except ImportError:
                self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys, termios # import termios now or else you'll get the Unix version on the Mac

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

class _GetchMacCarbon:
    """
    A function which returns the current ASCII key that is down;
    if no ASCII key is down, the null string is returned.  The
    page http://www.mactech.com/macintosh-c/chap02-1.html was
    very helpful in figuring out how to do this.
    """
    def __init__(self):
        from Carbon import Evt
        Evt #see if it has this (in Unix, it doesn't)

    def __call__(self):
        from Carbon import Evt
        if Evt.EventAvail(0x0008)[0] == 0: # 0x0008 is the keyDownMask
            return ''
        else:
            #
            # The event contains the following info:
            # (what,msg,when,where,mod)=Evt.GetNextEvent(0x0008)[1]
            #
            # The message (msg) contains the ASCII char which is
            # extracted with the 0x000000FF charCodeMask; this
            # number is converted to an ASCII character with chr() and
            # returned
            #
            (what, msg, when, where, mod) = Evt.GetNextEvent(0x0008)[1]
            return chr(msg & 0x000000FF)
getch = _Getch()


from os.path import join
from os import getenv
from optparse import OptionParser


def main():
    import os
    import sys
    from os.path import dirname, exists, join
    path = os.getcwd()

    #os.chroot(path) 
    sys.argv = sys.argv[:1]

    hg_branch = os.popen("hg branches").readlines()
    while True:
        t = []
        for i in hg_branch:
            i = i.strip()
            if i and i.find(":") > 0:
                name = i.split(" ", 1)
                if name[0] != "default":
                    t.append(map(str.strip, name))
        print "\n"
        for pos, i in enumerate(t, 1):
            print "%s\t%s\t%s"%(str(pos).ljust(3), i[0].ljust(35), i[1])
        num = raw_input("\nCLOSE BRANCH  : ").strip()
        if num.isdigit():
            num = int(num) - 1
            if num < 0:
                break
            if num >= 0 and num < len(t):
                branch = t[num][0]
                cmd = """
hg update %s
hg commit --close-branch -m close
hg update default
    """%branch
                line_break = "-"*64
                cmd = [i.strip() for i in cmd.split("\n") if i]
                print "\n关闭分支 %s ?(Y确认,否则取消)"%branch
                if getch() in ["y", "Y"]:
                    print line_break
                    import os
                    success = True
                    for i in cmd:
                        print ">>>%s"%i
                        if os.system(i) != 0:
                             success = False
                             break





if __name__ == "__main__":
    main()

