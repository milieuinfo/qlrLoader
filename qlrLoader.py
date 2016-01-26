# -*- coding: utf-8 -*-
from PyQt4.QtGui import QFileDialog, QDialog, QAction, QIcon
from qgis.core import QgsMapLayerRegistry, QgsMapLayer

from resources_rc import *

class qlrLoader:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # Declare instance attributes
        self.actions = []
        self.menu = u'&qlrLoader'
        self.toolbar = self.iface.addToolBar(u'qlrLoader')
        self.toolbar.setObjectName(u'qlrLoader')

    def add_action(self, icon_path, text,  callback,
                   enabled_flag=True, add_to_menu=True, add_to_toolbar=True, parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        icon_path = ':/plugins/qlrLoader/icon.png'
        self.add_action(icon_path, text=u'Open een QLR File',
                        callback=self.run, parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(u'&qlrLoader', action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def run(self):
        dialog = QFileDialog(self.iface.mainWindow())
        dialog.setWindowTitle('Open qlr File')
        dialog.setNameFilter('QGIS layer File (*.qlr)')
        dialog.setFileMode(QFileDialog.ExistingFiles)

        if dialog.exec_() == QDialog.Accepted:
            self.loadQlrs( dialog.selectedFiles() )

    @staticmethod
    def loadQlrs(qlrList):
        for qlr in qlrList:
            lyrs = QgsMapLayer.fromLayerDefinitionFile(qlr)
            QgsMapLayerRegistry.instance().addMapLayers(lyrs)

