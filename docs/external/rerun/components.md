---
source: https://ref.rerun.io/docs/python/stable/common/components
title: Components
---

# Components



### rerun.components



#### AggregationPolicyArrayLike=AggregationPolicy|Literal['Average','Max','Min','MinMax','MinMaxAverage','Off','average','max','min','minmax','minmaxaverage','off']|int|Sequence[AggregationPolicyLike]module-attribute



A type alias for any AggregationPolicy-like array object.



#### AggregationPolicyLike=AggregationPolicy|Literal['Average','Max','Min','MinMax','MinMaxAverage','Off','average','max','min','minmax','minmaxaverage','off']|intmodule-attribute



A type alias for any AggregationPolicy-like object.



#### AnnotationContextArrayLike=AnnotationContext|Sequence[AnnotationContextLike]module-attribute



A type alias for any AnnotationContext-like array object.



#### AnnotationContextLike=AnnotationContext|datatypes.ClassDescriptionArrayLike|Sequence[datatypes.ClassDescriptionMapElemLike]module-attribute



A type alias for any AnnotationContext-like object.



#### ChannelMessageCountsArrayLike=ChannelMessageCounts|Sequence[ChannelMessageCountsLike]|dict[int,int]|Sequence[dict[int,int]]module-attribute



A type alias for any ChannelMessageCounts-like array object.



#### ChannelMessageCountsLike=ChannelMessageCounts|dict[int,int]module-attribute



A type alias for any ChannelMessageCounts-like object.



#### ColormapArrayLike=Colormap|Literal['CyanToYellow','Grayscale','Inferno','Magma','Plasma','Spectral','Turbo','Twilight','Viridis','cyantoyellow','grayscale','inferno','magma','plasma','spectral','turbo','twilight','viridis']|int|Sequence[ColormapLike]module-attribute



A type alias for any Colormap-like array object.



#### ColormapLike=Colormap|Literal['CyanToYellow','Grayscale','Inferno','Magma','Plasma','Spectral','Turbo','Twilight','Viridis','cyantoyellow','grayscale','inferno','magma','plasma','spectral','turbo','twilight','viridis']|intmodule-attribute



A type alias for any Colormap-like object.



#### FillModeArrayLike=FillMode|Literal['DenseWireframe','MajorWireframe','Solid','densewireframe','majorwireframe','solid']|int|Sequence[FillModeLike]module-attribute



A type alias for any FillMode-like array object.



#### FillModeLike=FillMode|Literal['DenseWireframe','MajorWireframe','Solid','densewireframe','majorwireframe','solid']|intmodule-attribute



A type alias for any FillMode-like object.



#### GeoLineStringArrayLike=GeoLineString|Sequence[GeoLineStringLike]|npt.NDArray[np.float64]module-attribute



A type alias for any GeoLineString-like array object.



#### GeoLineStringLike=GeoLineString|datatypes.DVec2DArrayLike|npt.NDArray[np.float64]module-attribute



A type alias for any GeoLineString-like object.



#### GraphTypeArrayLike=GraphType|Literal['Directed','Undirected','directed','undirected']|int|Sequence[GraphTypeLike]module-attribute



A type alias for any GraphType-like array object.



#### GraphTypeLike=GraphType|Literal['Directed','Undirected','directed','undirected']|intmodule-attribute



A type alias for any GraphType-like object.



#### KeyValuePairsArrayLike=KeyValuePairs|Sequence[KeyValuePairsLike]|dict[str,str]|Sequence[dict[str,str]]module-attribute



A type alias for any KeyValuePairs-like array object.



#### KeyValuePairsLike=KeyValuePairs|dict[str,str]module-attribute



A type alias for any KeyValuePairs-like object.



#### LineStrip2DArrayLike=LineStrip2D|Sequence[LineStrip2DLike]|npt.NDArray[np.float32]module-attribute



A type alias for any LineStrip2D-like array object.



#### LineStrip2DLike=LineStrip2D|datatypes.Vec2DArrayLike|npt.NDArray[np.float32]module-attribute



A type alias for any LineStrip2D-like object.



#### LineStrip3DArrayLike=LineStrip3D|Sequence[LineStrip3DLike]|npt.NDArray[np.float32]module-attribute



A type alias for any LineStrip3D-like array object.



#### LineStrip3DLike=LineStrip3D|datatypes.Vec3DArrayLike|npt.NDArray[np.float32]module-attribute



A type alias for any LineStrip3D-like object.



#### MagnificationFilterArrayLike=MagnificationFilter|Literal['Linear','Nearest','linear','nearest']|int|Sequence[MagnificationFilterLike]module-attribute



A type alias for any MagnificationFilter-like array object.



#### MagnificationFilterLike=MagnificationFilter|Literal['Linear','Nearest','linear','nearest']|intmodule-attribute



A type alias for any MagnificationFilter-like object.



#### MarkerShapeArrayLike=MarkerShape|Literal['Asterisk','Circle','Cross','Diamond','Down','Left','Plus','Right','Square','Up','asterisk','circle','cross','diamond','down','left','plus','right','square','up']|int|Sequence[MarkerShapeLike]module-attribute



A type alias for any MarkerShape-like array object.



#### MarkerShapeLike=MarkerShape|Literal['Asterisk','Circle','Cross','Diamond','Down','Left','Plus','Right','Square','Up','asterisk','circle','cross','diamond','down','left','plus','right','square','up']|intmodule-attribute



A type alias for any MarkerShape-like object.



#### TransformRelationArrayLike=TransformRelation|Literal['ChildFromParent','ParentFromChild','childfromparent','parentfromchild']|int|Sequence[TransformRelationLike]module-attribute



A type alias for any TransformRelation-like array object.



#### TransformRelationLike=TransformRelation|Literal['ChildFromParent','ParentFromChild','childfromparent','parentfromchild']|intmodule-attribute



A type alias for any TransformRelation-like object.



#### VideoCodecArrayLike=VideoCodec|Literal['AV1','H264','H265','av1','h264','h265']|int|Sequence[VideoCodecLike]module-attribute



A type alias for any VideoCodec-like array object.



#### VideoCodecLike=VideoCodec|Literal['AV1','H264','H265','av1','h264','h265']|intmodule-attribute



A type alias for any VideoCodec-like object.



#### classAggregationPolicy



Bases: `Enum`



**Component**: Policy for aggregation of multiple scalar plot values.



This is used for lines in plots when the X axis distance of individual points goes below a single pixel,
i.e. a single pixel covers more than one tick worth of data. It can greatly improve performance
(and readability) in such situations as it prevents overdraw.



##### Average=2class-attributeinstance-attribute



Average all points in the range together.



##### Max=3class-attributeinstance-attribute



Keep only the maximum values in the range.



##### Min=4class-attributeinstance-attribute



Keep only the minimum values in the range.



##### MinMax=5class-attributeinstance-attribute



Keep both the minimum and maximum values in the range.



This will yield two aggregated points instead of one, effectively creating a vertical line.



##### MinMaxAverage=6class-attributeinstance-attribute



Find both the minimum and maximum values in the range, then use the average of those.



##### Off=1class-attributeinstance-attribute



No aggregation.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classAlbedoFactor



Bases: `Rgba32`, `ComponentMixin`



**Component**: A color multiplier, usually applied to a whole entity, e.g. a mesh.



##### def__init__(rgba)



Create a new instance of the Rgba32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classAnnotationContext



Bases: `AnnotationContextExt`, `ComponentMixin`



**Component**: The annotation context provides additional information on how to display entities.



Entities can use [datatypes.ClassId](../datatypes/#rerun.datatypes.ClassId)s and [datatypes.KeypointId](../datatypes/#rerun.datatypes.KeypointId)s to provide annotations, and
the labels and colors will be looked up in the appropriate
annotation context. We use the *first* annotation context we find in the
path-hierarchy when searching up through the ancestors of a given entity
path.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(class_map)



Create a new instance of the AnnotationContext component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| class_map | List of class descriptions, mapping class indices to class names, colors etc.TYPE:AnnotationContextLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classAxisLength



Bases: `Float32`, `ComponentMixin`



**Component**: The length of an axis in local units of the space.



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



#### classBlob



Bases: `Blob`, `ComponentMixin`



**Component**: A binary blob of data.



##### def__init__(data)



Create a new instance of the Blob datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classChannelId



Bases: `UInt16`, `ComponentMixin`



**Component**: A 16-bit ID representing an MCAP channel.



Used to identify specific channels within an MCAP file.



##### def__init__(value)



Create a new instance of the UInt16 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classChannelMessageCounts



Bases: `ComponentMixin`



**Component**: A mapping of channel IDs to their respective message counts.



Used in MCAP statistics to track how many messages were recorded per channel.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(counts)



Create a new instance of the ChannelMessageCounts component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| counts | The channel ID to message count pairs.TYPE:ChannelMessageCountsLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classClassId



Bases: `ClassId`, `ComponentMixin`



**Component**: A 16-bit ID representing a type of semantic class.



##### def__init__(id)



Create a new instance of the ClassId datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classClearIsRecursive



Bases: `ClearIsRecursiveExt`, `Bool`, `ComponentMixin`



**Component**: Configures how a clear operation should behave - recursive or not.



##### def__init__(recursive=True)



Disconnect an entity from its parent.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recursive | If true, also clears all recursive children entities.TYPE:boolDEFAULT:True |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classColor



Bases: `ColorExt`, `Rgba32`, `ComponentMixin`



**Component**: An RGBA color with unmultiplied/separate alpha, in sRGB gamma space with linear alpha.



The color is stored as a 32-bit integer, where the most significant
byte is `R` and the least significant byte is `A`.



Float colors are assumed to be in 0-1 gamma sRGB space.
All other colors are assumed to be in 0-255 gamma sRGB space.
If there is an alpha, we assume it is in linear space, and separate (NOT pre-multiplied).



##### def__init__(rgba)



Create a new instance of the Rgba32 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### deffrom_string(s)staticmethod



Generate a random yet deterministic color based on a string.



The color is guaranteed to be identical for the same input string.



#### classColormap



Bases: `Enum`



**Component**: Colormap for mapping scalar values within a given range to a color.



This provides a number of popular pre-defined colormaps.
In the future, the Rerun Viewer will allow users to define their own colormaps,
but currently the Viewer is limited to the types defined here.



##### CyanToYellow=7class-attributeinstance-attribute



Rasmusgo's Cyan to Yellow colormap



This is a perceptually uniform colormap which is robust to color blindness.
It is especially suited for visualizing signed values.
It interpolates from cyan to blue to dark gray to brass to yellow.



##### Grayscale=1class-attributeinstance-attribute



A simple black to white gradient.



This is a sRGB gray gradient which is perceptually uniform.



##### Inferno=2class-attributeinstance-attribute



The Inferno colormap from Matplotlib.



This is a perceptually uniform colormap.
It interpolates from black to red to bright yellow.



##### Magma=3class-attributeinstance-attribute



The Magma colormap from Matplotlib.



This is a perceptually uniform colormap.
It interpolates from black to purple to white.



##### Plasma=4class-attributeinstance-attribute



The Plasma colormap from Matplotlib.



This is a perceptually uniform colormap.
It interpolates from dark blue to purple to yellow.



##### Spectral=8class-attributeinstance-attribute



The Spectral colormap from Matplotlib.



This is a diverging colormap, often used to visualize data with a meaningful center point,
where deviations from that center are important to highlight.
It interpolates from red to orange to yellow to green to blue to violet.



##### Turbo=5class-attributeinstance-attribute



Google's Turbo colormap map.



This is a perceptually non-uniform rainbow colormap addressing many issues of
more traditional rainbow colormaps like Jet.
It is more perceptually uniform without sharp transitions and is more colorblind-friendly.
Details: [https://research.google/blog/turbo-an-improved-rainbow-colormap-for-visualization/](https://research.google/blog/turbo-an-improved-rainbow-colormap-for-visualization/)



##### Twilight=9class-attributeinstance-attribute



The Twilight colormap from Matplotlib.



This is a perceptually uniform cyclic colormap from Matplotlib, it is useful for
visualizing periodic or cyclic data.



It interpolates from white to blue to purple to red to orange and back to white.



##### Viridis=6class-attributeinstance-attribute



The Viridis colormap from Matplotlib



This is a perceptually uniform colormap which is robust to color blindness.
It interpolates from dark purple to green to yellow.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classCount



Bases: `UInt64`, `ComponentMixin`



**Component**: A generic count value.



Used for counting various entities like messages, schemas, channels, etc.



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



#### classDepthMeter



Bases: `Float32`, `ComponentMixin`



**Component**: The world->depth map scaling factor.



This measures how many depth map units are in a world unit.
For instance, if a depth map uses millimeters and the world uses meters,
this value would be `1000`.



Note that the only effect on 2D views is the physical depth values shown when hovering the image.
In 3D views on the other hand, this affects where the points of the point cloud are placed.



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



#### classDrawOrder



Bases: `Float32`, `ComponentMixin`



**Component**: Draw order of 2D elements. Higher values are drawn on top of lower values.



An entity can have only a single draw order component.
Within an entity draw order is governed by the order of the components.



Draw order for entities with the same draw order is generally undefined.



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



#### classEntityPath



Bases: `EntityPath`, `ComponentMixin`



**Component**: A path to an entity, usually to reference some data that is part of the target entity.



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



#### classFillMode



Bases: `Enum`



**Component**: How a geometric shape is drawn and colored.



##### DenseWireframe=2class-attributeinstance-attribute



Many lines are drawn to represent the surface of the shape in a see-through fashion.



Examples of what this means:



- An [archetypes.Ellipsoids3D](../archetypes/#rerun.archetypes.Ellipsoids3D) will draw a wireframe triangle mesh that approximates each
    ellipsoid.
- For [archetypes.Boxes3D](../archetypes/#rerun.archetypes.Boxes3D), it is the edges of the box, identical to components.FillMode.MajorWireframe.



##### MajorWireframe=1class-attributeinstance-attribute



Lines are drawn around the parts of the shape which directly correspond to the logged data.



Examples of what this means:



- An [archetypes.Ellipsoids3D](../archetypes/#rerun.archetypes.Ellipsoids3D) will draw three axis-aligned ellipses that are cross-sections
    of each ellipsoid, each of which displays two out of three of the sizes of the ellipsoid.
- For [archetypes.Boxes3D](../archetypes/#rerun.archetypes.Boxes3D), it is the edges of the box, identical to components.FillMode.DenseWireframe.



##### Solid=3class-attributeinstance-attribute



The surface of the shape is filled in with a solid color. No lines are drawn.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classFillRatio



Bases: `Float32`, `ComponentMixin`



**Component**: How much a primitive fills out the available space.



Used for instance to scale the points of the point cloud created from [archetypes.DepthImage](../archetypes/#rerun.archetypes.DepthImage) projection in 3D views.
Valid range is from 0 to max float although typically values above 1.0 are not useful.



Defaults to 1.0.



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



#### classGammaCorrection



Bases: `Float32`, `ComponentMixin`



**Component**: A gamma correction value to be used with a scalar value or color.



Used to adjust the gamma of a color or scalar value between 0 and 1 before rendering.
`new_value = old_value ^ gamma`



Must be a positive number.
Defaults to 1.0 unless otherwise specified.



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



#### classGeoLineString



Bases: `GeoLineStringExt`, `ComponentMixin`



**Component**: A geospatial line string expressed in [EPSG:4326](https://epsg.io/4326) latitude and longitude (North/East-positive degrees).



##### def__init__(*,lat_lon)



Create a new instance of the GeoLineString component.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classGraphEdge



Bases: `Utf8Pair`, `ComponentMixin`



**Component**: An edge in a graph connecting two nodes.



##### def__init__(first,second)



Create a new instance of the Utf8Pair datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| first | The first string.TYPE:Utf8Like |
| second | The second string.TYPE:Utf8Like |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classGraphNode



Bases: `Utf8`, `ComponentMixin`



**Component**: A string-based ID representing a node in a graph.



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



#### classGraphType



Bases: `Enum`



**Component**: Specifies if a graph has directed or undirected edges.



##### Directed=2class-attributeinstance-attribute



The graph has directed edges.



##### Undirected=1class-attributeinstance-attribute



The graph has undirected edges.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classHalfSize2D



Bases: `Vec2D`, `ComponentMixin`



**Component**: Half-size (radius) of a 2D box.



Measured in its local coordinate system.



The box extends both in negative and positive direction along each axis.
Negative sizes indicate that the box is flipped along the respective axis, but this has no effect on how it is displayed.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classHalfSize3D



Bases: `Vec3D`, `ComponentMixin`



**Component**: Half-size (radius) of a 3D box.



Measured in its local coordinate system.



The box extends both in negative and positive direction along each axis.
Negative sizes indicate that the box is flipped along the respective axis, but this has no effect on how it is displayed.



##### def__init__(xyz)



Create a new instance of the Vec3D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classImageBuffer



Bases: `Blob`, `ComponentMixin`



**Component**: A buffer that is known to store image data.



To interpret the contents of this buffer, see, components.ImageFormat.



##### def__init__(data)



Create a new instance of the Blob datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classImageFormat



Bases: `ImageFormat`, `ComponentMixin`



**Component**: The metadata describing the contents of a components.ImageBuffer.



##### def__init__(width,height,*,pixel_format=None,color_model=None,channel_datatype=None)



Create a new instance of the ImageFormat datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | The width of the image in pixels.TYPE:int |
| height | The height of the image in pixels.TYPE:int |
| pixel_format | Used mainly for chroma downsampled formats and differing number of bits per channel.If specified, this takes precedence over bothdatatypes.ColorModelanddatatypes.ChannelDatatype(which are ignored).TYPE:PixelFormatLike\| NoneDEFAULT:None |
| color_model | L, RGB, RGBA, â¦Also requires adatatypes.ChannelDatatypeto fully specify the pixel format.TYPE:ColorModelLike\| NoneDEFAULT:None |
| channel_datatype | The data type of each channel (e.g. the red channel) of the image data (U8, F16, â¦).Also requires adatatypes.ColorModelto fully specify the pixel format.TYPE:ChannelDatatypeLike\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classImagePlaneDistance



Bases: `Float32`, `ComponentMixin`



**Component**: The distance from the camera origin to the image plane when the projection is shown in a 3D viewer.



This is only used for visualization purposes, and does not affect the projection itself.



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



#### classInteractive



Bases: `Bool`, `ComponentMixin`



**Component**: Whether the entity can be interacted with.



Non interactive components are still visible, but mouse interactions in the view are disabled.



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



#### classKeyValuePairs



Bases: `KeyValuePairsExt`, `ComponentMixin`



**Component**: A map of string keys to string values.



This component can be used to attach arbitrary metadata or annotations to entities.
Each key-value pair is stored as a UTF-8 string mapping.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(pairs)



Create a new instance of the KeyValuePairs component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| pairs | The key-value pairs that make up this string map.TYPE:KeyValuePairsLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classKeypointId



Bases: `KeypointId`, `ComponentMixin`



**Component**: A 16-bit ID representing a type of semantic keypoint within a class.



`KeypointId`s are only meaningful within the context of a [`rerun.datatypes.ClassDescription`].



Used to look up an [`rerun.datatypes.AnnotationInfo`] for a Keypoint within the
[`rerun.components.AnnotationContext`].



##### def__init__(id)



Create a new instance of the KeypointId datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLatLon



Bases: `DVec2D`, `ComponentMixin`



**Component**: A geospatial position expressed in [EPSG:4326](https://epsg.io/4326) latitude and longitude (North/East-positive degrees).



##### def__init__(xy)



Create a new instance of the DVec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLength



Bases: `Float32`, `ComponentMixin`



**Component**: Length, or one-dimensional size.



Measured in its local coordinate system; consult the archetype in use to determine which
axis or part of the entity this is the length of.



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



#### classLineStrip2D



Bases: `LineStrip2DExt`, `ComponentMixin`



**Component**: A line strip in 2D space.



A line strip is a list of points connected by line segments. It can be used to draw
approximations of smooth curves.



The points will be connected in order, like so:

```
2------3     5
      /        \   /
0----1          \ /
                 4
```



##### def__init__(points)



Create a new instance of the LineStrip2D component.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLineStrip3D



Bases: `LineStrip3DExt`, `ComponentMixin`



**Component**: A line strip in 3D space.



A line strip is a list of points connected by line segments. It can be used to draw
approximations of smooth curves.



The points will be connected in order, like so:

```
2------3     5
      /        \   /
0----1          \ /
                 4
```



##### def__init__(points)



Create a new instance of the LineStrip3D component.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classLinearSpeed



Bases: `Float64`, `ComponentMixin`



**Component**: Linear speed, used for translation speed for example.



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



#### classMagnificationFilter



Bases: `Enum`



**Component**: Filter used when magnifying an image/texture such that a single pixel/texel is displayed as multiple pixels on screen.



##### Linear=2class-attributeinstance-attribute



Linearly interpolate the nearest neighbors, creating a smoother look when zooming in.



Used as default for mesh rendering.



##### Nearest=1class-attributeinstance-attribute



Show the nearest pixel value.



This will give a blocky appearance when zooming in.
Used as default when rendering 2D images.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classMarkerShape



Bases: `Enum`



**Component**: The visual appearance of a point in e.g. a 2D plot.



##### Asterisk=10class-attributeinstance-attribute



`*`



##### Circle=1class-attributeinstance-attribute



`âº`



##### Cross=4class-attributeinstance-attribute



`x`



##### Diamond=2class-attributeinstance-attribute



`â`



##### Down=7class-attributeinstance-attribute



`â¼`



##### Left=8class-attributeinstance-attribute



`â`



##### Plus=5class-attributeinstance-attribute



`+`



##### Right=9class-attributeinstance-attribute



`â¶`



##### Square=3class-attributeinstance-attribute



`â¼ï¸`



##### Up=6class-attributeinstance-attribute



`â²`



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classMarkerSize



Bases: `Float32`, `ComponentMixin`



**Component**: Radius of a marker of a point in e.g. a 2D plot, measured in UI points.



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



#### classMediaType



Bases: `MediaTypeExt`, `Utf8`, `ComponentMixin`



**Component**: A standardized media type (RFC2046, formerly known as MIME types), encoded as a string.



The complete reference of officially registered media types is maintained by the IANA and can be
consulted at [https://www.iana.org/assignments/media-types/media-types.xhtml](https://www.iana.org/assignments/media-types/media-types.xhtml).



##### GLB:MediaType=Noneclass-attributeinstance-attribute



Binary [glTF](https://en.wikipedia.org/wiki/GlTF): `model/gltf-binary`.



[https://www.iana.org/assignments/media-types/model/gltf-binary](https://www.iana.org/assignments/media-types/model/gltf-binary)



##### GLTF:MediaType=Noneclass-attributeinstance-attribute



[glTF](https://en.wikipedia.org/wiki/GlTF): `model/gltf+json`.



[https://www.iana.org/assignments/media-types/model/gltf+json](https://www.iana.org/assignments/media-types/model/gltf+json)



##### JPEG:MediaType=Noneclass-attributeinstance-attribute



[JPEG image](https://en.wikipedia.org/wiki/JPEG): `image/jpeg`.



##### MARKDOWN:MediaType=Noneclass-attributeinstance-attribute



Markdown: `text/markdown`.



[https://www.iana.org/assignments/media-types/text/markdown](https://www.iana.org/assignments/media-types/text/markdown)



##### MP4:MediaType=Noneclass-attributeinstance-attribute



[mp4](https://en.wikipedia.org/wiki/MP4_file_format): `video/mp4`.



[https://www.iana.org/assignments/media-types/video/mp4](https://www.iana.org/assignments/media-types/video/mp4)



##### OBJ:MediaType=Noneclass-attributeinstance-attribute



[Wavefront .obj](https://en.wikipedia.org/wiki/Wavefront_.obj_file): `model/obj`.



[https://www.iana.org/assignments/media-types/model/obj](https://www.iana.org/assignments/media-types/model/obj)



##### PNG:MediaType=Noneclass-attributeinstance-attribute



[PNG image](https://en.wikipedia.org/wiki/PNG): `image/png`.



[https://www.iana.org/assignments/media-types/image/png](https://www.iana.org/assignments/media-types/image/png)



##### RVL:MediaType=Noneclass-attributeinstance-attribute



RVL compressed depth: `application/rvl`.



Run length encoding and Variable Length encoding schemes (RVL) compressed depth data format.
[https://www.microsoft.com/en-us/research/wp-content/uploads/2018/09/p100-wilson.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2018/09/p100-wilson.pdf)



##### STL:MediaType=Noneclass-attributeinstance-attribute



[Stereolithography Modelstl](https://en.wikipedia.org/wiki/STL_(file_format)): `model/stl`.
Either binary or ASCII.



[https://www.iana.org/assignments/media-types/model/stl](https://www.iana.org/assignments/media-types/model/stl)



##### TEXT:MediaType=Noneclass-attributeinstance-attribute



Plain text: `text/plain`.



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



#### className



Bases: `Utf8`, `ComponentMixin`



**Component**: A display name, typically for an entity or a item like a plot series.



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



#### classOpacity



Bases: `Float32`, `ComponentMixin`



**Component**: Degree of transparency ranging from 0.0 (fully transparent) to 1.0 (fully opaque).



The final opacity value may be a result of multiplication with alpha values as specified by other color sources.
Unless otherwise specified, the default value is 1.



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



#### classPinholeProjection



Bases: `Mat3x3`, `ComponentMixin`



**Component**: Camera projection, from image coordinates to view coordinates.



Child from parent.
Image coordinates from camera view coordinates.



Example:

```
1496.1     0.0  980.5
   0.0  1496.1  744.5
   0.0     0.0    1.0
```



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classPlane3D



Bases: `Plane3D`, `ComponentMixin`



**Component**: An infinite 3D plane represented by a unit normal vector and a distance.



Any point P on the plane fulfills the equation `dot(xyz, P) - d = 0`,
where `xyz` is the plane's normal and `d` the distance of the plane from the origin.
This representation is also known as the Hesse normal form.



Note: although the normal will be passed through to the
datastore as provided, when used in the Viewer, planes will always be normalized.
I.e. the plane with xyz = (2, 0, 0), d = 1 is equivalent to xyz = (1, 0, 0), d = 0.5



##### def__init__(normal,distance=None)



Create a new instance of the Plane3D datatype.



Does *not* normalize the plane.



| PARAMETER | DESCRIPTION |
| --- | --- |
| normal | Normal vector of the plane.TYPE:Vec3DLike |
| distance | Distance of the plane from the origin. Defaults to zero.TYPE:float\|int\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defdistance()



Returns the distance of the plane from the origin.



##### defnormal()



Returns the normal vector of the plane.



##### defwith_distance(distance)



Returns a new plane with the same normal but with the distance set to the given amount.



#### classPosition2D



Bases: `Vec2D`, `ComponentMixin`



**Component**: A position in 2D space.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classPosition3D



Bases: `Vec3D`, `ComponentMixin`



**Component**: A position in 3D space.



##### def__init__(xyz)



Create a new instance of the Vec3D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classRadius



Bases: `RadiusExt`, `Float32`, `ComponentMixin`



**Component**: The radius of something, e.g. a point.



Internally, positive values indicate scene units, whereas negative values
are interpreted as UI points.



UI points are independent of zooming in Views, but are sensitive to the application UI scaling.
at 100% UI scaling, UI points are equal to pixels
The Viewer's UI scaling defaults to the OS scaling which typically is 100% for full HD screens and 200% for 4k screens.



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



##### defui_points(radii)staticmethod



Create a radius or list of radii in UI points.



By default, radii are interpreted as scene units.
Ui points on the other hand are independent of zooming in Views, but are sensitive to the application UI scaling.
at 100% UI scaling, UI points are equal to pixels
The Viewer's UI scaling defaults to the OS scaling which typically is 100% for full HD screens and 200% for 4k screens.



Internally, ui radii are stored as negative values.
Therefore, all this method does is to ensure that all returned values are negative.



#### classRange1D



Bases: `Range1D`, `ComponentMixin`



**Component**: A 1D range, specifying a lower and upper bound.



##### def__init__(range)



Create a new instance of the Range1D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classResolution



Bases: `Vec2D`, `ComponentMixin`



**Component**: Pixel resolution width & height, e.g. of a camera sensor.



Typically in integer units, but for some use cases floating point may be used.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classRotationAxisAngle



Bases: `RotationAxisAngle`, `ComponentMixin`



**Component**: 3D rotation represented by a rotation around a given axis.



If normalization of the rotation axis fails the rotation is treated as an invalid transform, unless the
angle is zero in which case it is treated as an identity.



##### def__init__(axis,angle=None,*,radians=None,degrees=None)



Create a new instance of the RotationAxisAngle datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| axis | Axis to rotate around.This is not required to be normalized.  If normalization fails (typically because the vector is length zero), the rotation is silently  ignored.TYPE:Vec3DLike |
| angle | How much to rotate around the axis.TYPE:AngleLike\| NoneDEFAULT:None |
| radians | How much to rotate around the axis, in radians. Specify this instead ofdegreesorangle.TYPE:float\| NoneDEFAULT:None |
| degrees | How much to rotate around the axis, in degrees. Specify this instead ofradiansorangle.TYPE:float\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classRotationQuat



Bases: `Quaternion`, `ComponentMixin`



**Component**: A 3D rotation expressed as a quaternion.



Note: although the x,y,z,w components of the quaternion will be passed through to the
datastore as provided, when used in the Viewer, quaternions will always be normalized.
If normalization fails the rotation is treated as an invalid transform.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classScalar



Bases: `Float64`, `ComponentMixin`



**Component**: A scalar value, encoded as a 64-bit floating point.



Used for time series plots.



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



#### classScale3D



Bases: `Scale3DExt`, `Vec3D`, `ComponentMixin`



**Component**: A 3D scale factor.



A scale of 1.0 means no scaling.
A scale of 2.0 means doubling the size.
Each component scales along the corresponding axis.



##### def__init__(uniform_or_per_axis=True)



3D scaling factor.



A scale of 1.0 means no scaling.
A scale of 2.0 means doubling the size.
Each component scales along the corresponding axis.



| PARAMETER | DESCRIPTION |
| --- | --- |
| uniform_or_per_axis | If a single value is given, it is applied the same to all three axis (uniform scaling).TYPE:Vec3DLike\|Float32Like\| NoneDEFAULT:True |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classSchemaId



Bases: `UInt16`, `ComponentMixin`



**Component**: A 16-bit unique identifier for a schema within the MCAP file.



##### def__init__(value)



Create a new instance of the UInt16 datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classSeriesVisible



Bases: `Bool`, `ComponentMixin`



**Component**: Like components.Visible, but for time series.



TODO(#10632): This is a temporary workaround. Right now we can't use components.Visible since it would conflict with the entity-wide visibility state.



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



#### classShowLabels



Bases: `Bool`, `ComponentMixin`



**Component**: Whether the entity's components.Text label is shown.



The main purpose of this component existing separately from the labels themselves
is to be overridden when desired, to allow hiding and showing from the viewer and
blueprints.



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



#### classStrokeWidth



Bases: `Float32`, `ComponentMixin`



**Component**: The width of a stroke specified in UI points.



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



#### classTensorData



Bases: `TensorData`, `ComponentMixin`



**Component**: An N-dimensional array of numbers.



The number of dimensions and their respective lengths is specified by the `shape` field.
The dimensions are ordered from outermost to innermost. For example, in the common case of
a 2D RGB Image, the shape would be `[height, width, channel]`.



These dimensions are combined with an index to look up values from the `buffer` field,
which stores a contiguous array of typed values.



##### def__init__(*,shape=None,buffer=None,array=None,dim_names=None)



Construct a `TensorData` object.



The `TensorData` object is internally represented by three fields: `shape` and `buffer`.



This constructor provides additional arguments 'array', and 'dim_names'. When passing in a
multi-dimensional array such as a `np.ndarray`, the `shape` and `buffer` fields will be
populated automagically.



| PARAMETER | DESCRIPTION |
| --- | --- |
| self | The TensorData object to construct.TYPE:Any |
| shape | The shape of the tensor. If None, and an array is provided, the shape will be inferred from the shape of the array.TYPE:Sequence[int] \| NoneDEFAULT:None |
| buffer | The buffer of the tensor. If None, and an array is provided, the buffer will be generated from the array.TYPE:TensorBufferLike\| NoneDEFAULT:None |
| array | A numpy array (or The array of the tensor. If None, the array will be inferred from the buffer.TYPE:TensorLike\| NoneDEFAULT:None |
| dim_names | The names of the tensor dimensions.TYPE:Sequence[str] \| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defnumpy(force)



Convert the TensorData back to a numpy array.



#### classTensorDimensionIndexSelection



Bases: `TensorDimensionIndexSelection`, `ComponentMixin`



**Component**: Specifies a concrete index on a tensor dimension.



##### def__init__(dimension,index)



Create a new instance of the TensorDimensionIndexSelection datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number to select.TYPE:int |
| index | The index along the dimension to use.TYPE:int |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTensorHeightDimension



Bases: `TensorDimensionSelection`, `ComponentMixin`



**Component**: Specifies which dimension to use for height.



##### def__init__(dimension,*,invert=False)



Create a new instance of the TensorDimensionSelection datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number to select.TYPE:int |
| invert | Invert the direction of the dimension.TYPE:boolDEFAULT:False |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTensorWidthDimension



Bases: `TensorDimensionSelection`, `ComponentMixin`



**Component**: Specifies which dimension to use for width.



##### def__init__(dimension,*,invert=False)



Create a new instance of the TensorDimensionSelection datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number to select.TYPE:int |
| invert | Invert the direction of the dimension.TYPE:boolDEFAULT:False |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTexcoord2D



Bases: `Vec2D`, `ComponentMixin`



**Component**: A 2D texture UV coordinate.



Texture coordinates specify a position on a 2D texture.
A range from 0-1 covers the entire texture in the respective dimension.
Unless configured otherwise, the texture repeats outside of this range.
Rerun uses top-left as the origin for UV coordinates.



0     U     1
0 + --------- â
  |           .
V |           .
  |           .
1 â . . . . . .



This is the same convention as in Vulkan/Metal/DX12/WebGPU, but (!) unlike OpenGL,
which places the origin at the bottom-left.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classText



Bases: `Utf8`, `ComponentMixin`



**Component**: A string of text, e.g. for labels and text documents.



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



#### classTextLogLevel



Bases: `TextLogLevelExt`, `Utf8`, `ComponentMixin`



**Component**: The severity level of a text log message.



Recommended to be one of:
* `"CRITICAL"`
* `"ERROR"`
* `"WARN"`
* `"INFO"`
* `"DEBUG"`
* `"TRACE"`



##### CRITICAL:TextLogLevel=Noneclass-attributeinstance-attribute



Designates catastrophic failures.



##### DEBUG:TextLogLevel=Noneclass-attributeinstance-attribute



Designates lower priority information.



##### ERROR:TextLogLevel=Noneclass-attributeinstance-attribute



Designates very serious errors.



##### INFO:TextLogLevel=Noneclass-attributeinstance-attribute



Designates useful information.



##### TRACE:TextLogLevel=Noneclass-attributeinstance-attribute



Designates very low priority, often extremely verbose, information.



##### WARN:TextLogLevel=Noneclass-attributeinstance-attribute



Designates hazardous situations.



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



#### classTimestamp



Bases: `TimeInt`, `ComponentMixin`



**Component**: When the recording started.



Should be an absolute time, i.e. relative to Unix Epoch.



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



#### classTransformFrameId



Bases: `Utf8`, `ComponentMixin`



**Component**: A string identifier for a transform frame.



Transform frames may be derived from entity paths to refer to Rerun's implicit
entity path driven hierarchy which is defined via [archetypes.Transform3D](../archetypes/#rerun.archetypes.Transform3D), [archetypes.Pinhole](../archetypes/#rerun.archetypes.Pinhole) etc..
These implicit transform frames look like `tf#path/to/entity`.



Note that any [archetypes.Transform3D](../archetypes/#rerun.archetypes.Transform3D)s logged with both `parent_frame` and `child_frame` set
describes a relationship between these parent and child transform frames, **not** the transform frame
that the entity path may be using (defined by an [archetypes.CoordinateFrame](../archetypes/#rerun.archetypes.CoordinateFrame)).



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



#### classTransformMat3x3



Bases: `Mat3x3`, `ComponentMixin`



**Component**: A 3x3 transformation matrix Matrix.



3x3 matrixes are able to represent any affine transformation in 3D space,
i.e. rotation, scaling, shearing, reflection etc.



Matrices in Rerun are stored as flat list of coefficients in column-major order:

```
column 0       column 1       column 2
       -------------------------------------------------
row 0 | flat_columns[0] flat_columns[3] flat_columns[6]
row 1 | flat_columns[1] flat_columns[4] flat_columns[7]
row 2 | flat_columns[2] flat_columns[5] flat_columns[8]
```



However, construction is done from a list of rows, which follows NumPy's convention:

```
np.testing.assert_array_equal(
    rr.components.TransformMat3x3([1, 2, 3, 4, 5, 6, 7, 8, 9]).flat_columns, np.array([1, 4, 7, 2, 5, 8, 3, 6, 9], dtype=np.float32)
)
np.testing.assert_array_equal(
    rr.components.TransformMat3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).flat_columns,
    np.array([1, 4, 7, 2, 5, 8, 3, 6, 9], dtype=np.float32),
)
```

If you want to construct a matrix from a list of columns instead, use the named `columns` parameter:

```
np.testing.assert_array_equal(
    rr.components.TransformMat3x3(columns=[1, 2, 3, 4, 5, 6, 7, 8, 9]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32),
)
np.testing.assert_array_equal(
    rr.components.TransformMat3x3(columns=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32),
)
```



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTransformRelation



Bases: `Enum`



**Component**: Specifies relation a spatial transform describes.



##### ChildFromParent=2class-attributeinstance-attribute



The transform describes how to transform into the child entity's space.



E.g. a translation of (0, 1, 0) with this components.TransformRelation logged at `parent/child` means
that from the point of view of `parent`, `parent/child` is translated -1 unit along `parent`'s Y axis.
From perspective of `parent/child`, the `parent` entity is translated 1 unit along `parent/child`'s Y axis.



##### ParentFromChild=1class-attributeinstance-attribute



The transform describes how to transform into the parent entity's space.



E.g. a translation of (0, 1, 0) with this components.TransformRelation logged at `parent/child` means
that from the point of view of `parent`, `parent/child` is translated 1 unit along `parent`'s Y axis.
From perspective of `parent/child`, the `parent` entity is translated -1 unit along `parent/child`'s Y axis.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classTranslation3D



Bases: `Vec3D`, `ComponentMixin`



**Component**: A translation vector in 3D space.



##### def__init__(xyz)



Create a new instance of the Vec3D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classTriangleIndices



Bases: `UVec3D`, `ComponentMixin`



**Component**: The three indices of a triangle in a triangle mesh.



##### def__init__(xyz)



Create a new instance of the UVec3D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classValueRange



Bases: `Range1D`, `ComponentMixin`



**Component**: Range of expected or valid values, specifying a lower and upper bound.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(range)



Create a new instance of the Range1D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVector2D



Bases: `Vec2D`, `ComponentMixin`



**Component**: A vector in 2D space.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVector3D



Bases: `Vec3D`, `ComponentMixin`



**Component**: A vector in 3D space.



##### def__init__(xyz)



Create a new instance of the Vec3D datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVideoCodec



Bases: `Enum`



**Component**: The codec used to encode video stored in components.VideoSample.



Support of these codecs by the Rerun Viewer is platform dependent.
For more details see check the [video reference](https://rerun.io/docs/reference/video).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### AV1=1635135537class-attributeinstance-attribute



AOMedia Video 1 (AV1)



See [https://en.wikipedia.org/wiki/AV1](https://en.wikipedia.org/wiki/AV1)



components.VideoSamples using this codec should be formatted according the "Low overhead bitstream format",
as specified in Section 5.2 of the [AV1 specification](https://aomediacodec.github.io/av1-spec/#low-overhead-bitstream-format).
Each sample should be formatted as a sequence of OBUs (Open Bitstream Units) long enough to decode at least one video frame.
Samples containing keyframes must include a sequence header OBU before the `KEY_FRAME` OBU to enable
extraction of frame dimensions, bit depth, and color information. `INTRA_ONLY` frames are not treated
as keyframes since they may reference existing decoder state.



Enum value is the fourcc for 'av01' (the WebCodec string assigned to this codec) in big endian.



##### H264=1635148593class-attributeinstance-attribute



Advanced Video Coding (AVC/H.264)



See [https://en.wikipedia.org/wiki/Advanced_Video_Coding](https://en.wikipedia.org/wiki/Advanced_Video_Coding)



components.VideoSamples using this codec should be formatted according to Annex B specification.
(Note that this is different from AVCC format found in MP4 files.
To learn more about Annex B, check for instance [https://membrane.stream/learn/h264/3](https://membrane.stream/learn/h264/3))
Key frames (IDR) require inclusion of a SPS (Sequence Parameter Set)



Enum value is the fourcc for 'avc1' (the WebCodec string assigned to this codec) in big endian.



##### H265=1751479857class-attributeinstance-attribute



High Efficiency Video Coding (HEVC/H.265)



See [https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding)



components.VideoSamples using this codec should be formatted according to Annex B specification.
(Note that this is different from AVCC format found in MP4 files.
To learn more about Annex B, check for instance [https://membrane.stream/learn/h264/3](https://membrane.stream/learn/h264/3))
Key frames (IRAP) require inclusion of a SPS (Sequence Parameter Set)



Enum value is the fourcc for 'hev1' (the WebCodec string assigned to this codec) in big endian.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classVideoSample



Bases: `Blob`, `ComponentMixin`



**Component**: Video sample data (also known as "video chunk").



Each video sample must contain enough data for exactly one video frame
(this restriction may be relaxed in the future for some codecs).



Keyframes may require additional data, for details see components.VideoCodec.



##### def__init__(data)



Create a new instance of the Blob datatype.



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVideoTimestamp



Bases: `VideoTimestampExt`, `VideoTimestamp`, `ComponentMixin`



**Component**: Timestamp inside a [archetypes.AssetVideo](../archetypes/#rerun.archetypes.AssetVideo).



##### def__init__(*,nanoseconds=None,seconds=None)



Create a new instance of the VideoTimestamp component.



| PARAMETER | DESCRIPTION |
| --- | --- |
| nanoseconds | Presentation timestamp in nanoseconds. Mutually exclusive withseconds.TYPE:int\| NoneDEFAULT:None |
| seconds | Presentation timestamp in seconds. Mutually exclusive withnanoseconds.TYPE:float\| NoneDEFAULT:None |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defmilliseconds(milliseconds)staticmethod



Create a video timestamp batch from milliseconds since video start.



| PARAMETER | DESCRIPTION |
| --- | --- |
| milliseconds | Timestamp values in milliseconds since video start.TYPE:ArrayLike |



##### defnanoseconds(nanoseconds)staticmethod



Create a video timestamp batch from nanoseconds since video start.



| PARAMETER | DESCRIPTION |
| --- | --- |
| nanoseconds | Timestamp values in nanoseconds since video start.TYPE:ArrayLike |



##### defseconds(seconds)staticmethod



Create a video timestamp batch from seconds since video start.



| PARAMETER | DESCRIPTION |
| --- | --- |
| seconds | Timestamp values in seconds since video start.TYPE:ArrayLike |



#### classViewCoordinates



Bases: `ViewCoordinatesExt`, `ViewCoordinates`, `ComponentMixin`



**Component**: How we interpret the coordinate system of an entity/space.



For instance: What is "up"? What does the Z axis mean?



The three coordinates are always ordered as [x, y, z].



For example [Right, Down, Forward] means that the X axis points to the right, the Y axis points
down, and the Z axis points forward.



â  [Rerun does not yet support left-handed coordinate systems](https://github.com/rerun-io/rerun/issues/5032).



The following constants are used to represent the different directions:
 * Up = 1
 * Down = 2
 * Right = 3
 * Left = 4
 * Forward = 5
 * Back = 6



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### BDL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Down, Z=Left



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### BDR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Down, Z=Right



##### BLD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Left, Z=Down



##### BLU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Left, Z=Up



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### BRD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Right, Z=Down



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### BRU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Right, Z=Up



##### BUL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Up, Z=Left



##### BUR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Back, Y=Up, Z=Right



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### DBL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Back, Z=Left



##### DBR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Back, Z=Right



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### DFL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Forward, Z=Left



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### DFR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Forward, Z=Right



##### DLB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Left, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### DLF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Left, Z=Forward



##### DRB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Right, Z=Back



##### DRF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Right, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### FDL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Down, Z=Left



##### FDR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Down, Z=Right



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### FLD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Left, Z=Down



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### FLU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Left, Z=Up



##### FRD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Right, Z=Down



##### FRU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Right, Z=Up



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### FUL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Up, Z=Left



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### FUR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Forward, Y=Up, Z=Right



##### LBD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Back, Z=Down



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LBU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Back, Z=Up



##### LDB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Down, Z=Back



##### LDF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Down, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_X_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Right, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_X_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Right, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_Y_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Down, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_Y_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Up, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_Z_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Forward, Z=Down



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LEFT_HAND_Z_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Back, Z=Up



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LFD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Forward, Z=Down



##### LFU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Forward, Z=Up



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LUB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Up, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### LUF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Left, Y=Up, Z=Forward



##### RBD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Back, Z=Down



##### RBU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Back, Z=Up



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### RDB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Down, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### RDF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Down, Z=Forward



##### RFD:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Forward, Z=Down



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### RFU:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Forward, Z=Up



##### RIGHT_HAND_X_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Down, Y=Right, Z=Back



##### RIGHT_HAND_X_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Right, Z=Forward



##### RIGHT_HAND_Y_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Down, Z=Forward



##### RIGHT_HAND_Y_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Up, Z=Back



##### RIGHT_HAND_Z_DOWN:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Back, Z=Down



##### RIGHT_HAND_Z_UP:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Forward, Z=Up



##### RUB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Up, Z=Back



##### RUF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Right, Y=Up, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### UBL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Back, Z=Left



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### UBR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Back, Z=Right



##### UFL:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Forward, Z=Left



##### UFR:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Forward, Z=Right



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### ULB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Left, Z=Back



##### ULF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Left, Z=Forward



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### URB:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Right, Z=Back



â ï¸ This is a left-handed coordinate system, which is [not yet supported by Rerun](https://github.com/rerun-io/rerun/issues/5032).



##### URF:ViewCoordinates=Noneclass-attributeinstance-attribute



X=Up, Y=Right, Z=Forward



##### def__init__(coordinates)



Create a new instance of the ViewCoordinates datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| coordinates | The directions of the [x, y, z] axes.TYPE:ViewCoordinatesLike |



##### defarrow_type()classmethod



The pyarrow type of this batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defas_arrow_array()



The component as an arrow batch.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



##### defcomponent_type()classmethod



Returns the name of the component.



Part of the [rerun.ComponentBatchLike](../interfaces/#rerun.ComponentBatchLike) logging interface.



#### classVisible



Bases: `Bool`, `ComponentMixin`



**Component**: Whether the container, view, entity or instance is currently visible.



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