#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.2),
    on Март 22, 2021, at 16:18
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

WelcomeText = ""
RespImage = " "
PressSpace = " "
ThankYou = " "
TextSecond = ""


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.2'
expName = 'time_perception_2Phases_ENRU'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='Z:\\temp\\time_perception2\\time_perception_2Phases_ENRU_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Choose_Language"
Choose_LanguageClock = core.Clock()
CH_Language = visual.TextStim(win=win, name='CH_Language',
    text='Выберите удобный язык инструкций.\nChoose the interface language.\n\nРУССКИЙ\nнажмите "1"\n\nENGLISH\npress "2"',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
Lang_Select = keyboard.Keyboard()
WelcomeRUS = "Здравствуйте!\n\nВаша задача сравнить длительности последовательно предъявляемых двух звездочек и указать какая из них была на экране больше времени:\n\nпервая (нажать клавишу 1) или вторая (нажать клавишу 2).\n\nВо время выполнения задания мы просим Вас отложить все другие дела и полагаться на Ваше внутреннее чувство времени, не пользоваться часами и не считать про себя.\n\n Нажмите клавишу 'Пробел' для начала эксперимента."
WelcomeENG = "Hello!\n\nYour task is to compare durations of two successively presented asterisks and indicate, which is longer in duration:\n\nthe first one (press button 1) or the second one (press button 2).\n\nPlease withdraw from any other activity during the task performance and rely on your inner sense of time. Try NOT to count or implement similar strategis (hand/foot tapping).\n\n\n Press 'Space' to start the experiment."

# Initialize components for Routine "welcomeScreen"
welcomeScreenClock = core.Clock()
welcomeText = visual.TextStim(win=win, name='welcomeText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
welcomeResp = keyboard.Keyboard()

# Initialize components for Routine "Random_Sequence"
Random_SequenceClock = core.Clock()

# Initialize components for Routine "firstInterval"
firstIntervalClock = core.Clock()
firstImg = visual.ImageStim(
    win=win,
    name='firstImg', 
    image='img/stim.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blackScreen1"
blackScreen1Clock = core.Clock()
blackImg1 = visual.ImageStim(
    win=win,
    name='blackImg1', 
    image='img/black.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "secondInterval"
secondIntervalClock = core.Clock()
secondImg = visual.ImageStim(
    win=win,
    name='secondImg', 
    image='img/stim.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blackScreen2"
blackScreen2Clock = core.Clock()
blackImg2 = visual.ImageStim(
    win=win,
    name='blackImg2', 
    image='img/black.png', mask=None,
    ori=0, pos=(0, 0), size=(2, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "responseScreen"
responseScreenClock = core.Clock()
responseImg = visual.ImageStim(
    win=win,
    name='responseImg', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
choice = keyboard.Keyboard()

# Initialize components for Routine "blackScreen3"
blackScreen3Clock = core.Clock()
responseText = visual.TextStim(win=win, name='responseText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
responseRepeat = keyboard.Keyboard()
Time1 = [5.6,4.0]
Time2 = [4.0,5.6]
Seq = 0 #Current sequence. For Seq = 0 -> Sequence starts from 5.6. For Seq = 1 -> Sequence starts from 4.0. 
TimeDurationExp = Time1[0]+Time2[0]

StepsMAX = 6
Steps = [0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4,0.4]
Bends = [[],[]]

status = ['down','up']
StepsCount = [0,0]
Experiment_Round = 1

# Initialize components for Routine "SecondPhase_Welcome"
SecondPhase_WelcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Choose_Language"-------
continueRoutine = True
# update component parameters for each repeat
Lang_Select.keys = []
Lang_Select.rt = []
_Lang_Select_allKeys = []
# keep track of which components have finished
Choose_LanguageComponents = [CH_Language, Lang_Select]
for thisComponent in Choose_LanguageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Choose_LanguageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Choose_Language"-------
while continueRoutine:
    # get current time
    t = Choose_LanguageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Choose_LanguageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *CH_Language* updates
    if CH_Language.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CH_Language.frameNStart = frameN  # exact frame index
        CH_Language.tStart = t  # local t and not account for scr refresh
        CH_Language.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CH_Language, 'tStartRefresh')  # time at next scr refresh
        CH_Language.setAutoDraw(True)
    
    # *Lang_Select* updates
    waitOnFlip = False
    if Lang_Select.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Lang_Select.frameNStart = frameN  # exact frame index
        Lang_Select.tStart = t  # local t and not account for scr refresh
        Lang_Select.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Lang_Select, 'tStartRefresh')  # time at next scr refresh
        Lang_Select.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Lang_Select.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Lang_Select.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Lang_Select.status == STARTED and not waitOnFlip:
        theseKeys = Lang_Select.getKeys(keyList=['1', '2'], waitRelease=False)
        _Lang_Select_allKeys.extend(theseKeys)
        if len(_Lang_Select_allKeys):
            Lang_Select.keys = _Lang_Select_allKeys[-1].name  # just the last key pressed
            Lang_Select.rt = _Lang_Select_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Choose_LanguageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Choose_Language"-------
for thisComponent in Choose_LanguageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('CH_Language.started', CH_Language.tStartRefresh)
thisExp.addData('CH_Language.stopped', CH_Language.tStopRefresh)
# check responses
if Lang_Select.keys in ['', [], None]:  # No response was made
    Lang_Select.keys = None
thisExp.addData('Lang_Select.keys',Lang_Select.keys)
if Lang_Select.keys != None:  # we had a response
    thisExp.addData('Lang_Select.rt', Lang_Select.rt)
thisExp.nextEntry()
if Lang_Select.keys == '1': 
    WelcomeText = WelcomeRUS
    RespImage = 'img"\\"resp_longer_rus.png'
    RespImage = RespImage.replace('"','')
    PressSpace = "Нажмите 'Пробел' для продолжения."
    ThankYou = "Спасибо большое за участие!"
else: 
    WelcomeText = WelcomeENG
    RespImage = 'img"\\"resp_longer.png'
    RespImage = RespImage.replace('"','')
    PressSpace = "Press SPACE to initiate a new trial"
    ThankYou = "Thank you!"
# the Routine "Choose_Language" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcomeScreen"-------
continueRoutine = True
# update component parameters for each repeat
welcomeText.setText(WelcomeText)
welcomeResp.keys = []
welcomeResp.rt = []
_welcomeResp_allKeys = []
# keep track of which components have finished
welcomeScreenComponents = [welcomeText, welcomeResp]
for thisComponent in welcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcomeScreen"-------
while continueRoutine:
    # get current time
    t = welcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText* updates
    if welcomeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText.frameNStart = frameN  # exact frame index
        welcomeText.tStart = t  # local t and not account for scr refresh
        welcomeText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText, 'tStartRefresh')  # time at next scr refresh
        welcomeText.setAutoDraw(True)
    
    # *welcomeResp* updates
    waitOnFlip = False
    if welcomeResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeResp.frameNStart = frameN  # exact frame index
        welcomeResp.tStart = t  # local t and not account for scr refresh
        welcomeResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeResp, 'tStartRefresh')  # time at next scr refresh
        welcomeResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(welcomeResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(welcomeResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if welcomeResp.status == STARTED and not waitOnFlip:
        theseKeys = welcomeResp.getKeys(keyList=['space'], waitRelease=False)
        _welcomeResp_allKeys.extend(theseKeys)
        if len(_welcomeResp_allKeys):
            welcomeResp.keys = _welcomeResp_allKeys[-1].name  # just the last key pressed
            welcomeResp.rt = _welcomeResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcomeScreen"-------
for thisComponent in welcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if welcomeResp.keys in ['', [], None]:  # No response was made
    welcomeResp.keys = None
thisExp.addData('welcomeResp.keys',welcomeResp.keys)
if welcomeResp.keys != None:  # we had a response
    thisExp.addData('welcomeResp.rt', welcomeResp.rt)
thisExp.nextEntry()
# the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SecondPhase = data.TrialHandler(nReps=1000.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='SecondPhase')
thisExp.addLoop(SecondPhase)  # add the loop to the experiment
thisSecondPhase = SecondPhase.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSecondPhase.rgb)
if thisSecondPhase != None:
    for paramName in thisSecondPhase:
        exec('{} = thisSecondPhase[paramName]'.format(paramName))

for thisSecondPhase in SecondPhase:
    currentLoop = SecondPhase
    # abbreviate parameter names if possible (e.g. rgb = thisSecondPhase.rgb)
    if thisSecondPhase != None:
        for paramName in thisSecondPhase:
            exec('{} = thisSecondPhase[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    time_durations = data.TrialHandler(nReps=1000, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='time_durations')
    thisExp.addLoop(time_durations)  # add the loop to the experiment
    thisTime_duration = time_durations.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTime_duration.rgb)
    if thisTime_duration != None:
        for paramName in thisTime_duration:
            exec('{} = thisTime_duration[paramName]'.format(paramName))
    
    for thisTime_duration in time_durations:
        currentLoop = time_durations
        # abbreviate parameter names if possible (e.g. rgb = thisTime_duration.rgb)
        if thisTime_duration != None:
            for paramName in thisTime_duration:
                exec('{} = thisTime_duration[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Random_Sequence"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Choosing randomly one of two sequences
        if random() <= 0.5: 
            Seq = 0
            if StepsCount[Seq]>5: Seq = 1
        else:
            Seq = 1
            if StepsCount[Seq]>5: Seq = 0
        # keep track of which components have finished
        Random_SequenceComponents = []
        for thisComponent in Random_SequenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Random_SequenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Random_Sequence"-------
        while continueRoutine:
            # get current time
            t = Random_SequenceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Random_SequenceClock)
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
            for thisComponent in Random_SequenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Random_Sequence"-------
        for thisComponent in Random_SequenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Random_Sequence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "firstInterval"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        firstIntervalComponents = [firstImg]
        for thisComponent in firstIntervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        firstIntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "firstInterval"-------
        while continueRoutine:
            # get current time
            t = firstIntervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=firstIntervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *firstImg* updates
            if firstImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                firstImg.frameNStart = frameN  # exact frame index
                firstImg.tStart = t  # local t and not account for scr refresh
                firstImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(firstImg, 'tStartRefresh')  # time at next scr refresh
                firstImg.setAutoDraw(True)
            if firstImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > firstImg.tStartRefresh + Time1[Seq]-frameTolerance:
                    # keep track of stop time/frame for later
                    firstImg.tStop = t  # not accounting for scr refresh
                    firstImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(firstImg, 'tStopRefresh')  # time at next scr refresh
                    firstImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in firstIntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "firstInterval"-------
        for thisComponent in firstIntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        time_durations.addData('firstImg.started', firstImg.tStartRefresh)
        time_durations.addData('firstImg.stopped', firstImg.tStopRefresh)
        # the Routine "firstInterval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blackScreen1"-------
        continueRoutine = True
        routineTimer.add(0.900000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blackScreen1Components = [blackImg1]
        for thisComponent in blackScreen1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blackScreen1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blackScreen1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blackScreen1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blackScreen1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackImg1* updates
            if blackImg1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackImg1.frameNStart = frameN  # exact frame index
                blackImg1.tStart = t  # local t and not account for scr refresh
                blackImg1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackImg1, 'tStartRefresh')  # time at next scr refresh
                blackImg1.setAutoDraw(True)
            if blackImg1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackImg1.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    blackImg1.tStop = t  # not accounting for scr refresh
                    blackImg1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackImg1, 'tStopRefresh')  # time at next scr refresh
                    blackImg1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blackScreen1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blackScreen1"-------
        for thisComponent in blackScreen1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "secondInterval"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        secondIntervalComponents = [secondImg]
        for thisComponent in secondIntervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        secondIntervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "secondInterval"-------
        while continueRoutine:
            # get current time
            t = secondIntervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=secondIntervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *secondImg* updates
            if secondImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                secondImg.frameNStart = frameN  # exact frame index
                secondImg.tStart = t  # local t and not account for scr refresh
                secondImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(secondImg, 'tStartRefresh')  # time at next scr refresh
                secondImg.setAutoDraw(True)
            if secondImg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > secondImg.tStartRefresh + Time2[Seq]-frameTolerance:
                    # keep track of stop time/frame for later
                    secondImg.tStop = t  # not accounting for scr refresh
                    secondImg.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(secondImg, 'tStopRefresh')  # time at next scr refresh
                    secondImg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in secondIntervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "secondInterval"-------
        for thisComponent in secondIntervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        time_durations.addData('secondImg.started', secondImg.tStartRefresh)
        time_durations.addData('secondImg.stopped', secondImg.tStopRefresh)
        # the Routine "secondInterval" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blackScreen2"-------
        continueRoutine = True
        routineTimer.add(0.900000)
        # update component parameters for each repeat
        # keep track of which components have finished
        blackScreen2Components = [blackImg2]
        for thisComponent in blackScreen2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blackScreen2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blackScreen2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = blackScreen2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blackScreen2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blackImg2* updates
            if blackImg2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blackImg2.frameNStart = frameN  # exact frame index
                blackImg2.tStart = t  # local t and not account for scr refresh
                blackImg2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blackImg2, 'tStartRefresh')  # time at next scr refresh
                blackImg2.setAutoDraw(True)
            if blackImg2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blackImg2.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    blackImg2.tStop = t  # not accounting for scr refresh
                    blackImg2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blackImg2, 'tStopRefresh')  # time at next scr refresh
                    blackImg2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blackScreen2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blackScreen2"-------
        for thisComponent in blackScreen2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "responseScreen"-------
        continueRoutine = True
        # update component parameters for each repeat
        responseImg.setImage(RespImage)
        choice.keys = []
        choice.rt = []
        _choice_allKeys = []
        # keep track of which components have finished
        responseScreenComponents = [responseImg, choice]
        for thisComponent in responseScreenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        responseScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "responseScreen"-------
        while continueRoutine:
            # get current time
            t = responseScreenClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=responseScreenClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *responseImg* updates
            if responseImg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                responseImg.frameNStart = frameN  # exact frame index
                responseImg.tStart = t  # local t and not account for scr refresh
                responseImg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(responseImg, 'tStartRefresh')  # time at next scr refresh
                responseImg.setAutoDraw(True)
            
            # *choice* updates
            waitOnFlip = False
            if choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                choice.frameNStart = frameN  # exact frame index
                choice.tStart = t  # local t and not account for scr refresh
                choice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(choice, 'tStartRefresh')  # time at next scr refresh
                choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(choice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if choice.status == STARTED and not waitOnFlip:
                theseKeys = choice.getKeys(keyList=['1', '2'], waitRelease=False)
                _choice_allKeys.extend(theseKeys)
                if len(_choice_allKeys):
                    choice.keys = _choice_allKeys[-1].name  # just the last key pressed
                    choice.rt = _choice_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseScreenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "responseScreen"-------
        for thisComponent in responseScreenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if choice.keys in ['', [], None]:  # No response was made
            choice.keys = None
        time_durations.addData('choice.keys',choice.keys)
        if choice.keys != None:  # we had a response
            time_durations.addData('choice.rt', choice.rt)
        # the Routine "responseScreen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "blackScreen3"-------
        continueRoutine = True
        # update component parameters for each repeat
        responseText.setText(PressSpace)
        responseRepeat.keys = []
        responseRepeat.rt = []
        _responseRepeat_allKeys = []
        # keep track of which components have finished
        blackScreen3Components = [responseText, responseRepeat]
        for thisComponent in blackScreen3Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        blackScreen3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "blackScreen3"-------
        while continueRoutine:
            # get current time
            t = blackScreen3Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=blackScreen3Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *responseText* updates
            if responseText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                responseText.frameNStart = frameN  # exact frame index
                responseText.tStart = t  # local t and not account for scr refresh
                responseText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(responseText, 'tStartRefresh')  # time at next scr refresh
                responseText.setAutoDraw(True)
            
            # *responseRepeat* updates
            waitOnFlip = False
            if responseRepeat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                responseRepeat.frameNStart = frameN  # exact frame index
                responseRepeat.tStart = t  # local t and not account for scr refresh
                responseRepeat.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(responseRepeat, 'tStartRefresh')  # time at next scr refresh
                responseRepeat.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(responseRepeat.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(responseRepeat.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if responseRepeat.status == STARTED and not waitOnFlip:
                theseKeys = responseRepeat.getKeys(keyList=['space'], waitRelease=False)
                _responseRepeat_allKeys.extend(theseKeys)
                if len(_responseRepeat_allKeys):
                    responseRepeat.keys = _responseRepeat_allKeys[-1].name  # just the last key pressed
                    responseRepeat.rt = _responseRepeat_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blackScreen3Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blackScreen3"-------
        for thisComponent in blackScreen3Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if responseRepeat.keys in ['', [], None]:  # No response was made
            responseRepeat.keys = None
        time_durations.addData('responseRepeat.keys',responseRepeat.keys)
        if responseRepeat.keys != None:  # we had a response
            time_durations.addData('responseRepeat.rt', responseRepeat.rt)
        # First Step - Writing current Trial data
        thisExp.addData('t1',Time1[Seq])
        thisExp.addData('t2',Time2[Seq])
        if Seq == 0: thisExp.addData('sequence',56)
        if Seq == 1: thisExp.addData('sequence',40)
        
        thisExp.addData('Status',status[Seq])
        thisExp.addData('Step56',StepsCount[0])
        thisExp.addData('Step40',StepsCount[1])
        
        # Second Step - Changing timing accordingly for next Trial (in the seme sequence)
        # For Key='1' (t1 longer t2) we always make t1 smaller and t2 larger
        if (choice.keys == '1') and status[Seq] == 'down':
            Time1[Seq] -= Steps[StepsCount[Seq]]
            Time2[Seq] += Steps[StepsCount[Seq]]
        elif (choice.keys == '1') and status[Seq] == 'up':
            Time1[Seq] -= Steps[StepsCount[Seq]]
            Time2[Seq] += Steps[StepsCount[Seq]] 
            status[Seq] = 'down'
            if StepsCount[Seq] >2: Bends[Seq].append(Time1[Seq])
            StepsCount[Seq] += 1
            
        # For Key='2' (t2 longer t1) we always make t1 larger and t1 smaller
        if (choice.keys == '2') and status[Seq] == 'down':
            Time1[Seq] += Steps[StepsCount[Seq]]
            Time2[Seq] -= Steps[StepsCount[Seq]]
            status[Seq] = 'up'
            if StepsCount[Seq] >2: Bends[Seq].append(Time1[Seq])
            StepsCount[Seq] += 1
        elif (choice.keys == '2') and status[Seq] == 'up':
            Time1[Seq] += Steps[StepsCount[Seq]]
            Time2[Seq] -= Steps[StepsCount[Seq]] 
        
        # We check if both sequences has made max steps - then quit the experiment
        if StepsCount[0] >= StepsMAX and StepsCount[1] >= StepsMAX:
            mean1 = round(np.array(Bends[0]).mean(),1) 
            mean2 = round(np.array(Bends[1]).mean(),1)
            meanBoth = round((mean1+mean2)/2,1)
            thisExp.addData('MeanSeq1',mean1)
            thisExp.addData('MeanSeq2',mean2)
            thisExp.addData('MeanBoth',meanBoth)
            SecondStart = TimeDurationExp - meanBoth
            Time1 = [meanBoth+0.8,SecondStart-0.8]
            Time2 = [meanBoth-0.8,SecondStart+0.8]
            thisExp.addData('NewTime1_start', Time1[0])
            thisExp.addData('NewTime1_end',Time2[0])
            thisExp.addData('NewTime2_start', Time1[1])
            thisExp.addData('NewTime2_end',Time2[1])
            #thisExp.addData('MeanSeq1&2',np.array(Bends[1]+Bends[0]).mean())
            if Experiment_Round <= 1:
                Experiment_Round = 2
                StepsCount=[0,0]
                Bends = [[],[]]
                status = ['down','up']
                time_durations.finished=True
            else: 
                Experiment_Round = 3
                SecondPhase.finished=True
                time_durations.finished=True 
        # the Routine "blackScreen3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1000 repeats of 'time_durations'
    
    
    # ------Prepare to start Routine "SecondPhase_Welcome"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Experiment_Round <= 2:
        TextSecond = "Завершилась первая часть эксперимента.\nОсталось пройти вторую часть.\nНажмите клавишу 'Пробел' для начала."
    else:
        TextSecond = "Ваш эксперимент завершен! \n\nНажмите, пожалуйста, клавишу 'Пробел'."
    text.setText(TextSecond)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    SecondPhase_WelcomeComponents = [text, key_resp]
    for thisComponent in SecondPhase_WelcomeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    SecondPhase_WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "SecondPhase_Welcome"-------
    while continueRoutine:
        # get current time
        t = SecondPhase_WelcomeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=SecondPhase_WelcomeClock)
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
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SecondPhase_WelcomeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "SecondPhase_Welcome"-------
    for thisComponent in SecondPhase_WelcomeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    SecondPhase.addData('text.started', text.tStartRefresh)
    SecondPhase.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    SecondPhase.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        SecondPhase.addData('key_resp.rt', key_resp.rt)
    # the Routine "SecondPhase_Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1000.0 repeats of 'SecondPhase'


# ------Prepare to start Routine "endScreen"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
endText.setText(ThankYou)
# keep track of which components have finished
endScreenComponents = [endText]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    if endText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > endText.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            endText.tStop = t  # not accounting for scr refresh
            endText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(endText, 'tStopRefresh')  # time at next scr refresh
            endText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

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
