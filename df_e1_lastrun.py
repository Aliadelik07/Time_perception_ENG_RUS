#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Mon Mar  8 12:26:13 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'df_e1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'condition': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rebeccalurie 1/Dropbox/grad/df/df_recallonly/df_e1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "consent"
consentClock = core.Clock()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
key_resp = keyboard.Keyboard()
ins = visual.TextStim(win=win, name='ins',
    text='We are interested to see how you experience art.\n\nWe have put together an assortment of art for you to view at your own pace.\n\nAfter you’ve seen all of the artwork, you will be tested to see how well you remember it. \n',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
con1 = visual.TextStim(win=win, name='con1',
    text='Press the spacebar to continue.',
    font='Open Sans',
    pos=(0, -0.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
if expInfo['condition'] == '1':
    grp = 'cv'
    thisExp.addData('condition', grp)
else:
    grp = 'vv'
    thisExp.addData('condition', grp)

import copy

all_rows = list(range(32))
shuffle(all_rows)

# Initialize components for Routine "b1_ins"
b1_insClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You will be viewing an assortment of artwork. For each piece of art, please take a photo. \n\nPress the spacebar when you are ready to move on to the next piece.\n\n\nPress the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "b1"
b1Clock = core.Clock()

# Initialize components for Routine "b2_ins"
b2_insClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will be viewing an assortment of artwork. \n\nPress the spacebar when you are ready to move on to the next piece.\n\n\nPress the spacebar to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "b2"
b2Clock = core.Clock()

# Initialize components for Routine "dist"
distClock = core.Clock()
key_resp_8 = keyboard.Keyboard()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='Press enter to continue to the next problem.',
    font='Open Sans',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test_ins"
test_insClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You will now be tested on the artwork that you saw earlier. \n\nOn the next screen, you will be asked to type all of the things that you remember seeing in the artwork shown to you earlier. \n\nPress the spacebar to continue to the test.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
textbox = visual.TextBox2(
     win, text=None, font='Open Sans',
     pos=(0, 0.5),     letterHeight=0.05,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='top-center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=True,
     name='textbox',
     autoLog=True,
)
button = visual.ButtonStim(win, 
   text="I'm Done", font='Open Sans',
   pos=(0, -0.8),
   letterHeight=0.05,
   size=(0.25, 0.1), borderWidth=0.0,
   fillColor='darkgrey', borderColor=None,
   color='black', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button')
button.buttonClock = core.Clock()
input = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Type your answers below. ',
    font='Open Sans',
    pos=(0, 0.8), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "debrief"
debriefClock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "consent"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
consentComponents = []
for thisComponent in consentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "consent"-------
while continueRoutine:
    # get current time
    t = consentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=consentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "consent"-------
for thisComponent in consentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "consent" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [key_resp, ins, con1]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ins* updates
    if ins.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ins.frameNStart = frameN  # exact frame index
        ins.tStart = t  # local t and not account for scr refresh
        ins.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ins, 'tStartRefresh')  # time at next scr refresh
        ins.setAutoDraw(True)
    
    # *con1* updates
    if con1.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        con1.frameNStart = frameN  # exact frame index
        con1.tStart = t  # local t and not account for scr refresh
        con1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(con1, 'tStartRefresh')  # time at next scr refresh
        con1.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ins.started', ins.tStartRefresh)
thisExp.addData('ins.stopped', ins.tStopRefresh)
thisExp.addData('con1.started', con1.tStartRefresh)
thisExp.addData('con1.stopped', con1.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "b1_ins"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
b1_insComponents = [text, key_resp_5]
for thisComponent in b1_insComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
b1_insClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "b1_ins"-------
while continueRoutine:
    # get current time
    t = b1_insClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=b1_insClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in b1_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "b1_ins"-------
for thisComponent in b1_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "b1_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection=all_rows[:16]),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "b1"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    b1Components = []
    for thisComponent in b1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    b1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "b1"-------
    while continueRoutine:
        # get current time
        t = b1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=b1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in b1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "b1"-------
    for thisComponent in b1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "b1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "b2_ins"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
b2_insComponents = [text_3, key_resp_6]
for thisComponent in b2_insComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
b2_insClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "b2_ins"-------
while continueRoutine:
    # get current time
    t = b2_insClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=b2_insClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in b2_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "b2_ins"-------
for thisComponent in b2_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "b2_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx', selection=all_rows[16:]),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "b2"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    b2Components = []
    for thisComponent in b2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    b2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "b2"-------
    while continueRoutine:
        # get current time
        t = b2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=b2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in b2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "b2"-------
    for thisComponent in b2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "b2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "dist"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    text_5.setText(distractQ)
    if trials_3.thisTrialN == 0:
        startTime = globalClock.getTime()
    # keep track of which components have finished
    distComponents = [key_resp_8, text_5, text_6]
    for thisComponent in distComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    distClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "dist"-------
    while continueRoutine:
        # get current time
        t = distClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=distClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['enter', 'return'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if globalClock.getTime() - startTime >= 30:
            trials_3.finished = True
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in distComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dist"-------
    for thisComponent in distComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    trials_3.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        trials_3.addData('key_resp_8.rt', key_resp_8.rt)
    trials_3.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    trials_3.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    trials_3.addData('text_5.started', text_5.tStartRefresh)
    trials_3.addData('text_5.stopped', text_5.tStopRefresh)
    trials_3.addData('text_6.started', text_6.tStartRefresh)
    trials_3.addData('text_6.stopped', text_6.tStopRefresh)
    # the Routine "dist" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "test_ins"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
test_insComponents = [text_2, key_resp_3]
for thisComponent in test_insComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
test_insClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test_ins"-------
while continueRoutine:
    # get current time
    t = test_insClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=test_insClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test_insComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test_ins"-------
for thisComponent in test_insComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "test_ins" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test"-------
continueRoutine = True
# update component parameters for each repeat
textbox.setText('')
input.keys = []
input.rt = []
_input_allKeys = []
# keep track of which components have finished
testComponents = [textbox, button, input, text_4]
for thisComponent in testComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "test"-------
while continueRoutine:
    # get current time
    t = testClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textbox* updates
    if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textbox.frameNStart = frameN  # exact frame index
        textbox.tStart = t  # local t and not account for scr refresh
        textbox.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
        textbox.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    
    # *input* updates
    waitOnFlip = False
    if input.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        input.frameNStart = frameN  # exact frame index
        input.tStart = t  # local t and not account for scr refresh
        input.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(input, 'tStartRefresh')  # time at next scr refresh
        input.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(input.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(input.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if input.status == STARTED and not waitOnFlip:
        theseKeys = input.getKeys(keyList=None, waitRelease=False)
        _input_allKeys.extend(theseKeys)
        if len(_input_allKeys):
            input.keys = _input_allKeys[-1].name  # just the last key pressed
            input.rt = _input_allKeys[-1].rt
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test"-------
for thisComponent in testComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textbox.text',textbox.text)
textbox.reset()
thisExp.addData('textbox.started', textbox.tStartRefresh)
thisExp.addData('textbox.stopped', textbox.tStopRefresh)
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn)
   thisExp.addData('button.timesOff', button.timesOff)
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
# check responses
if input.keys in ['', [], None]:  # No response was made
    input.keys = None
thisExp.addData('input.keys',input.keys)
if input.keys != None:  # we had a response
    thisExp.addData('input.rt', input.rt)
thisExp.addData('input.started', input.tStartRefresh)
thisExp.addData('input.stopped', input.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# the Routine "test" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "debrief"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
debriefComponents = []
for thisComponent in debriefComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
debriefClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "debrief"-------
while continueRoutine:
    # get current time
    t = debriefClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=debriefClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in debriefComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "debrief"-------
for thisComponent in debriefComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "debrief" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
