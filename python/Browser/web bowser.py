# import webbrowser
# import os
#
# with open('engine.txt') as setting:
#     if 'engine' not in setting.read():
#         engine = input('Search engine preference: ')
#     else:
#         engine = setting.read()
# def browse(inp):
#     inp = input("Search--URL--Mail recepient--File-file_name--update-info-updatedinfo: ")
#     inp = inp.lower()
#     while inp != "":
#         if "https://" in inp or "www." in inp or "file://" in inp:
#             webbrowser.open_new_tab(inp)
#         elif "https://" not in inp and "mail" not in inp and "www." not in inp and "update-info" not in inp and "file-open-" not in inp and "launch-" not in inp:
#             webbrowser.open_new_tab(f"https://www.google.com/search?q={inp}")
#         elif "-mail-" in inp.split()[0] and "-update-info-" not in inp:
#             inp = inp.split("-")
#             webbrowser.open_new_tab(f"mailto:{inp[1]}")
#         elif "-update-info-" in inp:
#             inpset = {inp}
#             inplist = inp.split("-")
#             print(inp[2])
#         elif "file-open-" in inp:
#             inp = inp.split("-")
#             webbrowser.open_new_tab(f"file://{inp[2]}")
#         elif "launch-" in inp:
#             inp = inp.split("-")
#             open(inp[1])
#         else:
#             print("AN UNKNOWN ERROR OCCURED")
#         print("EXECUTED")
# browse(inp)

# Source - https://stackoverflow.com/a/72911080
# Posted by Devco
# Retrieved 2025-12-23, License - CC BY-SA 4.0

from functools import cached_property
import sys
import keyboard
from prompt_toolkit.key_binding import KeyBindings
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

bindings = KeyBindings()
url = input('Enter URL: ')


class WebView(QtWebEngineWidgets.QWebEngineView):
    def javaScriptConsoleMessage(self, level, message, lineID, sourceID):
        # Ignore CSP related noise from DuckDuckGo
        if "Content Security Policy" in message or "Refused to prefetch" in message:
            return
        # Pass other messages through to the terminal
        super().javaScriptConsoleMessage(level, message, lineID, sourceID)

    def createWindow(self, type_):
        class WebView(QtWebEngineWidgets.QWebEngineView):
            def createWindow(self, type_):
                if not isinstance(self.window(), Browser):
                    return

                if type_ == QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
                    return self.window().tab_widget.create_tab()


class TabWidget(QtWidgets.QTabWidget):
    def create_tab(self):
        view = WebView()

        index = self.addTab(view, "...")
        self.setTabIcon(index, view.icon())
        view.titleChanged.connect(
            lambda title, view=view: self.update_title(view, title)
        )
        view.iconChanged.connect(lambda icon, view=view: self.update_icon(view, icon))
        self.setCurrentWidget(view)
        return view

    def update_title(self, view, title):
        index = self.indexOf(view)
        if 'DuckDuckGo' in title:
            self.setTabText(index, 'Welcome to the best web browser in existence; *Atoll*')
        else:
            self.setTabText(index, title)

    def update_icon(self, view, icon):
        index = self.indexOf(view)
        self.setTabIcon(index, icon)


class Browser(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # main browser function

        super().__init__(parent)
        self.setCentralWidget(self.tab_widget)

        view = self.tab_widget.create_tab()
        if url in ['https://', 'www.']:
            view.load(self.url)
        else:
            view.load(QtCore.QUrl(f"https://www.duckduckgo.com/{url}"))

        QtWebEngineWidgets.QWebEngineProfile.defaultProfile().downloadRequested.connect(self.on_downloadRequested)

    @QtCore.pyqtSlot("QWebEngineDownloadItem*")
    def on_downloadRequested(self, download):
        old_path = download.url().path()
        suffix = QtCore.QFileInfo(old_path).suffix()
        path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()

    @cached_property
    def tab_widget(self):
        return TabWidget()


def main():
    app = QtWidgets.QApplication(sys.argv)

    # ADD PARENTHESES to create an instance of the Browser class
    w = Browser()

    w.showMaximized()  # You can call showMaximized() directly
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
