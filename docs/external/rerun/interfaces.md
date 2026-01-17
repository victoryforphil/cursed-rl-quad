---
source: https://ref.rerun.io/docs/python/stable/common/interfaces
title: Interfaces
---

# Interfaces



### rerun



#### classComponentMixin



Bases: `ComponentBatchLike`



Makes components adhere to the `ComponentBatchLike` interface.



A single component will always map to a batch of size 1.



The class using the mixin must define the `_BATCH_TYPE` field, which should be a subclass of `BaseBatch`.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the rerun.ComponentBatchLike logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the rerun.ComponentBatchLike logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the rerun.ComponentBatchLike logging interface.



#### classComponentBatchLike



Bases: `Protocol`



Describes interface for objects that can be converted to batch of rerun Components.



##### defas_arrow_array()



Returns a `pyarrow.Array` of the component data.



#### classAsComponents



Bases: `Protocol`



Describes interface for interpreting an object as a bundle of Components.



##### defas_component_batches()



Returns an iterable of `ComponentBatchLike` objects.



Each object in the iterable must adhere to the `ComponentBatchLike` interface.



#### classComponentBatchLike



Bases: `Protocol`



Describes interface for objects that can be converted to batch of rerun Components.



##### defas_arrow_array()



Returns a `pyarrow.Array` of the component data.



#### classComponentColumn



A column of components that can be sent using `send_columns`.



This is represented by a ComponentBatch array that has been partitioned into multiple segments.
This is useful for reinterpreting a single contiguous batch as multiple sub-batches
to use with the [send_columns](../columnar_api/#rerun.send_columns) API.



##### def__init__(descriptor,component_batch,*,lengths=None)



Construct a new component column.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned column will be partitioned into unit-length sub-batches by default.
Use `ComponentColumn.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| descriptor | The component descriptor for this component batch.TYPE:str\|ComponentDescriptor |
| component_batch | The component batch to partition into a column.TYPE:ComponentBatchLike |
| lengths | The offsets to partition the component at. If specified,lengthsmust sum to the total length of the component batch. If left unspecified, it will default to unit-length batches.TYPE:ArrayLike\| NoneDEFAULT:None |



##### defas_arrow_array()



The component as an arrow batch.



Part of the rerun.ComponentBatchLike logging interface.



##### defcomponent_descriptor()



Returns the complete descriptor of the component.



Part of the rerun.ComponentBatchLike logging interface.



##### defpartition(lengths)



(Re)Partitions the column.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumn.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | The offsets to partition the component at.TYPE:ArrayLike |



| RETURNS | DESCRIPTION |
| --- | --- |
| The (re)partitioned column. |  |