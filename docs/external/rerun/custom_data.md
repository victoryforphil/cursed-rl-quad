---
source: https://ref.rerun.io/docs/python/stable/common/custom_data
title: Custom Data
---

# Custom Data



### rerun



#### classAnyValues



Bases: `AsComponents`



Helper to log arbitrary values as a bundle of components.

 Example

```
rr.log(
    "any_values", rr.AnyValues(
        confidence=[1.2, 3.4, 5.6],
        description="Bla bla blaâ¦",
        # URIs will become clickable links
        homepage="https://www.rerun.io",
        repository="https://github.com/rerun-io/rerun",
    ),
)
```



##### def__init__(drop_untyped_nones=True,**kwargs)



Construct a new AnyValues bundle.



Each kwarg will be logged as a separate component batch using the provided data.
 - The key will be used as the name of the component
 - The value must be able to be converted to an array of arrow types. In
   general, if you can pass it to [pyarrow.array](https://arrow.apache.org/docs/python/generated/pyarrow.array.html#pyarrow.array) you can log it as a
   extension component.



Note: rerun requires that a given component only take on a single type.
The first type logged will be the type that is used for all future logs
of that component. The API will make a best effort to do type conversion
if supported by numpy and arrow. Any components that can't be converted
will result in a warning (or an exception in strict mode).



`None` values provide a particular challenge as they have no type
information until after the component has been logged with a particular
type. By default, these values are dropped. This should generally be
fine as logging `None` to clear the value before it has been logged is
meaningless unless you are logging out-of-order data. In such cases,
consider introducing your own typed component via
[rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike).



You can change this behavior by setting `drop_untyped_nones` to `False`,
but be aware that this will result in potential warnings (or exceptions
in strict mode).



If you are want to inspect how your component will be converted to the
underlying arrow code, the following snippet is what is happening
internally:

```
np_value = np.atleast_1d(np.array(value, copy=False))
pa_value = pa.array(value)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| drop_untyped_nones | If True, any components that are either None or empty will be dropped unless they have been previously logged with a type.TYPE:boolDEFAULT:True |
| kwargs | The components to be logged.TYPE:AnyDEFAULT:{} |



##### defcolumns(drop_untyped_nones=True,**kwargs)classmethod



Construct a new column-oriented AnyValues bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



Each kwarg will be logged as a separate component column using the provided data.
 - The key will be used as the name of the component
 - The value must be able to be converted to an array of arrow types. In
   general, if you can pass it to [pyarrow.array](https://arrow.apache.org/docs/python/generated/pyarrow.array.html#pyarrow.array) you can log it as a
   extension component.



Note: rerun requires that a given component only take on a single type.
The first type logged will be the type that is used for all future logs
of that component. The API will make a best effort to do type conversion
if supported by numpy and arrow. Any components that can't be converted
will result in a warning (or an exception in strict mode).



`None` values provide a particular challenge as they have no type
information until after the component has been logged with a particular
type. By default, these values are dropped. This should generally be
fine as logging `None` to clear the value before it has been logged is
meaningless unless you are logging out-of-order data. In such cases,
consider introducing your own typed component via
[rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike).



You can change this behavior by setting `drop_untyped_nones` to `False`,
but be aware that this will result in potential warnings (or exceptions
in strict mode).



If you are want to inspect how your component will be converted to the
underlying arrow code, the following snippet is what is happening
internally:

```
np_value = np.atleast_1d(np.array(value, copy=False))
pa_value = pa.array(value)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| drop_untyped_nones | If True, any components that are either None or empty will be dropped unless they have been previously logged with a type.TYPE:boolDEFAULT:True |
| kwargs | The components to be logged.TYPE:AnyDEFAULT:{} |



##### defwith_component_from_data(descriptor,value,*,drop_untyped_nones=True)



Adds an `AnyValueBatch` to this `AnyValues` bundle.



##### defwith_component_override(field,component_type,value,*,drop_untyped_nones=True)



Adds an `AnyValueBatch` to this `AnyValues` bundle with name and component type.



#### classAnyBatchValue



Bases: `ComponentBatchLike`



Helper to log arbitrary data as a component batch or column.



This is a very simple helper that implements the `ComponentBatchLike` interface on top
of the `pyarrow` library array conversion functions.



See also rerun.AnyValues.



##### def__init__(descriptor,value,*,drop_untyped_nones=True)



Construct a new AnyBatchValue.



The value will be attempted to be converted into an arrow array by first calling
the `as_arrow_array()` method if it's defined. All Rerun Batch datatypes implement
this function so it's possible to pass them directly to AnyValues.



If the object doesn't implement `as_arrow_array()`, it will be passed as an argument
to [pyarrow.array](https://arrow.apache.org/docs/python/generated/pyarrow.array.html#pyarrow.array) .



Note: rerun requires that a given component only take on a single type.
The first type logged will be the type that is used for all future logs
of that component. The API will make a best effort to do type conversion
if supported by numpy and arrow. Any components that can't be converted
will be dropped, and a warning will be sent to the log.



If you are want to inspect how your component will be converted to the
underlying arrow code, we first attempt to cast it directly to a pyarrow
array. Failing this, we call



```
pa_scalar = pa.scalar(value)
pa_value = pa.array(pa_scalar)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| descriptor | Either the name or the full descriptor of the component.TYPE:str\|ComponentDescriptor |
| value | The data to be logged as a component.TYPE:Any |
| drop_untyped_nones | If True, any components that are either None or empty will be dropped unless they have been previously logged with a type.TYPE:boolDEFAULT:True |



##### defcolumn(descriptor,value,drop_untyped_nones=True)classmethod



Construct a new column-oriented AnyBatchValue.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumn.partition` to repartition the data as needed.



The value will be attempted to be converted into an arrow array by first calling
the `as_arrow_array()` method if it's defined. All Rerun Batch datatypes implement
this function so it's possible to pass them directly to AnyValues.



If the object doesn't implement `as_arrow_array()`, it will be passed as an argument
to [pyarrow.array](https://arrow.apache.org/docs/python/generated/pyarrow.array.html#pyarrow.array) .



Note: rerun requires that a given component only take on a single type.
The first type logged will be the type that is used for all future logs
of that component. The API will make a best effort to do type conversion
if supported by numpy and arrow. Any components that can't be converted
will be dropped, and a warning will be sent to the log.



If you want to inspect how your component will be converted to the
underlying arrow code, the following snippet is what is happening
internally:



```
np_value = np.atleast_1d(np.array(value, copy=False))
pa_value = pa.array(value)
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| descriptor | Either the name or the full descriptor of the component.TYPE:str\|ComponentDescriptor |
| value | The data to be logged as a component.TYPE:Any |
| drop_untyped_nones | If True, any components that are either None or empty will be dropped unless they have been previously logged with a type.TYPE:boolDEFAULT:True |



#### classComponentDescriptor



A `ComponentDescriptor` fully describes the semantics of a column of data.



Every component at a given entity path is uniquely identified by the
`component` field of the descriptor. The `archetype` and `component_type`
fields provide additional information about the semantics of the data.



##### archetype:str|Noneproperty



Optional name of the `Archetype` associated with this data.



`None` if the data wasn't logged through an archetype.



Example: `rerun.archetypes.Points3D`.



##### component:strproperty



Uniquely identifies of the component associated with this data.



Example: `Points3D:positions`.



##### component_type:str|Noneproperty



Optional type information for this component.



Can be used to inform applications on how to interpret the data.



Example: `rerun.components.Position3D`.



##### def__init__(component,archetype=None,component_type=None)



Creates a component descriptor.



##### defor_with_overrides(archetype=None,component_type=None)



Sets `archetype` and `component_type` to the given one iff it's not already set.



##### defwith_builtin_archetype(archetype)



Sets `archetype` in a format similar to built-in archetypes.



##### defwith_overrides(archetype=None,component_type=None)



Unconditionally sets `archetype` and `component_type` to the given ones (if specified).