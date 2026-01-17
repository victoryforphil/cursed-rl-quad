---
source: https://ref.rerun.io/docs/python/stable/common/datatypes
title: Datatypes
---

# Datatypes



### rerun.datatypes



#### AbsoluteTimeRangeArrayLike=AbsoluteTimeRange|Sequence[AbsoluteTimeRangeLike]module-attribute



A type alias for any AbsoluteTimeRange-like array object.



#### AbsoluteTimeRangeLike=AbsoluteTimeRangemodule-attribute



A type alias for any AbsoluteTimeRange-like object.



#### AngleArrayLike=Angle|Sequence[AngleLike]|npt.ArrayLike|Sequence[float]|Sequence[int]module-attribute



A type alias for any Angle-like array object.



#### AngleLike=Angle|float|intmodule-attribute



A type alias for any Angle-like object.



#### AnnotationInfoArrayLike=AnnotationInfo|Sequence[AnnotationInfoLike]module-attribute



A type alias for any AnnotationInfo-like array object.



#### AnnotationInfoLike=AnnotationInfo|int|tuple[int,str]|tuple[int,str,datatypes.Rgba32Like]module-attribute



A type alias for any AnnotationInfo-like object.



#### BlobArrayLike=Blob|Sequence[BlobLike]|bytes|npt.NDArray[np.uint8]module-attribute



A type alias for any Blob-like array object.



#### BlobLike=Blob|bytes|npt.NDArray[np.uint8]module-attribute



A type alias for any Blob-like object.



#### BoolArrayLike=Bool|Sequence[BoolLike]module-attribute



A type alias for any Bool-like array object.



#### BoolLike=Bool|boolmodule-attribute



A type alias for any Bool-like object.



#### ChannelCountPairArrayLike=ChannelCountPair|Sequence[ChannelCountPairLike]module-attribute



A type alias for any ChannelCountPair-like array object.



#### ChannelCountPairLike=ChannelCountPair|tuple[datatypes.UInt16Like,datatypes.UInt64Like]module-attribute



A type alias for any ChannelCountPair-like object.



#### ChannelDatatypeArrayLike=ChannelDatatype|Literal['F16','F32','F64','I16','I32','I64','I8','U16','U32','U64','U8','f16','f32','f64','i16','i32','i64','i8','u16','u32','u64','u8']|int|Sequence[ChannelDatatypeLike]module-attribute



A type alias for any ChannelDatatype-like array object.



#### ChannelDatatypeLike=ChannelDatatype|Literal['F16','F32','F64','I16','I32','I64','I8','U16','U32','U64','U8','f16','f32','f64','i16','i32','i64','i8','u16','u32','u64','u8']|intmodule-attribute



A type alias for any ChannelDatatype-like object.



#### ClassDescriptionArrayLike=ClassDescription|Sequence[ClassDescriptionLike]module-attribute



A type alias for any ClassDescription-like array object.



#### ClassDescriptionLike=ClassDescription|datatypes.AnnotationInfoLikemodule-attribute



A type alias for any ClassDescription-like object.



#### ClassDescriptionMapElemArrayLike=ClassDescriptionMapElem|Sequence[ClassDescriptionMapElemLike]module-attribute



A type alias for any ClassDescriptionMapElem-like array object.



#### ClassDescriptionMapElemLike=ClassDescriptionMapElem|datatypes.ClassDescriptionLikemodule-attribute



A type alias for any ClassDescriptionMapElem-like object.



#### ClassIdArrayLike=ClassId|Sequence[ClassIdLike]|int|npt.ArrayLikemodule-attribute



A type alias for any ClassId-like array object.



#### ClassIdLike=ClassId|intmodule-attribute



A type alias for any ClassId-like object.



#### ColorModelArrayLike=ColorModel|Literal['BGR','BGRA','L','RGB','RGBA','bgr','bgra','l','rgb','rgba']|int|Sequence[ColorModelLike]module-attribute



A type alias for any ColorModel-like array object.



#### ColorModelLike=ColorModel|Literal['BGR','BGRA','L','RGB','RGBA','bgr','bgra','l','rgb','rgba']|intmodule-attribute



A type alias for any ColorModel-like object.



#### DVec2DArrayLike=DVec2D|Sequence[DVec2DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any DVec2D-like array object.



#### DVec2DLike=DVec2D|npt.NDArray[Any]|npt.ArrayLike|Sequence[float]module-attribute



A type alias for any DVec2D-like object.



#### EntityPathArrayLike=EntityPath|Sequence[EntityPathLike]|Sequence[str]module-attribute



A type alias for any EntityPath-like array object.



#### EntityPathLike=EntityPath|strmodule-attribute



A type alias for any EntityPath-like object.



#### Float32ArrayLike=Float32|Sequence[Float32Like]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Float32-like array object.



#### Float32Like=Float32|floatmodule-attribute



A type alias for any Float32-like object.



#### Float64ArrayLike=Float64|Sequence[Float64Like]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Float64-like array object.



#### Float64Like=Float64|floatmodule-attribute



A type alias for any Float64-like object.



#### ImageFormatArrayLike=ImageFormat|Sequence[ImageFormatLike]module-attribute



A type alias for any ImageFormat-like array object.



#### ImageFormatLike=ImageFormatmodule-attribute



A type alias for any ImageFormat-like object.



#### KeypointIdArrayLike=KeypointId|Sequence[KeypointIdLike]|int|npt.ArrayLikemodule-attribute



A type alias for any KeypointId-like array object.



#### KeypointIdLike=KeypointId|intmodule-attribute



A type alias for any KeypointId-like object.



#### KeypointPairArrayLike=KeypointPair|Sequence[KeypointPairLike]module-attribute



A type alias for any KeypointPair-like array object.



#### KeypointPairLike=KeypointPair|Sequence[datatypes.KeypointIdLike]module-attribute



A type alias for any KeypointPair-like object.



#### Mat3x3ArrayLike=Mat3x3|Sequence[Mat3x3Like]|npt.ArrayLikemodule-attribute



A type alias for any Mat3x3-like array object.



#### Mat3x3Like=Mat3x3|npt.ArrayLikemodule-attribute



A type alias for any Mat3x3-like object.



#### Mat4x4ArrayLike=Mat4x4|Sequence[Mat4x4Like]module-attribute



A type alias for any Mat4x4-like array object.



#### Mat4x4Like=Mat4x4|npt.ArrayLikemodule-attribute



A type alias for any Mat4x4-like object.



#### PixelFormatArrayLike=PixelFormat|Literal['NV12','Y8_FullRange','Y8_LimitedRange','YUY2','Y_U_V12_FullRange','Y_U_V12_LimitedRange','Y_U_V16_FullRange','Y_U_V16_LimitedRange','Y_U_V24_FullRange','Y_U_V24_LimitedRange','nv12','y8_fullrange','y8_limitedrange','y_u_v12_fullrange','y_u_v12_limitedrange','y_u_v16_fullrange','y_u_v16_limitedrange','y_u_v24_fullrange','y_u_v24_limitedrange','yuy2']|int|Sequence[PixelFormatLike]module-attribute



A type alias for any PixelFormat-like array object.



#### PixelFormatLike=PixelFormat|Literal['NV12','Y8_FullRange','Y8_LimitedRange','YUY2','Y_U_V12_FullRange','Y_U_V12_LimitedRange','Y_U_V16_FullRange','Y_U_V16_LimitedRange','Y_U_V24_FullRange','Y_U_V24_LimitedRange','nv12','y8_fullrange','y8_limitedrange','y_u_v12_fullrange','y_u_v12_limitedrange','y_u_v16_fullrange','y_u_v16_limitedrange','y_u_v24_fullrange','y_u_v24_limitedrange','yuy2']|intmodule-attribute



A type alias for any PixelFormat-like object.



#### Plane3DArrayLike=Plane3D|Sequence[Plane3DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]module-attribute



A type alias for any Plane3D-like array object.



#### Plane3DLike=Plane3Dmodule-attribute



A type alias for any Plane3D-like object.



#### QuaternionArrayLike=Quaternion|Sequence[QuaternionLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]module-attribute



A type alias for any Quaternion-like array object.



#### QuaternionLike=Quaternionmodule-attribute



A type alias for any Quaternion-like object.



#### Range1DArrayLike=Range1D|Sequence[Range1DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Range1D-like array object.



#### Range1DLike=Range1D|npt.NDArray[Any]|npt.ArrayLike|Sequence[float]|slicemodule-attribute



A type alias for any Range1D-like object.



#### Range2DArrayLike=Range2D|Sequence[Range2DLike]module-attribute



A type alias for any Range2D-like array object.



#### Range2DLike=Range2Dmodule-attribute



A type alias for any Range2D-like object.



#### Rgba32ArrayLike=Rgba32|Sequence[Rgba32Like]|int|npt.ArrayLikemodule-attribute



A type alias for any Rgba32-like array object.



#### Rgba32Like=Rgba32|int|Sequence[int|float]|npt.NDArray[np.uint8|np.float32|np.float64]module-attribute



A type alias for any Rgba32-like object.



#### RotationAxisAngleArrayLike=RotationAxisAngle|Sequence[RotationAxisAngleLike]module-attribute



A type alias for any RotationAxisAngle-like array object.



#### RotationAxisAngleLike=RotationAxisAnglemodule-attribute



A type alias for any RotationAxisAngle-like object.



#### TensorBufferArrayLike=TensorBuffer|npt.NDArray[np.float16]|npt.NDArray[np.float32]|npt.NDArray[np.float64]|npt.NDArray[np.int16]|npt.NDArray[np.int32]|npt.NDArray[np.int64]|npt.NDArray[np.int8]|npt.NDArray[np.uint16]|npt.NDArray[np.uint32]|npt.NDArray[np.uint64]|npt.NDArray[np.uint8]|Sequence[TensorBufferLike]module-attribute



A type alias for any TensorBuffer-like array object.



#### TensorBufferLike=TensorBuffer|npt.NDArray[np.float16]|npt.NDArray[np.float32]|npt.NDArray[np.float64]|npt.NDArray[np.int16]|npt.NDArray[np.int32]|npt.NDArray[np.int64]|npt.NDArray[np.int8]|npt.NDArray[np.uint16]|npt.NDArray[np.uint32]|npt.NDArray[np.uint64]|npt.NDArray[np.uint8]module-attribute



A type alias for any TensorBuffer-like object.



#### TensorDataArrayLike=TensorData|Sequence[TensorDataLike]|npt.ArrayLikemodule-attribute



A type alias for any TensorData-like array object.



#### TensorDataLike=TensorData|npt.ArrayLikemodule-attribute



A type alias for any TensorData-like object.



#### TensorDimensionIndexSelectionArrayLike=TensorDimensionIndexSelection|Sequence[TensorDimensionIndexSelectionLike]module-attribute



A type alias for any TensorDimensionIndexSelection-like array object.



#### TensorDimensionIndexSelectionLike=TensorDimensionIndexSelectionmodule-attribute



A type alias for any TensorDimensionIndexSelection-like object.



#### TensorDimensionSelectionArrayLike=TensorDimensionSelection|Sequence[TensorDimensionSelectionLike]|npt.ArrayLikemodule-attribute



A type alias for any TensorDimensionSelection-like array object.



#### TensorDimensionSelectionLike=TensorDimensionSelection|intmodule-attribute



A type alias for any TensorDimensionSelection-like object.



#### TimeIntArrayLike=TimeInt|Sequence[TimeIntLike]module-attribute



A type alias for any TimeInt-like array object.



#### TimeIntLike=TimeInt|intmodule-attribute



A type alias for any TimeInt-like object.



#### TimeRangeArrayLike=TimeRange|Sequence[TimeRangeLike]module-attribute



A type alias for any TimeRange-like array object.



#### TimeRangeBoundaryArrayLike=TimeRangeBoundary|None|datatypes.TimeInt|Sequence[TimeRangeBoundaryLike]module-attribute



A type alias for any TimeRangeBoundary-like array object.



#### TimeRangeBoundaryLike=TimeRangeBoundary|None|datatypes.TimeIntmodule-attribute



A type alias for any TimeRangeBoundary-like object.



#### TimeRangeLike=TimeRangemodule-attribute



A type alias for any TimeRange-like object.



#### UInt16ArrayLike=UInt16|Sequence[UInt16Like]|int|npt.NDArray[np.uint16]module-attribute



A type alias for any UInt16-like array object.



#### UInt16Like=UInt16|intmodule-attribute



A type alias for any UInt16-like object.



#### UInt32ArrayLike=UInt32|Sequence[UInt32Like]|int|npt.NDArray[np.uint32]module-attribute



A type alias for any UInt32-like array object.



#### UInt32Like=UInt32|intmodule-attribute



A type alias for any UInt32-like object.



#### UInt64ArrayLike=UInt64|Sequence[UInt64Like]|int|npt.NDArray[np.uint64]module-attribute



A type alias for any UInt64-like array object.



#### UInt64Like=UInt64|intmodule-attribute



A type alias for any UInt64-like object.



#### UVec2DArrayLike=UVec2D|Sequence[UVec2DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[int]]|Sequence[int]module-attribute



A type alias for any UVec2D-like array object.



#### UVec2DLike=UVec2D|npt.NDArray[Any]|npt.ArrayLike|Sequence[int]module-attribute



A type alias for any UVec2D-like object.



#### UVec3DArrayLike=UVec3D|Sequence[UVec3DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[int]]|Sequence[int]module-attribute



A type alias for any UVec3D-like array object.



#### UVec3DLike=UVec3D|npt.NDArray[Any]|npt.ArrayLike|Sequence[int]module-attribute



A type alias for any UVec3D-like object.



#### UVec4DArrayLike=UVec4D|Sequence[UVec4DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[int]]|Sequence[int]module-attribute



A type alias for any UVec4D-like array object.



#### UVec4DLike=UVec4D|npt.NDArray[Any]|npt.ArrayLike|Sequence[int]module-attribute



A type alias for any UVec4D-like object.



#### Utf8ArrayLike=Utf8|Sequence[Utf8Like]|str|Sequence[str]|npt.ArrayLikemodule-attribute



A type alias for any Utf8-like array object.



#### Utf8Like=Utf8|strmodule-attribute



A type alias for any Utf8-like object.



#### Utf8PairArrayLike=Utf8Pair|Sequence[Utf8PairLike]|npt.NDArray[np.str_]module-attribute



A type alias for any Utf8Pair-like array object.



#### Utf8PairLike=Utf8Pair|tuple[datatypes.Utf8Like,datatypes.Utf8Like]module-attribute



A type alias for any Utf8Pair-like object.



#### UuidArrayLike=Uuid|Sequence[UuidLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[int]]|Sequence[int]|Sequence[bytes]module-attribute



A type alias for any Uuid-like array object.



#### UuidLike=Uuid|npt.NDArray[Any]|npt.ArrayLike|Sequence[int]|bytesmodule-attribute



A type alias for any Uuid-like object.



#### Vec2DArrayLike=Vec2D|Sequence[Vec2DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Vec2D-like array object.



#### Vec2DLike=Vec2D|npt.NDArray[Any]|npt.ArrayLike|Sequence[float]module-attribute



A type alias for any Vec2D-like object.



#### Vec3DArrayLike=Vec3D|Sequence[Vec3DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Vec3D-like array object.



#### Vec3DLike=Vec3D|npt.NDArray[Any]|npt.ArrayLike|Sequence[float]module-attribute



A type alias for any Vec3D-like object.



#### Vec4DArrayLike=Vec4D|Sequence[Vec4DLike]|npt.NDArray[Any]|npt.ArrayLike|Sequence[Sequence[float]]|Sequence[float]module-attribute



A type alias for any Vec4D-like array object.



#### Vec4DLike=Vec4D|npt.NDArray[Any]|npt.ArrayLike|Sequence[float]module-attribute



A type alias for any Vec4D-like object.



#### VideoTimestampArrayLike=VideoTimestamp|Sequence[VideoTimestampLike]|npt.NDArray[np.int64]module-attribute



A type alias for any VideoTimestamp-like array object.



#### VideoTimestampLike=VideoTimestamp|intmodule-attribute



A type alias for any VideoTimestamp-like object.



#### ViewCoordinatesArrayLike=ViewCoordinates|Sequence[ViewCoordinatesLike]|npt.ArrayLikemodule-attribute



A type alias for any ViewCoordinates-like array object.



#### ViewCoordinatesLike=ViewCoordinates|npt.ArrayLikemodule-attribute



A type alias for any ViewCoordinates-like object.



#### VisibleTimeRangeArrayLike=VisibleTimeRange|Sequence[VisibleTimeRangeLike]module-attribute



A type alias for any VisibleTimeRange-like array object.



#### VisibleTimeRangeLike=VisibleTimeRangemodule-attribute



A type alias for any VisibleTimeRange-like object.



#### classAbsoluteTimeRange



Bases: `AbsoluteTimeRangeExt`



**Datatype**: Two datatypes.TimeInt describing a range of time.



##### def__init__(min,max)



Create a new instance of the AbsoluteTimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| min | Beginning of the time range.TYPE:TimeIntLike |
| max | End of the time range.TYPE:TimeIntLike |



#### classAngle



Bases: `AngleExt`



**Datatype**: Angle in radians.



##### def__init__(rad=None,deg=None)



Create a new instance of the Angle datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| rad | Angle in radians, specify eitherradordeg.TYPE:float\| NoneDEFAULT:None |
| deg | Angle in degrees, specify eitherradordeg. Converts the angle to radians internally.TYPE:float\| NoneDEFAULT:None |



#### classAnnotationInfo



Bases: `AnnotationInfoExt`



**Datatype**: Annotation info annotating a class id or key-point id.



Color and label will be used to annotate entities/keypoints which reference the id.
The id refers either to a class or key-point id



##### def__init__(id,label=None,color=None)



Create a new instance of the AnnotationInfo datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| id | datatypes.ClassIdordatatypes.KeypointIdto which this annotation info belongs.TYPE:int |
| label | The label that will be shown in the UI.TYPE:Utf8Like\| NoneDEFAULT:None |
| color | The color that will be applied to the annotated entity.TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classBlob



Bases: `BlobExt`



**Datatype**: A binary blob of data.



##### def__init__(data)



Create a new instance of the Blob datatype.



#### classBool



**Datatype**: A single boolean.



##### def__init__(value)



Create a new instance of the Bool datatype.



#### classChannelCountPair



Bases: `ChannelCountPairExt`



**Datatype**: A pair representing a channel ID and its associated message count.



##### def__init__(channel_id,message_count)



Create a new instance of the ChannelCountPair datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| channel_id | The channel ID.TYPE:UInt16Like |
| message_count | The message count for this channel.TYPE:UInt64Like |



#### classChannelDatatype



Bases: `ChannelDatatypeExt`, `Enum`



**Datatype**: The innermost datatype of an image.



How individual color channel components are encoded.



##### F16=33class-attributeinstance-attribute



16-bit IEEE-754 floating point, also known as `half`.



##### F32=34class-attributeinstance-attribute



32-bit IEEE-754 floating point, also known as `float` or `single`.



##### F64=35class-attributeinstance-attribute



64-bit IEEE-754 floating point, also known as `double`.



##### I16=9class-attributeinstance-attribute



16-bit signed integer.



##### I32=11class-attributeinstance-attribute



32-bit signed integer.



##### I64=13class-attributeinstance-attribute



64-bit signed integer.



##### I8=7class-attributeinstance-attribute



8-bit signed integer.



##### U16=8class-attributeinstance-attribute



16-bit unsigned integer.



##### U32=10class-attributeinstance-attribute



32-bit unsigned integer.



##### U64=12class-attributeinstance-attribute



64-bit unsigned integer.



##### U8=6class-attributeinstance-attribute



8-bit unsigned integer.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classClassDescription



Bases: `ClassDescriptionExt`



**Datatype**: The description of a semantic Class.



If an entity is annotated with a corresponding [components.ClassId](../components/#rerun.components.ClassId), Rerun will use
the attached datatypes.AnnotationInfo to derive labels and colors.



Keypoints within an annotation class can similarly be annotated with a
[components.KeypointId](../components/#rerun.components.KeypointId) in which case we should defer to the label and color for the
datatypes.AnnotationInfo specifically associated with the Keypoint.



Keypoints within the class can also be decorated with skeletal edges.
Keypoint-connections are pairs of [components.KeypointId](../components/#rerun.components.KeypointId)s. If an edge is
defined, and both keypoints exist within the instance of the class, then the
keypoints should be connected with an edge. The edge should be labeled and
colored as described by the class's datatypes.AnnotationInfo.



Note that a `ClassDescription` can be directly logged using `rerun.log`.
This is equivalent to logging a `rerun.AnnotationContext` containing
a single `ClassDescription`.



##### def__init__(*,info,keypoint_annotations=[],keypoint_connections=[])



Create a new instance of the ClassDescription datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| info | TheAnnotationInfofor the class.TYPE:AnnotationInfoLike |
| keypoint_annotations | TheAnnotationInfofor all the keypoints.TYPE:Sequence[AnnotationInfoLike] \| NoneDEFAULT:[] |
| keypoint_connections | The connections between keypoints.TYPE:Sequence[KeypointPairLike] \| NoneDEFAULT:[] |



#### classClassDescriptionMapElem



Bases: `ClassDescriptionMapElemExt`



**Datatype**: A helper type for mapping datatypes.ClassIds to class descriptions.



This is internal to [components.AnnotationContext](../components/#rerun.components.AnnotationContext).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(class_id,class_description)



Create a new instance of the ClassDescriptionMapElem datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| class_id | The key: thecomponents.ClassId.TYPE:ClassIdLike |
| class_description | The value: class name, color, etc.TYPE:ClassDescriptionLike |



#### classClassId



**Datatype**: A 16-bit ID representing a type of semantic class.



##### def__init__(id)



Create a new instance of the ClassId datatype.



#### classColorModel



Bases: `ColorModelExt`, `Enum`



**Datatype**: Specified what color components are present in an [archetypes.Image](../archetypes/#rerun.archetypes.Image).



This combined with datatypes.ChannelDatatype determines the pixel format of an image.



##### BGR=4class-attributeinstance-attribute



Blue, Green, Red



##### BGRA=5class-attributeinstance-attribute



Blue, Green, Red, Alpha



##### L=1class-attributeinstance-attribute



Grayscale luminance intencity/brightness/value, sometimes called `Y`



##### RGB=2class-attributeinstance-attribute



Red, Green, Blue



##### RGBA=3class-attributeinstance-attribute



Red, Green, Blue, Alpha



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classDVec2D



Bases: `DVec2DExt`



**Datatype**: A double-precision vector in 2D space.



##### def__init__(xy)



Create a new instance of the DVec2D datatype.



#### classEntityPath



**Datatype**: A path to an entity in the `ChunkStore`.



##### def__init__(path)



Create a new instance of the EntityPath datatype.



#### classFloat32



**Datatype**: A single-precision 32-bit IEEE 754 floating point number.



##### def__init__(value)



Create a new instance of the Float32 datatype.



#### classFloat64



**Datatype**: A double-precision 64-bit IEEE 754 floating point number.



##### def__init__(value)



Create a new instance of the Float64 datatype.



#### classImageFormat



Bases: `ImageFormatExt`



**Datatype**: The metadata describing the contents of a [components.ImageBuffer](../components/#rerun.components.ImageBuffer).



##### def__init__(width,height,*,pixel_format=None,color_model=None,channel_datatype=None)



Create a new instance of the ImageFormat datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | The width of the image in pixels.TYPE:int |
| height | The height of the image in pixels.TYPE:int |
| pixel_format | Used mainly for chroma downsampled formats and differing number of bits per channel.If specified, this takes precedence over bothdatatypes.ColorModelanddatatypes.ChannelDatatype(which are ignored).TYPE:PixelFormatLike\| NoneDEFAULT:None |
| color_model | L, RGB, RGBA, â¦Also requires adatatypes.ChannelDatatypeto fully specify the pixel format.TYPE:ColorModelLike\| NoneDEFAULT:None |
| channel_datatype | The data type of each channel (e.g. the red channel) of the image data (U8, F16, â¦).Also requires adatatypes.ColorModelto fully specify the pixel format.TYPE:ChannelDatatypeLike\| NoneDEFAULT:None |



#### classKeypointId



**Datatype**: A 16-bit ID representing a type of semantic keypoint within a class.



`KeypointId`s are only meaningful within the context of a [`rerun.datatypes.ClassDescription`].



Used to look up an [`rerun.datatypes.AnnotationInfo`] for a Keypoint within the
[`rerun.components.AnnotationContext`].



##### def__init__(id)



Create a new instance of the KeypointId datatype.



#### classKeypointPair



Bases: `KeypointPairExt`



**Datatype**: A connection between two datatypes.KeypointIds.



##### def__init__(keypoint0,keypoint1)



Create a new instance of the KeypointPair datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| keypoint0 | The first point of the pair.TYPE:KeypointIdLike |
| keypoint1 | The second point of the pair.TYPE:KeypointIdLike |



#### classMat3x3



Bases: `Mat3x3Ext`



**Datatype**: A 3x3 Matrix.



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
    rr.datatypes.Mat3x3([1, 2, 3, 4, 5, 6, 7, 8, 9]).flat_columns, np.array([1, 4, 7, 2, 5, 8, 3, 6, 9], dtype=np.float32)
)
np.testing.assert_array_equal(
    rr.datatypes.Mat3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).flat_columns,
    np.array([1, 4, 7, 2, 5, 8, 3, 6, 9], dtype=np.float32),
)
```

If you want to construct a matrix from a list of columns instead, use the named `columns` parameter:

```
np.testing.assert_array_equal(
    rr.datatypes.Mat3x3(columns=[1, 2, 3, 4, 5, 6, 7, 8, 9]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32),
)
np.testing.assert_array_equal(
    rr.datatypes.Mat3x3(columns=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.float32),
)
```



#### classMat4x4



Bases: `Mat4x4Ext`



**Datatype**: A 4x4 Matrix.



Matrices in Rerun are stored as flat list of coefficients in column-major order:

```
column 0         column 1         column 2         column 3
       --------------------------------------------------------------------
row 0 | flat_columns[0]  flat_columns[4]  flat_columns[8]  flat_columns[12]
row 1 | flat_columns[1]  flat_columns[5]  flat_columns[9]  flat_columns[13]
row 2 | flat_columns[2]  flat_columns[6]  flat_columns[10] flat_columns[14]
row 3 | flat_columns[3]  flat_columns[7]  flat_columns[11] flat_columns[15]
```



However, construction is done from a list of rows, which follows NumPy's convention:

```
np.testing.assert_array_equal(
    rr.datatypes.Mat4x4([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).flat_columns,
    np.array([1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16], dtype=np.float32),
)
np.testing.assert_array_equal(
    rr.datatypes.Mat4x4([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]).flat_columns,
    np.array([1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16], dtype=np.float32),
)
```

If you want to construct a matrix from a list of columns instead, use the named `columns` parameter:

```
np.testing.assert_array_equal(
    rr.datatypes.Mat4x4(columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], dtype=np.float32),
)
np.testing.assert_array_equal(
    rr.datatypes.Mat4x4(columns=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]).flat_columns,
    np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], dtype=np.float32),
)
```



#### classPixelFormat



Bases: `Enum`



**Datatype**: Specifieds a particular format of an [archetypes.Image](../archetypes/#rerun.archetypes.Image).



Most images can be described by a datatypes.ColorModel and a datatypes.ChannelDatatype,
e.g. `RGB` and `U8` respectively.



However, some image formats has chroma downsampling and/or
use differing number of bits per channel, and that is what this datatypes.PixelFormat is for.



All these formats support random access.



For more compressed image formats, see [archetypes.EncodedImage](../archetypes/#rerun.archetypes.EncodedImage).



##### NV12=26class-attributeinstance-attribute



`NV12` (aka `Y_UV12`) is a YUV 4:2:0 chroma downsampled form at with 12 bits per pixel and 8 bits per channel.



This uses limited range YUV, i.e. Y is expected to be within [16, 235] and U/V within [16, 240].



First comes entire image in Y in one plane,
followed by a plane with interleaved lines ordered as U0, V0, U1, V1, etc.



##### Y8_FullRange=30class-attributeinstance-attribute



Monochrome Y plane only, essentially a YUV 4:0:0 planar format.



Also known as just "gray". This is virtually identical to a 8bit luminance/grayscale (see datatypes.ColorModel).



This uses entire range YUV, i.e. Y is expected to be within [0, 255].
(as opposed to "limited range" YUV as used e.g. in NV12).



##### Y8_LimitedRange=41class-attributeinstance-attribute



Monochrome Y plane only, essentially a YUV 4:0:0 planar format.



Also known as just "gray".



This uses limited range YUV, i.e. Y is expected to be within [16, 235].
If not for this range limitation/remapping, this is almost identical to 8bit luminace/grayscale (see datatypes.ColorModel).



##### YUY2=27class-attributeinstance-attribute



`YUY2` (aka 'YUYV', 'YUYV16' or 'NV21'), is a YUV 4:2:2 chroma downsampled format with 16 bits per pixel and 8 bits per channel.



This uses limited range YUV, i.e. Y is expected to be within [16, 235] and U/V within [16, 240].



The order of the channels is Y0, U0, Y1, V0, all in the same plane.



##### Y_U_V12_FullRange=44class-attributeinstance-attribute



`Y_U_V12` is a YUV 4:2:0 fully planar YUV format without chroma downsampling, also known as `I420`.



This uses full range YUV with all components ranging from 0 to 255
(as opposed to "limited range" YUV as used e.g. in NV12).



First comes entire image in Y in one plane, followed by the U and V planes, which each only have half
the resolution of the Y plane.



##### Y_U_V12_LimitedRange=20class-attributeinstance-attribute



`Y_U_V12` is a YUV 4:2:0 fully planar YUV format without chroma downsampling, also known as `I420`.



This uses limited range YUV, i.e. Y is expected to be within [16, 235] and U/V within [16, 240].



First comes entire image in Y in one plane, followed by the U and V planes, which each only have half
the resolution of the Y plane.



##### Y_U_V16_FullRange=50class-attributeinstance-attribute



`Y_U_V16` is a YUV 4:2:2 fully planar YUV format without chroma downsampling, also known as `I422`.



This uses full range YUV with all components ranging from 0 to 255
(as opposed to "limited range" YUV as used e.g. in NV12).



First comes entire image in Y in one plane, followed by the U and V planes, which each only have half
the horizontal resolution of the Y plane.



##### Y_U_V16_LimitedRange=49class-attributeinstance-attribute



`Y_U_V16` is a YUV 4:2:2 fully planar YUV format without chroma downsampling, also known as `I422`.



This uses limited range YUV, i.e. Y is expected to be within [16, 235] and U/V within [16, 240].



First comes entire image in Y in one plane, followed by the U and V planes, which each only have half
the horizontal resolution of the Y plane.



##### Y_U_V24_FullRange=40class-attributeinstance-attribute



`Y_U_V24` is a YUV 4:4:4 fully planar YUV format without chroma downsampling, also known as `I444`.



This uses full range YUV with all components ranging from 0 to 255
(as opposed to "limited range" YUV as used e.g. in NV12).



First comes entire image in Y in one plane, followed by the U and V planes.



##### Y_U_V24_LimitedRange=39class-attributeinstance-attribute



`Y_U_V24` is a YUV 4:4:4 fully planar YUV format without chroma downsampling, also known as `I444`.



This uses limited range YUV, i.e. Y is expected to be within [16, 235] and U/V within [16, 240].



First comes entire image in Y in one plane, followed by the U and V planes.



##### def__str__()



Returns the variant name.



##### defauto(val)classmethod



Best-effort converter, including a case-insensitive string matcher.



#### classPlane3D



Bases: `Plane3DExt`



**Datatype**: An infinite 3D plane represented by a unit normal vector and a distance.



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



##### defdistance()



Returns the distance of the plane from the origin.



##### defnormal()



Returns the normal vector of the plane.



##### defwith_distance(distance)



Returns a new plane with the same normal but with the distance set to the given amount.



#### classQuaternion



Bases: `QuaternionExt`



**Datatype**: A Quaternion represented by 4 real numbers.



Note: although the x,y,z,w components of the quaternion will be passed through to the
datastore as provided, when used in the Viewer Quaternions will always be normalized.



#### classRange1D



Bases: `Range1DExt`



**Datatype**: A 1D range, specifying a lower and upper bound.



##### def__init__(range)



Create a new instance of the Range1D datatype.



#### classRange2D



**Datatype**: An Axis-Aligned Bounding Box in 2D space, implemented as the minimum and maximum corners.



##### def__init__(x_range,y_range)



Create a new instance of the Range2D datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| x_range | The range of the X-axis (usually left and right bounds).TYPE:Range1DLike |
| y_range | The range of the Y-axis (usually top and bottom bounds).TYPE:Range1DLike |



#### classRgba32



Bases: `Rgba32Ext`



**Datatype**: An RGBA color with unmultiplied/separate alpha, in sRGB gamma space with linear alpha.



The color is stored as a 32-bit integer, where the most significant
byte is `R` and the least significant byte is `A`.



Float colors are assumed to be in 0-1 gamma sRGB space.
All other colors are assumed to be in 0-255 gamma sRGB space.
If there is an alpha, we assume it is in linear space, and separate (NOT pre-multiplied).



##### def__init__(rgba)



Create a new instance of the Rgba32 datatype.



#### classRotationAxisAngle



Bases: `RotationAxisAngleExt`



**Datatype**: 3D rotation represented by a rotation around a given axis.



##### def__init__(axis,angle=None,*,radians=None,degrees=None)



Create a new instance of the RotationAxisAngle datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| axis | Axis to rotate around.This is not required to be normalized.  If normalization fails (typically because the vector is length zero), the rotation is silently  ignored.TYPE:Vec3DLike |
| angle | How much to rotate around the axis.TYPE:AngleLike\| NoneDEFAULT:None |
| radians | How much to rotate around the axis, in radians. Specify this instead ofdegreesorangle.TYPE:float\| NoneDEFAULT:None |
| degrees | How much to rotate around the axis, in degrees. Specify this instead ofradiansorangle.TYPE:float\| NoneDEFAULT:None |



#### classTensorBuffer



Bases: `TensorBufferExt`



**Datatype**: The underlying storage for [archetypes.Tensor](../archetypes/#rerun.archetypes.Tensor).



Tensor elements are stored in a contiguous buffer of a single type.



##### inner:npt.NDArray[np.float16]|npt.NDArray[np.float32]|npt.NDArray[np.float64]|npt.NDArray[np.int16]|npt.NDArray[np.int32]|npt.NDArray[np.int64]|npt.NDArray[np.int8]|npt.NDArray[np.uint16]|npt.NDArray[np.uint32]|npt.NDArray[np.uint64]|npt.NDArray[np.uint8]=field(converter=TensorBufferExt.inner__field_converter_override)class-attributeinstance-attribute



Must be one of:



- U8 (npt.NDArray[np.uint8]):
      8bit unsigned integer.
- U16 (npt.NDArray[np.uint16]):
      16bit unsigned integer.
- U32 (npt.NDArray[np.uint32]):
      32bit unsigned integer.
- U64 (npt.NDArray[np.uint64]):
      64bit unsigned integer.
- I8 (npt.NDArray[np.int8]):
      8bit signed integer.
- I16 (npt.NDArray[np.int16]):
      16bit signed integer.
- I32 (npt.NDArray[np.int32]):
      32bit signed integer.
- I64 (npt.NDArray[np.int64]):
      64bit signed integer.
- F16 (npt.NDArray[np.float16]):
      16bit IEEE-754 floating point, also known as `half`.
- F32 (npt.NDArray[np.float32]):
      32bit IEEE-754 floating point, also known as `float` or `single`.
- F64 (npt.NDArray[np.float64]):
      64bit IEEE-754 floating point, also known as `double`.



#### classTensorData



Bases: `TensorDataExt`



**Datatype**: An N-dimensional array of numbers.



The number of dimensions and their respective lengths is specified by the `shape` field.
The dimensions are ordered from outermost to innermost. For example, in the common case of
a 2D RGB Image, the shape would be `[height, width, channel]`.



These dimensions are combined with an index to look up values from the `buffer` field,
which stores a contiguous array of typed values.



It's not currently possible to use `send_columns` with tensors since construction
of `rerun.components.TensorDataBatch` does not support more than a single element.
This will be addressed as part of [https://github.com/rerun-io/rerun/issues/6832](https://github.com/rerun-io/rerun/issues/6832).



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



##### defnumpy(force)



Convert the TensorData back to a numpy array.



#### classTensorDimensionIndexSelection



**Datatype**: Indexing a specific tensor dimension.



Selecting `dimension=2` and `index=42` is similar to doing `tensor[:, :, 42, :, :, â¦]` in numpy.



##### def__init__(dimension,index)



Create a new instance of the TensorDimensionIndexSelection datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number to select.TYPE:int |
| index | The index along the dimension to use.TYPE:int |



#### classTensorDimensionSelection



Bases: `TensorDimensionSelectionExt`



**Datatype**: Selection of a single tensor dimension.



##### def__init__(dimension,*,invert=False)



Create a new instance of the TensorDimensionSelection datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| dimension | The dimension number to select.TYPE:int |
| invert | Invert the direction of the dimension.TYPE:boolDEFAULT:False |



#### classTimeInt



Bases: `TimeIntExt`



**Datatype**: A 64-bit number describing either nanoseconds OR sequence numbers.



##### def__init__(*,seq=None,seconds=None,nanos=None)



Create a new instance of the TimeInt datatype.



Exactly one of `seq`, `seconds`, or `nanos` must be provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| seq | Time as a sequence number.TYPE:int\| NoneDEFAULT:None |
| seconds | Time in seconds.Interpreted either as a duration or time since unix epoch (depending on timeline type).TYPE:float\| NoneDEFAULT:None |
| nanos | Time in nanoseconds.Interpreted either as a duration or time since unix epoch (depending on timeline type).TYPE:int\| NoneDEFAULT:None |



#### classTimeRange



**Datatype**: Visible time range bounds for a specific timeline.



##### def__init__(start,end)



Create a new instance of the TimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| start | Low time boundary for sequence timeline.TYPE:TimeRangeBoundaryLike |
| end | High time boundary for sequence timeline.TYPE:TimeRangeBoundaryLike |



#### classTimeRangeBoundary



Bases: `TimeRangeBoundaryExt`



**Datatype**: Left or right boundary of a time range.



##### inner:None|datatypes.TimeInt=field()class-attributeinstance-attribute



Must be one of:



- CursorRelative (datatypes.TimeInt):
      Boundary is a value relative to the time cursor.
- Absolute (datatypes.TimeInt):
      Boundary is an absolute value.
- Infinite (None):
      The boundary extends to infinity.



##### kind:Literal['cursor_relative','absolute','infinite']=field(default='cursor_relative')class-attributeinstance-attribute



Possible values:



- "cursor_relative":
      Boundary is a value relative to the time cursor.
- "absolute":
      Boundary is an absolute value.
- "infinite":
      The boundary extends to infinity.



##### defabsolute(time=None,*,seq=None,seconds=None,nanos=None)staticmethod



Boundary that is at an absolute time.



Exactly one of 'time', 'seq', 'seconds', or 'nanos' must be provided.



| PARAMETER | DESCRIPTION |
| --- | --- |
| time | Absolute time.TYPE:TimeInt\| NoneDEFAULT:None |
| seq | Absolute time in sequence numbers.Not compatible with temporal timelines.TYPE:int\| NoneDEFAULT:None |
| seconds | Absolute time in seconds.Interpreted either as a duration or time since unix epoch (depending on timeline type). Not compatible with sequence timelines.TYPE:float\| NoneDEFAULT:None |
| nanos | Absolute time in nanoseconds.Interpreted either as a duration or time since unix epoch (depending on timeline type). Not compatible with sequence timelines.TYPE:int\| NoneDEFAULT:None |



##### defcursor_relative(offset=None,*,seq=None,seconds=None,nanos=None)staticmethod



Boundary that is relative to the timeline cursor.



The offset can be positive or negative.
An offset of zero (the default) means the cursor time itself.



| PARAMETER | DESCRIPTION |
| --- | --- |
| offset | Offset from the cursor time.Mutually exclusive with seq, seconds and nanos.TYPE:TimeInt\| NoneDEFAULT:None |
| seq | Offset in sequence numbers.Use this for sequence timelines. Mutually exclusive with time, seconds and nanos.TYPE:int\| NoneDEFAULT:None |
| seconds | Offset in seconds.Use this for time based timelines. Mutually exclusive with time, seq and nanos.TYPE:float\| NoneDEFAULT:None |
| nanos | Offset in nanoseconds.Use this for time based timelines. Mutually exclusive with time, seq and seconds.TYPE:int\| NoneDEFAULT:None |



##### definfinite()staticmethod



Boundary that extends to infinity.



Depending on the context, this can mean the beginning or the end of the timeline.



#### classUInt16



**Datatype**: A 16bit unsigned integer.



##### def__init__(value)



Create a new instance of the UInt16 datatype.



#### classUInt32



**Datatype**: A 32bit unsigned integer.



##### def__init__(value)



Create a new instance of the UInt32 datatype.



#### classUInt64



**Datatype**: A 64bit unsigned integer.



##### def__init__(value)



Create a new instance of the UInt64 datatype.



#### classUVec2D



Bases: `UVec2DExt`



**Datatype**: A uint32 vector in 2D space.



##### def__init__(xy)



Create a new instance of the UVec2D datatype.



#### classUVec3D



Bases: `UVec3DExt`



**Datatype**: A uint32 vector in 3D space.



##### def__init__(xyz)



Create a new instance of the UVec3D datatype.



#### classUVec4D



**Datatype**: A uint vector in 4D space.



##### def__init__(xyzw)



Create a new instance of the UVec4D datatype.



#### classUtf8



**Datatype**: A string of text, encoded as UTF-8.



##### def__init__(value)



Create a new instance of the Utf8 datatype.



#### classUtf8Pair



Bases: `Utf8PairExt`



**Datatype**: Stores a tuple of UTF-8 strings.



##### def__init__(first,second)



Create a new instance of the Utf8Pair datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| first | The first string.TYPE:Utf8Like |
| second | The second string.TYPE:Utf8Like |



#### classUuid



Bases: `UuidExt`



**Datatype**: A 16-byte UUID.



##### def__init__(bytes)



Create a new instance of the Uuid datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| bytes | The raw bytes representing the UUID.TYPE:UuidLike |



#### classVec2D



Bases: `Vec2DExt`



**Datatype**: A vector in 2D space.



##### def__init__(xy)



Create a new instance of the Vec2D datatype.



#### classVec3D



Bases: `Vec3DExt`



**Datatype**: A vector in 3D space.



##### def__init__(xyz)



Create a new instance of the Vec3D datatype.



#### classVec4D



Bases: `Vec4DExt`



**Datatype**: A vector in 4D space.



##### def__init__(xyzw)



Create a new instance of the Vec4D datatype.



#### classVideoTimestamp



**Datatype**: Presentation timestamp within a [archetypes.AssetVideo](../archetypes/#rerun.archetypes.AssetVideo).



Specified in nanoseconds.
Presentation timestamps are typically measured as time since video start.



##### def__init__(timestamp_ns)



Create a new instance of the VideoTimestamp datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timestamp_ns | Presentation timestamp value in nanoseconds.TYPE:VideoTimestampLike |



#### classViewCoordinates



Bases: `ViewCoordinatesExt`



**Datatype**: How we interpret the coordinate system of an entity/space.



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



##### def__init__(coordinates)



Create a new instance of the ViewCoordinates datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| coordinates | The directions of the [x, y, z] axes.TYPE:ViewCoordinatesLike |



#### classVisibleTimeRange



Bases: `VisibleTimeRangeExt`



**Datatype**: Visible time range bounds for a specific timeline.



##### def__init__(timeline,range=None,*,start=None,end=None)



Create a new instance of the VisibleTimeRange datatype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | Name of the timeline this applies to.TYPE:Utf8Like |
| range | Time range to use for this timeline.TYPE:TimeRangeLike\| NoneDEFAULT:None |
| start | Low time boundary for sequence timeline. Specify this instead ofrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |
| end | High time boundary for sequence timeline. Specify this instead ofrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |