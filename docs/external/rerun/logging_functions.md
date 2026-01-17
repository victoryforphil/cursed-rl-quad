---
source: https://ref.rerun.io/docs/python/stable/common/logging_functions
title: Logging functions
---

# Logging functions



### rerun



#### deflog(entity_path,entity,*extra,static=False,recording=None,strict=None)



Log data to Rerun.



This is the main entry point for logging data to rerun. It can be used to log anything
that implements the [rerun.AsComponents](../interfaces/#rerun.AsComponents) interface, or a collection of `ComponentBatchLike`
objects.



When logging data, you must always provide an [entity_path](https://www.rerun.io/docs/concepts/entity-path)
for identifying the data. Note that paths prefixed with "__" are considered reserved for use by the Rerun SDK
itself and should not be used for logging user data. This is where Rerun will log additional information
such as properties and warnings.



The most common way to log is with one of the rerun archetypes, all of which implement
the `AsComponents` interface.



For example, to log a 3D point:

```
rr.log("my/point", rr.Points3D(position=[1.0, 2.0, 3.0]))
```



The `log` function can flexibly accept an arbitrary number of additional objects which will
be merged into the first entity so long as they don't expose conflicting components, for instance:

```
# Log three points with arrows sticking out of them,
# and a custom "confidence" component.
rr.log(
    "my/points",
    rr.Points3D([[0.2, 0.5, 0.3], [0.9, 1.2, 0.1], [1.0, 4.2, 0.3]], radii=[0.1, 0.2, 0.3]),
    rr.Arrows3D(vectors=[[0.3, 2.1, 0.2], [0.9, -1.1, 2.3], [-0.4, 0.5, 2.9]]),
    rr.AnyValues(confidence=[0.3, 0.4, 0.9]),
)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | Path to the entity in the space hierarchy.The entity path can either be a string (with special characters escaped, split on unescaped slashes) or a list of unescaped strings. This means that logging to"world/my\ image\!"is the same as logging to ["world", "my image!"].Seehttps://www.rerun.io/docs/concepts/entity-pathfor more on entity paths.TYPE:str\|list[object] |
| entity | Anything that implements thererun.AsComponentsinterface, usually an archetype, or an iterable of (described)component batches.TYPE:AsComponents\|Iterable[DescribedComponentBatch] |
| *extra | An arbitrary number of additional component bundles implementing thererun.AsComponentsinterface, that are logged to the same entity path.TYPE:AsComponents\|Iterable[DescribedComponentBatch]DEFAULT:() |
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.set_timewill also be included.TYPE:boolDEFAULT:False |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |
| strict | If True, raise exceptions on non-loggable data. If False, warn on non-loggable data. if None, use the global default fromrerun.strict_mode()TYPE:bool\| NoneDEFAULT:None |



#### deflog_file_from_path(file_path,*,entity_path_prefix=None,static=False,recording=None)



Logs the file at the given `path` using all `DataLoader`s available.



A single `path` might be handled by more than one loader.



This method blocks until either at least one `DataLoader` starts
streaming data in or all of them fail.



See [https://www.rerun.io/docs/getting-started/data-in/open-any-file](https://www.rerun.io/docs/getting-started/data-in/open-any-file) for more information.



| PARAMETER | DESCRIPTION |
| --- | --- |
| file_path | Path to the file to be logged.TYPE:str\|Path |
| entity_path_prefix | What should the logged entity paths be prefixed with?TYPE:str\| NoneDEFAULT:None |
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.set_timewill also be included.TYPE:boolDEFAULT:False |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### deflog_file_from_contents(file_path,file_contents,*,entity_path_prefix=None,static=False,recording=None)



Logs the given `file_contents` using all `DataLoader`s available.



A single `path` might be handled by more than one loader.



This method blocks until either at least one `DataLoader` starts
streaming data in or all of them fail.



See [https://www.rerun.io/docs/getting-started/data-in/open-any-file](https://www.rerun.io/docs/getting-started/data-in/open-any-file) for more information.



| PARAMETER | DESCRIPTION |
| --- | --- |
| file_path | Path to the file that thefile_contentsbelong to.TYPE:str\|Path |
| file_contents | Contents to be logged.TYPE:bytes |
| entity_path_prefix | What should the logged entity paths be prefixed with?TYPE:str\| NoneDEFAULT:None |
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.set_timewill also be included.TYPE:boolDEFAULT:False |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |