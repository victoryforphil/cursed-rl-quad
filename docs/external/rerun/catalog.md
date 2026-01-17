---
source: https://ref.rerun.io/docs/python/stable/common/catalog
title: Catalog
---

# Catalog



### rerun.catalog



#### IndexValuesLike:TypeAlias=npt.NDArray[np.int_]|npt.NDArray[np.datetime64]|pa.Int64Arraymodule-attribute



A type alias for index values.



This can be any numpy-compatible array of integers, or a [pyarrow.Int64Array](https://arrow.apache.org/docs/python/generated/pyarrow.Int64Array.html#pyarrow.Int64Array)



#### VectorDistanceMetricLike:TypeAlias=VectorDistanceMetric|Literal['L2','Cosine','Dot','Hamming']module-attribute



A type alias for vector distance metrics.



#### classSchema



The schema representing a set of available columns for a dataset.



A schema contains both index columns (timelines) and component columns (entity/component data).



##### def__eq__(other)



Check equality with another Schema.



##### def__init__(inner)



Create a new Schema wrapper.



| PARAMETER | DESCRIPTION |
| --- | --- |
| inner | The internal schema object from the bindings.TYPE:SchemaInternal |



##### def__iter__()



Iterate over all column descriptors in the schema (index columns first, then component columns).



##### def__repr__()



Return a string representation of the schema.



##### defcolumn_for(entity_path,component)



Look up the column descriptor for a specific entity path and component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | The entity path to look up.TYPE:str |
| component | The component to look up. Example:Points3D:positions.TYPE:str |



| RETURNS | DESCRIPTION |
| --- | --- |
| ComponentColumnDescriptor\| None | The column descriptor, if it exists. |



##### defcolumn_for_selector(selector)



Look up the column descriptor for a specific selector.



| PARAMETER | DESCRIPTION |
| --- | --- |
| selector | The selector to look up.String arguments are expected to follow the format:"<entity_path>:<component_type>"TYPE:str\|ComponentColumnSelector\|ComponentColumnDescriptor |



| RETURNS | DESCRIPTION |
| --- | --- |
| ComponentColumnDescriptor | The column descriptor. |



| RAISES | DESCRIPTION |
| --- | --- |
| LookupError | If the column is not found. |
| ValueError | If the string selector format is invalid or the input type is unsupported. |
| Note: if the input is already a `ComponentColumnDescriptor`, it is |  |
| returned directly without checking for existence. |  |



##### defcolumn_names()



Return a list of all column names in the schema.



| RETURNS | DESCRIPTION |
| --- | --- |
| The names of all columns (index columns first, then component columns). |  |



##### defcomponent_columns()



Return a list of all the component columns in the schema.



Component columns contain the data for a specific component of an entity.



##### defindex_columns()



Return a list of all the index columns in the schema.



Index columns contain the index values for when the data was updated.
They generally correspond to Rerun timelines.



#### classComponentColumnDescriptor



The descriptor of a component column.



Component columns contain the data for a specific component of an entity.



Column descriptors are used to describe the columns in a
Schema. They are read-only. To select a component
column, use ComponentColumnSelector.



##### archetype:strproperty



The archetype name, if any.



This property is read-only.



##### component:strproperty



The component.



This property is read-only.



##### component_type:str|Noneproperty



The component type, if any.



This property is read-only.



##### entity_path:strproperty



The entity path.



This property is read-only.



##### is_static:boolproperty



Whether the column is static.



This property is read-only.



##### name:strproperty



The name of this column.



This property is read-only.



#### classComponentColumnSelector



A selector for a component column.



Component columns contain the data for a specific component of an entity.



##### component:strproperty



The component.



This property is read-only.



##### entity_path:strproperty



The entity path.



This property is read-only.



##### def__init__(entity_path,component)



Create a new `ComponentColumnSelector`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| entity_path | The entity path to select.TYPE:str |
| component | The component to select. Example:Points3D:positions.TYPE:str |



#### classIndexColumnDescriptor



The descriptor of an index column.



Index columns contain the index values for when the data was updated. They
generally correspond to Rerun timelines.



Column descriptors are used to describe the columns in a
Schema. They are read-only. To select an index
column, use IndexColumnSelector.



##### is_static:boolproperty



Part of generic ColumnDescriptor interface: always False for Index.



##### name:strproperty



The name of the index.



This property is read-only.



#### classIndexColumnSelector



A selector for an index column.



Index columns contain the index values for when the data was updated. They
generally correspond to Rerun timelines.



##### name:strproperty



The name of the index.



This property is read-only.



##### def__init__(index)



Create a new `IndexColumnSelector`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| index | The name of the index to select. Usually the name of a timeline.TYPE:str |



#### classAlreadyExistsError



Bases: `Exception`



Raised when trying to create a resource that already exists.



#### classCatalogClient



Client for a remote Rerun catalog server.



Note: the `datafusion` package is required to use this client. Initialization will fail with an error if the package
is not installed.



##### ctx:datafusion.SessionContextproperty



Returns a DataFusion session context for querying the catalog.



##### url:strproperty



Returns the catalog URL.



##### defall_entries()deprecated

 Deprecated

Use entries() instead



Returns a list of all entries in the catalog.



##### defappend_to_table(table_name,batches=None,**named_params)deprecated

 Deprecated

Use TableEntry.append() instead



Append record batches to an existing table.



| PARAMETER | DESCRIPTION |
| --- | --- |
| table_name | The name of the table entry to write to. This table must already exist.TYPE:str |
| batches | One or more record batches to write into the table.TYPE:RecordBatchReader\|RecordBatch\|Sequence[RecordBatch] \|Sequence[Sequence[RecordBatch]] \| NoneDEFAULT:None |
| **named_params | Named parameters to write to the table as columns.TYPE:AnyDEFAULT:{} |



##### defcreate_dataset(name)



Creates a new dataset with the given name.



##### defcreate_table(name,schema,url)



Create and register a new table.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the table entry to create. It must be unique within all entries in the catalog. An exception will be raised if an entry with the same name already exists.TYPE:str |
| schema | The schema of the table to create.TYPE:Schema |
| url | The URL of the directory for where to store the Lance table.TYPE:str |



##### defcreate_table_entry(name,schema,url)deprecated

 Deprecated

Use create_table() instead



Create and register a new table.



##### defdataset_entries()deprecated

 Deprecated

Use datasets() instead



Returns a list of all dataset entries in the catalog.



##### defdataset_names(*,include_hidden=False)



Returns a list of all dataset names in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include blueprint datasets.TYPE:boolDEFAULT:False |



##### defdatasets(*,include_hidden=False)



Returns a list of all dataset entries in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include blueprint datasets.TYPE:boolDEFAULT:False |



##### defdo_global_maintenance()



Perform maintenance tasks on the whole system.



##### defentries(*,include_hidden=False)



Returns a list of all entries in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include hidden entries (blueprint datasets and system tables like__entries).TYPE:boolDEFAULT:False |



##### defentry_names(*,include_hidden=False)



Returns a list of all entry names in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include hidden entries (blueprint datasets and system tables like__entries).TYPE:boolDEFAULT:False |



##### defget_dataset(name=None,*,id=None)



Returns a dataset by its ID or name.



Exactly one of `id` or `name` must be provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the dataset.TYPE:str\| NoneDEFAULT:None |
| id | The unique identifier of the dataset. Can be anEntryIdobject or its string representation.TYPE:EntryId\|str\| NoneDEFAULT:None |



##### defget_dataset_entry(*,id=None,name=None)deprecated

 Deprecated

Use get_dataset() instead



Returns a dataset by its ID or name.



##### defget_table(name=None,*,id=None)



Returns a table by its ID or name.



Exactly one of `id` or `name` must be provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the table.TYPE:str\| NoneDEFAULT:None |
| id | The unique identifier of the table. Can be anEntryIdobject or its string representation.TYPE:EntryId\|str\| NoneDEFAULT:None |



##### defget_table_entry(*,id=None,name=None)deprecated

 Deprecated

Use get_table() instead



Returns a table by its ID or name.



##### defregister_table(name,url)



Registers a foreign Lance table (identified by its URL) as a new table entry with the given name.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the table entry to create. It must be unique within all entries in the catalog. An exception will be raised if an entry with the same name already exists.TYPE:str |
| url | The URL of the Lance table to register.TYPE:str |



##### deftable_entries()deprecated

 Deprecated

Use tables() instead



Returns a list of all dataset entries in the catalog.



##### deftable_names(*,include_hidden=False)



Returns a list of all table names in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include system tables (e.g.,__entries).TYPE:boolDEFAULT:False |



##### deftables(*,include_hidden=False)



Returns a list of all table entries in the catalog.



| PARAMETER | DESCRIPTION |
| --- | --- |
| include_hidden | If True, include system tables (e.g.,__entries).TYPE:boolDEFAULT:False |



##### defupdate_table(table_name,batches=None,**named_params)deprecated

 Deprecated

Use TableEntry.upsert() instead



Upsert record batches to an existing table.



| PARAMETER | DESCRIPTION |
| --- | --- |
| table_name | The name of the table entry to write to. This table must already exist.TYPE:str |
| batches | One or more record batches to write into the table.TYPE:RecordBatchReader\|RecordBatch\|Sequence[RecordBatch] \|Sequence[Sequence[RecordBatch]] \| NoneDEFAULT:None |
| **named_params | Named parameters to write to the table as columns.TYPE:AnyDEFAULT:{} |



##### defwrite_table(name,batches,insert_mode)deprecated

 Deprecated

Use TableEntry.append(), overwrite(), or upsert() instead



Writes record batches into an existing table.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | The name of the table entry to write to. This table must already exist.TYPE:str |
| batches | One or more record batches to write into the table. For convenience, you can pass in a record batch, list of record batches, list of list of batches, or a [pyarrow.RecordBatchReader].TYPE:RecordBatchReader\|RecordBatch\|Sequence[RecordBatch] \|Sequence[Sequence[RecordBatch]] |
| insert_mode | Determines how rows should be added to the existing table.TYPE:TableInsertMode |



#### classDatasetEntry



Bases: `Entry[DatasetEntryInternal]`



A dataset entry in the catalog.



##### catalog:CatalogClientproperty



The catalog client that this entry belongs to.



##### created_at:datetimeproperty



The entry's creation date and time.



##### id:EntryIdproperty



The entry's id.



##### kind:EntryKindproperty



The entry's kind.



##### manifest_url:strproperty



Return the dataset manifest URL.



##### name:strproperty



The entry's name.



##### updated_at:datetimeproperty



The entry's last updated date and time.



##### def__eq__(other)



Compare this entry to another object.



Supports comparison with `str` and `EntryId` to enable the following patterns:

```
"entry_name" in client.entries()
entry_id in client.entries()
```



##### defarrow_schema()



Return the Arrow schema of the data contained in the dataset.



##### defblueprint_dataset()



The associated blueprint dataset, if any.



##### defblueprints()



Lists all blueprints currently registered with this dataset.



##### defcreate_fts_index(*,column,time_index,store_position=False,base_tokenizer='simple')deprecated

 Deprecated

use create_fts_search_index



##### defcreate_fts_search_index(*,column,time_index,store_position=False,base_tokenizer='simple')



Create a full-text search index on the given column.



##### defcreate_vector_index(*,column,time_index,target_partition_num_rows=None,num_sub_vectors=16,distance_metric='Cosine')deprecated

 Deprecated

use create_vector_search_index instead



##### defcreate_vector_search_index(*,column,time_index,target_partition_num_rows=None,num_sub_vectors=16,distance_metric='Cosine')



Create a vector index on the given column.



This will enable indexing and build the vector index over all existing values
in the specified component column.



Results can be retrieved using the `search_vector` API, which will include
the time-point on the indexed timeline.



Only one index can be created per component column -- executing this a second
time for the same component column will replace the existing index.



| PARAMETER | DESCRIPTION |
| --- | --- |
| column | The component column to create the index on.TYPE:str\|ComponentColumnSelector\|ComponentColumnDescriptor |
| time_index | Which timeline this index will map to.TYPE:IndexColumnSelector |
| target_partition_num_rows | The target size (in number of rows) for each partition. The underlying indexer (lance) will pick a default when no value is specified - today this is 8192. It will also cap the maximum number of partitions independently of this setting - currently 4096.TYPE:int\| NoneDEFAULT:None |
| num_sub_vectors | The number of sub-vectors to use when building the index.TYPE:intDEFAULT:16 |
| distance_metric | The distance metric to use for the index. ("L2", "Cosine", "Dot", "Hamming")TYPE:VectorDistanceMetric\|strDEFAULT:'Cosine' |



##### defdefault_blueprint()



Return the name currently set blueprint.



##### defdefault_blueprint_partition_id()deprecated

 Deprecated

Use default_blueprint_segment_id() instead



The default blueprint partition ID for this dataset, if any.



##### defdelete()



Delete this entry from the catalog.



##### defdelete_indexes(column)deprecated

 Deprecated

use delete_search_indexes instead



##### defdelete_search_indexes(column)



Deletes all user-defined indexes for the specified column.



##### defdo_maintenance(optimize_indexes=False,retrain_indexes=False,compact_fragments=False,cleanup_before=None,unsafe_allow_recent_cleanup=False)



Perform maintenance tasks on the datasets.



##### defdownload_partition(partition_id)deprecated

 Deprecated

Use download_segment() instead



Download a partition from the dataset.



##### defdownload_segment(segment_id)



Download a segment from the dataset.



##### deffilter_contents(exprs)



Return a new DatasetView filtered to the given entity paths.



Entity path expressions support wildcards:
- `"/points/**"` matches all entities under /points
- `"-/text/**"` excludes all entities under /text



| PARAMETER | DESCRIPTION |
| --- | --- |
| exprs | Entity path expression or list of entity path expressions.TYPE:str\|Sequence[str] |



| RETURNS | DESCRIPTION |
| --- | --- |
| DatasetView | A new view filtered to the matching entity paths. |



Examples:



```
# Filter to a single entity path
view = dataset.filter_contents("/points/**")

# Filter to specific entity paths
view = dataset.filter_contents(["/points/**"])

# Exclude certain paths
view = dataset.filter_contents(["/points/**", "-/text/**"])

# Chain with segment filters
view = dataset.filter_segments(["recording_0"]).filter_contents("/points/**")
```



##### deffilter_segments(segment_ids)



Return a new DatasetView filtered to the given segment IDs.



| PARAMETER | DESCRIPTION |
| --- | --- |
| segment_ids | A segment ID string, a list of segment ID strings, or a DataFusion DataFrame with a column named 'rerun_segment_id'. When passing a DataFrame, if there are additional columns, they will be ignored.TYPE:str\|Sequence[str] \|DataFrame |



| RETURNS | DESCRIPTION |
| --- | --- |
| DatasetView | A new view filtered to the given segments. |



Examples:



```
# Filter to a single segment
view = dataset.filter_segments("recording_0")

# Filter to specific segments
view = dataset.filter_segments(["recording_0", "recording_1"])

# Filter using a DataFrame
good_segments = segment_table.filter(col("success"))
view = dataset.filter_segments(good_segments)

# Read data from the filtered view
df = view.reader(index="timeline")
```



##### deflist_indexes()deprecated

 Deprecated

use list_search_indexes instead



##### deflist_search_indexes()



List all user-defined indexes in this dataset.



##### defmanifest()



Return the dataset manifest as a DataFusion DataFrame.



##### defpartition_ids()deprecated

 Deprecated

Use segment_ids() instead



Returns a list of partition IDs for the dataset.



##### defpartition_url(partition_id,timeline=None,start=None,end=None)deprecated

 Deprecated

Use segment_url() instead



Return the URL for the given partition.



##### defreader(index,*,include_semantically_empty_columns=False,include_tombstone_columns=False,fill_latest_at=False,using_index_values=None)



Create a reader over this dataset.



Returns a DataFusion DataFrame.

 Server side filters

The returned DataFrame supports server side filtering for both `rerun_segment_id`
and the index (timeline) column, which can greatly improve performance. For
example, the following filters will effectively be handled by the Rerun server.



```
dataset.reader(index="real_time").filter(col("rerun_segment_id") == "aabbccddee")
dataset.reader(index="real_time").filter(col("real_time") == "1234567890")
dataset.reader(index="real_time").filter(
    (col("rerun_segment_id") == "aabbccddee") & (col("real_time") == "1234567890")
)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| index | The index (timeline) to use for the view. PassNoneto read only static data.TYPE:str\| None |
| include_semantically_empty_columns | Whether to include columns that are semantically empty.TYPE:boolDEFAULT:False |
| include_tombstone_columns | Whether to include tombstone columns.TYPE:boolDEFAULT:False |
| fill_latest_at | Whether to fill null values with the latest valid data.TYPE:boolDEFAULT:False |
| using_index_values | If provided, specifies the exact index values to sample for all segments. Can be a numpy array (datetime64[ns] or int64), a pyarrow Array, or a sequence. Use withfill_latest_at=Trueto populate rows with the most recent data.TYPE:IndexValuesLike\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| DataFrame | A DataFusion DataFrame. |



##### defregister(recording_uri,*,layer_name='base')



Register RRD URIs to the dataset and return a handle to track progress.



This method initiates the registration of recordings to the dataset, and returns
a handle that can be used to wait for completion or iterate over results.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recording_uri | The URI(s) of the RRD(s) to register. Can be a single URI string or a sequence of URIs.TYPE:str\|Sequence[str] |
| layer_name | The layer(s) to which the recordings will be registered to. Can be a single layer name (applied to all recordings) or a sequence of layer names (must match the length ofrecording_uri). Defaults to"base".TYPE:str\|Sequence[str]DEFAULT:'base' |



| RETURNS | DESCRIPTION |
| --- | --- |
| RegistrationHandle | A handle to track and wait on the registration tasks. |



##### defregister_blueprint(uri,set_default=True)



Register an existing .rbl visible to the server.



By default, also set this blueprint as default.



##### defregister_prefix(recordings_prefix,layer_name=None)



Register all RRDs under a given prefix to the dataset and return a handle to track progress.



A prefix is a directory-like path in an object store (e.g. an S3 bucket or ABS container).
All RRDs that are recursively found under the given prefix will be registered to the dataset.



This method initiates the registration of the recordings to the dataset, and returns
a handle that can be used to wait for completion or iterate over results.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recordings_prefix | The prefix under which to register all RRDs.TYPE:str |
| layer_name | The layer to which the recordings will be registered to. IfNone, this defaults to"base".TYPE:str\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| A handle to track and wait on the registration tasks. |  |



##### defschema()



Return the schema of the data contained in the dataset.



##### defsearch_fts(query,column)



Search the dataset using a full-text search query.



##### defsearch_vector(query,column,top_k)



Search the dataset using a vector search query.



##### defsegment_ids()



Returns a list of segment IDs for the dataset.



##### defsegment_table(join_meta=None,join_key='rerun_segment_id')



Return the segment table as a DataFusion DataFrame.



The segment table contains metadata about each segment in the dataset,
including segment IDs, layer names, storage URLs, and size information.



| PARAMETER | DESCRIPTION |
| --- | --- |
| join_meta | Optional metadata table or DataFrame to join with the segment table. If aTableEntryis provided, it will be converted to a DataFrame usingreader().TYPE:TableEntry\|DataFrame\| NoneDEFAULT:None |
| join_key | The column name to use for joining, defaults to "rerun_segment_id". Both the segment table andjoin_metamust contain this column.TYPE:strDEFAULT:'rerun_segment_id' |



| RETURNS | DESCRIPTION |
| --- | --- |
| DataFrame | The segment metadata table, optionally joined withjoin_meta. |



##### defsegment_url(segment_id,timeline=None,start=None,end=None)



Return the URL for the given segment.



| PARAMETER | DESCRIPTION |
| --- | --- |
| segment_id | The ID of the segment to get the URL for.TYPE:str |
| timeline | The name of the timeline to display.TYPE:str\| NoneDEFAULT:None |
| start | The start selected time for the segment. Integer for ticks, or datetime/nanoseconds for timestamps.TYPE:datetime\|int\| NoneDEFAULT:None |
| end | The end selected time for the segment. Integer for ticks, or datetime/nanoseconds for timestamps.TYPE:datetime\|int\| NoneDEFAULT:None |



Examples:



###### With ticks



```
>>> start_tick, end_time = 0, 10
>>> dataset.segment_url("some_id", "log_tick", start_tick, end_time)
```



###### With timestamps



```
>>> start_time, end_time = datetime.now() - timedelta(seconds=4), datetime.now()
>>> dataset.segment_url("some_id", "real_time", start_time, end_time)
```



| RETURNS | DESCRIPTION |
| --- | --- |
| str | The URL for the given segment. |



##### defset_default_blueprint(blueprint_name)



Set an already-registered blueprint as default for this dataset.



##### defset_default_blueprint_partition_id(partition_id)deprecated

 Deprecated

Use set_default_blueprint_segment_id() instead



Set the default blueprint partition ID for this dataset.



##### defupdate(*,name=None)



Update this entry's properties.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | New name for the entryTYPE:str\| NoneDEFAULT:None |



#### classDatasetView



A filtered view over a dataset in the catalog.



A `DatasetView` provides lazy filtering over a dataset's segments and entity paths.
Filters are composed lazily and only applied when data is actually read.



Create a `DatasetView` by calling `filter_segments()` or `filter_contents()` on a
`DatasetEntry`.



Examples:



```
# Filter to specific segments
view = dataset.filter_segments(["recording_0", "recording_1"])

# Filter to specific entity paths
view = dataset.filter_contents(["/points/**"])

# Chain filters
view = dataset.filter_segments(["recording_0"]).filter_contents(["/points/**"])

# Read data
df = view.reader(index="timeline")
```



##### def__init__(internal)



Create a new DatasetView wrapper.



| PARAMETER | DESCRIPTION |
| --- | --- |
| internal | The internal Rust-side DatasetView object.TYPE:DatasetViewInternal |



##### def__repr__()



Return a string representation of the DatasetView.



##### defarrow_schema()



Return the filtered Arrow schema for this view.



| RETURNS | DESCRIPTION |
| --- | --- |
| Schema | The filtered Arrow schema. |



##### defdownload_segment(segment_id)deprecated

 Deprecated

This method is deprecated and will be removed in a future release



Download a specific segment from the dataset.



| PARAMETER | DESCRIPTION |
| --- | --- |
| segment_id | The ID of the segment to download.TYPE:str |



| RETURNS | DESCRIPTION |
| --- | --- |
| Recording | The downloaded recording. |



##### deffilter_contents(exprs)



Return a new DatasetView filtered to the given entity paths.



Entity path expressions support wildcards:
- `"/points/**"` matches all entities under /points
- `"-/text/**"` excludes all entities under /text



| PARAMETER | DESCRIPTION |
| --- | --- |
| exprs | Entity path expression or list of entity path expressions.TYPE:str\|Sequence[str] |



| RETURNS | DESCRIPTION |
| --- | --- |
| DatasetView | A new view filtered to the matching entity paths. |



##### deffilter_segments(segment_ids)



Return a new DatasetView filtered to the given segment IDs.



Filters are composed: if this view already has a segment filter,
the result is the intersection of both filters.



| PARAMETER | DESCRIPTION |
| --- | --- |
| segment_ids | A segment ID string, a list of segment ID strings, or a DataFusion DataFrame with a column named 'rerun_segment_id'.TYPE:str\|Sequence[str] \|DataFrame |



| RETURNS | DESCRIPTION |
| --- | --- |
| DatasetView | A new view filtered to the given segments. |



##### defreader(index,*,include_semantically_empty_columns=False,include_tombstone_columns=False,fill_latest_at=False,using_index_values=None)



Create a reader over this DatasetView.



Returns a DataFusion DataFrame.

 Server side filters

The returned DataFrame supports server side filtering for both `rerun_segment_id`
and the index (timeline) column, which can greatly improve performance. For
example, the following filters will effectively be handled by the Rerun server.



```
dataset.reader(index="real_time").filter(col("rerun_segment_id") == "aabbccddee")
dataset.reader(index="real_time").filter(col("real_time") == "1234567890")
dataset.reader(index="real_time").filter(
    (col("rerun_segment_id") == "aabbccddee") & (col("real_time") == "1234567890")
)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| index | The index (timeline) to use for the view. PassNoneto read only static data.TYPE:str\| None |
| include_semantically_empty_columns | Whether to include columns that are semantically empty.TYPE:boolDEFAULT:False |
| include_tombstone_columns | Whether to include tombstone columns.TYPE:boolDEFAULT:False |
| fill_latest_at | Whether to fill null values with the latest valid data.TYPE:boolDEFAULT:False |
| using_index_values | If provided, specifies the exact index values to sample for all segments. Can be a numpy array (datetime64[ns] or int64), a pyarrow Array, or a sequence. Use withfill_latest_at=Trueto populate rows with the most recent data.TYPE:IndexValuesLike\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| A DataFusion DataFrame. |  |



##### defschema()



Return the filtered schema for this view.



The schema reflects any content filters applied to the view.



| RETURNS | DESCRIPTION |
| --- | --- |
| Schema | The filtered schema. |



##### defsegment_ids()



Return the segment IDs for this view.



If segment filters have been applied, only matching segments are returned.



| RETURNS | DESCRIPTION |
| --- | --- |
| list[str] | The list of segment IDs. |



##### defsegment_table(join_meta=None,join_key='rerun_segment_id')



Return the segment table as a DataFusion DataFrame.



The segment table contains metadata about each segment in the dataset,
including segment IDs, layer names, storage URLs, and size information.



Only segments matching this view's filters are included.



| PARAMETER | DESCRIPTION |
| --- | --- |
| join_meta | Optional metadata table or DataFrame to join with the segment table. If aTableEntryis provided, it will be converted to a DataFrame usingreader().TYPE:TableEntry\|DataFrame\| NoneDEFAULT:None |
| join_key | The column name to use for joining, defaults to "rerun_segment_id". Both the segment table andjoin_metamust contain this column.TYPE:strDEFAULT:'rerun_segment_id' |



| RETURNS | DESCRIPTION |
| --- | --- |
| DataFrame | The segment metadata table, optionally joined withjoin_meta. |



#### classEntry



Bases: `ABC`, `Generic[InternalEntryT]`



An entry in the catalog.



##### catalog:CatalogClientproperty



The catalog client that this entry belongs to.



##### created_at:datetimeproperty



The entry's creation date and time.



##### id:EntryIdproperty



The entry's id.



##### kind:EntryKindproperty



The entry's kind.



##### name:strproperty



The entry's name.



##### updated_at:datetimeproperty



The entry's last updated date and time.



##### def__eq__(other)



Compare this entry to another object.



Supports comparison with `str` and `EntryId` to enable the following patterns:

```
"entry_name" in client.entries()
entry_id in client.entries()
```



##### defdelete()



Delete this entry from the catalog.



##### defupdate(*,name=None)



Update this entry's properties.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | New name for the entryTYPE:str\| NoneDEFAULT:None |



#### classEntryId



A unique identifier for an entry in the catalog.



##### def__init__(id)



Create a new `EntryId` from a string.



##### def__str__()



Return str(self).



#### classEntryKind



The kinds of entries that can be stored in the catalog.



##### def__int__()



int(self)



##### def__str__()



Return str(self).



#### classNotFoundError



Bases: `Exception`



Raised when the requested resource is not found.



#### classRegistrationHandle



Handle to track and wait on segment registration tasks.



##### defiter_results(timeout_secs=None)



Stream completed registrations as they finish.



Uses the server's streaming API to yield results as tasks complete.
Each result is yielded exactly once when its task completes (success or error).



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeout_secs | Timeout in seconds. None for blocking. Note that using None doesn't guarantee that a TimeoutError will never be eventually raised for long-running tasks. Setting a timeout and polling is recommended for monitoring very large registration batches.TYPE:int\| NoneDEFAULT:None |



| YIELDS | DESCRIPTION |
| --- | --- |
| SegmentRegistrationResult | The result of each completed registration. |



| RAISES | DESCRIPTION |
| --- | --- |
| TimeoutError | If the timeout is reached before all tasks complete. |



##### defwait(timeout_secs=None)



Block until all registrations complete.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeout_secs | Timeout in seconds. None for blocking. Note that using None doesn't guarantee that a TimeoutError will never be eventually raised for long-running tasks. Setting a timeout and polling is recommended for monitoring very large registration batches.TYPE:int\| NoneDEFAULT:None |



| RETURNS | DESCRIPTION |
| --- | --- |
| RegistrationResult | The result containing the list of segment IDs in registration order. |



| RAISES | DESCRIPTION |
| --- | --- |
| ValueError | If any registration fails. |
| TimeoutError | If the timeout is reached before all tasks complete. |



#### classSegmentRegistrationResultdataclass



Result of a completed segment registration.



##### error:str|Noneinstance-attribute



Error message if registration failed, or `None` if successful.



##### is_error:boolproperty



Returns True if the registration failed.



##### is_success:boolproperty



Returns True if the registration was successful.



##### segment_id:str|Noneinstance-attribute



The resulting segment ID. May be `None` if registration failed.



##### uri:strinstance-attribute



The source URI that was registered.



#### classTableEntry



Bases: `Entry[TableEntryInternal]`



A table entry in the catalog.



Note: this object acts as a table provider for DataFusion.



##### catalog:CatalogClientproperty



The catalog client that this entry belongs to.



##### created_at:datetimeproperty



The entry's creation date and time.



##### id:EntryIdproperty



The entry's id.



##### kind:EntryKindproperty



The entry's kind.



##### name:strproperty



The entry's name.



##### storage_url:strproperty



The table's storage URL.



##### updated_at:datetimeproperty



The entry's last updated date and time.



##### def__datafusion_table_provider__()



Returns a DataFusion table provider capsule.



##### def__eq__(other)



Compare this entry to another object.



Supports comparison with `str` and `EntryId` to enable the following patterns:

```
"entry_name" in client.entries()
entry_id in client.entries()
```



##### defappend(batches=None,**named_params)



Append to the Table.



| PARAMETER | DESCRIPTION |
| --- | --- |
| batches | Arrow data to append to the table. Can be a RecordBatchReader, a single RecordBatch, a list of RecordBatches, or a list of lists of RecordBatches (as returned bydatafusion.DataFrame.collect()).TYPE:_BatchesType\| NoneDEFAULT:None |
| **named_params | Each named parameter corresponds to a column in the table.TYPE:AnyDEFAULT:{} |



##### defarrow_schema()



Returns the Arrow schema of the table.



##### defdelete()



Delete this entry from the catalog.



##### defoverwrite(batches=None,**named_params)



Overwrite the Table with new data.



| PARAMETER | DESCRIPTION |
| --- | --- |
| batches | Arrow data to overwrite the table with. Can be a RecordBatchReader, a single RecordBatch, a list of RecordBatches, or a list of lists of RecordBatches (as returned bydatafusion.DataFrame.collect()).TYPE:_BatchesType\| NoneDEFAULT:None |
| **named_params | Each named parameter corresponds to a column in the table.TYPE:AnyDEFAULT:{} |



##### defreader()



Registers the table with the DataFusion context and return a DataFrame.



##### defto_arrow_reader()



Convert this table to a [pyarrow.RecordBatchReader](https://arrow.apache.org/docs/python/generated/pyarrow.RecordBatchReader.html#pyarrow.RecordBatchReader).



##### defupdate(*,name=None)



Update this entry's properties.



| PARAMETER | DESCRIPTION |
| --- | --- |
| name | New name for the entryTYPE:str\| NoneDEFAULT:None |



##### defupsert(batches=None,**named_params)



Upsert data into the Table.



To use upsert, the table must contain a column with the metadata:

```
{"rerun:is_table_index" = "true"}
```



Any row with a matching index value will have the new data inserted.
Any row without a matching index value will be appended as a new row.



| PARAMETER | DESCRIPTION |
| --- | --- |
| batches | Arrow data to upsert into the table. Can be a RecordBatchReader, a single RecordBatch, a list of RecordBatches, or a list of lists of RecordBatches (as returned bydatafusion.DataFrame.collect()).TYPE:_BatchesType\| NoneDEFAULT:None |
| **named_params | Each named parameter corresponds to a column in the tableTYPE:AnyDEFAULT:{} |



#### classVectorDistanceMetric



Bases: `Enum`



Which distance metric for use for vector index.