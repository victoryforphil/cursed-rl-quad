---
source: https://ref.rerun.io/docs/python/stable/common/blueprint_datatypes
title: Datatypes
---

# Datatypes



### rerun.blueprint.datatypes



#### ComponentColumnSelectorArrayLike=ComponentColumnSelector|Sequence[ComponentColumnSelectorLike]module-attribute



A type alias for any ComponentColumnSelector-like array object.



#### ComponentColumnSelectorLike=ComponentColumnSelector|strmodule-attribute



A type alias for any ComponentColumnSelector-like object.



#### FilterByRangeArrayLike=FilterByRange|Sequence[FilterByRangeLike]module-attribute



A type alias for any FilterByRange-like array object.



#### FilterByRangeLike=FilterByRangemodule-attribute



A type alias for any FilterByRange-like object.



#### FilterIsNotNullArrayLike=FilterIsNotNull|Sequence[FilterIsNotNullLike]module-attribute



A type alias for any FilterIsNotNull-like array object.



#### FilterIsNotNullLike=FilterIsNotNull|blueprint_datatypes.ComponentColumnSelectorLikemodule-attribute



A type alias for any FilterIsNotNull-like object.



#### SelectedColumnsArrayLike=SelectedColumns|Sequence[SelectedColumnsLike]module-attribute



A type alias for any SelectedColumns-like array object.



#### SelectedColumnsLike=SelectedColumns|Sequence[blueprint_datatypes.ComponentColumnSelectorLike|datatypes.Utf8Like]module-attribute



A type alias for any SelectedColumns-like object.



#### TensorDimensionIndexSliderArrayLike=TensorDimensionIndexSlider|Sequence[TensorDimensionIndexSliderLike]|npt.ArrayLikemodule-attribute



A type alias for any TensorDimensionIndexSlider-like array object.



#### TensorDimensionIndexSliderLike=TensorDimensionIndexSlider|intmodule-attribute



A type alias for any TensorDimensionIndexSlider-like object.



#### TextLogColumnArrayLike=TextLogColumn|Sequence[TextLogColumnLike]module-attribute



A type alias for any TextLogColumn-like array object.



#### TextLogColumnKindArrayLike=TextLogColumnKind|Literal['Body','EntityPath','LogLevel','body','entitypath','loglevel']|int|Sequence[TextLogColumnKindLike]module-attribute



A type alias for any TextLogColumnKind-like array object.



#### TextLogColumnKindLike=TextLogColumnKind|Literal['Body','EntityPath','LogLevel','body','entitypath','loglevel']|intmodule-attribute



A type alias for any TextLogColumnKind-like object.



#### TextLogColumnLike=TextLogColumn|blueprint_datatypes.TextLogColumnKindLikemodule-attribute



A type alias for any TextLogColumn-like object.



#### TimelineColumnArrayLike=TimelineColumn|Sequence[TimelineColumnLike]module-attribute



A type alias for any TimelineColumn-like array object.



#### TimelineColumnLike=TimelineColumn|datatypes.Utf8Likemodule-attribute



A type alias for any TimelineColumn-like object.



#### classComponentColumnSelector



Bases: `ComponentColumnSelectorExt`



**Datatype**: Describe a component column to be selected in the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(spec=None,*,entity_path=None,component=None)



Create a new instance of the ComponentColumnSelector datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| spec | A string in the format "/entity/path:Component". If used,entity_pathandcomponentmust beNone.TYPE:str\| NoneDEFAULT:None |
| entity_path | The column's entity path. If used,specmust beNoneandcomponentmust be provided.TYPE:EntityPathLike\| NoneDEFAULT:None |
| component | The column's component type. If used,specmust beNoneandentity_pathmust be provided.TYPE:Utf8Like\| NoneDEFAULT:None |



#### classFilterByRange



Bases: `FilterByRangeExt`



**Datatype**: Configuration for the filter-by-range feature of the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(start,end)



Create a new instance of the FilterByRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start | Beginning of the time range.TYPE:TimeIntLike |
| end | End of the time range (inclusive).TYPE:TimeIntLike |



#### classFilterIsNotNull



Bases: `FilterIsNotNullExt`



**Datatype**: Configuration for the filter is not null feature of the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(active,column)



Create a new instance of the FilterIsNotNull datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| active | Whether the filter by event feature is active.TYPE:BoolLike |
| column | The column used when the filter by event feature is used.TYPE:ComponentColumnSelectorLike |



#### classSelectedColumns



Bases: `SelectedColumnsExt`



**Datatype**: List of selected columns in a dataframe.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(columns)



Create a new instance of the `SelectedColumns` datatype.



Example:

```
SelectedColumns(["timeline", "/entity/path:Component"])
```



| PARAMETER | DESCRIPTION |
| --- | --- |
| columns | The columns to include.The column must be either of the timeline, or component kind. Timeline columns can be specified using astrwithout any:, or anUtf8. Component columns can be specified using either astrin the form of"/entity/path:Component", or aComponentColumnSelector.TYPE:Sequence[ComponentColumnSelectorLike\|Utf8Like] |



#### classTensorDimensionIndexSlider



Bases: `TensorDimensionIndexSliderExt`



**Datatype**: Defines a slider for the index of some dimension.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(dimension)



Create a new instance of the TensorDimensionIndexSlider datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number.TYPE:TensorDimensionIndexSliderLike |



#### classTextLogColumn



Bases: `TextLogColumnExt`



**Datatype**: A text log column.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(kind,*,visible=True)



Create a new instance of the TextLogColumn datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| kind | What kind of column is this?TYPE:TextLogColumnKindLike |
| visible | Is this column visible?TYPE:BoolLikeDEFAULT:True |



#### classTextLogColumnKind



Bases: `Enum`



**Datatype**: A text log column kind.



##### Body=3class-attributeinstance-attribute



The text message the log has.



##### EntityPath=1class-attributeinstance-attribute



Which entity path this was logged to.



##### LogLevel=2class-attributeinstance-attribute



The log level, i.e INFO, WARN, ERROR.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classTimelineColumn



Bases: `TimelineColumnExt`



**Datatype**: A timeline column in a table.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(timeline,*,visible=True)



Create a new instance of the TextLogColumn datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | What timeline is this?TYPE:Utf8Like |
| visible | Is this column visible?TYPE:BoolLikeDEFAULT:True |