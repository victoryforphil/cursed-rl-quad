---
source: https://ref.rerun.io/docs/python/stable/common/initialization_functions
title: Initialization functions
---

# Initialization functions



### rerun



#### classChunkBatcherConfig



Defines the different batching thresholds used within the RecordingStream.



##### chunk_max_rows_if_unsorted:intpropertywritable



Split a chunk if it contains >= rows than this threshold and one or more of its timelines are unsorted.



Equivalent to setting: `RERUN_CHUNK_MAX_ROWS_IF_UNSORTED` environment variable.



##### flush_num_bytes:intpropertywritable



Flush if the accumulated payload has a size in bytes equal or greater than this.



Equivalent to setting: `RERUN_FLUSH_NUM_BYTES` environment variable.



##### flush_num_rows:intpropertywritable



Flush if the accumulated payload has a number of rows equal or greater than this.



Equivalent to setting: `RERUN_FLUSH_NUM_ROWS` environment variable.



##### flush_tick:timedeltapropertywritable



Duration of the periodic tick.



Equivalent to setting: `RERUN_FLUSH_TICK_SECS` environment variable.



##### defALWAYS()staticmethod



Always flushes ASAP.



##### defDEFAULT()staticmethod



Default configuration, applicable to most use cases.



##### defLOW_LATENCY()staticmethod



Low-latency configuration, preferred when streaming directly to a viewer.



##### defNEVER()staticmethod



Never flushes unless manually told to (or hitting one the builtin invariants).



##### def__init__(flush_tick=None,flush_num_bytes=None,flush_num_rows=None,chunk_max_rows_if_unsorted=None)



Initialize the chunk batcher configuration.



| PARAMETER | DESCRIPTION |
| --- | --- |
| flush_tick | Duration of the periodic tick, by defaultNone. Equivalent to setting:RERUN_FLUSH_TICK_SECSenvironment variable.TYPE:int\|float\|timedelta\| NoneDEFAULT:None |
| flush_num_bytes | Flush if the accumulated payload has a size in bytes equal or greater than this, by defaultNone. Equivalent to setting:RERUN_FLUSH_NUM_BYTESenvironment variable.TYPE:int\| NoneDEFAULT:None |
| flush_num_rows | Flush if the accumulated payload has a number of rows equal or greater than this, by defaultNone. Equivalent to setting:RERUN_FLUSH_NUM_ROWSenvironment variable.TYPE:int\| NoneDEFAULT:None |
| chunk_max_rows_if_unsorted | Split a chunk if it contains >= rows than this threshold and one or more of its timelines are unsorted, by defaultNone. Equivalent to setting:RERUN_CHUNK_MAX_ROWS_IF_UNSORTEDenvironment variable.TYPE:int\| NoneDEFAULT:None |



#### classDescribedComponentBatch



A `ComponentBatchLike` object with its associated `ComponentDescriptor`.



Used by implementers of `AsComponents` to both efficiently expose their component data
and assign the right tags given the surrounding context.



##### defas_arrow_array()



Returns a `pyarrow.Array` of the component data.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_descriptor()



Returns the complete descriptor of the component.



##### defpartition(lengths=None)



Partitions the component batch into multiple sub-batches, forming a column.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumn.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | The offsets to partition the component at. If specified,lengthsmust sum to the total length of the component batch. If left unspecified, it will default to unit-length batches.TYPE:ArrayLike\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| The partitioned component batch as a column. |  |



#### classRecordingStream



A RecordingStream is used to send data to Rerun.



You can instantiate a RecordingStream by calling either rerun.init (to create a global
recording) or rerun.RecordingStream (for more advanced use cases).

 Multithreading

A RecordingStream can safely be copied and sent to other threads.
You can also set a recording as the global active one for all threads ([rerun.set_global_data_recording](../other_classes_and_functions/#rerun.set_global_data_recording))
or just for the current thread ([rerun.set_thread_local_data_recording](../other_classes_and_functions/#rerun.set_thread_local_data_recording)).



Similarly, the `with` keyword can be used to temporarily set the active recording for the
current thread, e.g.:

```
with rec:
    rr.log(...)
```

WARNING: if using a RecordingStream as a context manager, yielding from a generator function
while holding the context open will leak the context and likely cause your program to send data
to the wrong stream. See: [https://github.com/rerun-io/rerun/issues/6238](https://github.com/rerun-io/rerun/issues/6238). You can work around this
by using the [rerun.recording_stream_generator_ctx](../other_classes_and_functions/#rerun.recording_stream_generator_ctx) decorator.

Flushing or context manager exit guarantees that all previous data sent by the calling thread
has been recorded and (if applicable) flushed to the underlying OS-managed file descriptor,
but other threads may still have data in flight.



See also: [rerun.get_data_recording](../other_classes_and_functions/#rerun.get_data_recording), [rerun.get_global_data_recording](../other_classes_and_functions/#rerun.get_global_data_recording),
[rerun.get_thread_local_data_recording](../other_classes_and_functions/#rerun.get_thread_local_data_recording).

 Available methods

Every function in the Rerun SDK that takes an optional RecordingStream as a parameter can also
be called as a method on RecordingStream itself.



This includes, but isn't limited to:



- Metadata-related functions:
      [rerun.is_enabled](../other_classes_and_functions/#rerun.is_enabled), [rerun.get_recording_id](../other_classes_and_functions/#rerun.get_recording_id), â¦
- Sink-related functions:
      rerun.connect_grpc, rerun.spawn, â¦
- Time-related functions:
      [rerun.set_time](../timeline_functions/#rerun.set_time), [rerun.disable_timeline](../timeline_functions/#rerun.disable_timeline), [rerun.reset_time](../timeline_functions/#rerun.reset_time), â¦
- Log-related functions:
      [rerun.log](../logging_functions/#rerun.log), â¦



For an exhaustive list, see `help(rerun.RecordingStream)`.

 Micro-batching

Micro-batching using both space and time triggers (whichever comes first) is done automatically
in a dedicated background thread.



You can configure the frequency of the batches using the `batcher_config` parameter when creating
the RecordingStream, or via the following environment variables:



- `RERUN_FLUSH_TICK_SECS`:
      Flush frequency in seconds (default: `0.2` (200ms)).
- `RERUN_FLUSH_NUM_BYTES`:
      Flush threshold in bytes (default: `1048576` (1MiB)).
- `RERUN_FLUSH_NUM_ROWS`:
      Flush threshold in number of rows (default: `18446744073709551615` (u64::MAX)).



##### def__init__(application_id,*,recording_id=None,make_default=False,make_thread_default=False,default_enabled=True,send_properties=True,batcher_config=None)



Creates a new recording stream with a user-chosen application id (name) that can be used to log data.



If you only need a single global recording, rerun.init might be simpler.



Note that new recording streams always begin connected to a buffered sink.
To send the data to a viewer or file you will likely want to call rerun.connect_grpc or rerun.save
explicitly.



Warning



If you don't specify a `recording_id`, it will default to a random value that is generated once
at the start of the process.
That value will be kept around for the whole lifetime of the process, and even inherited by all
its subprocesses, if any.



This makes it trivial to log data to the same recording in a multiprocess setup, but it also means
that the following code will *not* create two distinct recordings:

```
rr.init("my_app")
rr.init("my_app")
```



To create distinct recordings from the same process, specify distinct recording IDs:

```
from uuid import uuid4
rec = rr.RecordingStream(application_id="test", recording_id=uuid4())
rec = rr.RecordingStream(application_id="test", recording_id=uuid4())
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| application_id | Your Rerun recordings will be categorized by this application id, so try to pick a unique one for each application that uses the Rerun SDK.For example, if you have one application doing object detection and another doing camera calibration, you could havererun.init("object_detector")andrerun.init("calibrator").TYPE:str |
| recording_id | Set the recording ID that this process is logging to, as a UUIDv4.The default recording_id is based onmultiprocessing.current_process().authkeywhich means that all processes spawned withmultiprocessingwill have the same default recording_id.If you are not usingmultiprocessingand still want several different Python processes to log to the same Rerun instance (and be part of the same recording), you will need to manually assign them all the same recording_id. Any random UUIDv4 will work, or copy the recording id for the parent process.TYPE:Optional[str]DEFAULT:None |
| make_default | If true (notthe default), the newly initialized recording will replace the current active one (if any) in the global scope.TYPE:boolDEFAULT:False |
| make_thread_default | If true (notthe default), the newly initialized recording will replace the current active one (if any) in the thread-local scope.TYPE:boolDEFAULT:False |
| default_enabled | Should Rerun logging be on by default? Can be overridden with the RERUN env-var, e.g.RERUN=onorRERUN=off.TYPE:boolDEFAULT:True |
| send_properties | Immediately send the recording properties to the viewer (default: True)TYPE:boolDEFAULT:True |
| batcher_config | Optional configuration for the chunk batcher.TYPE:ChunkBatcherConfig\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| RecordingStream | A handle to thererun.RecordingStream. Use it to log data to Rerun. |



Examples:



Using a recording stream object directly.

```
from uuid import uuid4
stream = rr.RecordingStream("my_app", recording_id=uuid4())
stream.connect_grpc()
stream.log("hello", rr.TextLog("Hello world"))
```



##### defconnect_grpc(url=None,*,default_blueprint=None)



Connect to a remote Rerun Viewer on the given URL.



This function returns immediately.



| PARAMETER | DESCRIPTION |
| --- | --- |
| url | The URL to connect toThe scheme must be one ofrerun://,rerun+http://, orrerun+https://, and the pathname must be/proxy.The default isrerun+http://127.0.0.1:9876/proxy.TYPE:str\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



##### defdisable_timeline(timeline)



Clear time information for the specified timeline on this thread.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The name of the timeline to clear the time for.TYPE:str |



##### defdisconnect()



Closes all gRPC connections, servers, and files.



Closes all gRPC connections, servers, and files that have been opened with
rerun.RecordingStream.connect_grpc, rerun.RecordingStream.serve_grpc,
rerun.RecordingStream.save or rerun.RecordingStream.spawn.



##### defflush(*,timeout_sec=1e+38)



Initiates a flush the batching pipeline and optionally waits for it to propagate to the underlying file descriptor (if any).



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeout_sec | Wait at most this many seconds. If the timeout is reached, an error is raised. If set to zero, the flush will be started but not waited for.TYPE:floatDEFAULT:1e+38 |



##### defget_recording_id()



Get the recording ID that this recording is logging to, as a UUIDv4.



| RETURNS | DESCRIPTION |
| --- | --- |
| str | The recording ID that this recording is logging to. |



##### deflog(entity_path,entity,*extra,static=False,strict=None)



Log data to Rerun.



This is the main entry point for logging data to rerun. It can be used to log anything
that implements the [rerun.AsComponents](../interfaces/#rerun.AsComponents) interface, or a collection of [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) objects.



When logging data, you must always provide an [entity_path](https://www.rerun.io/docs/concepts/entity-path)
for identifying the data. Note that paths prefixed with "__" are considered reserved for use by the Rerun SDK
itself and should not be used for logging user data. This is where Rerun will log additional information
such as properties and warnings.



The most common way to log is with one of the rerun archetypes, all of which implement
the [rerun.AsComponents](../interfaces/#rerun.AsComponents) interface.



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
| entity | Anything that implements thererun.AsComponentsinterface, usually an archetype.TYPE:AsComponents\|Iterable[DescribedComponentBatch] |
| *extra | An arbitrary number of additional component bundles implementing thererun.AsComponentsinterface, that are logged to the same entity path.TYPE:AsComponents\|Iterable[DescribedComponentBatch]DEFAULT:() |
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.RecordingStream.set_timewill also be included.TYPE:boolDEFAULT:False |
| strict | If True, raise exceptions on non-loggable data. If False, warn on non-loggable data. if None, use the global default fromrerun.strict_modeTYPE:bool\| NoneDEFAULT:None |



##### deflog_file_from_contents(file_path,file_contents,*,entity_path_prefix=None,static=False)



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
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.RecordingStream.set_timewill also be included.TYPE:boolDEFAULT:False |



##### deflog_file_from_path(file_path,*,entity_path_prefix=None,static=False)



Logs the file at the given `path` using all `DataLoader`s available.



A single `path` might be handled by more than one loader.



This method blocks until either at least one `DataLoader` starts
streaming data in or all of them fail.



See [https://www.rerun.io/docs/getting-started/data-in/open-any-file](https://www.rerun.io/docs/getting-started/data-in/open-any-file) for more information.



| PARAMETER | DESCRIPTION |
| --- | --- |
| file_path | Path to the file to be logged.TYPE:str\|Path |
| entity_path_prefix | What should the logged entity paths be prefixed with?TYPE:str\| NoneDEFAULT:None |
| static | If true, the components will be logged as static data.Static data has no time associated with it, exists on all timelines, and unconditionally shadows any temporal data of the same type.Otherwise, the data will be timestamped automatically withlog_timeandlog_tick. Additional timelines set byrerun.RecordingStream.set_timewill also be included.TYPE:boolDEFAULT:False |



##### defmemory_recording()



Streams all log-data to a memory buffer.



This can be used to display the RRD to alternative formats such as html.
See: rerun.notebook_show.



| RETURNS | DESCRIPTION |
| --- | --- |
| MemoryRecording | A memory recording object that can be used to read the data. |



##### defnotebook_show(*,width=None,height=None,blueprint=None)



Output the Rerun viewer in a notebook using IPython [IPython.core.display.HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML).



Any data logged to the recording after initialization will be sent directly to the viewer.



Note that this can be called at any point during cell execution. The call will block until the embedded
viewer is initialized and ready to receive data. Thereafter any log calls will immediately send data
to the viewer.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | The width of the viewer in pixels.TYPE:intDEFAULT:None |
| height | The height of the viewer in pixels.TYPE:intDEFAULT:None |
| blueprint | A blueprint object to send to the viewer. It will be made active and set as the default blueprint in the recording.Setting this is equivalent to callingrerun.RecordingStream.send_blueprintbefore initializing the viewer.TYPE:BlueprintLikeDEFAULT:None |



##### defreset_time()



Clear all timeline information on this thread.



This is the same as calling `disable_timeline` for all of the active timelines.



Used for all subsequent logging on the same thread,
until the next call to rerun.RecordingStream.set_time.



##### defsave(path,default_blueprint=None)



Stream all log-data to a file.



Call this *before* you log any data!



The Rerun Viewer is able to read continuously from the resulting rrd file while it is being written.
However, depending on your OS and configuration, changes may not be immediately visible due to file caching.
This is a common issue on Windows and (to a lesser extent) on MacOS.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | The path to save the data to.TYPE:str\|Path |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



##### defsend_blueprint(blueprint,*,make_active=True,make_default=True)



Create a blueprint from a `BlueprintLike` and send it to the `RecordingStream`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blueprint | A blueprint object to send to the viewer.TYPE:BlueprintLike |
| make_active | Immediately make this the active blueprint for the associatedapp_id. Note that setting this tofalsedoes not mean the blueprint may not still end up becoming active. In particular, ifmake_defaultis true and there is no other currently active blueprint.TYPE:boolDEFAULT:True |
| make_default | Make this the default blueprint for theapp_id. The default blueprint will be used as the template when the user resets the blueprint for the app. It will also become the active blueprint if no other blueprint is currently active.TYPE:boolDEFAULT:True |



##### defsend_columns(entity_path,indexes,columns,*,strict=None)



Send columnar data to Rerun.



Unlike the regular `log` API, which is row-oriented, this API lets you submit the data
in a columnar form. Each `TimeColumnLike` and `ComponentColumn` object represents a column
of data that will be sent to Rerun. The lengths of all these columns must match, and all
data that shares the same index across the different columns will act as a single logical row,
equivalent to a single call to `rr.log()`.



Note that this API ignores any stateful time set on the log stream via rerun.RecordingStream.set_time.
Furthermore, this will *not* inject the default timelines `log_tick` and `log_time` timeline columns.



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | Path to the entity in the space hierarchy.Seehttps://www.rerun.io/docs/concepts/entity-pathfor more on entity paths.TYPE:str |
| indexes | The time values of this batch of data. EachTimeColumnLikeobject represents a single column of timestamps. Generally, you should use one of the provided classTimeColumn.TYPE:Iterable[TimeColumnLike] |
| columns | The columns of components to log. Each object represents a single column of data.In order to send multiple components per time value, explicitly create aComponentColumneither by constructing it directly, or by calling the.columns()method on anArchetypetype.TYPE:Iterable[ComponentColumn] |
| strict | If True, raise exceptions on non-loggable data. If False, warn on non-loggable data. If None, use the global default fromrerun.strict_modeTYPE:bool\| NoneDEFAULT:None |



##### defsend_dataframe(df)



Coerce a pyarrow `RecordBatchReader` or `Table` to Rerun structure.



##### defsend_property(name,values)



```
Send a property of the recording.
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | Name of the property.TYPE:str |
| values | Anything that implements thererun.AsComponentsinterface, usually an archetype, or an iterable of (described)component batches.TYPE:AsComponents\|Iterable[DescribedComponentBatch] |



##### defsend_record_batch(batch)



Coerce a single pyarrow `RecordBatch` to Rerun structure.



##### defsend_recording(recording)



Send a `Recording` loaded from a `.rrd` to the `RecordingStream`.



.. warning::
    â ï¸ This API is experimental and may change or be removed in future versions! â ï¸



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | ARecordingloaded from a.rrd.TYPE:Recording |



##### defsend_recording_name(name)



Send the name of the recording.



This name is shown in the Rerun Viewer.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the recording.TYPE:str |



##### defsend_recording_start_time_nanos(nanos)



Send the start time of the recording.



This timestamp is shown in the Rerun Viewer.



| PARAMETER | DESCRIPTION |
| --- | --- |
| nanos | The start time of the recording.TYPE:int |



##### defserve_grpc(*,grpc_port=None,default_blueprint=None,server_memory_limit='25%',newest_first=False)



Serve log-data over gRPC.



You can to this server with the native viewer using `rerun rerun+http://localhost:{grpc_port}/proxy`.



The gRPC server will buffer all log data in memory so that late connecting viewers will get all the data.
You can limit the amount of data buffered by the gRPC server with the `server_memory_limit` argument.
Once reached, the earliest logged data will be dropped. Static data is never dropped.



If server & client are running on the same machine and all clients are expected to connect before
any data is sent, it is highly recommended that you set the memory limit to `0B`,
otherwise you're potentially doubling your memory usage!



Returns the URI of the server so you can connect the viewer to it.



This function returns immediately.



NOTE: When the `RecordingStream` is disconnected, or otherwise goes out of scope, it will shut down the
gRPC server.



| PARAMETER | DESCRIPTION |
| --- | --- |
| grpc_port | The port to serve the gRPC server on (defaults to 9876)TYPE:int\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.RecordingStream.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| server_memory_limit | Maximum amount of memory to use for buffering log data for clients that connect late. This can be a percentage of the total ram (e.g. "50%") or an absolute value (e.g. "4GB").TYPE:strDEFAULT:'25%' |
| newest_first | IfTrue, the server will start sending back the newest messagesfirst. IfFalse, the messages will be played back in the order they arrived.TYPE:boolDEFAULT:False |



##### defset_sinks(*sinks,default_blueprint=None)



Stream data to multiple different sinks.



Duplicate sinks are not allowed. For example, two [rerun.GrpcSink](../other_classes_and_functions/#rerun.GrpcSink)s that
use the same `url` will cause this function to throw a `ValueError`.



This *replaces* existing sinks. Calling `rr.init(spawn=True)`, `rr.spawn()`,
`rr.connect_grpc()` or similar followed by `set_sinks` will result in only
the sinks passed to `set_sinks` remaining active.



Only data logged *after* the `set_sinks` call will be logged to the newly attached sinks.



| PARAMETER | DESCRIPTION |
| --- | --- |
| sinks | A list of sinks to wrap.Seererun.GrpcSink,rerun.FileSink.TYPE:LogSinkLikeDEFAULT:() |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |

 Example

```
rec = rr.RecordingStream("rerun_example_tee")
rec.set_sinks(
    rr.GrpcSink(),
    rr.FileSink("data.rrd")
)
rec.log("my/point", rr.Points3D(position=[1.0, 2.0, 3.0]))
```



##### defset_time(timeline,*,sequence=None,duration=None,timestamp=None)



Set the current time of a timeline for this thread.



Used for all subsequent logging on the same thread, until the next call to
rerun.RecordingStream.set_time, rerun.RecordingStream.reset_time or
rerun.RecordingStream.disable_timeline.



For example: `set_time("frame_nr", sequence=frame_nr)`.



There is no requirement of monotonicity. You can move the time backwards if you like.



You are expected to set exactly ONE of the arguments `sequence`, `duration`, or `timestamp`.
You may NOT change the type of a timeline, so if you use `duration` for a specific timeline,
you must only use `duration` for that timeline going forward.



The columnar equivalent to this function is [rerun.TimeColumn](../columnar_api/#rerun.TimeColumn).



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The name of the timeline to set the time for.TYPE:str |
| sequence | Used for sequential indices, likeframe_nr. Must be an integer.TYPE:int\| NoneDEFAULT:None |
| duration | Used for relative times, liketime_since_start. Must either be in seconds, adatetime.timedelta, ornumpy.timedelta64. For nanosecond precision, usenumpy.timedelta64(nanoseconds, 'ns').TYPE:int\|float\|timedelta\|timedelta64\| NoneDEFAULT:None |
| timestamp | Used for absolute time indices, likecapture_time. Must either be in seconds since Unix epoch, adatetime.datetime, ornumpy.datetime64. For nanosecond precision, usenumpy.datetime64(nanoseconds, 'ns').TYPE:int\|float\|datetime\|datetime64\| NoneDEFAULT:None |



##### defspawn(*,port=9876,connect=True,memory_limit='75%',hide_welcome_screen=False,detach_process=True,default_blueprint=None)



Spawn a Rerun Viewer, listening on the given port.



You can also call rerun.init with a `spawn=True` argument.



| PARAMETER | DESCRIPTION |
| --- | --- |
| port | The port to listen on.TYPE:intDEFAULT:9876 |
| connect | also connect to the viewer and stream logging data to it.TYPE:boolDEFAULT:True |
| memory_limit | An upper limit on how much memory the Rerun Viewer should use. When this limit is reached, Rerun will drop the oldest data. Example:16GBor50%(of system total).TYPE:strDEFAULT:'75%' |
| hide_welcome_screen | Hide the normal Rerun welcome screen.TYPE:boolDEFAULT:False |
| detach_process | Detach Rerun Viewer process from the application process.TYPE:boolDEFAULT:True |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.RecordingStream.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



##### defstdout(default_blueprint=None)



Stream all log-data to stdout.



Pipe it into a Rerun Viewer to visualize it.



Call this *before* you log any data!



If there isn't any listener at the other end of the pipe, the `RecordingStream` will
default back to `buffered` mode, in order not to break the user's terminal.



| PARAMETER | DESCRIPTION |
| --- | --- |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



#### classTimeColumnLike



Bases: `Protocol`



Describes interface for objects that can be converted to a column of rerun time values.



##### defas_arrow_array()



Returns the name of the component.



##### deftimeline_name()



Returns the name of the timeline.



#### definit(application_id,*,recording_id=None,spawn=False,init_logging=True,default_enabled=True,strict=None,default_blueprint=None,send_properties=True)



Initialize the Rerun SDK with a user-chosen application id (name).



You must call this function first in order to initialize a global recording.
Without an active recording, all methods of the SDK will turn into no-ops.



For more advanced use cases, e.g. multiple recordings setups, see rerun.RecordingStream.



To deal with accumulation of recording state when calling init() multiple times, this function will
have the side-effect of flushing all existing recordings. After flushing, any recordings which
are otherwise orphaned will also be destructed to free resources, close open file-descriptors, etc.



Warning



If you don't specify a `recording_id`, it will default to a random value that is generated once
at the start of the process.
That value will be kept around for the whole lifetime of the process, and even inherited by all
its subprocesses, if any.



This makes it trivial to log data to the same recording in a multiprocess setup, but it also means
that the following code will *not* create two distinct recordings:

```
rr.init("my_app")
rr.init("my_app")
```



To create distinct recordings from the same process, specify distinct recording IDs:

```
from uuid import uuid4
rr.init("my_app", recording_id=uuid4())
rr.init("my_app", recording_id=uuid4())
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| application_id | Your Rerun recordings will be categorized by this application id, so try to pick a unique one for each application that uses the Rerun SDK.For example, if you have one application doing object detection and another doing camera calibration, you could havererun.init("object_detector")andrerun.init("calibrator").Application ids starting withrerun_example_are reserved for Rerun examples, and will be treated specially by the Rerun Viewer. In particular, it will opt-in to more analytics, and will also seed the global random number generator deterministically.TYPE:str |
| recording_id | Set the recording ID that this process is logging to, as a UUIDv4.The default recording_id is based onmultiprocessing.current_process().authkeywhich means that all processes spawned withmultiprocessingwill have the same default recording_id.If you are not usingmultiprocessingand still want several different Python processes to log to the same Rerun instance (and be part of the same recording), you will need to manually assign them all the same recording_id. Any random UUIDv4 will work, or copy the recording id for the parent process.TYPE:Optional[str]DEFAULT:None |
| spawn | Spawn a Rerun Viewer and stream logging data to it. Short for callingspawnseparately. If you don't call this, log events will be buffered indefinitely until you call eitherconnect_grpc,show, orsaveTYPE:boolDEFAULT:False |
| default_enabled | Should Rerun logging be on by default? Can be overridden with the RERUN env-var, e.g.RERUN=onorRERUN=off.TYPE:boolDEFAULT:True |
| init_logging | Should we initialize the logging for this application?TYPE:boolDEFAULT:True |
| strict | IfTrue, an exception is raised on use error (wrong parameter types, etc.). IfFalse, errors are logged as warnings instead. If unset, this can alternatively be overridden using the RERUN_STRICT environment variable. If not otherwise specified, the default behavior will be equivalent toFalse.TYPE:bool\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| send_properties | Immediately send the recording properties to the viewer (default: True)TYPE:boolDEFAULT:True |



#### defset_sinks(*sinks,default_blueprint=None,recording=None)



Stream data to multiple different sinks.



Duplicate sinks are not allowed. For example, two [rerun.GrpcSink](../other_classes_and_functions/#rerun.GrpcSink)s that
use the same `url` will cause this function to throw a `ValueError`.



This *replaces* existing sinks. Calling `rr.init(spawn=True)`, `rr.spawn()`,
`rr.connect_grpc()` or similar followed by `set_sinks` will result in only
the sinks passed to `set_sinks` remaining active.



Only data logged *after* the `set_sinks` call will be logged to the newly attached sinks.



| PARAMETER | DESCRIPTION |
| --- | --- |
| sinks | A list of sinks to wrap.Seererun.GrpcSink,rerun.FileSink.TYPE:LogSinkLikeDEFAULT:() |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |

 Example

```
rr.init("rerun_example_tee")
rr.set_sinks(
    rr.GrpcSink(),
    rr.FileSink("data.rrd")
)
rr.log("my/point", rr.Points3D(position=[1.0, 2.0, 3.0]))
```



#### defconnect_grpc(url=None,*,default_blueprint=None,recording=None)



Connect to a remote Rerun Viewer on the given URL.



This function returns immediately.



| PARAMETER | DESCRIPTION |
| --- | --- |
| url | The URL to connect to.The scheme must be one ofrerun://,rerun+http://, orrerun+https://, and the pathname must be/proxy.The default isrerun+http://127.0.0.1:9876/proxy.TYPE:str\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### defdisconnect(recording=None)



Closes all gRPC connections, servers, and files.



Closes all gRPC connections, servers, and files that have been opened with
[`rerun.connect_grpc`], [`rerun.serve`], [`rerun.save`] or [`rerun.spawn`].



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### defsave(path,default_blueprint=None,recording=None)



Stream all log-data to a file.



Call this *before* you log any data!



The Rerun Viewer is able to read continuously from the resulting rrd file while it is being written.
However, depending on your OS and configuration, changes may not be immediately visible due to file caching.
This is a common issue on Windows and (to a lesser extent) on MacOS.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | The path to save the data to.TYPE:str\|Path |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### defsend_blueprint(blueprint,*,make_active=True,make_default=True,recording=None)



Create a blueprint from a `BlueprintLike` and send it to the `RecordingStream`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blueprint | A blueprint object to send to the viewer.TYPE:BlueprintLike |
| make_active | Immediately make this the active blueprint for the associatedapp_id. Note that setting this tofalsedoes not mean the blueprint may not still end up becoming active. In particular, ifmake_defaultis true and there is no other currently active blueprint.TYPE:boolDEFAULT:True |
| make_default | Make this the default blueprint for theapp_id. The default blueprint will be used as the template when the user resets the blueprint for the app. It will also become the active blueprint if no other blueprint is currently active.TYPE:boolDEFAULT:True |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### defserve_grpc(*,grpc_port=None,default_blueprint=None,recording=None,server_memory_limit='25%',newest_first=False)



Serve log-data over gRPC.



You can connect to this server with the native viewer using `rerun rerun+http://localhost:{grpc_port}/proxy`.



The gRPC server will buffer all log data in memory so that late connecting viewers will get all the data.
You can limit the amount of data buffered by the gRPC server with the `server_memory_limit` argument.
Once reached, the earliest logged data will be dropped. Static data is never dropped.



If server & client are running on the same machine and all clients are expected to connect before
any data is sent, it is highly recommended that you set the memory limit to `0B`,
otherwise you're potentially doubling your memory usage!



Returns the URI of the server so you can connect the viewer to it.



This function returns immediately. In order to keep the server running, you must keep the Python process running
as well.



NOTE: The grpc server is associated with a rerun.RecordingStream object. By default, if no other recording
was specified, this will be the global recording. When that `RecordingStream` is disconnected, or otherwise goes
out of scope, the associated gRPC server will be shut down.
See: [Issue: #12313](https://github.com/rerun-io/rerun/issues/12313) for possible complications.



| PARAMETER | DESCRIPTION |
| --- | --- |
| grpc_port | The port to serve the gRPC server on (defaults to 9876)TYPE:int\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |
| server_memory_limit | Maximum amount of memory to use for buffering log data for clients that connect late. This can be a percentage of the total ram (e.g. "50%") or an absolute value (e.g. "4GB").TYPE:strDEFAULT:'25%' |
| newest_first | IfTrue, the server will start sending back the newest messagesfirst. IfFalse, the messages will be played back in the order they arrived.TYPE:boolDEFAULT:False |



#### defserve_web_viewer(*,web_port=None,open_browser=True,connect_to=None)



Host a web viewer over HTTP.



You can pass this function the URL returned from rerun.serve_grpc and  rerun.RecordingStream.serve_grpc
so that the spawned web viewer connects to that server.



Note that this is NOT a log sink, and this does NOT host a gRPC server.
If you want to log data to a gRPC server and connect the web viewer to it, you can do so like this:

```
server_uri = rr.serve_grpc()
rr.serve_web_viewer(connect_to=server_uri)
```



This function returns immediately.
In order to keep the web server running you must keep the Python process running too.



| PARAMETER | DESCRIPTION |
| --- | --- |
| web_port | The port to serve the web viewer on (defaults to 9090).TYPE:int\| NoneDEFAULT:None |
| open_browser | Open the default browser to the viewer.TYPE:boolDEFAULT:True |
| connect_to | Ifopen_browseris true, then this is the URL the web viewer will connect to.TYPE:str\| NoneDEFAULT:None |



#### defspawn(*,port=9876,connect=True,memory_limit='75%',server_memory_limit='0B',hide_welcome_screen=False,detach_process=True,default_blueprint=None,recording=None)



Spawn a Rerun Viewer, listening on the given port.



This is often the easiest and best way to use Rerun.
Just call this once at the start of your program.



You can also call rerun.init with a `spawn=True` argument.



| PARAMETER | DESCRIPTION |
| --- | --- |
| port | The port to listen on.TYPE:intDEFAULT:9876 |
| connect | also connect to the viewer and stream logging data to it.TYPE:boolDEFAULT:True |
| memory_limit | An upper limit on how much memory the Rerun Viewer should use. When this limit is reached, Rerun will drop the oldest data. Example:16GBor50%(of system total).TYPE:strDEFAULT:'75%' |
| server_memory_limit | An upper limit on how much memory the gRPC server running in the same process as the Rerun Viewer should use. When this limit is reached, Rerun will drop the oldest data. Example:16GBor50%(of system total).Defaults to0B.TYPE:strDEFAULT:'0B' |
| hide_welcome_screen | Hide the normal Rerun welcome screen.TYPE:boolDEFAULT:False |
| detach_process | Detach Rerun Viewer process from the application process.TYPE:boolDEFAULT:True |
| recording | Specifies thererun.RecordingStreamto use ifconnect = True. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |
| default_blueprint | Optionally set a default blueprint to use for this application. If the application already has an active blueprint, the new blueprint won't become active until the user clicks the "reset blueprint" button. If you want to activate the new blueprint immediately, instead use thererun.send_blueprintAPI.TYPE:BlueprintLike\| NoneDEFAULT:None |



#### defmemory_recording(recording=None)



Streams all log-data to a memory buffer.



This can be used to display the RRD to alternative formats such as html.
See: rerun.notebook_show.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| MemoryRecording | A memory recording object that can be used to read the data. |



#### defnotebook_show(*,width=None,height=None,blueprint=None,recording=None)



Output the Rerun viewer in a notebook using IPython [IPython.core.display.HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML).



Any data logged to the recording after initialization will be sent directly to the viewer.



Note that this can be called at any point during cell execution. The call will block until the embedded
viewer is initialized and ready to receive data. Thereafter any log calls will immediately send data
to the viewer.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | The width of the viewer in pixels.TYPE:intDEFAULT:None |
| height | The height of the viewer in pixels.TYPE:intDEFAULT:None |
| blueprint | A blueprint object to send to the viewer. It will be made active and set as the default blueprint in the recording.Setting this is equivalent to callingrerun.send_blueprintbefore initializing the viewer.TYPE:BlueprintLikeDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



#### deflegacy_notebook_show(*,width=DEFAULT_WIDTH,height=DEFAULT_HEIGHT,app_url=None,timeout_ms=DEFAULT_TIMEOUT,blueprint=None,recording=None)



Output the Rerun viewer in a notebook using IPython [IPython.core.display.HTML](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.HTML).



This is a legacy function that uses a limited mechanism of inlining an RRD into a self-contained
HTML template that loads the viewer in an iframe.



In general, rerun.notebook_show should be preferred. However, this function can be useful
in some systems with incomplete support for the `anywidget` library.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | The width of the viewer in pixels.TYPE:intDEFAULT:DEFAULT_WIDTH |
| height | The height of the viewer in pixels.TYPE:intDEFAULT:DEFAULT_HEIGHT |
| app_url | Alternative HTTP url to find the Rerun web viewer. This will default to usinghttps://app.rerun.ioor localhost ifrerun.start_web_viewer_serverhas been called.TYPE:strDEFAULT:None |
| timeout_ms | The number of milliseconds to wait for the Rerun web viewer to load.TYPE:intDEFAULT:DEFAULT_TIMEOUT |
| blueprint | The blueprint to display in the viewer.TYPE:BlueprintLikeDEFAULT:None |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |