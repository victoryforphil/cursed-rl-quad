---
source: https://ref.rerun.io/docs/python/stable/common/utilities
title: Utilities
---

# Utilities



### rerun.utilities



#### datafusion



DataFusion utilities.



##### collect



###### defcollect_to_string_list(df,col,remove_nulls=True)



Collect a single column of a DataFrame into a Python string list.



This is a convenience function. DataFusion collection returns a stream
of record batches. Sometimes it is preferable to extract a single column
out of all of these batches and convert it to a string.



| PARAMETER | DESCRIPTION |
| --- | --- |
| df | The input DataFusion DataFrameTYPE:DataFrame |
| col | The column to collect. You can provide either a string column name or a DataFusion expression.TYPE:str\|Expr |
| remove_nulls | If true, anynullvalues will be removed from the result. If false these will be converted into None.TYPE:boolDEFAULT:True |



##### functions



###### url_generation

 `def partition_url(dataset, *, partition_id_col=None, timestamp_col=None, timeline_name=None)` `deprecated` Deprecated

Use segment_url() instead



Compute the URL for a partition within a dataset.

 `def partition_url_udf(dataset)` `deprecated` Deprecated

Use segment_url_udf() instead



Create a UDF to the URL for a partition within a Dataset.

 `def partition_url_with_timeref_udf(dataset, timeline_name)` `deprecated` Deprecated

Use segment_url_with_timeref_udf() instead



Create a UDF to the URL for a partition within a Dataset with timestamp.

 `def segment_url(dataset, *, segment_id_col=None, timestamp_col=None, timeline_name=None)`

Compute the URL for a segment within a dataset.



This is a Rerun focused DataFusion function that will create a DataFusion
expression for the segment URL.



To manually invoke the underlying UDF, see `segment_url_udf` or
`segment_url_with_timeref_udf`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dataset | The input Rerun Dataset.TYPE:DatasetEntry |
| segment_id_col | The column containing the segment ID. If not provided, it will assume a default value ofrerun_segment_id. You may pass either a DataFusion expression or a string column name.TYPE:str\|Expr\| NoneDEFAULT:None |
| timestamp_col | If this parameter is passed in, generate a URL that will jump to a specific timestamp within the segment.TYPE:str\|Expr\| NoneDEFAULT:None |
| timeline_name | When used in combination withtimestamp_col, this specifies which timeline to seek along. By default this will use the same string as timestamp_col.TYPE:str\| NoneDEFAULT:None |

 `def segment_url_udf(dataset)`

Create a UDF to the URL for a segment within a Dataset.



This function will generate a UDF that expects one column of input,
a string containing the segment ID.

 `def segment_url_with_timeref_udf(dataset, timeline_name)`

Create a UDF to the URL for a segment within a Dataset with timestamp.



This function will generate a UDF that expects two columns of input,
a string containing the segment ID and the timestamp in nanoseconds.