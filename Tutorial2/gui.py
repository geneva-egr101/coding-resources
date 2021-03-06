import threading
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog


def install_thread_excepthook():
    """
    Workaround for sys.excepthook thread bug
    (https://sourceforge.net/tracker/?func=detail&atid=105470&aid=1230540&group_id=5470).
    Call once from __main__ before creating any threads.
    If using psyco, call psycho.cannotcompile(threading.Thread.run)
    since this replaces a new-style class method.
    """
    import sys
    run_old = threading.Thread.run
    def run(*args, **kwargs):
        try:
            run_old(*args, **kwargs)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            sys.excepthook(*sys.exc_info())
    threading.Thread.run = run


class MainWindow(QDialog):
    def __init__(self, app, filename, custom_closeEvent=None):
        super(MainWindow, self).__init__()
        uic.loadUi(filename, self)

        self._app = app
        self.filename = filename
        self.custom_closeEvent = custom_closeEvent if custom_closeEvent else lambda: None
        self.closed = False

    
    def connect_event(self, event, target, args=[]):
        event.connect(lambda: target(*args), Qt.DirectConnection)

    
    def update(self):
        self._app.processEvents()


    def closeEvent(self, event):
        self.custom_closeEvent()
        self.closed = True
        event.accept()


def create(*args):
    app = QApplication([])
    window = MainWindow(app, *args)
    return window


install_thread_excepthook()
