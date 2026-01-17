---
source: https://ref.rerun.io/docs/python/stable/common/archetypes
title: Archetypes
---

# Archetypes



### rerun.archetypes



#### classAnnotationContext



Bases: `Archetype`



**Archetype**: The annotation context provides additional information on how to display entities.



Entities can use [components.ClassId](../components/#rerun.components.ClassId)s and [components.KeypointId](../components/#rerun.components.KeypointId)s to provide annotations, and
the labels and colors will be looked up in the appropriate
annotation context. We use the *first* annotation context we find in the
path-hierarchy when searching up through the ancestors of a given entity
path.



See also [datatypes.ClassDescription](../datatypes/#rerun.datatypes.ClassDescription).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Segmentation:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_annotation_context_segmentation", spawn=True)

# Create a simple segmentation image
image = np.zeros((200, 300), dtype=np.uint8)
image[50:100, 50:120] = 1
image[100:180, 130:280] = 2

# Log an annotation context to assign a label and color to each class
rr.log("segmentation", rr.AnnotationContext([(1, "red", (255, 0, 0)), (2, "green", (0, 255, 0))]), static=True)

rr.log("segmentation/image", rr.SegmentationImage(image))
```

 ![](https://static.rerun.io/annotation_context_segmentation/6c9e88fc9d44a08031cadd444c2e58a985cc1208/full.png)

##### def__init__(context)



Create a new instance of the AnnotationContext archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| context | List of class descriptions, mapping class indices to class names, colors etc.TYPE:AnnotationContextLike |



##### defcleared()classmethod



Clear all the fields of a `AnnotationContext`.



##### defcolumns(*,context=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| context | List of class descriptions, mapping class indices to class names, colors etc.TYPE:AnnotationContextArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,context=None)classmethod



Update only some specific fields of a `AnnotationContext`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| context | List of class descriptions, mapping class indices to class names, colors etc.TYPE:AnnotationContextLike\| NoneDEFAULT:None |



#### classArrows2D



Bases: `Arrows2DExt`, `Archetype`



**Archetype**: 2D arrows with optional colors, radii, labels, etc.

 Example

###### Simple batch of 2D arrows:



```
import rerun as rr

rr.init("rerun_example_arrow2d", spawn=True)

rr.log(
    "arrows",
    rr.Arrows2D(
        origins=[[0.25, 0.0], [0.25, 0.0], [-0.1, -0.1]],
        vectors=[[1.0, 0.0], [0.0, -1.0], [-0.7, 0.7]],
        colors=[[255, 0, 0], [0, 255, 0], [127, 0, 255]],
        labels=["right", "up", "left-down"],
        radii=0.025,
    ),
)
```

 ![](https://static.rerun.io/arrow2d_simple/59f044ccc03f7bc66ee802288f75706618b29a6e/full.png)

##### def__init__(*,vectors,origins=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)



Create a new instance of the Arrows2D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec2DArrayLike |
| origins | All the origin points for each arrow in the batch.If no origins are set, (0, 0, 0) is used as the origin for each arrow.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order of the arrows.Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Arrows2D`.



##### defcolumns(*,vectors=None,origins=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| origins | All the origin (base) positions for each arrow in the batch.If no origins are set, (0, 0) is used as the origin for each arrow.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,vectors=None,origins=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Update only some specific fields of a `Arrows2D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| origins | All the origin (base) positions for each arrow in the batch.If no origins are set, (0, 0) is used as the origin for each arrow.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classArrows3D



Bases: `Arrows3DExt`, `Archetype`



**Archetype**: 3D arrows with optional colors, radii, labels, etc.

 Example

###### Simple batch of 3D arrows:



```
from math import tau

import numpy as np
import rerun as rr

rr.init("rerun_example_arrow3d", spawn=True)

lengths = np.log2(np.arange(0, 100) + 1)
angles = np.arange(start=0, stop=tau, step=tau * 0.01)
origins = np.zeros((100, 3))
vectors = np.column_stack([np.sin(angles) * lengths, np.zeros(100), np.cos(angles) * lengths])
colors = [[1.0 - c, c, 0.5, 0.5] for c in angles / tau]

rr.log("arrows", rr.Arrows3D(origins=origins, vectors=vectors, colors=colors))
```

 ![](https://static.rerun.io/arrow3d_simple/55e2f794a520bbf7527d7b828b0264732146c5d0/full.png)

##### def__init__(*,vectors,origins=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the Arrows3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec3DArrayLike |
| origins | All the origin points for each arrow in the batch.If no origins are set, (0, 0, 0) is used as the origin for each arrow.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Arrows3D`.



##### defcolumns(*,vectors=None,origins=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| origins | All the origin (base) positions for each arrow in the batch.If no origins are set, (0, 0, 0) is used as the origin for each arrow.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,vectors=None,origins=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `Arrows3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| vectors | All the vectors for each arrow in the batch.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| origins | All the origin (base) positions for each arrow in the batch.If no origins are set, (0, 0, 0) is used as the origin for each arrow.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the arrows.The shaft is rendered as a line withradius = 0.5 * radius. The tip is rendered withheight = 2.0 * radiusandradius = 1.0 * radius.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the arrows.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classAsset3D



Bases: `Asset3DExt`, `Archetype`



**Archetype**: A prepacked 3D asset (`.gltf`, `.glb`, `.obj`, `.stl`, etc.).



See also archetypes.Mesh3D.



If there are multiple archetypes.InstancePoses3D instances logged to the same entity as a mesh,
an instance of the mesh will be drawn for each transform.

 Example

###### Simple 3D asset:



```
import sys

import rerun as rr

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <path_to_asset.[gltf|glb|obj|stl]>")
    sys.exit(1)

rr.init("rerun_example_asset3d", spawn=True)

rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)  # Set an up-axis
rr.log("world/asset", rr.Asset3D(path=sys.argv[1]))
```

 ![](https://static.rerun.io/asset3d_simple/af238578188d3fd0de3e330212120e2842a8ddb2/full.png)

##### def__init__(*,path=None,contents=None,media_type=None,albedo_factor=None)



Create a new instance of the Asset3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | A path to an file stored on the local filesystem. Mutually exclusive withcontents.TYPE:str\|Path\| NoneDEFAULT:None |
| contents | The contents of the file. Can be a BufferedReader, BytesIO, or bytes. Mutually exclusive withpath.TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.For instance:  *model/gltf-binary*model/gltf+json*model/obj*model/stlIf omitted, it will be guessed from thepath(if any), or the viewer will try to guess from the contents (magic header). If the media type cannot be guessed, the viewer won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |
| albedo_factor | Optional color multiplier for the whole meshTYPE:Rgba32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Asset3D`.



##### defcolumns(*,blob=None,media_type=None,albedo_factor=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blob | The asset's bytes.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *model/gltf-binary*model/gltf+json*model/obj(.mtl material files are not supported yet, references are silently ignored) *model/stlIf omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| albedo_factor | A color multiplier applied to the whole asset.For mesh who already havealbedo_factorin materials, it will be overwritten by actualalbedo_factorofarchetypes.Asset3D(if specified).TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,blob=None,media_type=None,albedo_factor=None)classmethod



Update only some specific fields of a `Asset3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| blob | The asset's bytes.TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *model/gltf-binary*model/gltf+json*model/obj(.mtl material files are not supported yet, references are silently ignored) *model/stlIf omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |
| albedo_factor | A color multiplier applied to the whole asset.For mesh who already havealbedo_factorin materials, it will be overwritten by actualalbedo_factorofarchetypes.Asset3D(if specified).TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classAssetVideo



Bases: `AssetVideoExt`, `Archetype`



**Archetype**: A video binary.



Only MP4 containers are currently supported.



See [https://rerun.io/docs/reference/video](https://rerun.io/docs/reference/video) for codec support and more general information.



In order to display a video, you also need to log a archetypes.VideoFrameReference for each frame.



Examples:



###### Video with automatically determined frames:



```
import sys

import rerun as rr

if len(sys.argv) < 2:
    # TODO(#7354): Only mp4 is supported for now.
    print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
    sys.exit(1)

rr.init("rerun_example_asset_video_auto_frames", spawn=True)

# Log video asset which is referred to by frame references.
video_asset = rr.AssetVideo(path=sys.argv[1])
rr.log("video", video_asset, static=True)

# Send automatically determined video frame timestamps.
frame_timestamps_ns = video_asset.read_frame_timestamps_nanos()
rr.send_columns(
    "video",
    # Note timeline values don't have to be the same as the video timestamps.
    indexes=[rr.TimeColumn("video_time", duration=1e-9 * frame_timestamps_ns)],
    columns=rr.VideoFrameReference.columns_nanos(frame_timestamps_ns),
)
```

 ![](https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/full.png)

###### Demonstrates manual use of video frame references:



```
import sys

import rerun as rr
import rerun.blueprint as rrb

if len(sys.argv) < 2:
    # TODO(#7354): Only mp4 is supported for now.
    print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
    sys.exit(1)

rr.init("rerun_example_asset_video_manual_frames", spawn=True)

# Log video asset which is referred to by frame references.
rr.log("video_asset", rr.AssetVideo(path=sys.argv[1]), static=True)

# Create two entities, showing the same video frozen at different times.
rr.log(
    "frame_1s",
    rr.VideoFrameReference(seconds=1.0, video_reference="video_asset"),
)
rr.log(
    "frame_2s",
    rr.VideoFrameReference(seconds=2.0, video_reference="video_asset"),
)

# Send blueprint that shows two 2D views next to each other.
rr.send_blueprint(rrb.Horizontal(rrb.Spatial2DView(origin="frame_1s"), rrb.Spatial2DView(origin="frame_2s")))
```

 ![](https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/full.png)

##### def__init__(*,path=None,contents=None,media_type=None)



Create a new instance of the AssetVideo archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | A path to an file stored on the local filesystem. Mutually exclusive withcontents.TYPE:str\|Path\| NoneDEFAULT:None |
| contents | The contents of the file. Can be a BufferedReader, BytesIO, or bytes. Mutually exclusive withpath.TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.For instance:  *video/mp4If omitted, it will be guessed from thepath(if any), or the viewer will try to guess from the contents (magic header). If the media type cannot be guessed, the viewer won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `AssetVideo`.



##### defcolumns(*,blob=None,media_type=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blob | The asset's bytes.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *video/mp4If omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,blob=None,media_type=None)classmethod



Update only some specific fields of a `AssetVideo`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| blob | The asset's bytes.TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *video/mp4If omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defread_frame_timestamps_nanos()



Determines the presentation timestamps of all frames inside the video.



Throws a runtime exception if the video cannot be read.



#### classBarChart



Bases: `BarChartExt`, `Archetype`



**Archetype**: A bar chart.



The bar heights will be the provided values, and the x coordinates of the bars will be the provided abscissa or default to the index of the provided values.

 Example

###### Simple bar chart:



```
import rerun as rr

rr.init("rerun_example_bar_chart", spawn=True)
rr.log("bar_chart", rr.BarChart([8, 4, 0, 9, 1, 4, 1, 6, 9, 0]))
rr.log("bar_chart_custom_abscissa", rr.BarChart([8, 4, 0, 9, 1, 4], abscissa=[0, 1, 3, 4, 7, 11]))
rr.log(
    "bar_chart_custom_abscissa_and_widths",
    rr.BarChart([8, 4, 0, 9, 1, 4], abscissa=[0, 1, 3, 4, 7, 11], widths=[1, 2, 1, 3, 4, 1]),
)
```

 ![](https://static.rerun.io/bar_chart/ba274527813ccb9049f6760d82f36c8da6a6f2ff/full.png)

##### def__init__(values,*,color=None,abscissa=None,widths=None)



Create a new instance of the BarChart archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| values | The values. Should always be a 1-dimensional tensor (i.e. a vector).TYPE:TensorDataLike |
| color | The color of the bar chartTYPE:Rgba32Like\| NoneDEFAULT:None |
| abscissa | The abscissa corresponding to each value. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:TensorDataLike\| NoneDEFAULT:None |
| widths | The width of the bins, defined in x-axis units and defaults to 1. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `BarChart`.



##### defcolumns(*,values=None,color=None,abscissa=None,widths=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| values | The values. Should always be a 1-dimensional tensor (i.e. a vector).TYPE:TensorDataArrayLike\| NoneDEFAULT:None |
| color | The color of the bar chartTYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| abscissa | The abscissa corresponding to each value. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:TensorDataArrayLike\| NoneDEFAULT:None |
| widths | The width of the bins, defined in x-axis units and defaults to 1. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,values=None,color=None,abscissa=None,widths=None)classmethod



Update only some specific fields of a `BarChart`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| values | The values. Should always be a 1-dimensional tensor (i.e. a vector).TYPE:TensorDataLike\| NoneDEFAULT:None |
| color | The color of the bar chartTYPE:Rgba32Like\| NoneDEFAULT:None |
| abscissa | The abscissa corresponding to each value. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:TensorDataLike\| NoneDEFAULT:None |
| widths | The width of the bins, defined in x-axis units and defaults to 1. Should be a 1-dimensional tensor (i.e. a vector) in same length as values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



#### classBoxes2D



Bases: `Boxes2DExt`, `Archetype`



**Archetype**: 2D boxes with half-extents and optional center, colors etc.

 Example

###### Simple 2D boxes:



```
import rerun as rr

rr.init("rerun_example_box2d", spawn=True)

rr.log("simple", rr.Boxes2D(mins=[-1, -1], sizes=[2, 2]))
```

 ![](https://static.rerun.io/box2d_simple/ac4424f3cf747382867649610cbd749c45b2020b/full.png)

##### def__init__(*,sizes=None,mins=None,half_sizes=None,centers=None,array=None,array_format=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)



Create a new instance of the Boxes2D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| sizes | Full extents in x/y. Incompatible witharrayandhalf_sizes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| half_sizes | All half-extents that make up the batch of boxes. Specify this instead ofsizesIncompatible witharrayandsizes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| mins | Minimum coordinates of the boxes. Specify this instead ofcenters. Incompatible witharray. Only valid when used together with eithersizesorhalf_sizes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| array | An array of boxes in the format specified byarray_format.Requiresspecifyingarray_format. Incompatible withsizes,half_sizes,minsandcenters.TYPE:ArrayLike\| NoneDEFAULT:None |
| array_format | How to interpret the data inarray.TYPE:Box2DFormat\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order. Objects with higher values are drawn on top of those with lower values.The default for 2D boxes is 10.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | OptionalClassIds for the boxes.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Boxes2D`.



##### defcolumns(*,half_sizes=None,centers=None,colors=None,radii=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| half_sizes | All half-extents that make up the batch of boxes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to10.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the boxes.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,half_sizes=None,centers=None,colors=None,radii=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Update only some specific fields of a `Boxes2D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| half_sizes | All half-extents that make up the batch of boxes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to10.0.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the boxes.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classBoxes3D



Bases: `Boxes3DExt`, `Archetype`



**Archetype**: 3D boxes with half-extents and optional center, rotations, colors etc.



If there's more instance poses than half sizes, the last box's orientation will be repeated for the remaining poses.
Orienting and placing boxes forms a separate transform that is applied prior to archetypes.InstancePoses3D and archetypes.Transform3D.

 Example

###### Batch of 3D boxes:



```
import rerun as rr

rr.init("rerun_example_box3d_batch", spawn=True)

rr.log(
    "batch",
    rr.Boxes3D(
        centers=[[2, 0, 0], [-2, 0, 0], [0, 0, 2]],
        half_sizes=[[2.0, 2.0, 1.0], [1.0, 1.0, 0.5], [2.0, 0.5, 1.0]],
        quaternions=[
            rr.Quaternion.identity(),
            rr.Quaternion(xyzw=[0.0, 0.0, 0.382683, 0.923880]),  # 45 degrees around Z
        ],
        radii=0.025,
        colors=[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
        fill_mode="solid",
        labels=["red", "green", "blue"],
    ),
)
```

 ![](https://static.rerun.io/box3d_batch/5aac5b5d29c9f2ecd572c93f6970fcec17f4984b/full.png)

##### def__init__(*,sizes=None,mins=None,half_sizes=None,centers=None,rotation_axis_angles=None,quaternions=None,rotations=None,colors=None,radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the Boxes3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| sizes | Full extents in x/y/z. Specify this instead ofhalf_sizesTYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| half_sizes | All half-extents that make up the batch of boxes. Specify this instead ofsizesTYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| mins | Minimum coordinates of the boxes. Specify this instead ofcenters.Only valid when used together with eithersizesorhalf_sizes.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.If not specified, the centers will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| rotations | Backwards compatible parameter for specifying rotations. Tries to infer the type of rotation from the input. Prefer usingquaternionsorrotation_axis_angles.TYPE:RotationAxisAngleArrayLike\|QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the boxes are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | OptionalClassIds for the boxes.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Boxes3D`.



##### defcolumns(*,half_sizes=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| half_sizes | All half-extents that make up the batch of boxes.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.If not specified, the centers will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the boxes are drawn with lines or solid.TYPE:FillModeArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the boxes.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,half_sizes=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `Boxes3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| half_sizes | All half-extents that make up the batch of boxes.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the boxes.If not specified, the centers will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the lines that make up the boxes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the boxes are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the boxes.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the boxes.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classCapsules3D



Bases: `Capsules3DExt`, `Archetype`



**Archetype**: 3D capsules; cylinders with hemispherical caps.



Capsules are defined by two endpoints (the centers of their end cap spheres), which are located
at (0, 0, 0) and (0, 0, length), that is, extending along the positive direction of the Z axis.
Capsules in other orientations may be produced by applying a rotation to the entity or
instances.



If there's more instance poses than lengths & radii, the last capsule's orientation will be repeated for the remaining poses.
Orienting and placing capsules forms a separate transform that is applied prior to archetypes.InstancePoses3D and archetypes.Transform3D.

 Example

###### Batch of capsules:



```
import rerun as rr

rr.init("rerun_example_capsule3d_batch", spawn=True)

rr.log(
    "capsules",
    rr.Capsules3D(
        lengths=[0.0, 2.0, 4.0, 6.0, 8.0],
        radii=[1.0, 0.5, 0.5, 0.5, 1.0],
        colors=[
            (255, 0, 0),
            (188, 188, 0),
            (0, 255, 0),
            (0, 188, 188),
            (0, 0, 255),
        ],
        translations=[
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 0.0),
            (4.0, 0.0, 0.0),
            (6.0, 0.0, 0.0),
            (8.0, 0.0, 0.0),
        ],
        rotation_axis_angles=[
            rr.RotationAxisAngle(
                [1.0, 0.0, 0.0],
                rr.Angle(deg=float(i) * -22.5),
            )
            for i in range(5)
        ],
    ),
)
```

 ![](https://static.rerun.io/capsule3d_batch/6e6a4acafcf528359372147d7247f85d84434101/full.png)

##### def__init__(*,lengths=None,radii=None,translations=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the Capsules3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | All lengths of the capsules.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | All radii of the capsules.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| translations | Optional translations of the capsules.If not specified, one end of each capsule will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the capsules.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the cylinder is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the capsules.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | OptionalClassIds for the capsules.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Capsules3D`.



##### defcolumns(*,lengths=None,radii=None,translations=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | Lengths of the capsules, defined as the distance between the centers of the endcaps.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | Radii of the capsules.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| translations | Optional translations of the capsules.If not specified, one end of each capsule will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the capsules.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the cylinder is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the capsules, which will be located at their centers.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,lengths=None,radii=None,translations=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `Capsules3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| lengths | Lengths of the capsules, defined as the distance between the centers of the endcaps.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | Radii of the capsules.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| translations | Optional translations of the capsules.If not specified, one end of each capsule will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the capsules.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the cylinder is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the capsules, which will be located at their centers.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classClear



Bases: `ClearExt`, `Archetype`



**Archetype**: Empties all the components of an entity.



The presence of a clear means that a latest-at query of components at a given path(s)
will not return any components that were logged at those paths before the clear.
Any logged components after the clear are unaffected by the clear.



This implies that a range query that includes time points that are before the clear,
still returns all components at the given path(s).
Meaning that in practice clears are ineffective when making use of visible time ranges.
Scalar plots are an exception: they track clears and use them to represent holes in the
data (i.e. discontinuous lines).

 Example

###### Flat:



```
import rerun as rr

rr.init("rerun_example_clear", spawn=True)

vectors = [(1.0, 0.0, 0.0), (0.0, -1.0, 0.0), (-1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
origins = [(-0.5, 0.5, 0.0), (0.5, 0.5, 0.0), (0.5, -0.5, 0.0), (-0.5, -0.5, 0.0)]
colors = [(200, 0, 0), (0, 200, 0), (0, 0, 200), (200, 0, 200)]

# Log a handful of arrows.
for i, (vector, origin, color) in enumerate(zip(vectors, origins, colors, strict=False)):
    rr.log(f"arrows/{i}", rr.Arrows3D(vectors=vector, origins=origin, colors=color))

# Now clear them, one by one on each tick.
for i in range(len(vectors)):
    rr.log(f"arrows/{i}", rr.Clear(recursive=False))  # or `rr.Clear.flat()`
```

 ![](https://static.rerun.io/clear_simple/2f5df95fcc53e9f0552f65670aef7f94830c5c1a/full.png)

##### def__init__(*,recursive)



Create a new instance of the Clear archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| recursive | Whether to recursively clear all children.TYPE:bool |



##### defcleared()classmethod



Clear all the fields of a `Clear`.



##### defcolumns(*,is_recursive=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



##### defflat()staticmethod



Returns a non-recursive clear archetype.



This will empty all components of the associated entity at the logged timepoint.
Children will be left untouched.



##### deffrom_fields(*,clear_unset=False,is_recursive=None)classmethod



Update only some specific fields of a `Clear`.



##### defrecursive()staticmethod



Returns a recursive clear archetype.



This will empty all components of the associated entity at the logged timepoint, as well as
all components of all its recursive children.



#### classCoordinateFrame



Bases: `Archetype`



**Archetype**: Specifies the coordinate frame for an entity.



If not specified, the coordinate frame uses an implicit frame derived from the entity path.
The implicit frame's name is `tf#/your/entity/path` and has an identity transform connection to its parent path.



To learn more about transforms see [Spaces & Transforms](https://rerun.io/docs/concepts/spaces-and-transforms) in the reference.

 Example

###### Change coordinate frame to different built-in frames:



```
import rerun as rr

rr.init("rerun_example_transform3d_hierarchy", spawn=True)

rr.set_time("time", sequence=0)
rr.log(
    "red_box",
    rr.Boxes3D(half_sizes=[0.5, 0.5, 0.5], colors=[255, 0, 0]),
    # Use Transform3D to place the box, so we actually change the underlying coordinate frame and not just the box's pose.
    rr.Transform3D(translation=[2.0, 0.0, 0.0]),
)
rr.log(
    "blue_box",
    rr.Boxes3D(half_sizes=[0.5, 0.5, 0.5], colors=[0, 0, 255]),
    # Use Transform3D to place the box, so we actually change the underlying coordinate frame and not just the box's pose.
    rr.Transform3D(translation=[-2.0, 0.0, 0.0]),
)
rr.log("point", rr.Points3D([0.0, 0.0, 0.0], radii=0.5))

# Change where the point is located by cycling through its coordinate frame.
for t, frame_id in enumerate(["tf#/red_box", "tf#/blue_box"]):
    rr.set_time("time", sequence=t + 1)  # leave it untouched at t==0.
    rr.log("point", rr.CoordinateFrame(frame_id))
```

 ![](https://static.rerun.io/coordinate_frame_builtin_frame/71f941f35cf73c299c6ea7fbc4487a140db8e8f8/full.png)

##### def__init__(frame)



Create a new instance of the CoordinateFrame archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| frame | The coordinate frame to use for the current entity.TYPE:Utf8Like |



##### defcleared()classmethod



Clear all the fields of a `CoordinateFrame`.



##### defcolumns(*,frame=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| frame | The coordinate frame to use for the current entity.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,frame=None)classmethod



Update only some specific fields of a `CoordinateFrame`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| frame | The coordinate frame to use for the current entity.TYPE:Utf8Like\| NoneDEFAULT:None |



#### classCylinders3D



Bases: `Cylinders3DExt`, `Archetype`



**Archetype**: 3D cylinders with flat caps.



This archetype is for cylinder primitives defined by their axial length and radius.
For points whose radii are for visualization purposes, use archetypes.Points3D instead.



Orienting and placing cylinders forms a separate transform that is applied prior to archetypes.InstancePoses3D and archetypes.Transform3D.

 Example

###### Batch of cylinders:



```
import rerun as rr

rr.init("rerun_example_cylinders3d_batch", spawn=True)

rr.log(
    "cylinders",
    rr.Cylinders3D(
        lengths=[0.0, 2.0, 4.0, 6.0, 8.0],
        radii=[1.0, 0.5, 0.5, 0.5, 1.0],
        colors=[
            (255, 0, 0),
            (188, 188, 0),
            (0, 255, 0),
            (0, 188, 188),
            (0, 0, 255),
        ],
        centers=[
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 0.0),
            (4.0, 0.0, 0.0),
            (6.0, 0.0, 0.0),
            (8.0, 0.0, 0.0),
        ],
        rotation_axis_angles=[
            rr.RotationAxisAngle(
                [1.0, 0.0, 0.0],
                rr.Angle(deg=float(i) * -22.5),
            )
            for i in range(5)
        ],
    ),
)
```

 ![](https://static.rerun.io/cylinders3d_batch/ef642dede2bef23704eaff0f22aa48284d482b23/full.png)

##### def__init__(*,lengths=None,radii=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the Cylinders3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | All lengths of the cylinders.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | All radii of the cylinders.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| centers | Optional centers of the cylinders.If not specified, each cylinder will be centered at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the cylinders.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines that make up the cylinders.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the cylinders.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | OptionalClassIds for the cylinders.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Cylinders3D`.



##### defcolumns(*,lengths=None,radii=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lengths | The total axial length of the cylinder, measured as the straight-line distance between the centers of its two endcaps.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | Radii of the cylinders.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| centers | Optional centers of the cylinders.If not specified, each cylinder will be centered at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the cylinders.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the cylinder is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the cylinders, which will be located at their centers.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,lengths=None,radii=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `Cylinders3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| lengths | The total axial length of the cylinder, measured as the straight-line distance between the centers of its two endcaps.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| radii | Radii of the cylinders.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| centers | Optional centers of the cylinders.If not specified, each cylinder will be centered at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the cylinders align with the +Z axis of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the cylinders.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the cylinder is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the cylinders are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the cylinders, which will be located at their centers.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classDepthImage



Bases: `DepthImageExt`, `Archetype`



**Archetype**: A depth image, i.e. as captured by a depth camera.



Each pixel corresponds to a depth value in units specified by [components.DepthMeter](../components/#rerun.components.DepthMeter).

 Example

###### Depth to 3D example:



```
import numpy as np
import rerun as rr

depth_image = 65535 * np.ones((200, 300), dtype=np.uint16)
depth_image[50:150, 50:150] = 20000
depth_image[130:180, 100:280] = 45000

rr.init("rerun_example_depth_image_3d", spawn=True)

# If we log a pinhole camera model, the depth gets automatically back-projected to 3D
rr.log(
    "world/camera",
    rr.Pinhole(
        width=depth_image.shape[1],
        height=depth_image.shape[0],
        focal_length=200,
    ),
)

# Log the tensor.
rr.log("world/camera/depth", rr.DepthImage(depth_image, meter=10_000.0, colormap="viridis"))
```

 ![](https://static.rerun.io/depth_image_3d/924e9d4d6a39d63d4fdece82582855fdaa62d15e/full.png)

##### def__init__(image,*,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)



Create a new instance of the DepthImage archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| image | A numpy array or tensor with the depth image data. Leading and trailing unit-dimensions are ignored, so that1x480x640x1is treated as a480x640.TYPE:ImageLike |
| meter | An optional floating point value that specifies how long a meter is in the native depth units.For instance: with uint16, perhaps meter=1000 which would mean you have millimeter precision and a range of up to ~65 meters (2^16 / 1000).Note that the only effect on 2D views is the physical depth values shown when hovering the image. In 3D views on the other hand, this affects where the points of the point cloud are placed.TYPE:Float32Like\| NoneDEFAULT:None |
| colormap | Colormap to use for rendering the depth image.If not set, the depth image will be rendered using the Turbo colormap.TYPE:ColormapLike\| NoneDEFAULT:None |
| depth_range | The expected range of depth values.This is typically the expected range of valid values. Everything outside of the range is clamped to the range for the purpose of colormpaping. Note that point clouds generated from this image will still display all points, regardless of this range.If not specified, the range will be automatically be estimated from the data. Note that the Viewer may try to guess a wider range than the minimum/maximum of values in the contents of the depth image. E.g. if all values are positive, some bigger than 1.0 and all smaller than 255.0, the Viewer will guess that the data likely came from an 8bit image, thus assuming a range of 0-255.TYPE:Range1DLike\| NoneDEFAULT:None |
| point_fill_ratio | Scale the radii of the points in the point cloud generated from this image.A fill ratio of 1.0 (the default) means that each point is as big as to touch the center of its neighbor if it is at the same depth, leaving no gaps. A fill ratio of 0.5 means that each point touches the edge of its neighbor if it has the same depth.TODO(#6744): This applies only to 3D views!TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order, used only if the depth image is shown as a 2D image.Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `DepthImage`.



##### defcolumns(*,buffer=None,format=None,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| buffer | The raw depth image data.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatArrayLike\| NoneDEFAULT:None |
| meter | An optional floating point value that specifies how long a meter is in the native depth units.For instance: with uint16, perhaps meter=1000 which would mean you have millimeter precision and a range of up to ~65 meters (2^16 / 1000).If omitted, the Viewer defaults to1.0for floating-point depth formats and1000.0for integer formats (millimeters).Note that the only effect on 2D views is the physical depth values shown when hovering the image. In 3D views on the other hand, this affects where the points of the point cloud are placed.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colormap | Colormap to use for rendering the depth image.If not set, the depth image will be rendered using the Turbo colormap.TYPE:ColormapArrayLike\| NoneDEFAULT:None |
| depth_range | The expected range of depth values.This is typically the expected range of valid values. Everything outside of the range is clamped to the range for the purpose of colormpaping. Note that point clouds generated from this image will still display all points, regardless of this range.If not specified, the range will be automatically estimated from the data. Note that the Viewer may try to guess a wider range than the minimum/maximum of values in the contents of the depth image. E.g. if all values are positive, some bigger than 1.0 and all smaller than 255.0, the Viewer will guess that the data likely came from an 8bit image, thus assuming a range of 0-255.TYPE:Range1DArrayLike\| NoneDEFAULT:None |
| point_fill_ratio | Scale the radii of the points in the point cloud generated from this image.A fill ratio of 1.0 (the default) means that each point is as big as to touch the center of its neighbor if it is at the same depth, leaving no gaps. A fill ratio of 0.5 means that each point touches the edge of its neighbor if it has the same depth.TODO(#6744): This applies only to 3D views!TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order, used only if the depth image is shown as a 2D image.Objects with higher values are drawn on top of those with lower values. Defaults to-20.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,buffer=None,format=None,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)classmethod



Update only some specific fields of a `DepthImage`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| buffer | The raw depth image data.TYPE:BlobLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatLike\| NoneDEFAULT:None |
| meter | An optional floating point value that specifies how long a meter is in the native depth units.For instance: with uint16, perhaps meter=1000 which would mean you have millimeter precision and a range of up to ~65 meters (2^16 / 1000).If omitted, the Viewer defaults to1.0for floating-point depth formats and1000.0for integer formats (millimeters).Note that the only effect on 2D views is the physical depth values shown when hovering the image. In 3D views on the other hand, this affects where the points of the point cloud are placed.TYPE:Float32Like\| NoneDEFAULT:None |
| colormap | Colormap to use for rendering the depth image.If not set, the depth image will be rendered using the Turbo colormap.TYPE:ColormapLike\| NoneDEFAULT:None |
| depth_range | The expected range of depth values.This is typically the expected range of valid values. Everything outside of the range is clamped to the range for the purpose of colormpaping. Note that point clouds generated from this image will still display all points, regardless of this range.If not specified, the range will be automatically estimated from the data. Note that the Viewer may try to guess a wider range than the minimum/maximum of values in the contents of the depth image. E.g. if all values are positive, some bigger than 1.0 and all smaller than 255.0, the Viewer will guess that the data likely came from an 8bit image, thus assuming a range of 0-255.TYPE:Range1DLike\| NoneDEFAULT:None |
| point_fill_ratio | Scale the radii of the points in the point cloud generated from this image.A fill ratio of 1.0 (the default) means that each point is as big as to touch the center of its neighbor if it is at the same depth, leaving no gaps. A fill ratio of 0.5 means that each point touches the edge of its neighbor if it has the same depth.TODO(#6744): This applies only to 3D views!TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order, used only if the depth image is shown as a 2D image.Objects with higher values are drawn on top of those with lower values. Defaults to-20.0.TYPE:Float32Like\| NoneDEFAULT:None |



#### classEllipsoids3D



Bases: `Ellipsoids3DExt`, `Archetype`



**Archetype**: 3D ellipsoids or spheres.



This archetype is for ellipsoids or spheres whose size is a key part of the data
(e.g. a bounding sphere).
For points whose radii are for the sake of visualization, use archetypes.Points3D instead.



If there's more instance poses than half sizes, the last ellipsoid/sphere's orientation will be repeated for the remaining poses.
Orienting and placing ellipsoids/spheres forms a separate transform that is applied prior to archetypes.InstancePoses3D and archetypes.Transform3D.

 Example

###### Covariance ellipsoid:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_ellipsoid_simple", spawn=True)

center = np.array([0, 0, 0])
sigmas = np.array([5, 3, 1])
points = np.random.randn(50_000, 3) * sigmas.reshape(1, -1)

rr.log("points", rr.Points3D(points, radii=0.02, colors=[188, 77, 185]))
rr.log(
    "ellipsoid",
    rr.Ellipsoids3D(
        centers=[center, center],
        half_sizes=[sigmas, 3 * sigmas],
        colors=[[255, 255, 0], [64, 64, 0]],
    ),
)
```

 ![](https://static.rerun.io/elliopsoid3d_simple/bd5d46e61b80ae44792b52ee07d750a7137002ea/full.png)

##### def__init__(*,half_sizes=None,radii=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the Ellipsoids3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| half_sizes | All half-extents that make up the batch of ellipsoids. Specify this instead ofradiiTYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | All radii that make up this batch of spheres. Specify this instead ofhalf_sizesTYPE:Float32ArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the ellipsoids.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the boxes align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the ellipsoids.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines that make up the ellipsoids.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the ellipsoids are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the ellipsoids.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | OptionalClassIds for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Ellipsoids3D`.



##### defcolumns(*,half_sizes=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| half_sizes | For each ellipsoid, half of its size on its three axes.If all components are equal, then it is a sphere with that radius.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the ellipsoids.If not specified, the centers will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the ellipsoid align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the ellipsoid align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the ellipsoids.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the ellipsoid is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the ellipsoids are drawn with lines or solid.TYPE:FillModeArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the ellipsoids.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,half_sizes=None,centers=None,rotation_axis_angles=None,quaternions=None,colors=None,line_radii=None,fill_mode=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `Ellipsoids3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| half_sizes | For each ellipsoid, half of its size on its three axes.If all components are equal, then it is a sphere with that radius.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| centers | Optional center positions of the ellipsoids.If not specified, the centers will be at (0, 0, 0).TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.If no rotation is specified, the axes of the ellipsoid align with the axes of the local coordinate system.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.If no rotation is specified, the axes of the ellipsoid align with the axes of the local coordinate system.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the ellipsoids.Alpha channel is used for transparency for solid fill-mode.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_radii | Optional radii for the lines used when the ellipsoid is rendered as a wireframe.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| fill_mode | Optionally choose whether the ellipsoids are drawn with lines or solid.TYPE:FillModeLike\| NoneDEFAULT:None |
| labels | Optional text labels for the ellipsoids.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class ID for the ellipsoids.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classEncodedDepthImage



Bases: `Archetype`



**Archetype**: A depth image encoded with a codec (e.g. RVL or PNG).



Rerun also supports uncompressed depth images with the [archetypes.DepthImage](https://rerun.io/docs/reference/types/archetypes/depth_image).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Encoded depth image:



```
import sys
from pathlib import Path

import rerun as rr

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <path_to_depth_image.[png|rvl]>", file=sys.stderr)
    sys.exit(1)

depth_path = Path(sys.argv[1])

rr.init("rerun_example_encoded_depth_image", spawn=True)

depth_png = depth_path.read_bytes()
if depth_path.suffix.lower() == ".png":
    media_type = rr.components.MediaType.PNG
else:
    media_type = rr.components.MediaType.RVL

rr.log(
    "depth/encoded",
    rr.EncodedDepthImage(
        blob=depth_png,
        media_type=media_type,
        meter=0.001,
    ),
)
```

 ![](https://static.rerun.io/encoded_depth_image/d8180f8167278f9601808c360ba52eafaab52839/full.png)

##### def__init__(blob,*,media_type=None,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)



Create a new instance of the EncodedDepthImage archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blob | The encoded depth payload.Supported are: * single channel PNG * RVL with ROS2 metadata (for details seehttps://github.com/ros-perception/image_transport_plugins/tree/jazzy)TYPE:BlobLike |
| media_type | Media type of the blob, e.g.:application/rvl(RVL-compressed 16-bit)image/pngTYPE:Utf8Like\| NoneDEFAULT:None |
| meter | Conversion from native units to meters (e.g.0.001for millimeters).If omitted, the Viewer defaults to1.0for floating-point depth formats and1000.0for integer formats (millimeters).TYPE:Float32Like\| NoneDEFAULT:None |
| colormap | Optional colormap for visualization of decoded depth.TYPE:ColormapLike\| NoneDEFAULT:None |
| depth_range | Optional visualization range for depth values.TYPE:Range1DLike\| NoneDEFAULT:None |
| point_fill_ratio | Optional point fill ratio for point-cloud projection.TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | Optional 2D draw order.TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `EncodedDepthImage`.



##### defcolumns(*,blob=None,media_type=None,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blob | The encoded depth payload.Supported are: * single channel PNG * RVL with ROS2 metadata (for details seehttps://github.com/ros-perception/image_transport_plugins/tree/jazzy)TYPE:BlobArrayLike\| NoneDEFAULT:None |
| media_type | Media type of the blob, e.g.:application/rvl(RVL-compressed 16-bit)image/pngTYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| meter | Conversion from native units to meters (e.g.0.001for millimeters).If omitted, the Viewer defaults to1.0for floating-point depth formats and1000.0for integer formats (millimeters).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colormap | Optional colormap for visualization of decoded depth.TYPE:ColormapArrayLike\| NoneDEFAULT:None |
| depth_range | Optional visualization range for depth values.TYPE:Range1DArrayLike\| NoneDEFAULT:None |
| point_fill_ratio | Optional point fill ratio for point-cloud projection.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | Optional 2D draw order.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,blob=None,media_type=None,meter=None,colormap=None,depth_range=None,point_fill_ratio=None,draw_order=None)classmethod



Update only some specific fields of a `EncodedDepthImage`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| blob | The encoded depth payload.Supported are: * single channel PNG * RVL with ROS2 metadata (for details seehttps://github.com/ros-perception/image_transport_plugins/tree/jazzy)TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | Media type of the blob, e.g.:application/rvl(RVL-compressed 16-bit)image/pngTYPE:Utf8Like\| NoneDEFAULT:None |
| meter | Conversion from native units to meters (e.g.0.001for millimeters).If omitted, the Viewer defaults to1.0for floating-point depth formats and1000.0for integer formats (millimeters).TYPE:Float32Like\| NoneDEFAULT:None |
| colormap | Optional colormap for visualization of decoded depth.TYPE:ColormapLike\| NoneDEFAULT:None |
| depth_range | Optional visualization range for depth values.TYPE:Range1DLike\| NoneDEFAULT:None |
| point_fill_ratio | Optional point fill ratio for point-cloud projection.TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | Optional 2D draw order.TYPE:Float32Like\| NoneDEFAULT:None |



#### classEncodedImage



Bases: `EncodedImageExt`, `Archetype`



**Archetype**: An image encoded as e.g. a JPEG or PNG.



Rerun also supports uncompressed images with the archetypes.Image.
For images that refer to video frames see archetypes.VideoFrameReference.



To compress an image, use rerun.Image.compress.

 Example

###### Encoded image:



```
from pathlib import Path

import rerun as rr

image_file_path = Path(__file__).parent / "ferris.png"

rr.init("rerun_example_encoded_image", spawn=True)

rr.log("image", rr.EncodedImage(path=image_file_path))
```

 ![](https://static.rerun.io/encoded_image/6e92868b6533be5fb2dfd9e26938eb7a256bfb01/full.png)

##### def__init__(*,path=None,contents=None,media_type=None,opacity=None,draw_order=None)



Create a new instance of the EncodedImage archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| path | A path to an file stored on the local filesystem. Mutually exclusive withcontents.TYPE:str\|Path\| NoneDEFAULT:None |
| contents | The contents of the file. Can be a BufferedReader, BytesIO, or bytes. Mutually exclusive withpath.TYPE:bytes\|IO[bytes] \|BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.For instance:  *image/jpeg*image/pngIf omitted, it will be guessed from thepath(if any), or the viewer will try to guess from the contents (magic header). If the media type cannot be guessed, the viewer won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering several media. Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order. Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `EncodedImage`.



##### defcolumns(*,blob=None,media_type=None,opacity=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| blob | The encoded content of some image file, e.g. a PNG or JPEG.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *image/jpeg*image/pngIf omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,blob=None,media_type=None,opacity=None,draw_order=None)classmethod



Update only some specific fields of a `EncodedImage`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| blob | The encoded content of some image file, e.g. a PNG or JPEG.TYPE:BlobLike\| NoneDEFAULT:None |
| media_type | The Media Type of the asset.Supported values: *image/jpeg*image/pngIf omitted, the viewer will try to guess from the data blob. If it cannot guess, it won't be able to render the asset.TYPE:Utf8Like\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |



#### classGeoLineStrings



Bases: `GeoLineStringsExt`, `Archetype`



**Archetype**: Geospatial line strings with positions expressed in [EPSG:4326](https://epsg.io/4326) latitude and longitude (North/East-positive degrees), and optional colors and radii.



Also known as "line strips" or "polylines".

 Example

###### Log a geospatial line string:



```
import rerun as rr

rr.init("rerun_example_geo_line_strings", spawn=True)

rr.log(
    "colorado",
    rr.GeoLineStrings(
        lat_lon=[
            [41.0000, -109.0452],
            [41.0000, -102.0415],
            [36.9931, -102.0415],
            [36.9931, -109.0452],
            [41.0000, -109.0452],
        ],
        radii=rr.Radius.ui_points(2.0),
        colors=[0, 0, 255],
    ),
)
```

 ![](https://static.rerun.io/geo_line_strings_simple/5669983eb10906ace303755b5b5039cad75b917f/full.png)

##### def__init__(*,lat_lon,radii=None,colors=None)



Create a new instance of the GeoLineStrings archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lat_lon | The line strings, expressed inEPSG:4326coordinates (North/East-positive degrees).TYPE:GeoLineStringArrayLike |
| radii | Optional radii for the line strings.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the linestrings.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `GeoLineStrings`.



##### defcolumns(*,line_strings=None,radii=None,colors=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| line_strings | The line strings, expressed inEPSG:4326coordinates (North/East-positive degrees).TYPE:GeoLineStringArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strings.Note: scene units radiii are interpreted as meters. Currently, the display scale only considers the latitude of the first vertex of each line string (seethis issue).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strings.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,line_strings=None,radii=None,colors=None)classmethod



Update only some specific fields of a `GeoLineStrings`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| line_strings | The line strings, expressed inEPSG:4326coordinates (North/East-positive degrees).TYPE:GeoLineStringArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strings.Note: scene units radiii are interpreted as meters. Currently, the display scale only considers the latitude of the first vertex of each line string (seethis issue).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strings.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



#### classGeoPoints



Bases: `GeoPointsExt`, `Archetype`



**Archetype**: Geospatial points with positions expressed in [EPSG:4326](https://epsg.io/4326) latitude and longitude (North/East-positive degrees), and optional colors and radii.

 Example

###### Log a geospatial point:



```
import rerun as rr

rr.init("rerun_example_geo_points", spawn=True)

rr.log(
    "rerun_hq",
    rr.GeoPoints(
        lat_lon=[59.319221, 18.075631],
        radii=rr.Radius.ui_points(10.0),
        colors=[255, 0, 0],
    ),
)
```

 ![](https://static.rerun.io/geopoint_simple/b86ce83e5871837587bd33a0ad639358b96e9010/full.png)

##### def__init__(*,lat_lon,radii=None,colors=None)



Create a new instance of the GeoPoints archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| lat_lon | TheEPSG:4326coordinates for the points (North/East-positive degrees).TYPE:DVec2DArrayLike |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `GeoPoints`.



##### defcolumns(*,positions=None,radii=None,colors=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| positions | TheEPSG:4326coordinates for the points (North/East-positive degrees).TYPE:DVec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.Note: scene units radiii are interpreted as meters.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,positions=None,radii=None,colors=None,class_ids=None)classmethod



Update only some specific fields of a `GeoPoints`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| positions | TheEPSG:4326coordinates for the points (North/East-positive degrees).TYPE:DVec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.Note: scene units radiii are interpreted as meters.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classGraphEdges



Bases: `Archetype`



**Archetype**: A list of edges in a graph.



By default, edges are undirected.

 Example

###### Simple directed graph:



```
import rerun as rr

rr.init("rerun_example_graph_directed", spawn=True)

rr.log(
    "simple",
    rr.GraphNodes(
        node_ids=["a", "b", "c"],
        positions=[(0.0, 100.0), (-100.0, 0.0), (100.0, 0.0)],
        labels=["A", "B", "C"],
    ),
    rr.GraphEdges(edges=[("a", "b"), ("b", "c"), ("c", "a")], graph_type="directed"),
)
```

 ![](https://static.rerun.io/graph_directed/ca29a37b65e1e0b6482251dce401982a0bc568fa/full.png)

##### def__init__(edges,*,graph_type=None)



Create a new instance of the GraphEdges archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| edges | A list of node tuples.TYPE:Utf8PairArrayLike |
| graph_type | Specifies if the graph is directed or undirected.If nocomponents.GraphTypeis provided, the graph is assumed to be undirected.TYPE:GraphTypeLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `GraphEdges`.



##### defcolumns(*,edges=None,graph_type=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| edges | A list of node tuples.TYPE:Utf8PairArrayLike\| NoneDEFAULT:None |
| graph_type | Specifies if the graph is directed or undirected.If nocomponents.GraphTypeis provided, the graph is assumed to be undirected.TYPE:GraphTypeArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,edges=None,graph_type=None)classmethod



Update only some specific fields of a `GraphEdges`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| edges | A list of node tuples.TYPE:Utf8PairArrayLike\| NoneDEFAULT:None |
| graph_type | Specifies if the graph is directed or undirected.If nocomponents.GraphTypeis provided, the graph is assumed to be undirected.TYPE:GraphTypeLike\| NoneDEFAULT:None |



#### classGraphNodes



Bases: `Archetype`



**Archetype**: A list of nodes in a graph with optional labels, colors, etc.

 Example

###### Simple directed graph:



```
import rerun as rr

rr.init("rerun_example_graph_directed", spawn=True)

rr.log(
    "simple",
    rr.GraphNodes(
        node_ids=["a", "b", "c"],
        positions=[(0.0, 100.0), (-100.0, 0.0), (100.0, 0.0)],
        labels=["A", "B", "C"],
    ),
    rr.GraphEdges(edges=[("a", "b"), ("b", "c"), ("c", "a")], graph_type="directed"),
)
```

 ![](https://static.rerun.io/graph_directed/ca29a37b65e1e0b6482251dce401982a0bc568fa/full.png)

##### def__init__(node_ids,*,positions=None,colors=None,labels=None,show_labels=None,radii=None)



Create a new instance of the GraphNodes archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| node_ids | A list of node IDs.TYPE:Utf8ArrayLike |
| positions | Optional center positions of the nodes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the node.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| radii | Optional radii for nodes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `GraphNodes`.



##### defcolumns(*,node_ids=None,positions=None,colors=None,labels=None,show_labels=None,radii=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| node_ids | A list of node IDs.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| positions | Optional center positions of the nodes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the node.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for nodes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,node_ids=None,positions=None,colors=None,labels=None,show_labels=None,radii=None)classmethod



Update only some specific fields of a `GraphNodes`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| node_ids | A list of node IDs.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| positions | Optional center positions of the nodes.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the boxes.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the node.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| radii | Optional radii for nodes.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



#### classImage



Bases: `ImageExt`, `Archetype`



**Archetype**: A monochrome or color image.



See also archetypes.DepthImage and archetypes.SegmentationImage.



Rerun also supports compressed images (JPEG, PNG, â¦), using archetypes.EncodedImage.
For images that refer to video frames see archetypes.VideoFrameReference.
Compressing images or using video data instead can save a lot of bandwidth and memory.



The raw image data is stored as a single buffer of bytes in a [components.Blob](../components/#rerun.components.Blob).
The meaning of these bytes is determined by the [components.ImageFormat](../components/#rerun.components.ImageFormat) which specifies the resolution
and the pixel format (e.g. RGB, RGBA, â¦).



The order of dimensions in the underlying [components.Blob](../components/#rerun.components.Blob) follows the typical
row-major, interleaved-pixel image format.



Examples:



###### image_simple:



```
import numpy as np
import rerun as rr

# Create an image with numpy
image = np.zeros((200, 300, 3), dtype=np.uint8)
image[:, :, 0] = 255
image[50:150, 50:150] = (0, 255, 0)

rr.init("rerun_example_image", spawn=True)

rr.log("image", rr.Image(image))
```

 ![](https://static.rerun.io/image_simple/06ba7f8582acc1ffb42a7fd0006fad7816f3e4e4/full.png)

###### Logging images with various formats:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_image_formats", spawn=True)

# Simple gradient image, logged in different formats.
image = np.array([[[x, min(255, x + y), y] for x in range(256)] for y in range(256)], dtype=np.uint8)
rr.log("image_rgb", rr.Image(image))
rr.log("image_green_only", rr.Image(image[:, :, 1], color_model="l"))  # Luminance only
rr.log("image_bgr", rr.Image(image[:, :, ::-1], color_model="bgr"))  # BGR

# New image with Separate Y/U/V planes with 4:2:2 chroma downsampling
y = bytes([128 for y in range(256) for x in range(256)])
u = bytes([x * 2 for y in range(256) for x in range(128)])  # Half horizontal resolution for chroma.
v = bytes([y for y in range(256) for x in range(128)])
rr.log("image_yuv422", rr.Image(bytes=y + u + v, width=256, height=256, pixel_format=rr.PixelFormat.Y_U_V16_FullRange))
```

 ![](https://static.rerun.io/image_formats/182a233fb4d0680eb31912a82f328ddaaa66324e/full.png)

##### def__init__(image=None,color_model=None,*,pixel_format=None,datatype=None,bytes=None,width=None,height=None,opacity=None,draw_order=None)



Create a new image with a given format.



There are three ways to create an image:
* By specifying an `image` as an appropriately shaped ndarray with an appropriate `color_model`.
* By specifying `bytes` of an image with a `pixel_format`, together with `width`, `height`.
* By specifying `bytes` of an image with a `datatype` and `color_model`, together with `width`, `height`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| image | A numpy array or tensor with the image data. Leading and trailing unit-dimensions are ignored, so that1x480x640x3x1is treated as a480x640x3. You also need to specify thecolor_modelof it (e.g. "RGB").TYPE:ImageLike\| NoneDEFAULT:None |
| color_model | L, RGB, RGBA, BGR, BGRA, etc, specifying how to interpretimage.TYPE:ColorModelLike\| NoneDEFAULT:None |
| pixel_format | NV12, YUV420, etc. For chroma-downsampling. Requireswidth,height, andbytes.TYPE:PixelFormatLike\| NoneDEFAULT:None |
| datatype | The datatype of the image data. If not specified, it is inferred from theimage.TYPE:ChannelDatatypeLike\|type\| NoneDEFAULT:None |
| bytes | The raw bytes of an image specified bypixel_format.TYPE:bytes\| NoneDEFAULT:None |
| width | The width of the image. Only requires forpixel_format.TYPE:int\| NoneDEFAULT:None |
| height | The height of the image. Only requires forpixel_format.TYPE:int\| NoneDEFAULT:None |
| opacity | Optional opacity of the image, in 0-1. Set to 0.5 for a translucent image.TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order. Objects with higher values are drawn on top of those with lower values.TYPE:Float32Like\| NoneDEFAULT:None |



##### defas_pil_image()



Convert the image to a PIL Image.



##### defcleared()classmethod



Clear all the fields of a `Image`.



##### defcolumns(*,buffer=None,format=None,opacity=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| buffer | The raw image data.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatArrayLike\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-10.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### defcompress(jpeg_quality=95)



Compress the given image as a JPEG.



JPEG compression works best for photographs.
Only U8 RGB and grayscale images are supported, not RGBA.
Note that compressing to JPEG costs a bit of CPU time,
both when logging and later when viewing them.



| PARAMETER | DESCRIPTION |
| --- | --- |
| jpeg_quality | Higher quality = larger file size. A quality of 95 saves a lot of space, but is still visually very similar.TYPE:intDEFAULT:95 |



##### deffrom_fields(*,clear_unset=False,buffer=None,format=None,opacity=None,draw_order=None)classmethod



Update only some specific fields of a `Image`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| buffer | The raw image data.TYPE:BlobLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatLike\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-10.0.TYPE:Float32Like\| NoneDEFAULT:None |



##### defimage_format()



Returns the image format of this image.



#### classInstancePoses3D



Bases: `Archetype`



**Archetype**: One or more transforms applied on the current entity's transform frame.



Unlike archetypes.Transform3D, it is *not* propagated in the transform hierarchy.
If archetypes.CoordinateFrame is specified, it acts relative to that coordinate frame,
otherwise it is relative to the entity's implicit coordinate frame.



Whenever you log this archetype, the state of the resulting overall pose is fully reset to the new archetype.
This means that if you first log a pose with only a translation, and then log one with only a rotation,
it will be resolved to a pose with only a rotation.
(This is unlike how we usually apply latest-at semantics on an archetype where we take the latest state of any component independently)



From the point of view of the entity's coordinate system,
all components are applied in the inverse order they are listed here.
E.g. if both a translation and a mat3x3 transform are present,
the 3x3 matrix is applied first, followed by the translation.



Currently, many visualizers support only a single instance transform per entity.
Check archetype documentations for details - if not otherwise specified, only the first instance transform is applied.
Some visualizers like the mesh visualizer used for archetypes.Mesh3D,
will draw an object for every pose, a behavior also known as "instancing".

 Example

###### Regular & instance transforms in tandem:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_instance_pose3d_combined", spawn=True)

rr.set_time("frame", sequence=0)

# Log a box and points further down in the hierarchy.
rr.log("world/box", rr.Boxes3D(half_sizes=[[1.0, 1.0, 1.0]]))
lin = np.linspace(-10, 10, 10)
z, y, x = np.meshgrid(lin, lin, lin, indexing="ij")
point_grid = np.vstack([x.flatten(), y.flatten(), z.flatten()]).T
rr.log("world/box/points", rr.Points3D(point_grid))

for i in range(180):
    rr.set_time("frame", sequence=i)

    # Log a regular transform which affects both the box and the points.
    rr.log("world/box", rr.Transform3D(rotation_axis_angle=rr.RotationAxisAngle([0, 0, 1], angle=rr.Angle(deg=i * 2))))

    # Log an instance pose which affects only the box.
    rr.log("world/box", rr.InstancePoses3D(translations=[0, 0, abs(i * 0.1 - 5.0) - 5.0]))
```

 ![](https://static.rerun.io/leaf_transform3d/41674f0082d6de489f8a1cd1583f60f6b5820ddf/full.png)

##### def__init__(*,translations=None,rotation_axis_angles=None,quaternions=None,scales=None,mat3x3=None)



Create a new instance of the InstancePoses3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| translations | Translation vectors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| scales | Scaling factors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| mat3x3 | 3x3 transformation matrices.TYPE:Mat3x3ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `InstancePoses3D`.



##### defcolumns(*,translations=None,rotation_axis_angles=None,quaternions=None,scales=None,mat3x3=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| translations | Translation vectors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| scales | Scaling factors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| mat3x3 | 3x3 transformation matrices.TYPE:Mat3x3ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,translations=None,rotation_axis_angles=None,quaternions=None,scales=None,mat3x3=None)classmethod



Update only some specific fields of a `InstancePoses3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| translations | Translation vectors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angles | Rotations via axis + angle.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternions | Rotations via quaternion.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| scales | Scaling factors.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| mat3x3 | 3x3 transformation matrices.TYPE:Mat3x3ArrayLike\| NoneDEFAULT:None |



#### classLineStrips2D



Bases: `Archetype`



**Archetype**: 2D line strips with positions and optional colors, radii, labels, etc.



Examples:



###### line_strips2d_batch:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_line_strip2d_batch", spawn=True)

rr.log(
    "strips",
    rr.LineStrips2D(
        [
            [[0, 0], [2, 1], [4, -1], [6, 0]],
            [[0, 3], [1, 4], [2, 2], [3, 4], [4, 2], [5, 4], [6, 3]],
        ],
        colors=[[255, 0, 0], [0, 255, 0]],
        radii=[0.025, 0.005],
        labels=["one strip here", "and one strip there"],
    ),
)

# Set view bounds:
rr.send_blueprint(rrb.Spatial2DView(visual_bounds=rrb.VisualBounds2D(x_range=[-1, 7], y_range=[-3, 6])))
```

 ![](https://static.rerun.io/line_strip2d_batch/c6f4062bcf510462d298a5dfe9fdbe87c754acee/full.png)

###### Lines with scene & UI radius each:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_line_strip2d_ui_radius", spawn=True)

# A blue line with a scene unit radii of 0.01.
points = [[0, 0], [0, 1], [1, 0], [1, 1]]
rr.log(
    "scene_unit_line",
    rr.LineStrips2D(
        [points],
        # By default, radii are interpreted as world-space units.
        radii=0.01,
        colors=[0, 0, 255],
    ),
)

# A red line with a ui point radii of 5.
# UI points are independent of zooming in Views, but are sensitive to the application UI scaling.
# For 100% ui scaling, UI points are equal to pixels.
points = [[3, 0], [3, 1], [4, 0], [4, 1]]
rr.log(
    "ui_points_line",
    rr.LineStrips2D(
        [points],
        # rr.Radius.ui_points produces radii that the viewer interprets as given in ui points.
        radii=rr.Radius.ui_points(5.0),
        colors=[255, 0, 0],
    ),
)

# Set view bounds:
rr.send_blueprint(rrb.Spatial2DView(visual_bounds=rrb.VisualBounds2D(x_range=[-1, 5], y_range=[-1, 2])))
```



##### def__init__(strips,*,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)



Create a new instance of the LineStrips2D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| strips | All the actual 2D line strips that make up the batch.TYPE:LineStrip2DArrayLike |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order of each line strip.Objects with higher values are drawn on top of those with lower values. Defaults to20.0.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `LineStrips2D`.



##### defcolumns(*,strips=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| strips | All the actual 2D line strips that make up the batch.TYPE:LineStrip2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order of each line strip.Objects with higher values are drawn on top of those with lower values. Defaults to20.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,strips=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None)classmethod



Update only some specific fields of a `LineStrips2D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| strips | All the actual 2D line strips that make up the batch.TYPE:LineStrip2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order of each line strip.Objects with higher values are drawn on top of those with lower values. Defaults to20.0.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classLineStrips3D



Bases: `Archetype`



**Archetype**: 3D line strips with positions and optional colors, radii, labels, etc.



Examples:



###### Many strips:



```
import rerun as rr

rr.init("rerun_example_line_strip3d_batch", spawn=True)

rr.log(
    "strips",
    rr.LineStrips3D(
        [
            [
                [0, 0, 2],
                [1, 0, 2],
                [1, 1, 2],
                [0, 1, 2],
            ],
            [
                [0, 0, 0],
                [0, 0, 1],
                [1, 0, 0],
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 1],
                [0, 1, 0],
                [0, 1, 1],
            ],
        ],
        colors=[[255, 0, 0], [0, 255, 0]],
        radii=[0.025, 0.005],
        labels=["one strip here", "and one strip there"],
    ),
)
```

 ![](https://static.rerun.io/line_strip3d_batch/15e8ff18a6c95a3191acb0eae6eb04adea3b4874/full.png)

###### Lines with scene & UI radius each:



```
import rerun as rr

rr.init("rerun_example_line_strip3d_ui_radius", spawn=True)

# A blue line with a scene unit radii of 0.01.
points = [[0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 0, 1]]
rr.log(
    "scene_unit_line",
    rr.LineStrips3D(
        [points],
        # By default, radii are interpreted as world-space units.
        radii=0.01,
        colors=[0, 0, 255],
    ),
)

# A red line with a ui point radii of 5.
# UI points are independent of zooming in Views, but are sensitive to the application UI scaling.
# For 100% ui scaling, UI points are equal to pixels.
points = [[3, 0, 0], [3, 0, 1], [4, 0, 0], [4, 0, 1]]
rr.log(
    "ui_points_line",
    rr.LineStrips3D(
        [points],
        # rr.Radius.ui_points produces radii that the viewer interprets as given in ui points.
        radii=rr.Radius.ui_points(5.0),
        colors=[255, 0, 0],
    ),
)
```

 ![](https://static.rerun.io/line_strip3d_ui_radius/36b98f47e45747b5a3601511ff39b8d74c61d120/full.png)

##### def__init__(strips,*,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)



Create a new instance of the LineStrips3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| strips | All the actual 3D line strips that make up the batch.TYPE:LineStrip3DArrayLike |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `LineStrips3D`.



##### defcolumns(*,strips=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| strips | All the actual 3D line strips that make up the batch.TYPE:LineStrip3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,strips=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None)classmethod



Update only some specific fields of a `LineStrips3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| strips | All the actual 3D line strips that make up the batch.TYPE:LineStrip3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the line strips.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the line strips.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the line strips.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optionalcomponents.ClassIds for the lines.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classMcapChannel



Bases: `Archetype`



**Archetype**: A channel within an MCAP file that defines how messages are structured and encoded.



Channels in MCAP files group messages by topic and define their encoding format.
Each channel has a unique identifier and specifies the message schema and encoding used
for all messages published to that topic.



See also archetypes.McapMessage for individual messages within a channel,
archetypes.McapSchema for the data structure definitions, and the
[MCAP specification](https://mcap.dev/) for complete format details.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,id,topic,message_encoding,metadata=None)



Create a new instance of the McapChannel archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| id | Unique identifier for this channel within the MCAP file.Channel IDs must be unique within a single MCAP file and are used to associate messages with their corresponding channel definition.TYPE:UInt16Like |
| topic | The topic name that this channel publishes to.Topics are hierarchical paths from the original robotics system (e.g., "/sensors/camera/image") that categorize and organize different data streams. Topics are separate from Rerun's entity paths, but they often can be mapped to them.TYPE:Utf8Like |
| message_encoding | The encoding format used for messages in this channel.Common encodings include: *ros1- ROS1 message format *cdr- Common Data Representation (CDR) message format, used by ROS2 *protobuf- Protocol Buffers *json- JSON encodingTYPE:Utf8Like |
| metadata | Additional metadata for this channel stored as key-value pairs.This can include channel-specific configuration, description, units, coordinate frames, or any other contextual information that helps interpret the data in this channel.TYPE:KeyValuePairsLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `McapChannel`.



##### defcolumns(*,id=None,topic=None,message_encoding=None,metadata=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| id | Unique identifier for this channel within the MCAP file.Channel IDs must be unique within a single MCAP file and are used to associate messages with their corresponding channel definition.TYPE:UInt16ArrayLike\| NoneDEFAULT:None |
| topic | The topic name that this channel publishes to.Topics are hierarchical paths from the original robotics system (e.g., "/sensors/camera/image") that categorize and organize different data streams. Topics are separate from Rerun's entity paths, but they often can be mapped to them.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| message_encoding | The encoding format used for messages in this channel.Common encodings include: *ros1- ROS1 message format *cdr- Common Data Representation (CDR) message format, used by ROS2 *protobuf- Protocol Buffers *json- JSON encodingTYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| metadata | Additional metadata for this channel stored as key-value pairs.This can include channel-specific configuration, description, units, coordinate frames, or any other contextual information that helps interpret the data in this channel.TYPE:KeyValuePairsArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,id=None,topic=None,message_encoding=None,metadata=None)classmethod



Update only some specific fields of a `McapChannel`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| id | Unique identifier for this channel within the MCAP file.Channel IDs must be unique within a single MCAP file and are used to associate messages with their corresponding channel definition.TYPE:UInt16Like\| NoneDEFAULT:None |
| topic | The topic name that this channel publishes to.Topics are hierarchical paths from the original robotics system (e.g., "/sensors/camera/image") that categorize and organize different data streams. Topics are separate from Rerun's entity paths, but they often can be mapped to them.TYPE:Utf8Like\| NoneDEFAULT:None |
| message_encoding | The encoding format used for messages in this channel.Common encodings include: *ros1- ROS1 message format *cdr- Common Data Representation (CDR) message format, used by ROS2 *protobuf- Protocol Buffers *json- JSON encodingTYPE:Utf8Like\| NoneDEFAULT:None |
| metadata | Additional metadata for this channel stored as key-value pairs.This can include channel-specific configuration, description, units, coordinate frames, or any other contextual information that helps interpret the data in this channel.TYPE:KeyValuePairsLike\| NoneDEFAULT:None |



#### classMcapMessage



Bases: `Archetype`



**Archetype**: The binary payload of a single MCAP message, without metadata.



This archetype represents only the raw message data from an MCAP file. It does not include
MCAP message metadata such as timestamps, channel IDs, sequence numbers, or publication times.
The binary payload represents sensor data, commands, or other information encoded according
to the format specified by the associated channel.



See archetypes.McapChannel for channel definitions that specify message encoding,
archetypes.McapSchema for data structure definitions, and the
[MCAP specification](https://mcap.dev/) for complete format details.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(data)



Create a new instance of the McapMessage archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| data | The raw message payload as a binary blob.This contains the actual message data encoded according to the format specified by the associated channel'smessage_encodingfield. The structure and interpretation of this binary data depends on the encoding format (e.g., ros1, cdr, protobuf) and the message schema defined for the channel.TYPE:BlobLike |



##### defcleared()classmethod



Clear all the fields of a `McapMessage`.



##### defcolumns(*,data=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| data | The raw message payload as a binary blob.This contains the actual message data encoded according to the format specified by the associated channel'smessage_encodingfield. The structure and interpretation of this binary data depends on the encoding format (e.g., ros1, cdr, protobuf) and the message schema defined for the channel.TYPE:BlobArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,data=None)classmethod



Update only some specific fields of a `McapMessage`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| data | The raw message payload as a binary blob.This contains the actual message data encoded according to the format specified by the associated channel'smessage_encodingfield. The structure and interpretation of this binary data depends on the encoding format (e.g., ros1, cdr, protobuf) and the message schema defined for the channel.TYPE:BlobLike\| NoneDEFAULT:None |



#### classMcapSchema



Bases: `Archetype`



**Archetype**: A schema definition that describes the structure of messages in an MCAP file.



Schemas define the data types and field structures used by messages in MCAP channels.
They provide the blueprint for interpreting message payloads, specifying field names,
types, and organization. Each schema is referenced by channels to indicate how their
messages should be decoded and understood.



See also archetypes.McapChannel for channels that reference these schemas,
archetypes.McapMessage for the messages that conform to these schemas, and the
[MCAP specification](https://mcap.dev/) for complete format details.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,id,name,encoding,data)



Create a new instance of the McapSchema archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| id | Unique identifier for this schema within the MCAP file.Schema IDs must be unique within an MCAP file and are referenced by channels to specify their message structure. A single schema can be shared across multiple channels.TYPE:UInt16Like |
| name | Human-readable name identifying this schema.Schema names typically describe the message type or data structure (e.g.,"geometry_msgs/msg/Twist","sensor_msgs/msg/Image","MyCustomMessage").TYPE:Utf8Like |
| encoding | The schema definition format used to describe the message structure.Common schema encodings include: *protobuf-Protocol Buffersschema definition *ros1msg-ROS1message definition format *ros2msg-ROS2message definition format *jsonschema-JSON Schemaspecification *flatbuffer-FlatBuffersschema definitionTYPE:Utf8Like |
| data | The schema definition content as binary data.This contains the actual schema specification in the format indicated by theencodingfield. For text-based schemas (like ROS message definitions or JSON Schema), this is typically UTF-8 encoded text. For binary schema formats, this contains the serialized schema data.TYPE:BlobLike |



##### defcleared()classmethod



Clear all the fields of a `McapSchema`.



##### defcolumns(*,id=None,name=None,encoding=None,data=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| id | Unique identifier for this schema within the MCAP file.Schema IDs must be unique within an MCAP file and are referenced by channels to specify their message structure. A single schema can be shared across multiple channels.TYPE:UInt16ArrayLike\| NoneDEFAULT:None |
| name | Human-readable name identifying this schema.Schema names typically describe the message type or data structure (e.g.,"geometry_msgs/msg/Twist","sensor_msgs/msg/Image","MyCustomMessage").TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| encoding | The schema definition format used to describe the message structure.Common schema encodings include: *protobuf-Protocol Buffersschema definition *ros1msg-ROS1message definition format *ros2msg-ROS2message definition format *jsonschema-JSON Schemaspecification *flatbuffer-FlatBuffersschema definitionTYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| data | The schema definition content as binary data.This contains the actual schema specification in the format indicated by theencodingfield. For text-based schemas (like ROS message definitions or JSON Schema), this is typically UTF-8 encoded text. For binary schema formats, this contains the serialized schema data.TYPE:BlobArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,id=None,name=None,encoding=None,data=None)classmethod



Update only some specific fields of a `McapSchema`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| id | Unique identifier for this schema within the MCAP file.Schema IDs must be unique within an MCAP file and are referenced by channels to specify their message structure. A single schema can be shared across multiple channels.TYPE:UInt16Like\| NoneDEFAULT:None |
| name | Human-readable name identifying this schema.Schema names typically describe the message type or data structure (e.g.,"geometry_msgs/msg/Twist","sensor_msgs/msg/Image","MyCustomMessage").TYPE:Utf8Like\| NoneDEFAULT:None |
| encoding | The schema definition format used to describe the message structure.Common schema encodings include: *protobuf-Protocol Buffersschema definition *ros1msg-ROS1message definition format *ros2msg-ROS2message definition format *jsonschema-JSON Schemaspecification *flatbuffer-FlatBuffersschema definitionTYPE:Utf8Like\| NoneDEFAULT:None |
| data | The schema definition content as binary data.This contains the actual schema specification in the format indicated by theencodingfield. For text-based schemas (like ROS message definitions or JSON Schema), this is typically UTF-8 encoded text. For binary schema formats, this contains the serialized schema data.TYPE:BlobLike\| NoneDEFAULT:None |



#### classMcapStatistics



Bases: `Archetype`



**Archetype**: Recording-level statistics about an MCAP file, logged as a part of archetypes.RecordingInfo.



This archetype contains summary information about an entire MCAP recording, including
counts of messages, schemas, channels, and other records, as well as timing information
spanning the full recording duration. It is typically logged once per recording to provide
an overview of the dataset's structure and content.



See also archetypes.McapChannel for individual channel definitions,
archetypes.McapMessage for message content, archetypes.McapSchema for schema definitions,
and the [MCAP specification](https://mcap.dev/) for complete format details.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,message_count,schema_count,channel_count,attachment_count,metadata_count,chunk_count,message_start_time,message_end_time,channel_message_counts=None)



Create a new instance of the McapStatistics archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| message_count | Total number of data messages contained in the MCAP recording.This count includes all timestamped data messages but excludes metadata records, schema definitions, and other non-message records.TYPE:UInt64Like |
| schema_count | Number of unique schema definitions in the recording.Each schema defines the structure for one or more message types used by channels.TYPE:UInt64Like |
| channel_count | Number of channels defined in the recording.Each channel represents a unique topic and encoding combination for publishing messages.TYPE:UInt64Like |
| attachment_count | Number of file attachments embedded in the recording.Attachments can include calibration files, configuration data, or other auxiliary files.TYPE:UInt64Like |
| metadata_count | Number of metadata records providing additional context about the recording.Metadata records contain key-value pairs with information about the recording environment, system configuration, or other contextual data.TYPE:UInt64Like |
| chunk_count | Number of data chunks used to organize messages in the file.Chunks group related messages together for efficient storage and indexed access.TYPE:UInt64Like |
| message_start_time | Timestamp of the earliest message in the recording.This marks the beginning of the recorded data timeline.TYPE:TimeIntLike |
| message_end_time | Timestamp of the latest message in the recording.Together withmessage_start_time, this defines the total duration of the recording.TYPE:TimeIntLike |
| channel_message_counts | Detailed breakdown of message counts per channel.TYPE:ChannelMessageCountsLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `McapStatistics`.



##### defcolumns(*,message_count=None,schema_count=None,channel_count=None,attachment_count=None,metadata_count=None,chunk_count=None,message_start_time=None,message_end_time=None,channel_message_counts=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| message_count | Total number of data messages contained in the MCAP recording.This count includes all timestamped data messages but excludes metadata records, schema definitions, and other non-message records.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| schema_count | Number of unique schema definitions in the recording.Each schema defines the structure for one or more message types used by channels.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| channel_count | Number of channels defined in the recording.Each channel represents a unique topic and encoding combination for publishing messages.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| attachment_count | Number of file attachments embedded in the recording.Attachments can include calibration files, configuration data, or other auxiliary files.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| metadata_count | Number of metadata records providing additional context about the recording.Metadata records contain key-value pairs with information about the recording environment, system configuration, or other contextual data.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| chunk_count | Number of data chunks used to organize messages in the file.Chunks group related messages together for efficient storage and indexed access.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |
| message_start_time | Timestamp of the earliest message in the recording.This marks the beginning of the recorded data timeline.TYPE:TimeIntArrayLike\| NoneDEFAULT:None |
| message_end_time | Timestamp of the latest message in the recording.Together withmessage_start_time, this defines the total duration of the recording.TYPE:TimeIntArrayLike\| NoneDEFAULT:None |
| channel_message_counts | Detailed breakdown of message counts per channel.TYPE:ChannelMessageCountsArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,message_count=None,schema_count=None,channel_count=None,attachment_count=None,metadata_count=None,chunk_count=None,message_start_time=None,message_end_time=None,channel_message_counts=None)classmethod



Update only some specific fields of a `McapStatistics`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| message_count | Total number of data messages contained in the MCAP recording.This count includes all timestamped data messages but excludes metadata records, schema definitions, and other non-message records.TYPE:UInt64Like\| NoneDEFAULT:None |
| schema_count | Number of unique schema definitions in the recording.Each schema defines the structure for one or more message types used by channels.TYPE:UInt64Like\| NoneDEFAULT:None |
| channel_count | Number of channels defined in the recording.Each channel represents a unique topic and encoding combination for publishing messages.TYPE:UInt64Like\| NoneDEFAULT:None |
| attachment_count | Number of file attachments embedded in the recording.Attachments can include calibration files, configuration data, or other auxiliary files.TYPE:UInt64Like\| NoneDEFAULT:None |
| metadata_count | Number of metadata records providing additional context about the recording.Metadata records contain key-value pairs with information about the recording environment, system configuration, or other contextual data.TYPE:UInt64Like\| NoneDEFAULT:None |
| chunk_count | Number of data chunks used to organize messages in the file.Chunks group related messages together for efficient storage and indexed access.TYPE:UInt64Like\| NoneDEFAULT:None |
| message_start_time | Timestamp of the earliest message in the recording.This marks the beginning of the recorded data timeline.TYPE:TimeIntLike\| NoneDEFAULT:None |
| message_end_time | Timestamp of the latest message in the recording.Together withmessage_start_time, this defines the total duration of the recording.TYPE:TimeIntLike\| NoneDEFAULT:None |
| channel_message_counts | Detailed breakdown of message counts per channel.TYPE:ChannelMessageCountsLike\| NoneDEFAULT:None |



#### classMesh3D



Bases: `Mesh3DExt`, `Archetype`



**Archetype**: A 3D triangle mesh as specified by its per-mesh and per-vertex properties.



See also archetypes.Asset3D.



If there are multiple archetypes.InstancePoses3D instances logged to the same entity as a mesh,
an instance of the mesh will be drawn for each transform.



The viewer draws meshes always two-sided. However, for transparency ordering
front faces are assumed to those with counter clockwise triangle winding order (this is the same as in the GLTF specification).



Examples:



###### Simple indexed 3D mesh:



```
import rerun as rr

rr.init("rerun_example_mesh3d_indexed", spawn=True)

rr.log(
    "triangle",
    rr.Mesh3D(
        vertex_positions=[[0.0, 1.0, 0.0], [1.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        vertex_normals=[0.0, 0.0, 1.0],
        vertex_colors=[[0, 0, 255], [0, 255, 0], [255, 0, 0]],
        triangle_indices=[2, 1, 0],
    ),
)
```

 ![](https://static.rerun.io/mesh3d_indexed/57c70dc992e6dc0bd9c5222ca084f5b6240cea75/full.png)

###### 3D mesh with instancing:



```
import rerun as rr

rr.init("rerun_example_mesh3d_instancing", spawn=True)
rr.set_time("frame", sequence=0)

rr.log(
    "shape",
    rr.Mesh3D(
        vertex_positions=[[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]],
        triangle_indices=[[0, 2, 1], [0, 3, 1], [0, 3, 2], [1, 3, 2]],
        vertex_colors=[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],
    ),
)
# This box will not be affected by its parent's instance poses!
rr.log(
    "shape/box",
    rr.Boxes3D(half_sizes=[[5.0, 5.0, 5.0]]),
)

for i in range(100):
    rr.set_time("frame", sequence=i)
    rr.log(
        "shape",
        rr.InstancePoses3D(
            translations=[[2, 0, 0], [0, 2, 0], [0, -2, 0], [-2, 0, 0]],
            rotation_axis_angles=rr.RotationAxisAngle([0, 0, 1], rr.Angle(deg=i * 2)),
        ),
    )
```

 ![](https://static.rerun.io/mesh3d_leaf_transforms3d/c2d0ee033129da53168f5705625a9b033f3a3d61/full.png)

##### def__init__(*,vertex_positions,triangle_indices=None,vertex_normals=None,vertex_colors=None,vertex_texcoords=None,albedo_texture=None,albedo_factor=None,class_ids=None)



Create a new instance of the Mesh3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vertex_positions | The positions of each vertex. If noindicesare specified, then each triplet of positions is interpreted as a triangle.TYPE:Vec3DArrayLike |
| triangle_indices | Optional indices for the triangles that make up the mesh.TYPE:UVec3DArrayLike\| NoneDEFAULT:None |
| vertex_normals | An optional normal for each vertex. If specified, this must have as many elements asvertex_positions.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| vertex_texcoords | An optional texture coordinate for each vertex. If specified, this must have as many elements asvertex_positions.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| vertex_colors | An optional color for each vertex.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| albedo_factor | Optional color multiplier for the whole meshTYPE:Rgba32Like\| NoneDEFAULT:None |
| albedo_texture | Optional albedo texture. Used withvertex_texcoordsonMesh3D. Currently supports only sRGB(A) textures, ignoring alpha. (meaning that the texture must have 3 or 4 channels)TYPE:ImageLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the vertices. The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Mesh3D`.



##### defcolumns(*,vertex_positions=None,triangle_indices=None,vertex_normals=None,vertex_colors=None,vertex_texcoords=None,albedo_factor=None,albedo_texture_buffer=None,albedo_texture_format=None,class_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| vertex_positions | The positions of each vertex.If notriangle_indicesare specified, then each triplet of positions is interpreted as a triangle.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| triangle_indices | Optional indices for the triangles that make up the mesh.TYPE:UVec3DArrayLike\| NoneDEFAULT:None |
| vertex_normals | An optional normal for each vertex.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| vertex_colors | An optional color for each vertex.The alpha channel is ignored.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| vertex_texcoords | An optional uv texture coordinate for each vertex.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| albedo_factor | A color multiplier applied to the whole mesh.Alpha channel governs the overall mesh transparency.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| albedo_texture_buffer | Optional albedo texture.Used with thecomponents.Texcoord2Dof the mesh.Currently supports only sRGB(A) textures, ignoring alpha. (meaning that the tensor must have 3 or 4 channels and use theu8format)The alpha channel is ignored.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| albedo_texture_format | The format of thealbedo_texture_buffer, if any.TYPE:ImageFormatArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the vertices.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,vertex_positions=None,triangle_indices=None,vertex_normals=None,vertex_colors=None,vertex_texcoords=None,albedo_factor=None,albedo_texture_buffer=None,albedo_texture_format=None,class_ids=None)classmethod



Update only some specific fields of a `Mesh3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| vertex_positions | The positions of each vertex.If notriangle_indicesare specified, then each triplet of positions is interpreted as a triangle.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| triangle_indices | Optional indices for the triangles that make up the mesh.TYPE:UVec3DArrayLike\| NoneDEFAULT:None |
| vertex_normals | An optional normal for each vertex.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| vertex_colors | An optional color for each vertex.The alpha channel is ignored.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| vertex_texcoords | An optional uv texture coordinate for each vertex.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| albedo_factor | A color multiplier applied to the whole mesh.Alpha channel governs the overall mesh transparency.TYPE:Rgba32Like\| NoneDEFAULT:None |
| albedo_texture_buffer | Optional albedo texture.Used with thecomponents.Texcoord2Dof the mesh.Currently supports only sRGB(A) textures, ignoring alpha. (meaning that the tensor must have 3 or 4 channels and use theu8format)The alpha channel is ignored.TYPE:BlobLike\| NoneDEFAULT:None |
| albedo_texture_format | The format of thealbedo_texture_buffer, if any.TYPE:ImageFormatLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the vertices.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |



#### classPinhole



Bases: `PinholeExt`, `Archetype`



**Archetype**: Camera perspective projection (a.k.a. intrinsics).



If archetypes.Transform3D is logged for the same child/parent relationship (e.g. for the camera extrinsics), it takes precedence over archetypes.Pinhole.



If you use named transform frames via the `child_frame` and `parent_frame` fields, you don't have to use archetypes.CoordinateFrame
as it is the case with other visualizations: for any entity with an archetypes.Pinhole the viewer will always visualize it
directly without needing a archetypes.CoordinateFrame to refer to the pinhole's child/parent frame.



Examples:



###### Simple pinhole camera:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_pinhole", spawn=True)
rng = np.random.default_rng(12345)

image = rng.uniform(0, 255, size=[3, 3, 3])
rr.log("world/image", rr.Pinhole(focal_length=3, width=3, height=3))
rr.log("world/image", rr.Image(image))
```

 ![](https://static.rerun.io/pinhole_simple/9af9441a94bcd9fd54e1fea44fb0c59ff381a7f2/full.png)

###### Perspective pinhole camera:



```
import rerun as rr

rr.init("rerun_example_pinhole_perspective", spawn=True)

rr.log(
    "world/cam",
    rr.Pinhole(
        fov_y=0.7853982,
        aspect_ratio=1.7777778,
        camera_xyz=rr.ViewCoordinates.RUB,
        image_plane_distance=0.1,
        color=[255, 128, 0],
        line_width=0.003,
    ),
)

rr.log("world/points", rr.Points3D([(0.0, 0.0, -0.5), (0.1, 0.1, -0.5), (-0.1, -0.1, -0.5)], radii=0.025))
```

 ![](https://static.rerun.io/pinhole_perspective/317e2de6d212b238dcdad5b67037e9e2a2afafa0/full.png)

##### def__init__(*,image_from_camera=None,resolution=None,camera_xyz=None,width=None,height=None,focal_length=None,principal_point=None,fov_y=None,aspect_ratio=None,image_plane_distance=None,color=None,line_width=None)



Create a new instance of the Pinhole archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| image_from_camera | Row-major intrinsics matrix for projecting from camera space to image space. The first two axes are X=Right and Y=Down, respectively. Projection is done along the positive third (Z=Forward) axis. This can be specifiedinsteadoffocal_lengthandprincipal_point.TYPE:Mat3x3Like\| NoneDEFAULT:None |
| resolution | Pixel resolution (usually integers) of child image space. Width and height.image_from_cameraprojects onto the space spanned by(0,0)andresolution - 1.TYPE:Vec2DLike\| NoneDEFAULT:None |
| camera_xyz | Sets the view coordinates for the camera.All common values are available as constants on thecomponents.ViewCoordinatesclass.The default isViewCoordinates.RDF, i.e. X=Right, Y=Down, Z=Forward, and this is also the recommended setting. This means that the camera frustum will point along the positive Z axis of the parent space, and the cameras "up" direction will be along the negative Y axis of the parent space.The camera frustum will point whichever axis is set toF(or the opposite ofB). When logging a depth image under this entity, this is the direction the point cloud will be projected. WithRDF, the default forward is +Z.The frustum's "up" direction will be whichever axis is set toU(or the opposite ofD). This will match the negative Y direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default is up is -Y.The frustum's "right" direction will be whichever axis is set toR(or the opposite ofL). This will match the positive X direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default right is +x.Other common formats areRUB(X=Right, Y=Up, Z=Back) andFLU(X=Forward, Y=Left, Z=Up).NOTE: setting this to something else thanRDF(the default) will change the orientation of the camera frustum, and make the pinhole matrix not match up with the coordinate system of the pinhole entity.The pinhole matrix (theimage_from_cameraargument) always project along the third (Z) axis, but will be re-oriented to project along the forward axis of thecamera_xyzargument.TYPE:ViewCoordinatesLike\| NoneDEFAULT:None |
| focal_length | The focal length of the camera in pixels. This is the diagonal of the projection matrix. Set one value for symmetric cameras, or two values (X=Right, Y=Down) for anamorphic cameras.TYPE:float\|ArrayLike\| NoneDEFAULT:None |
| principal_point | The center of the camera in pixels. The default is half the width and height. This is the last column of the projection matrix. Expects two values along the dimensions Right and DownTYPE:ArrayLike\| NoneDEFAULT:None |
| width | Width of the image in pixels.TYPE:int\|float\| NoneDEFAULT:None |
| height | Height of the image in pixels.TYPE:int\|float\| NoneDEFAULT:None |
| fov_y | Vertical field of view in radians.TYPE:float\| NoneDEFAULT:None |
| aspect_ratio | Aspect ratio (width/height).TYPE:float\| NoneDEFAULT:None |
| image_plane_distance | The distance from the camera origin to the image plane when the projection is shown in a 3D viewer. This is only used for visualization purposes, and does not affect the projection itself.TYPE:float\| NoneDEFAULT:None |
| color | Color of the camera frustum lines in the 3D viewer.TYPE:Rgba32Like\| NoneDEFAULT:None |
| line_width | Width of the camera frustum lines in the 3D viewer.TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Pinhole`.



##### defcolumns(*,image_from_camera=None,resolution=None,camera_xyz=None,child_frame=None,parent_frame=None,image_plane_distance=None,color=None,line_width=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| image_from_camera | Camera projection, from image coordinates to view coordinates.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Mat3x3ArrayLike\| NoneDEFAULT:None |
| resolution | Pixel resolution (usually integers) of child image space. Width and height.Example:[1920.0, 1440.0]image_from_cameraproject onto the space spanned by(0,0)andresolution - 1.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| camera_xyz | Sets the view coordinates for the camera.All common values are available as constants on thecomponents.ViewCoordinatesclass.The default isViewCoordinates::RDF, i.e. X=Right, Y=Down, Z=Forward, and this is also the recommended setting. This means that the camera frustum will point along the positive Z axis of the parent space, and the cameras "up" direction will be along the negative Y axis of the parent space.The camera frustum will point whichever axis is set toF(or the opposite ofB). When logging a depth image under this entity, this is the direction the point cloud will be projected. WithRDF, the default forward is +Z.The frustum's "up" direction will be whichever axis is set toU(or the opposite ofD). This will match the negative Y direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default is up is -Y.The frustum's "right" direction will be whichever axis is set toR(or the opposite ofL). This will match the positive X direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default right is +x.Other common formats areRUB(X=Right, Y=Up, Z=Back) andFLU(X=Forward, Y=Left, Z=Up).NOTE: setting this to something else thanRDF(the default) will change the orientation of the camera frustum, and make the pinhole matrix not match up with the coordinate system of the pinhole entity.The pinhole matrix (theimage_from_cameraargument) always project along the third (Z) axis, but will be re-oriented to project along the forward axis of thecamera_xyzargument.TYPE:ViewCoordinatesArrayLike\| NoneDEFAULT:None |
| child_frame | The child frame this transform transforms from.The entity at which the transform relationship of any given child frame is specified mustn't change over time, but is allowed to be different for static time. E.g. if you specified the child frame"robot_arm"on an entity named"my_transforms", you may not log transforms with the child frame"robot_arm"on any other entity than"my_transforms"unless one of them was logged with static time.If not specified, this is set to the implicit transform frame of the current entity path. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity/path.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| parent_frame | The parent frame this transform transforms into.If not specified, this is set to the implicit transform frame of the current entity path's parent. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| image_plane_distance | The distance from the camera origin to the image plane when the projection is shown in a 3D viewer.This is only used for visualization purposes, and does not affect the projection itself.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| color | Color of the camera wireframe.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| line_width | Width of the camera wireframe lines.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,image_from_camera=None,resolution=None,camera_xyz=None,child_frame=None,parent_frame=None,image_plane_distance=None,color=None,line_width=None)classmethod



Update only some specific fields of a `Pinhole`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| image_from_camera | Camera projection, from image coordinates to view coordinates.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Mat3x3Like\| NoneDEFAULT:None |
| resolution | Pixel resolution (usually integers) of child image space. Width and height.Example:[1920.0, 1440.0]image_from_cameraproject onto the space spanned by(0,0)andresolution - 1.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec2DLike\| NoneDEFAULT:None |
| camera_xyz | Sets the view coordinates for the camera.All common values are available as constants on thecomponents.ViewCoordinatesclass.The default isViewCoordinates::RDF, i.e. X=Right, Y=Down, Z=Forward, and this is also the recommended setting. This means that the camera frustum will point along the positive Z axis of the parent space, and the cameras "up" direction will be along the negative Y axis of the parent space.The camera frustum will point whichever axis is set toF(or the opposite ofB). When logging a depth image under this entity, this is the direction the point cloud will be projected. WithRDF, the default forward is +Z.The frustum's "up" direction will be whichever axis is set toU(or the opposite ofD). This will match the negative Y direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default is up is -Y.The frustum's "right" direction will be whichever axis is set toR(or the opposite ofL). This will match the positive X direction of pixel space (all images are assumed to have xyz=RDF). WithRDF, the default right is +x.Other common formats areRUB(X=Right, Y=Up, Z=Back) andFLU(X=Forward, Y=Left, Z=Up).NOTE: setting this to something else thanRDF(the default) will change the orientation of the camera frustum, and make the pinhole matrix not match up with the coordinate system of the pinhole entity.The pinhole matrix (theimage_from_cameraargument) always project along the third (Z) axis, but will be re-oriented to project along the forward axis of thecamera_xyzargument.TYPE:ViewCoordinatesLike\| NoneDEFAULT:None |
| child_frame | The child frame this transform transforms from.The entity at which the transform relationship of any given child frame is specified mustn't change over time, but is allowed to be different for static time. E.g. if you specified the child frame"robot_arm"on an entity named"my_transforms", you may not log transforms with the child frame"robot_arm"on any other entity than"my_transforms"unless one of them was logged with static time.If not specified, this is set to the implicit transform frame of the current entity path. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity/path.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8Like\| NoneDEFAULT:None |
| parent_frame | The parent frame this transform transforms into.If not specified, this is set to the implicit transform frame of the current entity path's parent. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8Like\| NoneDEFAULT:None |
| image_plane_distance | The distance from the camera origin to the image plane when the projection is shown in a 3D viewer.This is only used for visualization purposes, and does not affect the projection itself.TYPE:Float32Like\| NoneDEFAULT:None |
| color | Color of the camera wireframe.TYPE:Rgba32Like\| NoneDEFAULT:None |
| line_width | Width of the camera wireframe lines.TYPE:Float32Like\| NoneDEFAULT:None |



#### classPoints2D



Bases: `Points2DExt`, `Archetype`



**Archetype**: A 2D point cloud with positions and optional colors, radii, labels, etc.



Examples:



###### Randomly distributed 2D points with varying color and radius:



```
import rerun as rr
import rerun.blueprint as rrb
from numpy.random import default_rng

rr.init("rerun_example_points2d_random", spawn=True)
rng = default_rng(12345)

positions = rng.uniform(-3, 3, size=[10, 2])
colors = rng.uniform(0, 255, size=[10, 4])
radii = rng.uniform(0, 1, size=[10])

rr.log("random", rr.Points2D(positions, colors=colors, radii=radii))

# Set view bounds:
rr.send_blueprint(rrb.Spatial2DView(visual_bounds=rrb.VisualBounds2D(x_range=[-4, 4], y_range=[-4, 4])))
```

 ![](https://static.rerun.io/point2d_random/8e8ac75373677bd72bd3f56a15e44fcab309a168/full.png)

###### Log points with radii given in UI points:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_points2d_ui_radius", spawn=True)

# Two blue points with scene unit radii of 0.1 and 0.3.
rr.log(
    "scene_units",
    rr.Points2D(
        [[0, 0], [0, 1]],
        # By default, radii are interpreted as world-space units.
        radii=[0.1, 0.3],
        colors=[0, 0, 255],
    ),
)

# Two red points with ui point radii of 40 and 60.
# UI points are independent of zooming in Views, but are sensitive to the application UI scaling.
# For 100% ui scaling, UI points are equal to pixels.
rr.log(
    "ui_points",
    rr.Points2D(
        [[1, 0], [1, 1]],
        # rr.Radius.ui_points produces radii that the viewer interprets as given in ui points.
        radii=rr.Radius.ui_points([40.0, 60.0]),
        colors=[255, 0, 0],
    ),
)

# Set view bounds:
rr.send_blueprint(rrb.Spatial2DView(visual_bounds=rrb.VisualBounds2D(x_range=[-1, 2], y_range=[-1, 2])))
```

 ![](https://static.rerun.io/point2d_ui_radius/ce804fc77300d89c348b4ab5960395171497b7ac/full.png)

##### def__init__(positions,*,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None,keypoint_ids=None)



Create a new instance of the Points2D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| positions | All the 2D positions at which the point cloud shows points.TYPE:Vec2DArrayLike |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space,  As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.  Objects with higher values are drawn on top of those with lower values.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but no class IDs were specified, the class ID will  default to 0.  This is useful to identify points within a single classification (which is identified  withclass_id).  E.g. the classification might be 'Person' and the keypoints refer to joints on a  detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Points2D`.



##### defcolumns(*,positions=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None,keypoint_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| positions | All the 2D positions at which the point cloud shows points.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to30.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but nocomponents.ClassIds were specified, thecomponents.ClassIdwill default to 0. This is useful to identify points within a single classification (which is identified withclass_id). E.g. the classification might be 'Person' and the keypoints refer to joints on a detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,positions=None,radii=None,colors=None,labels=None,show_labels=None,draw_order=None,class_ids=None,keypoint_ids=None)classmethod



Update only some specific fields of a `Points2D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| positions | All the 2D positions at which the point cloud shows points.TYPE:Vec2DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to30.0.TYPE:Float32Like\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but nocomponents.ClassIds were specified, thecomponents.ClassIdwill default to 0. This is useful to identify points within a single classification (which is identified withclass_id). E.g. the classification might be 'Person' and the keypoints refer to joints on a detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



#### classPoints3D



Bases: `Points3DExt`, `Archetype`



**Archetype**: A 3D point cloud with positions and optional colors, radii, labels, etc.



If there are multiple instance poses, the entire point cloud will be repeated for each of the poses.



Examples:



###### Simple 3D points:



```
import rerun as rr

rr.init("rerun_example_points3d", spawn=True)

rr.log("points", rr.Points3D([[0, 0, 0], [1, 1, 1]]))
```

 ![](https://static.rerun.io/point3d_simple/32fb3e9b65bea8bd7ffff95ad839f2f8a157a933/full.png)

###### Update a point cloud over time:



```
import numpy as np
import rerun as rr

rr.init("rerun_example_points3d_row_updates", spawn=True)

# Prepare a point cloud that evolves over 5 timesteps, changing the number of points in the process.
times = np.arange(10, 15, 1.0)
# fmt: off
positions = [
    [[1.0, 0.0, 1.0], [0.5, 0.5, 2.0]],
    [[1.5, -0.5, 1.5], [1.0, 1.0, 2.5], [-0.5, 1.5, 1.0], [-1.5, 0.0, 2.0]],
    [[2.0, 0.0, 2.0], [1.5, -1.5, 3.0], [0.0, -2.0, 2.5], [1.0, -1.0, 3.5]],
    [[-2.0, 0.0, 2.0], [-1.5, 1.5, 3.0], [-1.0, 1.0, 3.5]],
    [[1.0, -1.0, 1.0], [2.0, -2.0, 2.0], [3.0, -1.0, 3.0], [2.0, 0.0, 4.0]],
]
# fmt: on

# At each timestep, all points in the cloud share the same but changing color and radius.
colors = [0xFF0000FF, 0x00FF00FF, 0x0000FFFF, 0xFFFF00FF, 0x00FFFFFF]
radii = [0.05, 0.01, 0.2, 0.1, 0.3]

for i in range(5):
    rr.set_time("time", duration=10 + i)
    rr.log("points", rr.Points3D(positions[i], colors=colors[i], radii=radii[i]))
```

 ![](https://static.rerun.io/points3d_row_updates/fba056871b1ec3fc6978ab605d9a63e44ef1f6de/full.png)

###### Update a point cloud over time, in a single operation:



```
from __future__ import annotations

import numpy as np
import rerun as rr

rr.init("rerun_example_points3d_column_updates", spawn=True)

# Prepare a point cloud that evolves over 5 timesteps, changing the number of points in the process.
times = np.arange(10, 15, 1.0)
# fmt: off
positions = [
    [1.0, 0.0, 1.0], [0.5, 0.5, 2.0],
    [1.5, -0.5, 1.5], [1.0, 1.0, 2.5], [-0.5, 1.5, 1.0], [-1.5, 0.0, 2.0],
    [2.0, 0.0, 2.0], [1.5, -1.5, 3.0], [0.0, -2.0, 2.5], [1.0, -1.0, 3.5],
    [-2.0, 0.0, 2.0], [-1.5, 1.5, 3.0], [-1.0, 1.0, 3.5],
    [1.0, -1.0, 1.0], [2.0, -2.0, 2.0], [3.0, -1.0, 3.0], [2.0, 0.0, 4.0],
]
# fmt: on

# At each timestep, all points in the cloud share the same but changing color and radius.
colors = [0xFF0000FF, 0x00FF00FF, 0x0000FFFF, 0xFFFF00FF, 0x00FFFFFF]
radii = [0.05, 0.01, 0.2, 0.1, 0.3]

rr.send_columns(
    "points",
    indexes=[rr.TimeColumn("time", duration=times)],
    columns=[
        *rr.Points3D.columns(positions=positions).partition(lengths=[2, 4, 4, 3, 4]),
        *rr.Points3D.columns(colors=colors, radii=radii),
    ],
)
```

 ![](https://static.rerun.io/points3d_row_updates/fba056871b1ec3fc6978ab605d9a63e44ef1f6de/full.png)

###### Update specific properties of a point cloud over time:



```
import rerun as rr

rr.init("rerun_example_points3d_partial_updates", spawn=True)

positions = [[i, 0, 0] for i in range(10)]

rr.set_time("frame", sequence=0)
rr.log("points", rr.Points3D(positions))

for i in range(10):
    colors = [[20, 200, 20] if n < i else [200, 20, 20] for n in range(10)]
    radii = [0.6 if n < i else 0.2 for n in range(10)]

    # Update only the colors and radii, leaving everything else as-is.
    rr.set_time("frame", sequence=i)
    rr.log("points", rr.Points3D.from_fields(radii=radii, colors=colors))

# Update the positions and radii, and clear everything else in the process.
rr.set_time("frame", sequence=20)
rr.log("points", rr.Points3D.from_fields(clear_unset=True, positions=positions, radii=0.3))
```

 ![](https://static.rerun.io/points3d_partial_updates/d8bec9c3388d2bd0fe59dff01ab8cde0bdda135e/full.png)

##### def__init__(positions,*,radii=None,colors=None,labels=None,show_labels=None,class_ids=None,keypoint_ids=None)



Create a new instance of the Points3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| positions | All the 3D positions at which the point cloud shows points.TYPE:Vec3DArrayLike |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space,  As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Optional choice of whether the text labels should be shown by default.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.The class ID provides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but no class IDs were specified, the class ID will  default to 0.  This is useful to identify points within a single classification (which is identified  withclass_id).  E.g. the classification might be 'Person' and the keypoints refer to joints on a  detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Points3D`.



##### defcolumns(*,positions=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None,keypoint_ids=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| positions | All the 3D positions at which the point cloud shows points.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but nocomponents.ClassIds were specified, thecomponents.ClassIdwill default to 0. This is useful to identify points within a single classification (which is identified withclass_id). E.g. the classification might be 'Person' and the keypoints refer to joints on a detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,positions=None,radii=None,colors=None,labels=None,show_labels=None,class_ids=None,keypoint_ids=None)classmethod



Update only some specific fields of a `Points3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| positions | All the 3D positions at which the point cloud shows points.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| radii | Optional radii for the points, effectively turning them into circles.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| colors | Optional colors for the points.The colors are interpreted as RGB or RGBA in sRGB gamma-space, As either 0-1 floats or 0-255 integers, with separate alpha.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| labels | Optional text labels for the points.If there's a single label present, it will be placed at the center of the entity. Otherwise, each instance will have its own label.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| show_labels | Whether the text labels should be shown.If not set, labels will automatically appear when there is exactly one label for this entity or the number of instances on this entity is under a certain threshold.TYPE:BoolLike\| NoneDEFAULT:None |
| class_ids | Optional class Ids for the points.Thecomponents.ClassIdprovides colors and labels if not specified explicitly.TYPE:ClassIdArrayLike\| NoneDEFAULT:None |
| keypoint_ids | Optional keypoint IDs for the points, identifying them within a class.If keypoint IDs are passed in but nocomponents.ClassIds were specified, thecomponents.ClassIdwill default to 0. This is useful to identify points within a single classification (which is identified withclass_id). E.g. the classification might be 'Person' and the keypoints refer to joints on a detected skeleton.TYPE:KeypointIdArrayLike\| NoneDEFAULT:None |



#### classRecordingInfo



Bases: `Archetype`



**Archetype**: A list of properties associated with a recording.



##### def__init__(*,start_time=None,name=None)



Create a new instance of the RecordingInfo archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start_time | When the recording started.Should be an absolute time, i.e. relative to Unix Epoch.TYPE:TimeIntLike\| NoneDEFAULT:None |
| name | A user-chosen name for the recording.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `RecordingInfo`.



##### defcolumns(*,start_time=None,name=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start_time | When the recording started.Should be an absolute time, i.e. relative to Unix Epoch.TYPE:TimeIntArrayLike\| NoneDEFAULT:None |
| name | A user-chosen name for the recording.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,start_time=None,name=None)classmethod



Update only some specific fields of a `RecordingInfo`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| start_time | When the recording started.Should be an absolute time, i.e. relative to Unix Epoch.TYPE:TimeIntLike\| NoneDEFAULT:None |
| name | A user-chosen name for the recording.TYPE:Utf8Like\| NoneDEFAULT:None |



#### classScalars



Bases: `Archetype`



**Archetype**: One or more double-precision scalar values, e.g. for use for time-series plots.



The current timeline value will be used for the time/X-axis, hence scalars
should not be static.
Number of scalars per timestamp is expected to be the same over time.



When used to produce a plot, this archetype is used to provide the data that
is referenced by archetypes.SeriesLines or archetypes.SeriesPoints. You can do
this by logging both archetypes to the same path, or alternatively configuring
the plot-specific archetypes through the blueprint.



Examples:



###### Update a scalar over time:



```
from __future__ import annotations

import math

import rerun as rr

rr.init("rerun_example_scalar_row_updates", spawn=True)

for step in range(64):
    rr.set_time("step", sequence=step)
    rr.log("scalars", rr.Scalars(math.sin(step / 10.0)))
```

 ![](https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/full.png)

###### Update a scalar over time, in a single operation:



```
from __future__ import annotations

import numpy as np
import rerun as rr

rr.init("rerun_example_scalar_column_updates", spawn=True)

times = np.arange(0, 64)
scalars = np.sin(times / 10.0)

rr.send_columns(
    "scalars",
    indexes=[rr.TimeColumn("step", sequence=times)],
    columns=rr.Scalars.columns(scalars=scalars),
)
```

 ![](https://static.rerun.io/transform3d_column_updates/2b7ccfd29349b2b107fcf7eb8a1291a92cf1cafc/full.png)

##### def__init__(scalars)



Create a new instance of the Scalars archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| scalars | The scalar values to log.TYPE:Float64ArrayLike |



##### defcleared()classmethod



Clear all the fields of a `Scalars`.



##### defcolumns(*,scalars=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| scalars | The scalar values to log.TYPE:Float64ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,scalars=None)classmethod



Update only some specific fields of a `Scalars`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| scalars | The scalar values to log.TYPE:Float64ArrayLike\| NoneDEFAULT:None |



#### classSegmentationImage



Bases: `SegmentationImageExt`, `Archetype`



**Archetype**: An image made up of integer [components.ClassId](../components/#rerun.components.ClassId)s.



Each pixel corresponds to a [components.ClassId](../components/#rerun.components.ClassId) that will be mapped to a color based on archetypes.AnnotationContext.



In the case of floating point images, the label will be looked up based on rounding to the nearest
integer value.



Use archetypes.AnnotationContext to associate each class with a color and a label.

 Example

###### Simple segmentation image:



```
import numpy as np
import rerun as rr

# Create a segmentation image
image = np.zeros((8, 12), dtype=np.uint8)
image[0:4, 0:6] = 1
image[4:8, 6:12] = 2

rr.init("rerun_example_segmentation_image", spawn=True)

# Assign a label and color to each class
rr.log("/", rr.AnnotationContext([(1, "red", (255, 0, 0)), (2, "green", (0, 255, 0))]), static=True)

rr.log("image", rr.SegmentationImage(image))
```

 ![](https://static.rerun.io/segmentation_image_simple/f8aac62abcf4c59c5d62f9ebc2d86fd0285c1736/full.png)

##### defcleared()classmethod



Clear all the fields of a `SegmentationImage`.



##### defcolumns(*,buffer=None,format=None,opacity=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| buffer | The raw image data.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatArrayLike\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering the segmentation image on top of another image.Defaults to 0.5 if there's any other images in the scene, otherwise 1.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to0.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,buffer=None,format=None,opacity=None,draw_order=None)classmethod



Update only some specific fields of a `SegmentationImage`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| buffer | The raw image data.TYPE:BlobLike\| NoneDEFAULT:None |
| format | The format of the image.TYPE:ImageFormatLike\| NoneDEFAULT:None |
| opacity | Opacity of the image, useful for layering the segmentation image on top of another image.Defaults to 0.5 if there's any other images in the scene, otherwise 1.0.TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to0.0.TYPE:Float32Like\| NoneDEFAULT:None |



#### classSeriesLines



Bases: `Archetype`



**Archetype**: Define the style properties for one or more line series in a chart.



This archetype only provides styling information.
Changes over time are supported for most but not all its fields (see respective fields for details),
it's generally recommended to log this type as static.



The underlying data needs to be logged to the same entity-path using archetypes.Scalars.
Dimensionality of the scalar arrays logged at each time point is assumed to be the same over time.

 Example

###### Line series:



```
from math import cos, sin, tau

import rerun as rr

rr.init("rerun_example_series_line_style", spawn=True)

# Set up plot styling:
# They are logged as static as they don't change over time and apply to all timelines.
# Log two lines series under a shared root so that they show in the same plot by default.
rr.log("trig/sin", rr.SeriesLines(colors=[255, 0, 0], names="sin(0.01t)", widths=2), static=True)
rr.log("trig/cos", rr.SeriesLines(colors=[0, 255, 0], names="cos(0.01t)", widths=4), static=True)

# Log the data on a timeline called "step".
for t in range(int(tau * 2 * 100.0)):
    rr.set_time("step", sequence=t)

    rr.log("trig/sin", rr.Scalars(sin(float(t) / 100.0)))
    rr.log("trig/cos", rr.Scalars(cos(float(t) / 100.0)))
```

 ![](https://static.rerun.io/series_line_style/d2616d98b1e46bdb85849b8669154fdf058e3453/full.png)

##### def__init__(*,colors=None,widths=None,names=None,visible_series=None,aggregation_policy=None)



Create a new instance of the SeriesLines archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| widths | Stroke width for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time, but can cause discontinuities in the line.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| aggregation_policy | Configures the zoom-dependent scalar aggregation.This is done only if steps on the X axis go below a single pixel, i.e. a single pixel covers more than one tick worth of data. It can greatly improve performance (and readability) in such situations as it prevents overdraw.Expected to be unchanging over time.TYPE:AggregationPolicyLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `SeriesLines`.



##### defcolumns(*,colors=None,widths=None,names=None,visible_series=None,aggregation_policy=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| widths | Stroke width for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time, but can cause discontinuities in the line.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| aggregation_policy | Configures the zoom-dependent scalar aggregation.This is done only if steps on the X axis go below a single pixel, i.e. a single pixel covers more than one tick worth of data. It can greatly improve performance (and readability) in such situations as it prevents overdraw.Expected to be unchanging over time.TYPE:AggregationPolicyArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,colors=None,widths=None,names=None,visible_series=None,aggregation_policy=None)classmethod



Update only some specific fields of a `SeriesLines`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| widths | Stroke width for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time, but can cause discontinuities in the line.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| aggregation_policy | Configures the zoom-dependent scalar aggregation.This is done only if steps on the X axis go below a single pixel, i.e. a single pixel covers more than one tick worth of data. It can greatly improve performance (and readability) in such situations as it prevents overdraw.Expected to be unchanging over time.TYPE:AggregationPolicyLike\| NoneDEFAULT:None |



#### classSeriesPoints



Bases: `SeriesPointsExt`, `Archetype`



**Archetype**: Define the style properties for one or more point series (scatter plot) in a chart.



This archetype only provides styling information.
Changes over time are supported for most but not all its fields (see respective fields for details),
it's generally recommended to log this type as static.



The underlying data needs to be logged to the same entity-path using archetypes.Scalars.
Dimensionality of the scalar arrays logged at each time point is assumed to be the same over time.

 Example

###### Point series:



```
from math import cos, sin, tau

import rerun as rr

rr.init("rerun_example_series_point_style", spawn=True)

# Set up plot styling:
# They are logged as static as they don't change over time and apply to all timelines.
# Log two point series under a shared root so that they show in the same plot by default.
rr.log(
    "trig/sin",
    rr.SeriesPoints(
        colors=[255, 0, 0],
        names="sin(0.01t)",
        markers="circle",
        marker_sizes=4,
    ),
    static=True,
)
rr.log(
    "trig/cos",
    rr.SeriesPoints(
        colors=[0, 255, 0],
        names="cos(0.01t)",
        markers="cross",
        marker_sizes=2,
    ),
    static=True,
)

# Log the data on a timeline called "step".
for t in range(int(tau * 2 * 10.0)):
    rr.set_time("step", sequence=t)

    rr.log("trig/sin", rr.Scalars(sin(float(t) / 10.0)))
    rr.log("trig/cos", rr.Scalars(cos(float(t) / 10.0)))
```

 ![](https://static.rerun.io/series_point_style/82207a705da6c086b28ce161db1db9e8b12258b7/full.png)

##### def__init__(*,colors=None,markers=None,names=None,visible_series=None,marker_sizes=None)



Create a new instance of the SeriesPoints archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| markers | What shape to use to represent the pointMay change over time.TYPE:MarkerShapeArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| marker_sizes | Sizes of the markers.May change over time.If no other components are set, a defaultMarkerShape.Circlewill be logged.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `SeriesPoints`.



##### defcolumns(*,colors=None,markers=None,names=None,visible_series=None,marker_sizes=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| markers | What shape to use to represent the pointMay change over time.TYPE:MarkerShapeArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| marker_sizes | Sizes of the markers.May change over time.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,colors=None,markers=None,names=None,visible_series=None,marker_sizes=None)classmethod



Update only some specific fields of a `SeriesPoints`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| colors | Color for the corresponding series.May change over time, but can cause discontinuities in the line.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |
| markers | What shape to use to represent the pointMay change over time.TYPE:MarkerShapeArrayLike\| NoneDEFAULT:None |
| names | Display name of the series.Used in the legend. Expected to be unchanging over time.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| visible_series | Which lines are visible.If not set, all line series on this entity are visible. Unlike with the regular visibility property of the entire entity, any series that is hidden via this property will still be visible in the legend.May change over time.TYPE:BoolArrayLike\| NoneDEFAULT:None |
| marker_sizes | Sizes of the markers.May change over time.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



#### classTensor



Bases: `TensorExt`, `Archetype`



**Archetype**: An N-dimensional array of numbers.



It's not currently possible to use `send_columns` with tensors since construction
of `rerun.components.TensorDataBatch` does not support more than a single element.
This will be addressed as part of [https://github.com/rerun-io/rerun/issues/6832](https://github.com/rerun-io/rerun/issues/6832).

 Example

###### Simple tensor:



```
import numpy as np
import rerun as rr

tensor = np.random.randint(0, 256, (8, 6, 3, 5), dtype=np.uint8)  # 4-dimensional tensor

rr.init("rerun_example_tensor", spawn=True)

# Log the tensor, assigning names to each dimension
rr.log("tensor", rr.Tensor(tensor, dim_names=("width", "height", "channel", "batch")))
```

 ![](https://static.rerun.io/tensor_simple/baacb07712f7b706e3c80e696f70616c6c20b367/full.png)

##### def__init__(data=None,*,dim_names=None,value_range=None)



Construct a `Tensor` archetype.



The `Tensor` archetype internally contains a single component: `TensorData`.



See the `TensorData` constructor for more advanced options to interpret buffers
as `TensorData` of varying shapes.



For simple cases, you can pass array objects and optionally specify the names of
the dimensions. The shape of the `TensorData` will be inferred from the array.



| PARAMETER | DESCRIPTION |
| --- | --- |
| self | The TensorData object to construct.TYPE:Any |
| data | A TensorData object, or type that can be converted to a numpy array.TYPE:TensorDataLike\|TensorLike\| NoneDEFAULT:None |
| dim_names | The names of the tensor dimensions when generating the shape from an array.TYPE:Sequence[str] \| NoneDEFAULT:None |
| value_range | The range of values to use for colormapping.If not specified, the range will be estimated from the data.TYPE:Range1DLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Tensor`.



##### defcolumns(*,data=None,value_range=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| data | The tensor dataTYPE:TensorDataArrayLike\| NoneDEFAULT:None |
| value_range | The expected range of values.This is typically the expected range of valid values. Everything outside of the range is clamped to the range for the purpose of colormpaping. Any colormap applied for display, will map this range.If not specified, the range will be automatically estimated from the data. Note that the Viewer may try to guess a wider range than the minimum/maximum of values in the contents of the tensor. E.g. if all values are positive, some bigger than 1.0 and all smaller than 255.0, the Viewer will guess that the data likely came from an 8bit image, thus assuming a range of 0-255.TYPE:Range1DArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,data=None,value_range=None)classmethod



Update only some specific fields of a `Tensor`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| data | The tensor dataTYPE:TensorDataLike\| NoneDEFAULT:None |
| value_range | The expected range of values.This is typically the expected range of valid values. Everything outside of the range is clamped to the range for the purpose of colormpaping. Any colormap applied for display, will map this range.If not specified, the range will be automatically estimated from the data. Note that the Viewer may try to guess a wider range than the minimum/maximum of values in the contents of the tensor. E.g. if all values are positive, some bigger than 1.0 and all smaller than 255.0, the Viewer will guess that the data likely came from an 8bit image, thus assuming a range of 0-255.TYPE:Range1DLike\| NoneDEFAULT:None |



#### classTextDocument



Bases: `Archetype`



**Archetype**: A text element intended to be displayed in its own text box.



Supports raw text and markdown.

 Example

###### Markdown text document:



```
import rerun as rr

rr.init("rerun_example_text_document", spawn=True)

rr.log("text_document", rr.TextDocument("Hello, TextDocument!"))

rr.log(
    "markdown",
    rr.TextDocument(
        '''
# Hello Markdown!
[Click here to see the raw text](recording://markdown:Text).

Basic formatting:

| **Feature**       | **Alternative** |
| ----------------- | --------------- |
| Plain             |                 |
| *italics*         | _italics_       |
| **bold**          | __bold__        |
| ~~strikethrough~~ |                 |
| `inline code`     |                 |

----------------------------------

## Support
- [x] [Commonmark](https://commonmark.org/help/) support
- [x] GitHub-style strikethrough, tables, and checkboxes
- Basic syntax highlighting for:
  - [x] C and C++
  - [x] Python
  - [x] Rust
  - [ ] Other languages

## Links
You can link to [an entity](recording://markdown),
a [specific instance of an entity](recording://markdown[#0]),
or a [specific component](recording://markdown:Text).

Of course you can also have [normal https links](https://github.com/rerun-io/rerun), e.g. <https://rerun.io>.

## Image
![A random image](https://picsum.photos/640/480)
'''.strip(),
        media_type=rr.MediaType.MARKDOWN,
    ),
)
```

 ![](https://static.rerun.io/textdocument/babda19558ee32ed8d730495b595aee7a5e2c174/full.png)

##### def__init__(text,*,media_type=None)



Create a new instance of the TextDocument archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| text | Contents of the text document.TYPE:Utf8Like |
| media_type | The Media Type of the text.For instance: *text/plain*text/markdownIf omitted,text/plainis assumed.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TextDocument`.



##### defcolumns(*,text=None,media_type=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| text | Contents of the text document.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| media_type | The Media Type of the text.For instance: *text/plain*text/markdownIf omitted,text/plainis assumed.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,text=None,media_type=None)classmethod



Update only some specific fields of a `TextDocument`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| text | Contents of the text document.TYPE:Utf8Like\| NoneDEFAULT:None |
| media_type | The Media Type of the text.For instance: *text/plain*text/markdownIf omitted,text/plainis assumed.TYPE:Utf8Like\| NoneDEFAULT:None |



#### classTextLog



Bases: `Archetype`



**Archetype**: A log entry in a text log, comprised of a text body and its log level.

 Example

###### text_log_integration:



```
import logging

import rerun as rr

rr.init("rerun_example_text_log_integration", spawn=True)

# Log a text entry directly
rr.log("logs", rr.TextLog("this entry has loglevel TRACE", level=rr.TextLogLevel.TRACE))

# Or log via a logging handler
logging.getLogger().addHandler(rr.LoggingHandler("logs/handler"))
logging.getLogger().setLevel(-1)
logging.info("This INFO log got added through the standard logging interface")
```

 ![](https://static.rerun.io/text_log_integration/9737d0c986325802a9885499d6fcc773b1736488/full.png)

##### def__init__(text,*,level=None,color=None)



Create a new instance of the TextLog archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| text | The body of the message.TYPE:Utf8Like |
| level | The verbosity level of the message.This can be used to filter the log messages in the Rerun Viewer.TYPE:Utf8Like\| NoneDEFAULT:None |
| color | Optional color to use for the log line in the Rerun Viewer.TYPE:Rgba32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TextLog`.



##### defcolumns(*,text=None,level=None,color=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| text | The body of the message.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| level | The verbosity level of the message.This can be used to filter the log messages in the Rerun Viewer.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| color | Optional color to use for the log line in the Rerun Viewer.TYPE:Rgba32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,text=None,level=None,color=None)classmethod



Update only some specific fields of a `TextLog`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| text | The body of the message.TYPE:Utf8Like\| NoneDEFAULT:None |
| level | The verbosity level of the message.This can be used to filter the log messages in the Rerun Viewer.TYPE:Utf8Like\| NoneDEFAULT:None |
| color | Optional color to use for the log line in the Rerun Viewer.TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classTransform3D



Bases: `Transform3DExt`, `Archetype`



**Archetype**: A transform between two 3D spaces, i.e. a pose.



From the point of view of the entity's coordinate system,
all components are applied in the inverse order they are listed here.
E.g. if both a translation and a mat3x3 transform are present,
the 3x3 matrix is applied first, followed by the translation.



Whenever you log this archetype, the state of the resulting transform relationship is fully reset to the new archetype.
This means that if you first log a transform with only a translation, and then log one with only a rotation,
it will be resolved to a transform with only a rotation.
(This is unlike how we usually apply latest-at semantics on an archetype where we take the latest state of any component independently)



For transforms that affect only a single entity and do not propagate along the entity tree refer to archetypes.InstancePoses3D.



Examples:



###### Variety of 3D transforms:



```
from math import pi

import rerun as rr
from rerun.datatypes import Angle, RotationAxisAngle

rr.init("rerun_example_transform3d", spawn=True)

arrow = rr.Arrows3D(origins=[0, 0, 0], vectors=[0, 1, 0])

rr.log("base", arrow)

rr.log("base/translated", rr.Transform3D(translation=[1, 0, 0]))
rr.log("base/translated", arrow)

rr.log(
    "base/rotated_scaled",
    rr.Transform3D(
        rotation=RotationAxisAngle(axis=[0, 0, 1], angle=Angle(rad=pi / 4)),
        scale=2,
    ),
)
rr.log("base/rotated_scaled", arrow)
```

 ![](https://static.rerun.io/transform3d_simple/141368b07360ce3fcb1553079258ae3f42bdb9ac/full.png)

###### Update a transform over time:



```
import math

import rerun as rr

def truncated_radians(deg: float) -> float:
    return float(int(math.radians(deg) * 1000.0)) / 1000.0

rr.init("rerun_example_transform3d_row_updates", spawn=True)

rr.set_time("tick", sequence=0)
rr.log(
    "box",
    rr.Boxes3D(half_sizes=[4.0, 2.0, 1.0], fill_mode=rr.components.FillMode.Solid),
    rr.TransformAxes3D(10.0),
)

for t in range(100):
    rr.set_time("tick", sequence=t + 1)
    rr.log(
        "box",
        rr.Transform3D(
            translation=[0, 0, t / 10.0],
            rotation_axis_angle=rr.RotationAxisAngle(axis=[0.0, 1.0, 0.0], radians=truncated_radians(t * 4)),
        ),
    )
```

 ![](https://static.rerun.io/transform3d_column_updates/80634e1c7c7a505387e975f25ea8b6bc1d4eb9db/full.png)

###### Update a transform over time, in a single operation:



```
import math

import rerun as rr

def truncated_radians(deg: float) -> float:
    return float(int(math.radians(deg) * 1000.0)) / 1000.0

rr.init("rerun_example_transform3d_column_updates", spawn=True)

rr.set_time("tick", sequence=0)
rr.log(
    "box",
    rr.Boxes3D(half_sizes=[4.0, 2.0, 1.0], fill_mode=rr.components.FillMode.Solid),
    rr.TransformAxes3D(10.0),
)

rr.send_columns(
    "box",
    indexes=[rr.TimeColumn("tick", sequence=range(1, 101))],
    columns=rr.Transform3D.columns(
        translation=[[0, 0, t / 10.0] for t in range(100)],
        rotation_axis_angle=[
            rr.RotationAxisAngle(axis=[0.0, 1.0, 0.0], radians=truncated_radians(t * 4)) for t in range(100)
        ],
    ),
)
```

 ![](https://static.rerun.io/transform3d_column_updates/80634e1c7c7a505387e975f25ea8b6bc1d4eb9db/full.png)

###### Update specific properties of a transform over time:



```
import math

import rerun as rr

def truncated_radians(deg: float) -> float:
    return float(int(math.radians(deg) * 1000.0)) / 1000.0

rr.init("rerun_example_transform3d_partial_updates", spawn=True)

# Set up a 3D box.
rr.log(
    "box",
    rr.Boxes3D(half_sizes=[4.0, 2.0, 1.0], fill_mode=rr.components.FillMode.Solid),
)

# Update only the rotation of the box.
for deg in range(46):
    rad = truncated_radians(deg * 4)
    rr.log(
        "box",
        rr.Transform3D.from_fields(
            rotation_axis_angle=rr.RotationAxisAngle(axis=[0.0, 1.0, 0.0], radians=rad),
        ),
    )

# Update only the position of the box.
for t in range(51):
    rr.log(
        "box",
        rr.Transform3D.from_fields(translation=[0, 0, t / 10.0]),
    )

# Update only the rotation of the box.
for deg in range(46):
    rad = truncated_radians((deg + 45) * 4)
    rr.log(
        "box",
        rr.Transform3D.from_fields(
            rotation_axis_angle=rr.RotationAxisAngle(axis=[0.0, 1.0, 0.0], radians=rad),
        ),
    )

# Clear all of the box's attributes.
rr.log(
    "box",
    rr.Transform3D.from_fields(clear_unset=True),
)
```

 ![](https://static.rerun.io/transform3d_partial_updates/11815bebc69ae400847896372b496cdd3e9b19fb/full.png)

##### def__init__(*,translation=None,rotation=None,rotation_axis_angle=None,quaternion=None,scale=None,mat3x3=None,from_parent=None,relation=None,child_frame=None,parent_frame=None)



Create a new instance of the Transform3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| translation | 3D translation vector.TYPE:Vec3DLike\| NoneDEFAULT:None |
| rotation | 3D rotation, either a quaternion or an axis-angle. Mutually exclusive withquaternionandrotation_axis_angle.TYPE:QuaternionLike\|RotationAxisAngleLike\| NoneDEFAULT:None |
| rotation_axis_angle | Axis-angle representing rotation.Mutually exclusive withrotationparameter.TYPE:RotationAxisAngleLike\| NoneDEFAULT:None |
| quaternion | Quaternion representing rotation.Mutually exclusive withrotationparameter.TYPE:QuaternionLike\| NoneDEFAULT:None |
| scale | 3D scale.TYPE:Vec3DLike\|Float32Like\| NoneDEFAULT:None |
| mat3x3 | 3x3 matrix representing scale and rotation, applied after translation. Not compatible withrotationandscaleparameters. TODO(#3559): Support 4x4 and 4x3 matrices.TYPE:Mat3x3Like\| NoneDEFAULT:None |
| from_parent | If true, the transform maps from the parent space to the space where the transform was logged. Otherwise, the transform maps from the space to its parent. Deprecated in favor ofrelation=rerun.TransformRelation.ChildFromParent.Mutually exclusive withrelation.TYPE:bool\| NoneDEFAULT:None |
| relation | Allows to explicitly specify the transform's relationship with the parent entity. Otherwise, the transform maps from the space to its parent.Mutually exclusive withfrom_parent.TYPE:TransformRelationLike\| NoneDEFAULT:None |
| child_frame | The child frame this transform transforms from.The entity at which the transform relationship of any given child frame is specified mustn't change over time. E.g. if you specified the child frame"robot_arm"on an entity named"my_transforms", you may not log transforms with the child frame"robot_arm"on any other entity than"my_transforms". An exception to this rule is static time - you may first mention a child frame on one entity statically and later on another one temporally.â  This currently also affects the child frame ofarchetypes.Pinhole. â  This currently is also used as the frame id ofarchetypes.InstancePoses3D.If not specified, this is set to the implicit transform frame of the current entity path. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity/path.To set the frame an entity is part of seearchetypes.CoordinateFrame.TYPE:Utf8Like\| NoneDEFAULT:None |
| parent_frame | The parent frame this transform transforms into.â  This currently also affects the parent frame ofarchetypes.Pinhole.If not specified, this is set to the implicit transform frame of the current entity path's parent. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity.To set the frame an entity is part of seearchetypes.CoordinateFrame.TYPE:Utf8Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Transform3D`.



##### defcolumns(*,translation=None,rotation_axis_angle=None,quaternion=None,scale=None,mat3x3=None,relation=None,child_frame=None,parent_frame=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| translation | Translation vector.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| rotation_axis_angle | Rotation via axis + angle.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:RotationAxisAngleArrayLike\| NoneDEFAULT:None |
| quaternion | Rotation via quaternion.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:QuaternionArrayLike\| NoneDEFAULT:None |
| scale | Scaling factor.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec3DArrayLike\| NoneDEFAULT:None |
| mat3x3 | 3x3 transformation matrix.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Mat3x3ArrayLike\| NoneDEFAULT:None |
| relation | Specifies the relation this transform establishes between this entity and its parent.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:TransformRelationArrayLike\| NoneDEFAULT:None |
| child_frame | The child frame this transform transforms from.The entity at which the transform relationship of any given child frame is specified mustn't change over time, but is allowed to be different for static time. E.g. if you specified the child frame"robot_arm"on an entity named"my_transforms", you may not log transforms with the child frame"robot_arm"on any other entity than"my_transforms"unless one of them was logged with static time.If not specified, this is set to the implicit transform frame of the current entity path. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity/path.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |
| parent_frame | The parent frame this transform transforms into.If not specified, this is set to the implicit transform frame of the current entity path's parent. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,translation=None,rotation_axis_angle=None,quaternion=None,scale=None,mat3x3=None,relation=None,child_frame=None,parent_frame=None)classmethod



Update only some specific fields of a `Transform3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| translation | Translation vector.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec3DLike\| NoneDEFAULT:None |
| rotation_axis_angle | Rotation via axis + angle.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:RotationAxisAngleLike\| NoneDEFAULT:None |
| quaternion | Rotation via quaternion.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:QuaternionLike\| NoneDEFAULT:None |
| scale | Scaling factor.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Vec3DLike\| NoneDEFAULT:None |
| mat3x3 | 3x3 transformation matrix.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Mat3x3Like\| NoneDEFAULT:None |
| relation | Specifies the relation this transform establishes between this entity and its parent.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:TransformRelationLike\| NoneDEFAULT:None |
| child_frame | The child frame this transform transforms from.The entity at which the transform relationship of any given child frame is specified mustn't change over time, but is allowed to be different for static time. E.g. if you specified the child frame"robot_arm"on an entity named"my_transforms", you may not log transforms with the child frame"robot_arm"on any other entity than"my_transforms"unless one of them was logged with static time.If not specified, this is set to the implicit transform frame of the current entity path. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity/path.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8Like\| NoneDEFAULT:None |
| parent_frame | The parent frame this transform transforms into.If not specified, this is set to the implicit transform frame of the current entity path's parent. This means that if aarchetypes.Transform3Dis set on an entity called/my/entity/paththen this will default totf#/my/entity.To set the frame an entity is part of seearchetypes.CoordinateFrame.Any update to this field will reset all other transform properties that aren't changed in the same log call orsend_columnsrow.TYPE:Utf8Like\| NoneDEFAULT:None |



#### classTransformAxes3D



Bases: `Archetype`



**Archetype**: A visual representation of a archetypes.Transform3D.

 Example

###### Visual representation of a transform as three arrows:



```
import rerun as rr

rr.init("rerun_example_transform3d_axes", spawn=True)

rr.set_time("step", sequence=0)

# Set the axis lengths for all the transforms
rr.log("base", rr.Transform3D(), rr.TransformAxes3D(1.0))

# Now sweep out a rotation relative to the base
for deg in range(360):
    rr.set_time("step", sequence=deg)
    rr.log(
        "base/rotated",
        rr.Transform3D.from_fields(
            rotation_axis_angle=rr.RotationAxisAngle(
                axis=[1.0, 1.0, 1.0],
                degrees=deg,
            ),
        ),
        rr.TransformAxes3D(0.5),
    )
    rr.log(
        "base/rotated/translated",
        rr.Transform3D.from_fields(
            translation=[2.0, 0, 0],
        ),
        rr.TransformAxes3D(0.5),
    )
```

 ![](https://static.rerun.io/transform3d_axes/574c482088e9d317b19127fc8bef957dbfd3abe8/full.png)

##### def__init__(axis_length,*,show_frame=None)



Create a new instance of the TransformAxes3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| axis_length | Visual length of the 3 axes.The length is interpreted in the local coordinate system of the transform. If the transform is scaled, the axes will be scaled accordingly.TYPE:Float32Like |
| show_frame | Whether to show a text label with the corresponding frame.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TransformAxes3D`.



##### defcolumns(*,axis_length=None,show_frame=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| axis_length | Visual length of the 3 axes.The length is interpreted in the local coordinate system of the transform. If the transform is scaled, the axes will be scaled accordingly.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| show_frame | Whether to show a text label with the corresponding frame.TYPE:BoolArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,axis_length=None,show_frame=None)classmethod



Update only some specific fields of a `TransformAxes3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| axis_length | Visual length of the 3 axes.The length is interpreted in the local coordinate system of the transform. If the transform is scaled, the axes will be scaled accordingly.TYPE:Float32Like\| NoneDEFAULT:None |
| show_frame | Whether to show a text label with the corresponding frame.TYPE:BoolLike\| NoneDEFAULT:None |



#### classVideoFrameReference



Bases: `VideoFrameReferenceExt`, `Archetype`



**Archetype**: References a single video frame.



Used to display individual video frames from a archetypes.AssetVideo.
To show an entire video, a video frame reference for each frame of the video should be logged.



See [https://rerun.io/docs/reference/video](https://rerun.io/docs/reference/video) for details of what is and isn't supported.



TODO(#10422): archetypes.VideoFrameReference does not yet work with archetypes.VideoStream.



Examples:



###### Video with automatically determined frames:



```
import sys

import rerun as rr

if len(sys.argv) < 2:
    # TODO(#7354): Only mp4 is supported for now.
    print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
    sys.exit(1)

rr.init("rerun_example_asset_video_auto_frames", spawn=True)

# Log video asset which is referred to by frame references.
video_asset = rr.AssetVideo(path=sys.argv[1])
rr.log("video", video_asset, static=True)

# Send automatically determined video frame timestamps.
frame_timestamps_ns = video_asset.read_frame_timestamps_nanos()
rr.send_columns(
    "video",
    # Note timeline values don't have to be the same as the video timestamps.
    indexes=[rr.TimeColumn("video_time", duration=1e-9 * frame_timestamps_ns)],
    columns=rr.VideoFrameReference.columns_nanos(frame_timestamps_ns),
)
```

 ![](https://static.rerun.io/video_manual_frames/320a44e1e06b8b3a3161ecbbeae3e04d1ccb9589/full.png)

###### Demonstrates manual use of video frame references:



```
import sys

import rerun as rr
import rerun.blueprint as rrb

if len(sys.argv) < 2:
    # TODO(#7354): Only mp4 is supported for now.
    print(f"Usage: {sys.argv[0]} <path_to_video.[mp4]>")
    sys.exit(1)

rr.init("rerun_example_asset_video_manual_frames", spawn=True)

# Log video asset which is referred to by frame references.
rr.log("video_asset", rr.AssetVideo(path=sys.argv[1]), static=True)

# Create two entities, showing the same video frozen at different times.
rr.log(
    "frame_1s",
    rr.VideoFrameReference(seconds=1.0, video_reference="video_asset"),
)
rr.log(
    "frame_2s",
    rr.VideoFrameReference(seconds=2.0, video_reference="video_asset"),
)

# Send blueprint that shows two 2D views next to each other.
rr.send_blueprint(rrb.Horizontal(rrb.Spatial2DView(origin="frame_1s"), rrb.Spatial2DView(origin="frame_2s")))
```

 ![](https://static.rerun.io/video_manual_frames/9f41c00f84a98cc3f26875fba7c1d2fa2bad7151/full.png)

##### def__init__(timestamp=None,*,seconds=None,nanoseconds=None,video_reference=None)



Create a new instance of the VideoFrameReference archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timestamp | References the closest video frame to this timestamp.Note that this uses the closest video frame instead of the latest at this timestamp in order to be more forgiving of rounding errors for inprecise timestamp types.Mutually exclusive withsecondsandnanoseconds.TYPE:VideoTimestampLike\| NoneDEFAULT:None |
| seconds | Sets the timestamp to the given number of seconds.Mutually exclusive withtimestampandnanoseconds.TYPE:float\| NoneDEFAULT:None |
| nanoseconds | Sets the timestamp to the given number of nanoseconds.Mutually exclusive withtimestampandseconds.TYPE:int\| NoneDEFAULT:None |
| video_reference | Optional reference to an entity with aarchetypes.AssetVideo.If none is specified, the video is assumed to be at the same entity. Note that blueprint overrides on the referenced video will be ignored regardless, as this is always interpreted as a reference to the data store.For a series of video frame references, it is recommended to specify this path only once at the beginning of the series and then rely on latest-at query semantics to keep the video reference active.TYPE:EntityPathLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `VideoFrameReference`.



##### defcolumns(*,timestamp=None,video_reference=None,opacity=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timestamp | References the closest video frame to this timestamp.Note that this uses the closest video frame instead of the latest at this timestamp in order to be more forgiving of rounding errors for inprecise timestamp types.Timestamps are relative to the start of the video, i.e. a timestamp of 0 always corresponds to the first frame. This is oftentimes equivalent to presentation timestamps (known as PTS), but in the presence of B-frames (bidirectionally predicted frames) there may be an offset on the first presentation timestamp in the video.TYPE:VideoTimestampArrayLike\| NoneDEFAULT:None |
| video_reference | Optional reference to an entity with aarchetypes.AssetVideo.If none is specified, the video is assumed to be at the same entity. Note that blueprint overrides on the referenced video will be ignored regardless, as this is always interpreted as a reference to the data store.For a series of video frame references, it is recommended to specify this path only once at the beginning of the series and then rely on latest-at query semantics to keep the video reference active.TYPE:EntityPathArrayLike\| NoneDEFAULT:None |
| opacity | Opacity of the video, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-15.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### defcolumns_millis(milliseconds)classmethod



Helper for `VideoFrameReference.columns` with milliseconds-based `timestamp`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| milliseconds | Timestamp values in milliseconds since video start.TYPE:ArrayLike |



##### defcolumns_nanos(nanoseconds)classmethod



Helper for `VideoFrameReference.columns` with nanoseconds-based `timestamp`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| nanoseconds | Timestamp values in nanoseconds since video start.TYPE:ArrayLike |



##### defcolumns_secs(seconds)classmethod



Helper for `VideoFrameReference.columns` with seconds-based `timestamp`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| seconds | Timestamp values in seconds since video start.TYPE:ArrayLike |



##### deffrom_fields(*,clear_unset=False,timestamp=None,video_reference=None,opacity=None,draw_order=None)classmethod



Update only some specific fields of a `VideoFrameReference`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| timestamp | References the closest video frame to this timestamp.Note that this uses the closest video frame instead of the latest at this timestamp in order to be more forgiving of rounding errors for inprecise timestamp types.Timestamps are relative to the start of the video, i.e. a timestamp of 0 always corresponds to the first frame. This is oftentimes equivalent to presentation timestamps (known as PTS), but in the presence of B-frames (bidirectionally predicted frames) there may be an offset on the first presentation timestamp in the video.TYPE:VideoTimestampLike\| NoneDEFAULT:None |
| video_reference | Optional reference to an entity with aarchetypes.AssetVideo.If none is specified, the video is assumed to be at the same entity. Note that blueprint overrides on the referenced video will be ignored regardless, as this is always interpreted as a reference to the data store.For a series of video frame references, it is recommended to specify this path only once at the beginning of the series and then rely on latest-at query semantics to keep the video reference active.TYPE:EntityPathLike\| NoneDEFAULT:None |
| opacity | Opacity of the video, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-15.0.TYPE:Float32Like\| NoneDEFAULT:None |



#### classVideoStream



Bases: `Archetype`



**Archetype**: Video stream consisting of raw video chunks.



For logging video containers like mp4, refer to archetypes.AssetVideo and archetypes.VideoFrameReference.
To learn more about video support in Rerun, check the [video reference](https://rerun.io/docs/reference/video).



All components except `sample` are typically logged statically once per entity.
`sample` is then logged repeatedly for each frame on the timeline.



TODO(#10422): archetypes.VideoFrameReference does not yet work with archetypes.VideoStream.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Live streaming of on-the-fly encoded video:



```
import av
import numpy as np
import numpy.typing as npt
import rerun as rr

fps = 30
duration_seconds = 4
width = 480
height = 320
ball_radius = 30
codec = rr.VideoCodec.H265  # rr.VideoCodec.H264

formats = {rr.VideoCodec.H265: "hevc", rr.VideoCodec.H264: "h264"}
encoders = {rr.VideoCodec.H265: "libx265", rr.VideoCodec.H264: "libx264"}

def create_example_video_frame(frame_i: int) -> npt.NDArray[np.uint8]:
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for h in range(height):
        img[h, :] = [0, int(100 * h / height), int(200 * h / height)]  # Blue to purple gradient.

    x_pos = width // 2  # Center horizontally.
    y_pos = height // 2 + 80 * np.sin(2 * np.pi * frame_i / fps)
    y, x = np.ogrid[:height, :width]
    r_sq = (x - x_pos) ** 2 + (y - y_pos) ** 2
    img[r_sq < ball_radius**2] = [255, 200, 0]  # Gold color

    return img

rr.init("rerun_example_video_stream_synthetic", spawn=True)

# Setup encoding pipeline.
av.logging.set_level(av.logging.VERBOSE)
container = av.open("/dev/null", "w", format=formats[codec])  # Use AnnexB H.265 stream.
stream = container.add_stream(encoders[codec], rate=fps)
# Type narrowing
assert isinstance(stream, av.video.stream.VideoStream)
stream.width = width
stream.height = height
# TODO(#10090): Rerun Video Streams don't support b-frames yet.
# Note that b-frames are generally not recommended for low-latency streaming and may make logging more complex.
stream.max_b_frames = 0

# Log codec only once as static data (it naturally never changes). This isn't strictly necessary, but good practice.
rr.log("video_stream", rr.VideoStream(codec=codec), static=True)

# Generate frames and stream them directly to Rerun.
for frame_i in range(fps * duration_seconds):
    img = create_example_video_frame(frame_i)
    frame = av.VideoFrame.from_ndarray(img, format="rgb24")
    for packet in stream.encode(frame):
        if packet.pts is None:
            continue
        rr.set_time("time", duration=float(packet.pts * packet.time_base))
        rr.log("video_stream", rr.VideoStream.from_fields(sample=bytes(packet)))

# Flush stream.
for packet in stream.encode():
    if packet.pts is None:
        continue
    rr.set_time("time", duration=float(packet.pts * packet.time_base))
    rr.log("video_stream", rr.VideoStream.from_fields(sample=bytes(packet)))
```

 ![](https://static.rerun.io/video_stream_synthetic/4dd34da01980afa5604994fa4cce34d7573b0763/full.png)

##### def__init__(codec,*,sample=None,opacity=None,draw_order=None)



Create a new instance of the VideoStream archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| codec | The codec used to encode the video chunks.This property is expected to be constant over time and is ideally logged statically once per stream.TYPE:VideoCodecLike |
| sample | Video sample data (also known as "video chunk").The current timestamp is used as presentation timestamp (PTS) for all data in this sample. There is currently no way to log differing decoding timestamps, meaning that there is no support for B-frames. Seehttps://github.com/rerun-io/rerun/issues/10090for more details.Rerun chunks containing frames (i.e. bundles of sample data) may arrive out of order, but may cause the video playback in the Viewer to reset. It is recommended to have all chunks for a video stream to be ordered temporally order.Logging separate videos on the same entity is allowed iff they share the exact same codec parameters & resolution.The samples are expected to be encoded using thecodecfield. Each video sample must contain enough data for exactly one video frame (this restriction may be relaxed in the future for some codecs).Unless your stream consists entirely of key-frames (in which case you should considerarchetypes.EncodedImage) never log this component as static data as this means that you loose all information of previous samples which may be required to decode an image.Seecomponents.VideoCodecfor codec specific requirements.TYPE:BlobLike\| NoneDEFAULT:None |
| opacity | Opacity of the video stream, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-15.0.TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `VideoStream`.



##### defcolumns(*,codec=None,sample=None,opacity=None,draw_order=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| codec | The codec used to encode the video chunks.This property is expected to be constant over time and is ideally logged statically once per stream.TYPE:VideoCodecArrayLike\| NoneDEFAULT:None |
| sample | Video sample data (also known as "video chunk").The current timestamp is used as presentation timestamp (PTS) for all data in this sample. There is currently no way to log differing decoding timestamps, meaning that there is no support for B-frames. Seehttps://github.com/rerun-io/rerun/issues/10090for more details.Rerun chunks containing frames (i.e. bundles of sample data) may arrive out of order, but may cause the video playback in the Viewer to reset. It is recommended to have all chunks for a video stream to be ordered temporally order.Logging separate videos on the same entity is allowed iff they share the exact same codec parameters & resolution.The samples are expected to be encoded using thecodecfield. Each video sample must contain enough data for exactly one video frame (this restriction may be relaxed in the future for some codecs).Unless your stream consists entirely of key-frames (in which case you should considerarchetypes.EncodedImage) never log this component as static data as this means that you loose all information of previous samples which may be required to decode an image.Seecomponents.VideoCodecfor codec specific requirements.TYPE:BlobArrayLike\| NoneDEFAULT:None |
| opacity | Opacity of the video stream, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-15.0.TYPE:Float32ArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,codec=None,sample=None,opacity=None,draw_order=None)classmethod



Update only some specific fields of a `VideoStream`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| codec | The codec used to encode the video chunks.This property is expected to be constant over time and is ideally logged statically once per stream.TYPE:VideoCodecLike\| NoneDEFAULT:None |
| sample | Video sample data (also known as "video chunk").The current timestamp is used as presentation timestamp (PTS) for all data in this sample. There is currently no way to log differing decoding timestamps, meaning that there is no support for B-frames. Seehttps://github.com/rerun-io/rerun/issues/10090for more details.Rerun chunks containing frames (i.e. bundles of sample data) may arrive out of order, but may cause the video playback in the Viewer to reset. It is recommended to have all chunks for a video stream to be ordered temporally order.Logging separate videos on the same entity is allowed iff they share the exact same codec parameters & resolution.The samples are expected to be encoded using thecodecfield. Each video sample must contain enough data for exactly one video frame (this restriction may be relaxed in the future for some codecs).Unless your stream consists entirely of key-frames (in which case you should considerarchetypes.EncodedImage) never log this component as static data as this means that you loose all information of previous samples which may be required to decode an image.Seecomponents.VideoCodecfor codec specific requirements.TYPE:BlobLike\| NoneDEFAULT:None |
| opacity | Opacity of the video stream, useful for layering several media.Defaults to 1.0 (fully opaque).TYPE:Float32Like\| NoneDEFAULT:None |
| draw_order | An optional floating point value that specifies the 2D drawing order.Objects with higher values are drawn on top of those with lower values. Defaults to-15.0.TYPE:Float32Like\| NoneDEFAULT:None |



#### classViewCoordinates



Bases: `ViewCoordinatesExt`, `Archetype`



**Archetype**: How we interpret the coordinate system of an entity/space.



For instance: What is "up"? What does the Z axis mean?



The three coordinates are always ordered as [x, y, z].



For example [Right, Down, Forward] means that the X axis points to the right, the Y axis points
down, and the Z axis points forward.



Make sure that this archetype is logged at or above the origin entity path of your 3D views.



â  [Rerun does not yet support left-handed coordinate systems](https://github.com/rerun-io/rerun/issues/5032).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### View coordinates for adjusting the eye camera:



```
import rerun as rr

rr.init("rerun_example_view_coordinates", spawn=True)

rr.log("world", rr.ViewCoordinates.RIGHT_HAND_Z_UP, static=True)  # Set an up-axis
rr.log(
    "world/xyz",
    rr.Arrows3D(
        vectors=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
        colors=[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    ),
)
```

 ![](https://static.rerun.io/viewcoordinates/0833f0dc8616a676b7b2c566f2a6f613363680c5/full.png)

##### def__init__(xyz)



Create a new instance of the ViewCoordinates archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| xyz | The directions of the [x, y, z] axes.TYPE:ViewCoordinatesLike |



##### defcleared()classmethod



Clear all the fields of a `ViewCoordinates`.



##### defcolumns(*,xyz=None)classmethod



Construct a new column-oriented component bundle.



This makes it possible to use `rr.send_columns` to send columnar data directly into Rerun.



The returned columns will be partitioned into unit-length sub-batches by default.
Use `ComponentColumnList.partition` to repartition the data as needed.



| PARAMETER | DESCRIPTION |
| --- | --- |
| xyz | The directions of the [x, y, z] axes.TYPE:ViewCoordinatesArrayLike\| NoneDEFAULT:None |



##### deffrom_fields(*,clear_unset=False,xyz=None)classmethod



Update only some specific fields of a `ViewCoordinates`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| xyz | The directions of the [x, y, z] axes.TYPE:ViewCoordinatesLike\| NoneDEFAULT:None |