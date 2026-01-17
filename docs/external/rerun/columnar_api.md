---
source: https://ref.rerun.io/docs/python/stable/common/columnar_api
title: Columnar API
---

# Columnar API



### rerun



#### classTimeColumn



Bases: `TimeColumnLike`



A column of index (time) values.



Columnar equivalent to [rerun.set_time](../timeline_functions/#rerun.set_time).



##### def__init__(timeline,*,sequence=None,duration=None,timestamp=None)



Create a column of index values.



There is no requirement of monotonicity. You can move the time backwards if you like.



You are expected to set exactly ONE of the arguments `sequence`, `duration`, or `timestamp`.
You may NOT change the type of a timeline, so if you use `duration` for a specific timeline,
you must only use `duration` for that timeline going forward.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The name of the timeline.TYPE:str |
| sequence | Used for sequential indices, likeframe_nr. Must be integers.TYPE:Iterable[int] \| NoneDEFAULT:None |
| duration | Used for relative times, liketime_since_start. Must either be in seconds,datetime.timedelta, ornumpy.timedelta64.TYPE:Iterable[int] \|Iterable[float] \|Iterable[timedelta] \|Iterable[timedelta64] \| NoneDEFAULT:None |
| timestamp | Used for absolute time indices, likecapture_time. Must either be in seconds since Unix epoch,datetime.datetime, ornumpy.datetime64.TYPE:Iterable[int] \|Iterable[float] \|Iterable[datetime] \|Iterable[datetime64] \| NoneDEFAULT:None |



##### deftimeline_name()



Returns the name of the timeline.



#### defsend_columns(entity_path,indexes,columns,*,recording=None,strict=None)



Send columnar data to Rerun.



Unlike the regular `log` API, which is row-oriented, this API lets you submit the data
in a columnar form. Each `TimeColumnLike` and `ComponentColumn` object represents a column
of data that will be sent to Rerun. The lengths of all these columns must match, and all
data that shares the same index across the different columns will act as a single logical row,
equivalent to a single call to `rr.log()`.



Note that this API ignores any stateful time set on the log stream via [rerun.set_time](../timeline_functions/#rerun.set_time).
Furthermore, this will *not* inject the default timelines `log_tick` and `log_time` timeline columns.



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | Path to the entity in the space hierarchy.Seehttps://www.rerun.io/docs/concepts/entity-pathfor more on entity paths.TYPE:str |
| indexes | The time values of this batch of data. EachTimeColumnLikeobject represents a single column of timestamps. You usually want to usererun.TimeColumnfor this.TYPE:Iterable[TimeColumnLike] |
| columns | The columns of components to log. Each object represents a single column of data.In order to send multiple components per time value, explicitly create aComponentColumneither by constructing it directly, or by calling the.columns()method on anArchetypetype.TYPE:Iterable[ComponentColumn] |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |
| strict | If True, raise exceptions on non-loggable data. If False, warn on non-loggable data. If None, use the global default fromrerun.strict_mode()TYPE:bool\| NoneDEFAULT:None |



#### defsend_record_batch(batch,recording=None)



Coerce a single pyarrow `RecordBatch` to Rerun structure.



#### defsend_dataframe(df,recording=None)



Coerce a pyarrow `RecordBatchReader` or `Table` to Rerun structure.