/************************************* 
 * Time_Perception_2Phases_Enru Test *
 *************************************/

import { PsychoJS } from './lib/core-2021.1.3.js';
import * as core from './lib/core-2021.1.3.js';
import { TrialHandler } from './lib/data-2021.1.3.js';
import { Scheduler } from './lib/util-2021.1.3.js';
import * as visual from './lib/visual-2021.1.3.js';
import * as sound from './lib/sound-2021.1.3.js';
import * as util from './lib/util-2021.1.3.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'time_perception_2Phases_ENRU';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(Choose_LanguageRoutineBegin());
flowScheduler.add(Choose_LanguageRoutineEachFrame());
flowScheduler.add(Choose_LanguageRoutineEnd());
flowScheduler.add(welcomeScreenRoutineBegin());
flowScheduler.add(welcomeScreenRoutineEachFrame());
flowScheduler.add(welcomeScreenRoutineEnd());
const SecondPhaseLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(SecondPhaseLoopBegin, SecondPhaseLoopScheduler);
flowScheduler.add(SecondPhaseLoopScheduler);
flowScheduler.add(SecondPhaseLoopEnd);
flowScheduler.add(endScreenRoutineBegin());
flowScheduler.add(endScreenRoutineEachFrame());
flowScheduler.add(endScreenRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var Choose_LanguageClock;
var CH_Language;
var Lang_Select;
var welcomeScreenClock;
var welcomeText;
var welcomeResp;
var Random_SequenceClock;
var firstIntervalClock;
var firstImg;
var blackScreen1Clock;
var blackImg1;
var secondIntervalClock;
var secondImg;
var blackScreen2Clock;
var blackImg2;
var responseScreenClock;
var responseImg;
var choice;
var blackScreen3Clock;
var responseText;
var responseRepeat;
var SecondPhase_WelcomeClock;
var text;
var key_resp;
var endScreenClock;
var endText;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Choose_Language"
  Choose_LanguageClock = new util.Clock();
  CH_Language = new visual.TextStim({
    win: psychoJS.window,
    name: 'CH_Language',
    text: 'Выберите удобный язык инструкций.\nChoose the interface language.\n\nРУССКИЙ\nнажмите "1"\n\nENGLISH\npress "2"',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  Lang_Select = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "welcomeScreen"
  welcomeScreenClock = new util.Clock();
  welcomeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.03,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  welcomeResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Random_Sequence"
  Random_SequenceClock = new util.Clock();
  // Initialize components for Routine "firstInterval"
  firstIntervalClock = new util.Clock();
  firstImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'firstImg', units : undefined, 
    image : 'img/stim.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "blackScreen1"
  blackScreen1Clock = new util.Clock();
  blackImg1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blackImg1', units : undefined, 
    image : 'img/black.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "secondInterval"
  secondIntervalClock = new util.Clock();
  secondImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'secondImg', units : undefined, 
    image : 'img/stim.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "blackScreen2"
  blackScreen2Clock = new util.Clock();
  blackImg2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'blackImg2', units : undefined, 
    image : 'img/black.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [2, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "responseScreen"
  responseScreenClock = new util.Clock();
  responseImg = new visual.ImageStim({
    win : psychoJS.window,
    name : 'responseImg', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  choice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blackScreen3"
  blackScreen3Clock = new util.Clock();
  responseText = new visual.TextStim({
    win: psychoJS.window,
    name: 'responseText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  responseRepeat = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SecondPhase_Welcome"
  SecondPhase_WelcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "endScreen"
  endScreenClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _Lang_Select_allKeys;
var Choose_LanguageComponents;
function Choose_LanguageRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Choose_Language'-------
    t = 0;
    Choose_LanguageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Lang_Select.keys = undefined;
    Lang_Select.rt = undefined;
    _Lang_Select_allKeys = [];
    // keep track of which components have finished
    Choose_LanguageComponents = [];
    Choose_LanguageComponents.push(CH_Language);
    Choose_LanguageComponents.push(Lang_Select);
    
    for (const thisComponent of Choose_LanguageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Choose_LanguageRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Choose_Language'-------
    // get current time
    t = Choose_LanguageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *CH_Language* updates
    if (t >= 0.0 && CH_Language.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CH_Language.tStart = t;  // (not accounting for frame time here)
      CH_Language.frameNStart = frameN;  // exact frame index
      
      CH_Language.setAutoDraw(true);
    }

    
    // *Lang_Select* updates
    if (t >= 0.0 && Lang_Select.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Lang_Select.tStart = t;  // (not accounting for frame time here)
      Lang_Select.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Lang_Select.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Lang_Select.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Lang_Select.clearEvents(); });
    }

    if (Lang_Select.status === PsychoJS.Status.STARTED) {
      let theseKeys = Lang_Select.getKeys({keyList: ['1', '2'], waitRelease: false});
      _Lang_Select_allKeys = _Lang_Select_allKeys.concat(theseKeys);
      if (_Lang_Select_allKeys.length > 0) {
        Lang_Select.keys = _Lang_Select_allKeys[_Lang_Select_allKeys.length - 1].name;  // just the last key pressed
        Lang_Select.rt = _Lang_Select_allKeys[_Lang_Select_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Choose_LanguageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Choose_LanguageRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Choose_Language'-------
    for (const thisComponent of Choose_LanguageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Lang_Select.keys', Lang_Select.keys);
    if (typeof Lang_Select.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Lang_Select.rt', Lang_Select.rt);
        routineTimer.reset();
        }
    
    Lang_Select.stop();
    // the Routine "Choose_Language" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _welcomeResp_allKeys;
var welcomeScreenComponents;
function welcomeScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'welcomeScreen'-------
    t = 0;
    welcomeScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcomeText.setText(WelcomeText);
    welcomeResp.keys = undefined;
    welcomeResp.rt = undefined;
    _welcomeResp_allKeys = [];
    // keep track of which components have finished
    welcomeScreenComponents = [];
    welcomeScreenComponents.push(welcomeText);
    welcomeScreenComponents.push(welcomeResp);
    
    for (const thisComponent of welcomeScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function welcomeScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'welcomeScreen'-------
    // get current time
    t = welcomeScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeText* updates
    if (t >= 0.0 && welcomeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeText.tStart = t;  // (not accounting for frame time here)
      welcomeText.frameNStart = frameN;  // exact frame index
      
      welcomeText.setAutoDraw(true);
    }

    
    // *welcomeResp* updates
    if (t >= 0.0 && welcomeResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeResp.tStart = t;  // (not accounting for frame time here)
      welcomeResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcomeResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcomeResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcomeResp.clearEvents(); });
    }

    if (welcomeResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcomeResp.getKeys({keyList: ['space'], waitRelease: false});
      _welcomeResp_allKeys = _welcomeResp_allKeys.concat(theseKeys);
      if (_welcomeResp_allKeys.length > 0) {
        welcomeResp.keys = _welcomeResp_allKeys[_welcomeResp_allKeys.length - 1].name;  // just the last key pressed
        welcomeResp.rt = _welcomeResp_allKeys[_welcomeResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of welcomeScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'welcomeScreen'-------
    for (const thisComponent of welcomeScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('welcomeResp.keys', welcomeResp.keys);
    if (typeof welcomeResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcomeResp.rt', welcomeResp.rt);
        routineTimer.reset();
        }
    
    welcomeResp.stop();
    // the Routine "welcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var SecondPhase;
var currentLoop;
function SecondPhaseLoopBegin(SecondPhaseLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  SecondPhase = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1000, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'SecondPhase'
  });
  psychoJS.experiment.addLoop(SecondPhase); // add the loop to the experiment
  currentLoop = SecondPhase;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisSecondPhase of SecondPhase) {
    const snapshot = SecondPhase.getSnapshot();
    SecondPhaseLoopScheduler.add(importConditions(snapshot));
    const time_durationsLoopScheduler = new Scheduler(psychoJS);
    SecondPhaseLoopScheduler.add(time_durationsLoopBegin, time_durationsLoopScheduler);
    SecondPhaseLoopScheduler.add(time_durationsLoopScheduler);
    SecondPhaseLoopScheduler.add(time_durationsLoopEnd);
    SecondPhaseLoopScheduler.add(SecondPhase_WelcomeRoutineBegin(snapshot));
    SecondPhaseLoopScheduler.add(SecondPhase_WelcomeRoutineEachFrame(snapshot));
    SecondPhaseLoopScheduler.add(SecondPhase_WelcomeRoutineEnd(snapshot));
    SecondPhaseLoopScheduler.add(endLoopIteration(SecondPhaseLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var time_durations;
function time_durationsLoopBegin(time_durationsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  time_durations = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1000, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'time_durations'
  });
  psychoJS.experiment.addLoop(time_durations); // add the loop to the experiment
  currentLoop = time_durations;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTime_duration of time_durations) {
    const snapshot = time_durations.getSnapshot();
    time_durationsLoopScheduler.add(importConditions(snapshot));
    time_durationsLoopScheduler.add(Random_SequenceRoutineBegin(snapshot));
    time_durationsLoopScheduler.add(Random_SequenceRoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(Random_SequenceRoutineEnd(snapshot));
    time_durationsLoopScheduler.add(firstIntervalRoutineBegin(snapshot));
    time_durationsLoopScheduler.add(firstIntervalRoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(firstIntervalRoutineEnd(snapshot));
    time_durationsLoopScheduler.add(blackScreen1RoutineBegin(snapshot));
    time_durationsLoopScheduler.add(blackScreen1RoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(blackScreen1RoutineEnd(snapshot));
    time_durationsLoopScheduler.add(secondIntervalRoutineBegin(snapshot));
    time_durationsLoopScheduler.add(secondIntervalRoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(secondIntervalRoutineEnd(snapshot));
    time_durationsLoopScheduler.add(blackScreen2RoutineBegin(snapshot));
    time_durationsLoopScheduler.add(blackScreen2RoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(blackScreen2RoutineEnd(snapshot));
    time_durationsLoopScheduler.add(responseScreenRoutineBegin(snapshot));
    time_durationsLoopScheduler.add(responseScreenRoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(responseScreenRoutineEnd(snapshot));
    time_durationsLoopScheduler.add(blackScreen3RoutineBegin(snapshot));
    time_durationsLoopScheduler.add(blackScreen3RoutineEachFrame(snapshot));
    time_durationsLoopScheduler.add(blackScreen3RoutineEnd(snapshot));
    time_durationsLoopScheduler.add(endLoopIteration(time_durationsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function time_durationsLoopEnd() {
  psychoJS.experiment.removeLoop(time_durations);

  return Scheduler.Event.NEXT;
}


function SecondPhaseLoopEnd() {
  psychoJS.experiment.removeLoop(SecondPhase);

  return Scheduler.Event.NEXT;
}


var Random_SequenceComponents;
function Random_SequenceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Random_Sequence'-------
    t = 0;
    Random_SequenceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    Random_SequenceComponents = [];
    
    for (const thisComponent of Random_SequenceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Random_SequenceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Random_Sequence'-------
    // get current time
    t = Random_SequenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Random_SequenceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Random_SequenceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Random_Sequence'-------
    for (const thisComponent of Random_SequenceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Random_Sequence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var firstIntervalComponents;
function firstIntervalRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'firstInterval'-------
    t = 0;
    firstIntervalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    firstIntervalComponents = [];
    firstIntervalComponents.push(firstImg);
    
    for (const thisComponent of firstIntervalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function firstIntervalRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'firstInterval'-------
    // get current time
    t = firstIntervalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *firstImg* updates
    if (t >= 0.0 && firstImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      firstImg.tStart = t;  // (not accounting for frame time here)
      firstImg.frameNStart = frameN;  // exact frame index
      
      firstImg.setAutoDraw(true);
    }

    frameRemains = 0.0 + Time1[Seq] - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (firstImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      firstImg.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of firstIntervalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function firstIntervalRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'firstInterval'-------
    for (const thisComponent of firstIntervalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "firstInterval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blackScreen1Components;
function blackScreen1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'blackScreen1'-------
    t = 0;
    blackScreen1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.900000);
    // update component parameters for each repeat
    // keep track of which components have finished
    blackScreen1Components = [];
    blackScreen1Components.push(blackImg1);
    
    for (const thisComponent of blackScreen1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blackScreen1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'blackScreen1'-------
    // get current time
    t = blackScreen1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackImg1* updates
    if (t >= 0.0 && blackImg1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackImg1.tStart = t;  // (not accounting for frame time here)
      blackImg1.frameNStart = frameN;  // exact frame index
      
      blackImg1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blackImg1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blackImg1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blackScreen1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blackScreen1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'blackScreen1'-------
    for (const thisComponent of blackScreen1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var secondIntervalComponents;
function secondIntervalRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'secondInterval'-------
    t = 0;
    secondIntervalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    secondIntervalComponents = [];
    secondIntervalComponents.push(secondImg);
    
    for (const thisComponent of secondIntervalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function secondIntervalRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'secondInterval'-------
    // get current time
    t = secondIntervalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *secondImg* updates
    if (t >= 0.0 && secondImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      secondImg.tStart = t;  // (not accounting for frame time here)
      secondImg.frameNStart = frameN;  // exact frame index
      
      secondImg.setAutoDraw(true);
    }

    frameRemains = 0.0 + Time2[Seq] - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (secondImg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      secondImg.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of secondIntervalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function secondIntervalRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'secondInterval'-------
    for (const thisComponent of secondIntervalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "secondInterval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var blackScreen2Components;
function blackScreen2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'blackScreen2'-------
    t = 0;
    blackScreen2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.900000);
    // update component parameters for each repeat
    // keep track of which components have finished
    blackScreen2Components = [];
    blackScreen2Components.push(blackImg2);
    
    for (const thisComponent of blackScreen2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blackScreen2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'blackScreen2'-------
    // get current time
    t = blackScreen2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blackImg2* updates
    if (t >= 0.0 && blackImg2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blackImg2.tStart = t;  // (not accounting for frame time here)
      blackImg2.frameNStart = frameN;  // exact frame index
      
      blackImg2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blackImg2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blackImg2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blackScreen2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blackScreen2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'blackScreen2'-------
    for (const thisComponent of blackScreen2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _choice_allKeys;
var responseScreenComponents;
function responseScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'responseScreen'-------
    t = 0;
    responseScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    responseImg.setImage(RespImage);
    choice.keys = undefined;
    choice.rt = undefined;
    _choice_allKeys = [];
    // keep track of which components have finished
    responseScreenComponents = [];
    responseScreenComponents.push(responseImg);
    responseScreenComponents.push(choice);
    
    for (const thisComponent of responseScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function responseScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'responseScreen'-------
    // get current time
    t = responseScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *responseImg* updates
    if (t >= 0.0 && responseImg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseImg.tStart = t;  // (not accounting for frame time here)
      responseImg.frameNStart = frameN;  // exact frame index
      
      responseImg.setAutoDraw(true);
    }

    
    // *choice* updates
    if (t >= 0.0 && choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      choice.tStart = t;  // (not accounting for frame time here)
      choice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { choice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { choice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { choice.clearEvents(); });
    }

    if (choice.status === PsychoJS.Status.STARTED) {
      let theseKeys = choice.getKeys({keyList: ['1', '2'], waitRelease: false});
      _choice_allKeys = _choice_allKeys.concat(theseKeys);
      if (_choice_allKeys.length > 0) {
        choice.keys = _choice_allKeys[_choice_allKeys.length - 1].name;  // just the last key pressed
        choice.rt = _choice_allKeys[_choice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of responseScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function responseScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'responseScreen'-------
    for (const thisComponent of responseScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('choice.keys', choice.keys);
    if (typeof choice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('choice.rt', choice.rt);
        routineTimer.reset();
        }
    
    choice.stop();
    // the Routine "responseScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _responseRepeat_allKeys;
var blackScreen3Components;
function blackScreen3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'blackScreen3'-------
    t = 0;
    blackScreen3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    responseText.setText(PressSpace);
    responseRepeat.keys = undefined;
    responseRepeat.rt = undefined;
    _responseRepeat_allKeys = [];
    // keep track of which components have finished
    blackScreen3Components = [];
    blackScreen3Components.push(responseText);
    blackScreen3Components.push(responseRepeat);
    
    for (const thisComponent of blackScreen3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function blackScreen3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'blackScreen3'-------
    // get current time
    t = blackScreen3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *responseText* updates
    if (t >= 0.0 && responseText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseText.tStart = t;  // (not accounting for frame time here)
      responseText.frameNStart = frameN;  // exact frame index
      
      responseText.setAutoDraw(true);
    }

    
    // *responseRepeat* updates
    if (t >= 0.0 && responseRepeat.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseRepeat.tStart = t;  // (not accounting for frame time here)
      responseRepeat.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { responseRepeat.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { responseRepeat.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { responseRepeat.clearEvents(); });
    }

    if (responseRepeat.status === PsychoJS.Status.STARTED) {
      let theseKeys = responseRepeat.getKeys({keyList: ['space'], waitRelease: false});
      _responseRepeat_allKeys = _responseRepeat_allKeys.concat(theseKeys);
      if (_responseRepeat_allKeys.length > 0) {
        responseRepeat.keys = _responseRepeat_allKeys[_responseRepeat_allKeys.length - 1].name;  // just the last key pressed
        responseRepeat.rt = _responseRepeat_allKeys[_responseRepeat_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blackScreen3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blackScreen3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'blackScreen3'-------
    for (const thisComponent of blackScreen3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('responseRepeat.keys', responseRepeat.keys);
    if (typeof responseRepeat.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('responseRepeat.rt', responseRepeat.rt);
        routineTimer.reset();
        }
    
    responseRepeat.stop();
    /* Syntax Error: Fix Python code */
    // the Routine "blackScreen3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var SecondPhase_WelcomeComponents;
function SecondPhase_WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'SecondPhase_Welcome'-------
    t = 0;
    SecondPhase_WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    text.setText(TextSecond);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    SecondPhase_WelcomeComponents = [];
    SecondPhase_WelcomeComponents.push(text);
    SecondPhase_WelcomeComponents.push(key_resp);
    
    for (const thisComponent of SecondPhase_WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SecondPhase_WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'SecondPhase_Welcome'-------
    // get current time
    t = SecondPhase_WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of SecondPhase_WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SecondPhase_WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'SecondPhase_Welcome'-------
    for (const thisComponent of SecondPhase_WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "SecondPhase_Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var endScreenComponents;
function endScreenRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'endScreen'-------
    t = 0;
    endScreenClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    endText.setText(ThankYou);
    // keep track of which components have finished
    endScreenComponents = [];
    endScreenComponents.push(endText);
    
    for (const thisComponent of endScreenComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function endScreenRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'endScreen'-------
    // get current time
    t = endScreenClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (endText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      endText.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of endScreenComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endScreenRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'endScreen'-------
    for (const thisComponent of endScreenComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
