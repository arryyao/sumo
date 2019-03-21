#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2019 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot)

# go to shape mode
netedit.shapeMode()

# go to shape mode
netedit.changeShape("poiLane")

# create poiLane
netedit.leftClick(referencePosition, 150, 215)

# go to inspect mode
netedit.inspectMode()

# inspect first POILane
netedit.leftClick(referencePosition, 140, 215)

# Change boolean parameter block
netedit.modifyBoolAttribute(16, True)

# go to move mode
netedit.moveMode()

# try to move POI
netedit.moveElement(referencePosition, -20, 215, 200, 215)

# go to inspect mode
netedit.inspectMode()

# inspect first POILane
netedit.leftClick(referencePosition, 140, 215)

# Change boolean parameter block
netedit.modifyBoolAttribute(16, True)

# go to move mode
netedit.moveMode()

# now move POI
netedit.moveElement(referencePosition, -20, 215, 200, 215)

# Check undo redo
netedit.undo(referencePosition, 4)
netedit.redo(referencePosition, 4)

# save shapes
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)