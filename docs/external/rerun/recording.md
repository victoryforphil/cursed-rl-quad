---
source: https://ref.rerun.io/docs/python/stable/common/recording
title: Recording
---

# Recording



### rerun.recording



#### classRecording



A single Rerun recording.



This can be loaded from an RRD file using load_recording().



A recording is a collection of data that was logged to Rerun. This data is organized
as a column for each index (timeline) and each entity/component pair that was logged.



You can examine the .schema() of the recording to see
what data is available.



##### defapplication_id()



The application ID of the recording.



##### defrecording_id()



The recording ID of the recording.



##### defschema()



The schema describing all the columns available in the recording.



##### defview(*,index,contents,include_semantically_empty_columns=False,include_tombstone_columns=False)deprecated

 Deprecated

Recording.view() is deprecated. Use the catalog API instead.
        See: https://rerun.io/docs/reference/migration/migration-0-28#recordingview-and-local-dataframe-api-deprecated



Create a `RecordingView` of the recording according to a particular index and content specification.



The only type of index currently supported is the name of a timeline, or `None` (see below
for details).



The view will only contain a single row for each unique value of the index
that is associated with a component column that was included in the view.
Component columns that are not included via the view contents will not
impact the rows that make up the view. If the same entity / component pair
was logged to a given index multiple times, only the most recent row will be
included in the view, as determined by the `row_id` column. This will
generally be the last value logged, as row_ids are guaranteed to be
monotonically increasing when data is sent from a single process.



If `None` is passed as the index, the view will contain only static columns (among those
specified) and no index columns. It will also contain a single row per segment.



| PARAMETER | DESCRIPTION |
| --- | --- |
| index | The index to use for the view. This is typically a timeline name. UseNoneto query static data only.TYPE:str\| None |
| contents | The content specification for the view.This can be a single string content-expression such as:"world/cameras/**", or a dictionary specifying multiple content-expressions and a respective list of components to select within that expression such as{"world/cameras/**": ["ImageBuffer", "PinholeProjection"]}.TYPE:ViewContentsLike |
| include_semantically_empty_columns | Whether to include columns that are semantically empty, by defaultFalse.Semantically empty columns are components that arenullor empty[]for every row in the recording.TYPE:boolDEFAULT:False |
| include_tombstone_columns | Whether to include tombstone columns, by defaultFalse.Tombstone columns are components used to represent clears. However, even without the clear tombstone columns, the view will still apply the clear semantics when resolving row contents.TYPE:boolDEFAULT:False |



| RETURNS | DESCRIPTION |
| --- | --- |
| RecordingView | The view of the recording. |



Examples:



All the data in the recording on the timeline "my_index":

```
recording.view(index="my_index", contents="/**")
```



Just the Position3D components in the "points" entity:

```
recording.view(index="my_index", contents={"points": "Position3D"})
```



#### classRRDArchive



An archive loaded from an RRD.



RRD archives may include 1 or more recordings or blueprints.



##### defall_recordings()



All the recordings in the archive.



##### defnum_recordings()



The number of recordings in the archive.



#### defload_archive(path_to_rrd)



Load a rerun archive from an RRD file.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path_to_rrd | The path to the file to load.TYPE:str\|PathLike[str] |



| RETURNS | DESCRIPTION |
| --- | --- |
| RRDArchive | The loaded archive. |



#### defload_recording(path_to_rrd)



Load a single recording from an RRD file.



Will raise a `ValueError` if the file does not contain exactly one recording.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path_to_rrd | The path to the file to load.TYPE:str\|PathLike[str] |



| RETURNS | DESCRIPTION |
| --- | --- |
| Recording | The loaded recording. |