import sys
import platform
def whereami():
        if 'idlelib.run' in sys.modules and sys.stdin is not sys.__stdin__:
                o="idle"
        elif platform.system()=="Linux":
                o="lin"
        else:
                o="win"
        return o
