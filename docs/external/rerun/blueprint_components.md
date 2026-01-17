---
source: https://ref.rerun.io/docs/python/stable/common/blueprint_components
title: Components
---

# Components



### rerun.blueprint.components



#### BackgroundKindArrayLike=BackgroundKind|Literal['GradientBright','GradientDark','SolidColor','gradientbright','gradientdark','solidcolor']|int|Sequence[BackgroundKindLike]module-attribute



A type alias for any BackgroundKind-like array object.



#### BackgroundKindLike=BackgroundKind|Literal['GradientBright','GradientDark','SolidColor','gradientbright','gradientdark','solidcolor']|intmodule-attribute



A type alias for any BackgroundKind-like object.



#### ContainerKindArrayLike=ContainerKind|Literal['Grid','Horizontal','Tabs','Vertical','grid','horizontal','tabs','vertical']|int|Sequence[ContainerKindLike]module-attribute



A type alias for any ContainerKind-like array object.



#### ContainerKindLike=ContainerKind|Literal['Grid','Horizontal','Tabs','Vertical','grid','horizontal','tabs','vertical']|intmodule-attribute



A type alias for any ContainerKind-like object.



#### Corner2DArrayLike=Corner2D|Literal['LeftBottom','LeftTop','RightBottom','RightTop','leftbottom','lefttop','rightbottom','righttop']|int|Sequence[Corner2DLike]module-attribute



A type alias for any Corner2D-like array object.



#### Corner2DLike=Corner2D|Literal['LeftBottom','LeftTop','RightBottom','RightTop','leftbottom','lefttop','rightbottom','righttop']|intmodule-attribute



A type alias for any Corner2D-like object.



#### Eye3DKindArrayLike=Eye3DKind|Literal['FirstPerson','Orbital','firstperson','orbital']|int|Sequence[Eye3DKindLike]module-attribute



A type alias for any Eye3DKind-like array object.



#### Eye3DKindLike=Eye3DKind|Literal['FirstPerson','Orbital','firstperson','orbital']|intmodule-attribute



A type alias for any Eye3DKind-like object.



#### LinkAxisArrayLike=LinkAxis|Literal['Independent','LinkToGlobal','independent','linktoglobal']|int|Sequence[LinkAxisLike]module-attribute



A type alias for any LinkAxis-like array object.



#### LinkAxisLike=LinkAxis|Literal['Independent','LinkToGlobal','independent','linktoglobal']|intmodule-attribute



A type alias for any LinkAxis-like object.



#### LoopModeArrayLike=LoopMode|Literal['All','Off','Selection','all','off','selection']|int|Sequence[LoopModeLike]module-attribute



A type alias for any LoopMode-like array object.



#### LoopModeLike=LoopMode|Literal['All','Off','Selection','all','off','selection']|intmodule-attribute



A type alias for any LoopMode-like object.



#### MapProviderArrayLike=MapProvider|Literal['MapboxDark','MapboxLight','MapboxSatellite','MapboxStreets','OpenStreetMap','mapboxdark','mapboxlight','mapboxsatellite','mapboxstreets','openstreetmap']|int|Sequence[MapProviderLike]module-attribute



A type alias for any MapProvider-like array object.



#### MapProviderLike=MapProvider|Literal['MapboxDark','MapboxLight','MapboxSatellite','MapboxStreets','OpenStreetMap','mapboxdark','mapboxlight','mapboxsatellite','mapboxstreets','openstreetmap']|intmodule-attribute



A type alias for any MapProvider-like object.



#### PanelStateArrayLike=PanelState|Literal['Collapsed','Expanded','Hidden','collapsed','expanded','hidden']|int|Sequence[PanelStateLike]module-attribute



A type alias for any PanelState-like array object.



#### PanelStateLike=PanelState|Literal['Collapsed','Expanded','Hidden','collapsed','expanded','hidden']|intmodule-attribute



A type alias for any PanelState-like object.



#### PlayStateArrayLike=PlayState|Literal['Following','Paused','Playing','following','paused','playing']|int|Sequence[PlayStateLike]module-attribute



A type alias for any PlayState-like array object.



#### PlayStateLike=PlayState|Literal['Following','Paused','Playing','following','paused','playing']|intmodule-attribute



A type alias for any PlayState-like object.



#### ViewFitArrayLike=ViewFit|Literal['Fill','FillKeepAspectRatio','Original','fill','fillkeepaspectratio','original']|int|Sequence[ViewFitLike]module-attribute



A type alias for any ViewFit-like array object.



#### ViewFitLike=ViewFit|Literal['Fill','FillKeepAspectRatio','Original','fill','fillkeepaspectratio','original']|intmodule-attribute



A type alias for any ViewFit-like object.



#### classAbsoluteTimeRange



Bases: `AbsoluteTimeRange`, `ComponentMixin`



**Component**: A reference to a range of time.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(min,max)



Create a new instance of the AbsoluteTimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| min | Beginning of the time range.TYPE:TimeIntLike |
| max | End of the time range.TYPE:TimeIntLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classActiveTab



Bases: `EntityPath`, `ComponentMixin`



**Component**: The active tab in a tabbed container.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(path)



Create a new instance of the EntityPath datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classAngularSpeed



Bases: `Float64`, `ComponentMixin`



**Component**: Angular speed, used for rotation speed for example.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classApplyLatestAt



Bases: `Bool`, `ComponentMixin`



**Component**: Whether empty cells in a dataframe should be filled with a latest-at query.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Bool datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classAutoLayout



Bases: `Bool`, `ComponentMixin`



**Component**: Whether the viewport layout is determined automatically.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Bool datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classAutoViews



Bases: `Bool`, `ComponentMixin`



**Component**: Whether or not views should be created automatically.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Bool datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classBackgroundKind



Bases: `Enum`



**Component**: The type of the background in a view.



##### GradientBright=2class-attributeinstance-attribute



A bright gradient.



In 3D views it changes depending on the direction of the view.



##### GradientDark=1class-attributeinstance-attribute



A dark gradient.



In 3D views it changes depending on the direction of the view.



##### SolidColor=3class-attributeinstance-attribute



Simple uniform color.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classColumnShare



Bases: `Float32`, `ComponentMixin`



**Component**: The layout share of a column in the container.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classComponentColumnSelector



Bases: `ComponentColumnSelector`, `ComponentMixin`



**Component**: Describe a component column to be selected in the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(spec=None,*,entity_path=None,component=None)



Create a new instance of the ComponentColumnSelector datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| spec | A string in the format "/entity/path:Component". If used,entity_pathandcomponentmust beNone.TYPE:str\| NoneDEFAULT:None |
| entity_path | The column's entity path. If used,specmust beNoneandcomponentmust be provided.TYPE:EntityPathLike\| NoneDEFAULT:None |
| component | The column's component type. If used,specmust beNoneandentity_pathmust be provided.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classContainerKind



Bases: `Enum`



**Component**: The kind of a blueprint container (tabs, grid, â¦).



##### Grid=4class-attributeinstance-attribute



Organize children in a grid layout



##### Horizontal=2class-attributeinstance-attribute



Order the children left to right



##### Tabs=1class-attributeinstance-attribute



Put children in separate tabs



##### Vertical=3class-attributeinstance-attribute



Order the children top to bottom



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classCorner2D



Bases: `Enum`



**Component**: One of four 2D corners, typically used to align objects.



##### LeftBottom=3class-attributeinstance-attribute



Left bottom corner.



##### LeftTop=1class-attributeinstance-attribute



Left top corner.



##### RightBottom=4class-attributeinstance-attribute



Right bottom corner.



##### RightTop=2class-attributeinstance-attribute



Right top corner.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classEnabled



Bases: `Bool`, `ComponentMixin`



**Component**: Whether a procedure is enabled.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Bool datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classEye3DKind



Bases: `Enum`



**Component**: The kind of the 3D eye to view a scene in a [views.Spatial3DView](../blueprint_views/#rerun.blueprint.views.Spatial3DView).



This is used to specify how the controls of the view react to user input (such as mouse gestures).



##### FirstPerson=1class-attributeinstance-attribute



First person point of view.



The camera perspective as if one is seeing it through the eyes of a person as popularized by first-person games.
The center of rotation is the position of the eye (the camera).
Dragging the mouse on the spatial 3D view, will rotation the scene as if one is moving
their head around.



##### Orbital=2class-attributeinstance-attribute



Orbital eye.



The center of rotation is located to a center location in front of the eye (it is different from the eye
location itself), as if the eye was orbiting around the scene.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classFilterByRange



Bases: `FilterByRange`, `ComponentMixin`



**Component**: Configuration for a filter-by-range feature of the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(start,end)



Create a new instance of the FilterByRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start | Beginning of the time range.TYPE:TimeIntLike |
| end | End of the time range (inclusive).TYPE:TimeIntLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classFilterIsNotNull



Bases: `FilterIsNotNull`, `ComponentMixin`



**Component**: Configuration for the filter is not null feature of the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(active,column)



Create a new instance of the FilterIsNotNull datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| active | Whether the filter by event feature is active.TYPE:BoolLike |
| column | The column used when the filter by event feature is used.TYPE:ComponentColumnSelectorLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classForceDistance



Bases: `Float64`, `ComponentMixin`



**Component**: The target distance between two nodes.



This is helpful to scale the layout, for example if long labels are involved.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classForceIterations



Bases: `UInt64`, `ComponentMixin`



**Component**: Specifies how often this force should be applied per iteration.



Increasing this parameter can lead to better results at the cost of longer computation time.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the UInt64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classForceStrength



Bases: `Float64`, `ComponentMixin`



**Component**: The strength of a given force.



Allows to assign different weights to the individual forces, prioritizing one over the other.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classFps



Bases: `Float64`, `ComponentMixin`



**Component**: Frames per second for a sequence timeline.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classGridColumns



Bases: `UInt32`, `ComponentMixin`



**Component**: How many columns a grid container should have.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the UInt32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classGridSpacing



Bases: `Float32`, `ComponentMixin`



**Component**: Space between grid lines of one line to the next in scene units.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classIncludedContent



Bases: `EntityPath`, `ComponentMixin`



**Component**: All the contents in the container.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(path)



Create a new instance of the EntityPath datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLinkAxis



Bases: `Enum`



**Component**: How should the horizontal/X/time axis be linked across multiple plots.



##### Independent=1class-attributeinstance-attribute



The axis is independent from all other plots.



##### LinkToGlobal=2class-attributeinstance-attribute



Link to all other plots that also have this options set.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classLockRangeDuringZoom



Bases: `Bool`, `ComponentMixin`



**Component**: Indicate whether the range should be locked when zooming in on the data.



Default is `false`, i.e. zoom will change the visualized range.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Bool datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLoopMode



Bases: `Enum`



**Component**: If playing, whether and how the playback time should loop.



##### All=3class-attributeinstance-attribute



We are looping the entire recording.



The loop selection is ignored.



##### Off=1class-attributeinstance-attribute



Looping is off.



##### Selection=2class-attributeinstance-attribute



We are looping within the current loop selection.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classMapProvider



Bases: `Enum`



**Component**: Name of the map provider to be used in Map views.



##### MapboxDark=3class-attributeinstance-attribute



Mapbox Dark is a dark-themed map designed by Mapbox.



##### MapboxLight=5class-attributeinstance-attribute



Mapbox Light is a light-themed map designed by Mapbox.



##### MapboxSatellite=4class-attributeinstance-attribute



Mapbox Satellite is a satellite map designed by Mapbox.



##### MapboxStreets=2class-attributeinstance-attribute



Mapbox Streets is a minimalistic map designed by Mapbox.



##### OpenStreetMap=1class-attributeinstance-attribute



`OpenStreetMap` is the default map provider.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classNearClipPlane



Bases: `Float32`, `ComponentMixin`



**Component**: Distance to the near clip plane used for `Spatial2DView`.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classPanelState



Bases: `Enum`



**Component**: Tri-state for panel controls.



##### Collapsed=2class-attributeinstance-attribute



Visible, but as small as possible on its shorter axis.



##### Expanded=3class-attributeinstance-attribute



Fully expanded.



##### Hidden=1class-attributeinstance-attribute



Completely hidden.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classPlayState



Bases: `Enum`



**Component**: The current play state.



##### Following=3class-attributeinstance-attribute



Follow the latest available data.



##### Paused=1class-attributeinstance-attribute



Time doesn't move.



##### Playing=2class-attributeinstance-attribute



Time move steadily.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classPlaybackSpeed



Bases: `Float64`, `ComponentMixin`



**Component**: A playback speed which determines how fast time progresses.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classQueryExpression



Bases: `Utf8`, `ComponentMixin`



**Component**: An individual query expression used to filter a set of [datatypes.EntityPath](../datatypes/#rerun.datatypes.EntityPath)s.



Each expression is either an inclusion or an exclusion expression.
Inclusions start with an optional `+` and exclusions must start with a `-`.



Multiple expressions are combined together as part of [archetypes.ViewContents](../blueprint_archetypes/#rerun.blueprint.archetypes.ViewContents).



The `/**` suffix matches the whole subtree, i.e. self and any child, recursively
(`/world/**` matches both `/world` and `/world/car/driver`).
Other uses of `*` are not (yet) supported.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Utf8 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classRootContainer



Bases: `Uuid`, `ComponentMixin`



**Component**: The container that sits at the root of a viewport.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(bytes)



Create a new instance of the Uuid datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| bytes | The raw bytes representing the UUID.TYPE:UuidLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classRowShare



Bases: `Float32`, `ComponentMixin`



**Component**: The layout share of a row in the container.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classSelectedColumns



Bases: `SelectedColumns`, `ComponentMixin`



**Component**: Describe a component column to be selected in the dataframe view.



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



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTensorDimensionIndexSlider



Bases: `TensorDimensionIndexSlider`, `ComponentMixin`



**Component**: Show a slider for the index of some dimension of a slider.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(dimension)



Create a new instance of the TensorDimensionIndexSlider datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number.TYPE:TensorDimensionIndexSliderLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTextLogColumn



Bases: `TextLogColumn`, `ComponentMixin`



**Component**: A text log column.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(kind,*,visible=True)



Create a new instance of the TextLogColumn datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| kind | What kind of column is this?TYPE:TextLogColumnKindLike |
| visible | Is this column visible?TYPE:BoolLikeDEFAULT:True |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTimeInt



Bases: `TimeInt`, `ComponentMixin`



**Component**: A reference to a time.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,seq=None,seconds=None,nanos=None)



Create a new instance of the TimeInt datatype.



Exactly one of `seq`, `seconds`, or `nanos` must be provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| seq | Time as a sequence number.TYPE:int\| NoneDEFAULT:None |
| seconds | Time in seconds.Interpreted either as a duration or time since unix epoch (depending on timeline type).TYPE:float\| NoneDEFAULT:None |
| nanos | Time in nanoseconds.Interpreted either as a duration or time since unix epoch (depending on timeline type).TYPE:int\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTimeRange



Bases: `TimeRange`, `ComponentMixin`



**Component**: A time range on an unspecified timeline using either relative or absolute boundaries.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(start,end)



Create a new instance of the TimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start | Low time boundary for sequence timeline.TYPE:TimeRangeBoundaryLike |
| end | High time boundary for sequence timeline.TYPE:TimeRangeBoundaryLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTimelineColumn



Bases: `TimelineColumn`, `ComponentMixin`



**Component**: A timeline column in a text log table.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(timeline,*,visible=True)



Create a new instance of the TextLogColumn datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | What timeline is this?TYPE:Utf8Like |
| visible | Is this column visible?TYPE:BoolLikeDEFAULT:True |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTimelineName



Bases: `Utf8`, `ComponentMixin`



**Component**: A timeline identified by its name.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Utf8 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classViewClass



Bases: `Utf8`, `ComponentMixin`



**Component**: The class identifier of view, e.g. `"2D"`, `"TextLog"`, â¦.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Utf8 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classViewFit



Bases: `Enum`



**Component**: Determines whether an image or texture should be scaled to fit the viewport.



##### Fill=2class-attributeinstance-attribute



Scale the image for the largest possible fit in the view's container.



##### FillKeepAspectRatio=3class-attributeinstance-attribute



Scale the image for the largest possible fit in the view's container, but keep the original aspect ratio.



##### Original=1class-attributeinstance-attribute



No scaling, pixel size will match the image's width/height dimensions in pixels.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classViewMaximized



Bases: `Uuid`, `ComponentMixin`



**Component**: Whether a view is maximized.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(bytes)



Create a new instance of the Uuid datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| bytes | The raw bytes representing the UUID.TYPE:UuidLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classViewOrigin



Bases: `EntityPath`, `ComponentMixin`



**Component**: The origin of a view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(path)



Create a new instance of the EntityPath datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classViewerRecommendationHash



Bases: `UInt64`, `ComponentMixin`



**Component**: Hash of a viewer recommendation.



The formation of this hash is considered an internal implementation detail of the viewer.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the UInt64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVisibleTimeRange



Bases: `VisibleTimeRange`, `ComponentMixin`



**Component**: The range of values on a given timeline that will be included in a view's query.



Refer to `VisibleTimeRanges` archetype for more information.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(timeline,range=None,*,start=None,end=None)



Create a new instance of the VisibleTimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | Name of the timeline this applies to.TYPE:Utf8Like |
| range | Time range to use for this timeline.TYPE:TimeRangeLike\| NoneDEFAULT:None |
| start | Low time boundary for sequence timeline. Specify this instead ofrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |
| end | High time boundary for sequence timeline. Specify this instead ofrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVisualBounds2D



Bases: `VisualBounds2DExt`, `Range2D`, `ComponentMixin`



**Component**: Visual bounds in 2D space used for `Spatial2DView`.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,x_range,y_range)



Create a new instance of the VisualBounds2D component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| x_range | The minimum visible range of the X-axis (usually left and right bounds).TYPE:Range1DLike |
| y_range | The minimum visible range of the Y-axis (usually left and right bounds).TYPE:Range1DLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVisualizerOverride



Bases: `Utf8`, `ComponentMixin`



**Component**: Single visualizer override the visualizers for an entity.



For details see [archetypes.VisualizerOverrides](../blueprint_archetypes/#rerun.blueprint.archetypes.VisualizerOverrides).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Utf8 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classZoomLevel



Bases: `Float64`, `ComponentMixin`



**Component**: A zoom level determines how much of the world is visible on a map.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(value)



Create a new instance of the Float64 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.