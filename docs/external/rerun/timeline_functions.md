---
source: https://ref.rerun.io/docs/python/stable/common/timeline_functions
title: Timeline functions
---

# Timeline functions



### rerun



#### defset_time(timeline,*,recording=None,sequence=None,duration=None,timestamp=None)



Set the current time of a timeline for this thread.



Used for all subsequent logging on the same thread, until the next call to
rerun.set_time, rerun.reset_time or rerun.disable_timeline.



For example: `set_time("frame_nr", sequence=frame_nr)`.



There is no requirement of monotonicity. You can move the time backwards if you like.



You are expected to set exactly ONE of the arguments `sequence`, `duration`, or `timestamp`.
You may NOT change the type of a timeline, so if you use `duration` for a specific timeline,
you must only use `duration` for that timeline going forward.



The columnar equivalent to this function is [rerun.TimeColumn](../columnar_api/#rerun.TimeColumn).



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The name of the timeline to set the time for.TYPE:str |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording (if there is one). See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |
| sequence | Used for sequential indices, likeframe_nr. Must be an integer.TYPE:int\| NoneDEFAULT:None |
| duration | Used for relative times, liketime_since_start. Must either be in seconds, adatetime.timedelta, ornumpy.timedelta64. For nanosecond precision, usenumpy.timedelta64(nanoseconds, 'ns').TYPE:int\|float\|timedelta\|timedelta64\| NoneDEFAULT:None |
| timestamp | Used for absolute time indices, likecapture_time. Must either be in seconds since Unix epoch, adatetime.datetime, ornumpy.datetime64. For nanosecond precision, usenumpy.datetime64(nanoseconds, 'ns').TYPE:int\|float\|datetime\|datetime64\|TimestampScalar\| NoneDEFAULT:None |



#### defdisable_timeline(timeline,recording=None)



Clear time information for the specified timeline on this thread.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The name of the timeline to clear the time for.TYPE:str |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### defreset_time(recording=None)



Clear all timeline information on this thread.



This is the same as calling `disable_timeline` for all of the active timelines.



Used for all subsequent logging on the same thread,
until the next call to rerun.set_time.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |