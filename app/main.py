# -*- coding: utf-8 -*-
# app/main.py

"""This module provides Desktop Reporting application."""

import sys

from PyQt5.QtWidgets import QApplication,QMainWindow
from .database import createConnection
from .views import Ui_MainWindow

def main():
    """Desktop Reporting main function."""
    # Create the application
    app = QApplication(sys.argv)
    # Connect to the database before creating any window
    if not createConnection("database.sqlite"):
        sys.exit(1)
    app.setStyle('fusion')
    # Create the main window
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # Run the event loop
    sys.exit(app.exec_())
