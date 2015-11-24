# -*- coding: utf-8 -*-
"""
/***************************************************************************
 qlrLoader
                                 A QGIS plugin
 QGIS laagbestand, QLR's inladen.
                             -------------------
        begin                : 2015-11-24
        copyright            : (C) 2015 by Kay Warrie
        email                : kaywarrie@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load qlrLoader class from file qlrLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .qlrLoader import qlrLoader
    return qlrLoader(iface)
