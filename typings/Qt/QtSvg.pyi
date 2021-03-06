# -*- coding=UTF-8 -*-
# This typing file was generated by typing_from_help.py
"""
Qt.QtSvg
"""

import six
import typing
import PySide
import Shiboken
class QGraphicsSvgItem(PySide.QtGui.QGraphicsObject):
    __new__: ...
    """
    T.__new__(S, ...) -> a new object with type S, a subtype of T
    """

    staticMetaObject: ...
    """
    <PySide.QtCore.QMetaObject object>
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...

    def boundingRect(self, *args, **kwargs):
        """
        """
        ...

    def elementId(self, *args, **kwargs):
        """
        """
        ...

    def isCachingEnabled(self, *args, **kwargs):
        """
        """
        ...

    def maximumCacheSize(self, *args, **kwargs):
        """
        """
        ...

    def paint(self, *args, **kwargs):
        """
        """
        ...

    def renderer(self, *args, **kwargs):
        """
        """
        ...

    def setCachingEnabled(self, *args, **kwargs):
        """
        """
        ...

    def setElementId(self, *args, **kwargs):
        """
        """
        ...

    def setMaximumCacheSize(self, *args, **kwargs):
        """
        """
        ...

    def setSharedRenderer(self, *args, **kwargs):
        """
        """
        ...

    def type(self, *args, **kwargs):
        """
        """
        ...

    ...

class QSvgGenerator(PySide.QtGui.QPaintDevice):
    __new__: ...
    """
    T.__new__(S, ...) -> a new object with type S, a subtype of T
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...

    def description(self, *args, **kwargs):
        """
        """
        ...

    def fileName(self, *args, **kwargs):
        """
        """
        ...

    def metric(self, *args, **kwargs):
        """
        """
        ...

    def outputDevice(self, *args, **kwargs):
        """
        """
        ...

    def paintEngine(self, *args, **kwargs):
        """
        """
        ...

    def resolution(self, *args, **kwargs):
        """
        """
        ...

    def setDescription(self, *args, **kwargs):
        """
        """
        ...

    def setFileName(self, *args, **kwargs):
        """
        """
        ...

    def setOutputDevice(self, *args, **kwargs):
        """
        """
        ...

    def setResolution(self, *args, **kwargs):
        """
        """
        ...

    def setSize(self, *args, **kwargs):
        """
        """
        ...

    def setTitle(self, *args, **kwargs):
        """
        """
        ...

    def setViewBox(self, *args, **kwargs):
        """
        """
        ...

    def size(self, *args, **kwargs):
        """
        """
        ...

    def title(self, *args, **kwargs):
        """
        """
        ...

    def viewBox(self, *args, **kwargs):
        """
        """
        ...

    def viewBoxF(self, *args, **kwargs):
        """
        """
        ...

    ...

class QSvgRenderer(PySide.QtCore.QObject):
    __new__: ...
    """
    T.__new__(S, ...) -> a new object with type S, a subtype of T
    """

    repaintNeeded: ...
    """
    Signal
    """

    staticMetaObject: ...
    """
    <PySide.QtCore.QMetaObject object>
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...

    def animated(self, *args, **kwargs):
        """
        """
        ...

    def animationDuration(self, *args, **kwargs):
        """
        """
        ...

    def boundsOnElement(self, *args, **kwargs):
        """
        """
        ...

    def currentFrame(self, *args, **kwargs):
        """
        """
        ...

    def defaultSize(self, *args, **kwargs):
        """
        """
        ...

    def elementExists(self, *args, **kwargs):
        """
        """
        ...

    def framesPerSecond(self, *args, **kwargs):
        """
        """
        ...

    def isValid(self, *args, **kwargs):
        """
        """
        ...

    def load(self, *args, **kwargs):
        """
        """
        ...

    def matrixForElement(self, *args, **kwargs):
        """
        """
        ...

    def render(self, *args, **kwargs):
        """
        """
        ...

    def setCurrentFrame(self, *args, **kwargs):
        """
        """
        ...

    def setFramesPerSecond(self, *args, **kwargs):
        """
        """
        ...

    def setViewBox(self, *args, **kwargs):
        """
        """
        ...

    def viewBox(self, *args, **kwargs):
        """
        """
        ...

    def viewBoxF(self, *args, **kwargs):
        """
        """
        ...

    ...

class QSvgWidget(PySide.QtGui.QWidget):
    __new__: ...
    """
    T.__new__(S, ...) -> a new object with type S, a subtype of T
    """

    staticMetaObject: ...
    """
    <PySide.QtCore.QMetaObject object>
    """

    def __init__(self, *args, **kwargs):
        """
        x.__init__(...) initializes x; see help(type(x)) for signature
        """
        ...

    def load(self, *args, **kwargs):
        """
        """
        ...

    def paintEvent(self, *args, **kwargs):
        """
        """
        ...

    def renderer(self, *args, **kwargs):
        """
        """
        ...

    def sizeHint(self, *args, **kwargs):
        """
        """
        ...

    ...

__all__: ...
"""
['QGraphicsSvgItem', 'QSvgGenerator', 'QSvgRenderer', 'QSvgW...
"""

