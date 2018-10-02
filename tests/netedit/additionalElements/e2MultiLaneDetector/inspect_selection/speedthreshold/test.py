#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
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
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# recompute
netedit.rebuildNetwork()

# go to additional mode
netedit.additionalMode()

# select E2
netedit.changeAdditional("e2MultilaneDetector")

# create E2 with default parameters
netedit.leftClick(referencePosition, 190, 240)
netedit.leftClick(referencePosition, 440, 240)
netedit.typeEnter()

# create second E2
netedit.leftClick(referencePosition, 440, 210)
netedit.leftClick(referencePosition, 190, 210)
netedit.typeEnter()

# go to select mode mode
netedit.selectMode()

#inspect E2 multilanes
netedit.leftClick(referencePosition, 320, 210)
netedit.leftClick(referencePosition, 320, 240)

# go to additional mode
netedit.inspectMode()

#inspect selection
netedit.leftClick(referencePosition, 320, 240)

# Change parameter 5 with a non valid value
netedit.modifyAttribute(5, "dummySpeedTreshold")

# Change parameter 5 with a non valid value
netedit.modifyAttribute(5, "-12.1")

# Change parameter 5 with a valid value
netedit.modifyAttribute(5, "6.3")

# Check undo redo
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
