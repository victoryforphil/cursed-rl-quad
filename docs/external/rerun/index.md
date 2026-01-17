---
source: https://ref.rerun.io/docs/python/stable/common/
title: Troubleshooting
---

## Getting Started



- [Quick start](https://www.rerun.io/docs/getting-started/quick-start/python)
- [Tutorial](https://www.rerun.io/docs/getting-started/data-in/python)
- [Examples on GitHub](https://github.com/rerun-io/rerun/tree/latest/examples/python)
- [Troubleshooting](https://www.rerun.io/docs/getting-started/troubleshooting)



There are many different ways of sending data to the Rerun Viewer depending on what you're trying
to achieve and whether the viewer is running in the same process as your code, in another process,
or even as a separate web application.



Checkout [SDK Operating Modes](https://www.rerun.io/docs/reference/sdk/operating-modes) for an
overview of what's possible and how.



## Supported Python Versions



Rerun will typically support Python version up until their end-of-life. If you are using an older version
of Python, you can use the table below to make sure you choose the proper Rerun version for your Python installation.



| Rerun Version | Release Date | Supported Python Version |
| --- | --- | --- |
| 0.27 | Nov. 10, 2025 | 3.10+ |
| 0.26 | Oct. 13, 2025 | 3.9+ |
| 0.25 | Sep. 16, 2025 | 3.9+ |
| 0.24 | Jul. 17, 2025 | 3.9+ |
| 0.23 | Apr. 24, 2025 | 3.9+ |
| 0.22 | Feb. 6, 2025 | 3.9+ |
| 0.21 | Dec. 18. 2024 | 3.9+ |
| 0.20 | Nov. 14, 2024 | 3.9+ |
| 0.19 | Oct. 17, 2024 | 3.8+ |



## APIs



### Initialization functions



| Function | Description |
| --- | --- |
| rerun.init() | Initialize the Rerun SDK with a user-chosen application id (name). |
| rerun.set_sinks() | Stream data to multiple different sinks. |
| rerun.connect_grpc() | Connect to a remote Rerun Viewer on the given URL. |
| rerun.disconnect() | Closes all gRPC connections, servers, and files. |
| rerun.save() | Stream all log-data to a file. |
| rerun.send_blueprint() | Create a blueprint from aBlueprintLikeand send it to theRecordingStream. |
| rerun.serve_grpc() | Serve log-data over gRPC. |
| rerun.serve_web_viewer() | Host a web viewer over HTTP. |
| rerun.spawn() | Spawn a Rerun Viewer, listening on the given port. |
| rerun.memory_recording() | Streams all log-data to a memory buffer. |
| rerun.notebook_show() | Output the Rerun viewer in a notebook using IPythonIPython.core.display.HTML. |
| rerun.legacy_notebook_show() | Output the Rerun viewer in a notebook using IPythonIPython.core.display.HTML. |



| Class | Description |
| --- | --- |
| rerun_bindings.rerun_bindings.ChunkBatcherConfig | Defines the different batching thresholds used within the RecordingStream. |
| rerun.DescribedComponentBatch | AComponentBatchLikeobject with its associatedComponentDescriptor. |
| rerun.RecordingStream | A RecordingStream is used to send data to Rerun. |
| rerun.TimeColumnLike | Describes interface for objects that can be converted to a column of rerun time values. |



### Logging functions



| Function | Description |
| --- | --- |
| rerun.log() | Log data to Rerun. |
| rerun.log_file_from_path() | Logs the file at the givenpathusing allDataLoaders available. |
| rerun.log_file_from_contents() | Logs the givenfile_contentsusing allDataLoaders available. |



### Timeline functions



| Function | Description |
| --- | --- |
| rerun.set_time() | Set the current time of a timeline for this thread. |
| rerun.disable_timeline() | Clear time information for the specified timeline on this thread. |
| rerun.reset_time() | Clear all timeline information on this thread. |



### Columnar API



| Function | Description |
| --- | --- |
| rerun.send_columns() | Send columnar data to Rerun. |
| rerun.send_record_batch() | Coerce a single pyarrowRecordBatchto Rerun structure. |
| rerun.send_dataframe() | Coerce a pyarrowRecordBatchReaderorTableto Rerun structure. |



| Class | Description |
| --- | --- |
| rerun.TimeColumn | A column of index (time) values. |



### Custom Data



| Class | Description |
| --- | --- |
| rerun.AnyValues | Helper to log arbitrary values as a bundle of components. |
| rerun.AnyBatchValue | Helper to log arbitrary data as a component batch or column. |
| rerun_bindings.rerun_bindings.ComponentDescriptor | AComponentDescriptorfully describes the semantics of a column of data. |



### General



| Class | Description |
| --- | --- |
| rerun.Clear | Archetype: Empties all the components of an entity. |
| rerun.blueprint.archetypes.EntityBehavior | Archetype: General visualization behavior of an entity. |
| rerun.archetypes.RecordingInfo | Archetype: A list of properties associated with a recording. |



### Annotations



| Class | Description |
| --- | --- |
| rerun.AnnotationContext | Archetype: The annotation context provides additional information on how to display entities. |
| rerun.AnnotationInfo | Datatype: Annotation info annotating a class id or key-point id. |
| rerun.ClassDescription | Datatype: The description of a semantic Class. |



### Images



| Class | Description |
| --- | --- |
| rerun.DepthImage | Archetype: A depth image, i.e. as captured by a depth camera. |
| rerun.Image | Archetype: A monochrome or color image. |
| rerun.EncodedImage | Archetype: An image encoded as e.g. a JPEG or PNG. |
| rerun.EncodedDepthImage | Archetype: A depth image encoded with a codec (e.g. RVL or PNG). |
| rerun.SegmentationImage | Archetype: An image made up of integercomponents.ClassIds. |



### Video



| Class | Description |
| --- | --- |
| rerun.VideoStream | Archetype: Video stream consisting of raw video chunks. |
| rerun.AssetVideo | Archetype: A video binary. |
| rerun.VideoFrameReference | Archetype: References a single video frame. |



### Plotting



| Class | Description |
| --- | --- |
| rerun.BarChart | Archetype: A bar chart. |
| rerun.Scalars | Archetype: One or more double-precision scalar values, e.g. for use for time-series plots. |
| rerun.SeriesLines | Archetype: Define the style properties for one or more line series in a chart. |
| rerun.SeriesPoints | Archetype: Define the style properties for one or more point series (scatter plot) in a chart. |



### Spatial Archetypes



| Class | Description |
| --- | --- |
| rerun.Arrows3D | Archetype: 3D arrows with optional colors, radii, labels, etc. |
| rerun.Arrows2D | Archetype: 2D arrows with optional colors, radii, labels, etc. |
| rerun.Asset3D | Archetype: A prepacked 3D asset (.gltf,.glb,.obj,.stl, etc.). |
| rerun.Boxes2D | Archetype: 2D boxes with half-extents and optional center, colors etc. |
| rerun.Boxes3D | Archetype: 3D boxes with half-extents and optional center, rotations, colors etc. |
| rerun.Capsules3D | Archetype: 3D capsules; cylinders with hemispherical caps. |
| rerun.Cylinders3D | Archetype: 3D cylinders with flat caps. |
| rerun.Ellipsoids3D | Archetype: 3D ellipsoids or spheres. |
| rerun.LineStrips2D | Archetype: 2D line strips with positions and optional colors, radii, labels, etc. |
| rerun.LineStrips3D | Archetype: 3D line strips with positions and optional colors, radii, labels, etc. |
| rerun.Mesh3D | Archetype: A 3D triangle mesh as specified by its per-mesh and per-vertex properties. |
| rerun.Points2D | Archetype: A 2D point cloud with positions and optional colors, radii, labels, etc. |
| rerun.Points3D | Archetype: A 3D point cloud with positions and optional colors, radii, labels, etc. |
| rerun.TransformAxes3D | Archetype: A visual representation of aarchetypes.Transform3D. |



### Geospatial Archetypes



| Class | Description |
| --- | --- |
| rerun.GeoLineStrings | Archetype: Geospatial line strings with positions expressed inEPSG:4326latitude and longitude (North/East-positive degrees), and optional colors and radii. |
| rerun.GeoPoints | Archetype: Geospatial points with positions expressed inEPSG:4326latitude and longitude (North/East-positive degrees), and optional colors and radii. |



### Graphs



| Class | Description |
| --- | --- |
| rerun.GraphNodes | Archetype: A list of nodes in a graph with optional labels, colors, etc. |
| rerun.GraphEdges | Archetype: A list of edges in a graph. |



### Tensors



| Class | Description |
| --- | --- |
| rerun.Tensor | Archetype: An N-dimensional array of numbers. |



### Text



| Class | Description |
| --- | --- |
| rerun.LoggingHandler | Provides a logging handler that forwards all events to the Rerun SDK. |
| rerun.TextDocument | Archetype: A text element intended to be displayed in its own text box. |
| rerun.TextLog | Archetype: A log entry in a text log, comprised of a text body and its log level. |



### Transforms and Coordinate Systems



| Class | Description |
| --- | --- |
| rerun.Pinhole | Archetype: Camera perspective projection (a.k.a. intrinsics). |
| rerun.Transform3D | Archetype: A transform between two 3D spaces, i.e. a pose. |
| rerun.InstancePoses3D | Archetype: One or more transforms applied on the current entity's transform frame. |
| rerun.ViewCoordinates | Archetype: How we interpret the coordinate system of an entity/space. |
| rerun.Scale3D | Component: A 3D scale factor. |
| rerun.Quaternion | Datatype: A Quaternion represented by 4 real numbers. |
| rerun.RotationAxisAngle | Datatype: 3D rotation represented by a rotation around a given axis. |
| rerun.CoordinateFrame | Archetype: Specifies the coordinate frame for an entity. |



### MCAP



| Class | Description |
| --- | --- |
| rerun.McapChannel | Archetype: A channel within an MCAP file that defines how messages are structured and encoded. |
| rerun.McapMessage | Archetype: The binary payload of a single MCAP message, without metadata. |
| rerun.McapSchema | Archetype: A schema definition that describes the structure of messages in an MCAP file. |
| rerun.McapStatistics | Archetype: Recording-level statistics about an MCAP file, logged as a part ofarchetypes.RecordingInfo. |



### Interfaces



| Class | Description |
| --- | --- |
| rerun.ComponentMixin | Makes components adhere to theComponentBatchLikeinterface. |
| rerun.ComponentBatchLike | Describes interface for objects that can be converted to batch of rerun Components. |
| rerun.AsComponents | Describes interface for interpreting an object as a bundle of Components. |
| rerun.ComponentBatchLike | Describes interface for objects that can be converted to batch of rerun Components. |
| rerun.ComponentColumn | A column of components that can be sent usingsend_columns. |



### Blueprint



| Class | Description |
| --- | --- |
| rerun.blueprint.Blueprint | The top-level description of the viewer blueprint. |
| rerun.blueprint.BlueprintLike | A type that can be converted to a blueprint. |
| rerun.blueprint.BlueprintPart | The types that make up a blueprint. |
| rerun.blueprint.Container | Base class for all container types. |
| rerun.blueprint.ContainerLike | A type that can be converted to a container. |
| rerun.blueprint.Horizontal | A horizontal container. |
| rerun.blueprint.Vertical | A vertical container. |
| rerun.blueprint.Grid | A grid container. |
| rerun.blueprint.Tabs | A tab container. |
| rerun.blueprint.View | Base class for all view types. |
| rerun.blueprint.BarChartView | View: A bar chart view. |
| rerun.blueprint.Spatial2DView | View: For viewing spatial 2D data. |
| rerun.blueprint.Spatial3DView | View: For viewing spatial 3D data. |
| rerun.blueprint.TensorView | View: A view on a tensor of any dimensionality. |
| rerun.blueprint.TextDocumentView | View: A view of a single text document, for use witharchetypes.TextDocument. |
| rerun.blueprint.TextLogView | View: A view of a text log, for use witharchetypes.TextLog. |
| rerun.blueprint.TimeSeriesView | View: A time series view for scalars over time, for use witharchetypes.Scalars. |
| rerun.blueprint.BlueprintPanel | The state of the blueprint panel. |
| rerun.blueprint.SelectionPanel | The state of the selection panel. |
| rerun.blueprint.TimePanel | The state of the time panel. |



### Catalog



| Class | Description |
| --- | --- |
| rerun.catalog.Schema | The schema representing a set of available columns for a dataset. |
| rerun_bindings.rerun_bindings.ComponentColumnDescriptor | The descriptor of a component column. |
| rerun_bindings.rerun_bindings.ComponentColumnSelector | A selector for a component column. |
| rerun_bindings.rerun_bindings.IndexColumnDescriptor | The descriptor of an index column. |
| rerun_bindings.rerun_bindings.IndexColumnSelector | A selector for an index column. |
| rerun_bindings.rerun_bindings.AlreadyExistsError | Raised when trying to create a resource that already exists. |
| rerun.catalog.CatalogClient | Client for a remote Rerun catalog server. |
| rerun.catalog.DatasetEntry | A dataset entry in the catalog. |
| rerun.catalog.DatasetView | A filtered view over a dataset in the catalog. |
| rerun.catalog.Entry | An entry in the catalog. |
| rerun_bindings.rerun_bindings.EntryId | A unique identifier for an entry in the catalog. |
| rerun_bindings.rerun_bindings.EntryKind | The kinds of entries that can be stored in the catalog. |
| rerun_bindings.types.IndexValuesLike | A type alias for index values. |
| rerun_bindings.rerun_bindings.NotFoundError | Raised when the requested resource is not found. |
| rerun.catalog.RegistrationHandle | Handle to track and wait on segment registration tasks. |
| rerun.catalog.SegmentRegistrationResult | Result of a completed segment registration. |
| rerun.catalog.TableEntry | A table entry in the catalog. |
| rerun_bindings.rerun_bindings.VectorDistanceMetric | Which distance metric for use for vector index. |
| rerun_bindings.types.VectorDistanceMetricLike | A type alias for vector distance metrics. |



### Recording



| Function | Description |
| --- | --- |
| rerun.recording.load_archive() | Load a rerun archive from an RRD file. |
| rerun.recording.load_recording() | Load a single recording from an RRD file. |



| Class | Description |
| --- | --- |
| rerun_bindings.rerun_bindings.Recording | A single Rerun recording. |
| rerun_bindings.rerun_bindings.RRDArchive | An archive loaded from an RRD. |



### Script Helpers



| Function | Description |
| --- | --- |
| rerun.script_add_args() | Add common Rerun script arguments toparser. |
| rerun.script_setup() | Run common Rerun script setup actions. Connect to the viewer if necessary. |
| rerun.script_teardown() | Run common post-actions. Sleep if serving the web viewer. |



# Troubleshooting



You can set `RUST_LOG=debug` before running your Python script
and/or `rerun` process to get some verbose logging output.



If you run into any issues don't hesitate to [open a ticket](https://github.com/rerun-io/rerun/issues/new/choose)
or [join our Discord](https://discord.gg/Gcm8BbTaAj).