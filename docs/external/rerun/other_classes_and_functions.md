---
source: https://ref.rerun.io/docs/python/stable/common/other_classes_and_functions
title: Other classes and functions
---

# Other classes and functions



### rerun



#### classLoggingHandler



Bases: `Handler`



Provides a logging handler that forwards all events to the Rerun SDK.



[Read more about logging handlers](https://docs.python.org/3/howto/logging.html#handlers).



##### def__init__(path_prefix=None)



Initializes the logging handler with an optional path prefix.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path_prefix | A common prefix for all logged entity paths. Defaults to no prefix.TYPE:str\| NoneDEFAULT:None |



##### defemit(record)



Emits a record to the Rerun SDK.



#### classMemoryRecording



A recording that stores data in memory.



##### defdrain_as_bytes()



Drains the MemoryRecording and returns the data as bytes.



This will flush the current sink before returning.



##### defnum_msgs()



The number of pending messages in the MemoryRecording.



Note: counting the messages will flush the batcher in order to get a deterministic count.



#### classGrpcSink



Used in [rerun.RecordingStream.set_sinks](../initialization_functions/#rerun.RecordingStream.set_sinks).



Connect the recording stream to a remote Rerun Viewer on the given URL.



##### def__init__(url=None)



Initialize a gRPC sink.



| PARAMETER | DESCRIPTION |
| --- | --- |
| url | The URL to connect toThe scheme must be one ofrerun://,rerun+http://, orrerun+https://, and the pathname must be/proxy.The default isrerun+http://127.0.0.1:9876/proxy.TYPE:str\| NoneDEFAULT:None |



#### classFileSink



Used in [rerun.RecordingStream.set_sinks](../initialization_functions/#rerun.RecordingStream.set_sinks).



Save the recording stream to a file.



##### def__init__(path)



Initialize a file sink.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | Path to write to. The file will be overwritten.TYPE:str\|PathLike[str] |



#### defget_data_recording(recording=None)



Returns the most appropriate recording to log data to, in the current context, if any.



- If `recording` is specified, returns that one;
- Otherwise, falls back to the currently active thread-local recording, if there is one;
- Otherwise, falls back to the currently active global recording, if there is one;
- Otherwise, returns None.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| Optional[RecordingStream] | The most appropriate recording to log data to, in the current context, if any. |



#### defget_global_data_recording()



Returns the currently active global recording, if any.



| RETURNS | DESCRIPTION |
| --- | --- |
| Optional[RecordingStream] | The currently active global recording, if any. |



#### defget_recording_id(recording=None)



Get the recording ID that this recording is logging to, as a UUIDv4, if any.



The default recording_id is based on `multiprocessing.current_process().authkey`
which means that all processes spawned with `multiprocessing`
will have the same default recording_id.



If you are not using `multiprocessing` and still want several different Python
processes to log to the same Rerun instance (and be part of the same recording),
you will need to manually assign them all the same recording_id.
Any random UUIDv4 will work, or copy the recording id for the parent process.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | Specifies thererun.RecordingStreamto use. If left unspecified, defaults to the current active data recording, if there is one. See also:rerun.init,rerun.set_global_data_recording.TYPE:RecordingStream\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| str | The recording ID that this recording is logging to. |



#### defget_thread_local_data_recording()



Returns the currently active thread-local recording, if any.



| RETURNS | DESCRIPTION |
| --- | --- |
| Optional[RecordingStream] | The currently active thread-local recording, if any. |



#### defis_enabled(recording=None)



Is this Rerun recording enabled.



If false, all calls to the recording are ignored.



The default can be set in [rerun.init](../initialization_functions/#rerun.init), but is otherwise `True`.



This can be controlled with the environment variable `RERUN` (e.g. `RERUN=on` or `RERUN=off`).



#### defset_global_data_recording(recording)



Replaces the currently active global recording with the specified one.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | The newly active global recording.TYPE:RecordingStream |



#### defset_thread_local_data_recording(recording)



Replaces the currently active thread-local recording with the specified one.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording | The newly active thread-local recording.TYPE:RecordingStream\| None |



#### defstart_web_viewer_server(port=0)



Start an HTTP server that hosts the rerun web viewer.



This only provides the web-server that makes the viewer available and
does not otherwise provide a rerun gRPC server or facilitate any routing of
data.



This is generally only necessary for application such as running a jupyter notebook
in a context where app.rerun.io is unavailable, or does not have the matching
resources for your build (such as when running from source.)



| PARAMETER | DESCRIPTION |
| --- | --- |
| port | Port to serve assets on. Defaults to 0 (random port).TYPE:intDEFAULT:0 |



#### defescape_entity_path_part(part)



Escape an individual part of an entity path.



For instance, `escape_entity_path_path("my image!")` will return `"my\ image\!"`.



See [https://www.rerun.io/docs/concepts/entity-path](https://www.rerun.io/docs/concepts/entity-path) for more on entity paths.



| PARAMETER | DESCRIPTION |
| --- | --- |
| part | An unescaped stringTYPE:str |



| RETURNS | DESCRIPTION |
| --- | --- |
| str | The escaped entity path.TYPE:str |



#### defnew_entity_path(entity_path)



Construct an entity path, defined by a list of (unescaped) parts.



If any part if not a string, it will be converted to a string using `str()`.



For instance, `new_entity_path(["world", 42, "my image!"])` will return `"world/42/my\ image\!"`.



See [https://www.rerun.io/docs/concepts/entity-path](https://www.rerun.io/docs/concepts/entity-path) for more on entity paths.



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | A list of strings to escape and join with slash.TYPE:list[Any] |



| RETURNS | DESCRIPTION |
| --- | --- |
| str | The escaped entity path.TYPE:str |



#### defthread_local_stream(application_id)



Create a thread-local recording stream and use it when executing the decorated function.



This can be helpful for decorating a function that represents a job or a task that you want to
to produce its own isolated recording.

 Example

```
@rr.thread_local_stream("rerun_example_job")
def job(name: str) -> None:
    rr.save(f"job_{name}.rrd")
    for i in range(5):
        time.sleep(0.2)
        rr.log("hello", rr.TextLog(f"Hello {i) from Job {name}"))

threading.Thread(target=job, args=("A",)).start()
threading.Thread(target=job, args=("B",)).start()
```

This will produce 2 separate rrd files, each only containing the logs from the respective threads.


| PARAMETER | DESCRIPTION |
| --- | --- |
| application_id | The application ID that this recording is associated with.TYPE:str |



#### defrecording_stream_generator_ctx(func)



Decorator to manage recording stream context for generator functions.



This is only necessary if you need to implement a generator which yields while holding an open
recording stream context which it created. This decorator will ensure that the recording stream
context is suspended and then properly resumed upon re-entering the generator.



See: https://github.com/rerun-io/rerun/issues/6238 for context on why this is necessary.



There are plenty of things that can go wrong when mixing context managers with generators, so
don't use this decorator unless you're sure you need it.



If you can plumb through `RecordingStream` objects and use those directly instead of relying on
the context manager, that will always be more robust.

 Example

```
@rr.recording_stream.recording_stream_generator_ctx
def my_generator(name: str) -> Iterator[None]:
    with rr.RecordingStream(name):
        rr.save(f"{name}.rrd")
        for i in range(10):
            rr.log("stream", rr.TextLog(f"{name} {i}"))
            yield i

for i in my_generator("foo"):
    pass
```