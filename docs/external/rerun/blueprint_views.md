---
source: https://ref.rerun.io/docs/python/stable/common/blueprint_views
title: Views
---

# Views



### rerun.blueprint.views



#### classBarChartView



Bases: `View`



**View**: A bar chart view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to create a BarChartView.:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_bar_chart", spawn=True)
rr.log("bar_chart", rr.BarChart([8, 4, 0, 9, 1, 4, 1, 6, 9, 0]))

# Create a bar chart view to display the chart.
blueprint = rrb.Blueprint(
    rrb.BarChartView(
        origin="bar_chart",
        name="Bar Chart",
        background=rrb.archetypes.PlotBackground(color=[50, 0, 50, 255], show_grid=False),
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/bar_chart_view/74fa45af3c7310b51cd283c37439ed8f8ca9356d/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,plot_legend=None,background=None)



Construct a blueprint for a new BarChartView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| plot_legend | Configures the legend of the plot.TYPE:PlotLegend\|Corner2D\| NoneDEFAULT:None |
| background | Configures the background of the plot.TYPE:PlotBackground\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classDataframeView



Bases: `View`



**View**: A view to display any data in a tabular form.



Any data from the store can be shown, using a flexibly, user-configurable query.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to customize a DataframeView.:



```
import math

import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_dataframe", spawn=True)

# Log some data.
for t in range(int(math.pi * 4 * 100.0)):
    rr.set_time("t", duration=t)
    rr.log("trig/sin", rr.Scalars(math.sin(float(t) / 100.0)))
    rr.log("trig/cos", rr.Scalars(math.cos(float(t) / 100.0)))

    # some sparse data
    if t % 5 == 0:
        rr.log("trig/tan_sparse", rr.Scalars(math.tan(float(t) / 100.0)))

# Create a Dataframe View
blueprint = rrb.Blueprint(
    rrb.DataframeView(
        origin="/trig",
        query=rrb.archetypes.DataframeQuery(
            timeline="t",
            filter_by_range=(rr.TimeInt(seconds=0), rr.TimeInt(seconds=20)),
            filter_is_not_null="/trig/tan_sparse:Scalar",
            select=["t", "log_tick", "/trig/sin:Scalar", "/trig/cos:Scalar", "/trig/tan_sparse:Scalar"],
        ),
    ),
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/dataframe_view/f89ae330b04baaa9b7576765dce37b5d4e7cef4e/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,query=None)



Construct a blueprint for a new DataframeView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| query | Query of the dataframe.TYPE:DataframeQuery\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classGraphView



Bases: `View`



**View**: A graph view to display time-variying, directed or undirected graph visualization.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to create a graph view.:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_graph_view", spawn=True)

rr.log(
    "simple",
    rr.GraphNodes(
        node_ids=["a", "b", "c"],
        positions=[(0.0, 100.0), (-100.0, 0.0), (100.0, 0.0)],
        labels=["A", "B", "C"],
    ),
)

# Create a Spatial2D view to display the points.
blueprint = rrb.Blueprint(
    rrb.GraphView(
        origin="/",
        name="Graph",
        # Note that this translates the viewbox.
        visual_bounds=rrb.VisualBounds2D(x_range=[-150, 150], y_range=[-50, 150]),
        background=rrb.archetypes.GraphBackground(color=[30, 10, 10]),
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/graph_lattice/f9169da9c3f35b7260c9d74cd5be5fe710aec6a8/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,background=None,visual_bounds=None,force_link=None,force_many_body=None,force_position=None,force_collision_radius=None,force_center=None)



Construct a blueprint for a new GraphView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| background | Configures the background of the graph.TYPE:GraphBackground\| NoneDEFAULT:None |
| visual_bounds | Everything within these bounds is guaranteed to be visible.Somethings outside of these bounds may also be visible due to letterboxing.TYPE:VisualBounds2D\| NoneDEFAULT:None |
| force_link | Allows to control the interaction between two nodes connected by an edge.TYPE:ForceLink\| NoneDEFAULT:None |
| force_many_body | A force between each pair of nodes that ressembles an electrical charge.TYPE:ForceManyBody\| NoneDEFAULT:None |
| force_position | Similar to gravity, this force pulls nodes towards a specific position.TYPE:ForcePosition\| NoneDEFAULT:None |
| force_collision_radius | Resolves collisions between the bounding spheres, according to the radius of the nodes.TYPE:ForceCollisionRadius\| NoneDEFAULT:None |
| force_center | Tries to move the center of mass of the graph to the origin.TYPE:ForceCenter\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classMapView



Bases: `View`



**View**: A 2D map view to display geospatial primitives.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to create a map view.:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_map_view", spawn=True)

rr.log("points", rr.GeoPoints(lat_lon=[[47.6344, 19.1397], [47.6334, 19.1399]], radii=rr.Radius.ui_points(20.0)))

# Create a map view to display the chart.
blueprint = rrb.Blueprint(
    rrb.MapView(
        origin="points",
        name="MapView",
        zoom=16.0,
        background=rrb.MapProvider.OpenStreetMap,
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/map_view/9d0a5ba3a6e8d4693ba98e1b3cfcc15d166fd41d/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,zoom=None,background=None)



Construct a blueprint for a new MapView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| zoom | Configures the zoom level of the map view.TYPE:MapZoom\|Float64Like\| NoneDEFAULT:None |
| background | Configuration for the background map of the map view.TYPE:MapBackground\|MapProviderLike\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classSpatial2DView



Bases: `View`



**View**: For viewing spatial 2D data.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to customize a Spatial2DView.:



```
import numpy as np
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_spatial_2d", spawn=True)

# Create a spiral of points:
n = 150
angle = np.linspace(0, 10 * np.pi, n)
spiral_radius = np.linspace(0.0, 3.0, n) ** 2
positions = np.column_stack((np.cos(angle) * spiral_radius, np.sin(angle) * spiral_radius))
colors = np.dstack((np.linspace(255, 255, n), np.linspace(255, 0, n), np.linspace(0, 255, n)))[0].astype(int)
radii = np.linspace(0.01, 0.7, n)

rr.log("points", rr.Points2D(positions, colors=colors, radii=radii))

# Create a Spatial2D view to display the points.
blueprint = rrb.Blueprint(
    rrb.Spatial2DView(
        origin="/",
        name="2D Scene",
        # Set the background color
        background=[105, 20, 105],
        # Note that this range is smaller than the range of the points,
        # so some points will not be visible.
        visual_bounds=rrb.VisualBounds2D(x_range=[-5, 5], y_range=[-5, 5]),
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/Spatial2DVIew/824a075e0c50ea4110eb6ddd60257f087cb2264d/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,background=None,visual_bounds=None,time_ranges=None)



Construct a blueprint for a new Spatial2DView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| background | Configuration for the background of the view.TYPE:Background\|Rgba32Like\|BackgroundKindLike\| NoneDEFAULT:None |
| visual_bounds | The visible parts of the scene, in the coordinate space of the scene.Everything within these bounds are guaranteed to be visible. Somethings outside of these bounds may also be visible due to letterboxing.TYPE:VisualBounds2D\| NoneDEFAULT:None |
| time_ranges | Configures which range on each timeline is shown by this view (unless specified differently per entity).If not specified, the default is to show the latest state of each component. If a timeline is specified more than once, the first entry will be used.TYPE:VisibleTimeRanges\|VisibleTimeRangeLike\|Sequence[VisibleTimeRangeLike] \| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classSpatial3DView



Bases: `View`



**View**: For viewing spatial 3D data.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to customize a Spatial3DView.:



```
import rerun as rr
import rerun.blueprint as rrb
from numpy.random import default_rng

rr.init("rerun_example_spatial_3d", spawn=True)

# Create some random points.
rng = default_rng(12345)
positions = rng.uniform(-5, 5, size=[50, 3])
colors = rng.uniform(0, 255, size=[50, 3])
radii = rng.uniform(0.1, 0.5, size=[50])

rr.log("points", rr.Points3D(positions, colors=colors, radii=radii))
rr.log("box", rr.Boxes3D(half_sizes=[5, 5, 5], colors=0))

# Create a Spatial3D view to display the points.
blueprint = rrb.Blueprint(
    rrb.Spatial3DView(
        origin="/",
        name="3D Scene",
        # Set the background color to light blue.
        background=[100, 149, 237],
        # Configure the eye controls.
        eye_controls=rrb.EyeControls3D(
            position=(0.0, 0.0, 2.0),
            look_target=(0.0, 2.0, 0.0),
            eye_up=(-1.0, 0.0, 0.0),
            spin_speed=0.2,
            kind=rrb.Eye3DKind.FirstPerson,
            speed=20.0,
        ),
        # Configure the line grid.
        line_grid=rrb.LineGrid3D(
            visible=True,  # The grid is enabled by default, but you can hide it with this property.
            spacing=0.1,  # Makes the grid more fine-grained.
            # By default, the plane is inferred from view coordinates setup, but you can set arbitrary planes.
            plane=rr.components.Plane3D.XY.with_distance(-5.0),
            stroke_width=2.0,  # Makes the grid lines twice as thick as usual.
            color=[255, 255, 255, 128],  # Colors the grid a half-transparent white.
        ),
        spatial_information=rrb.SpatialInformation(
            target_frame="tf#/",
            show_axes=True,
            show_bounding_box=True,
        ),
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/spatial3d/4816694fc4176cc284ff30d9c8f06c936a625ac9/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,background=None,line_grid=None,spatial_information=None,eye_controls=None,time_ranges=None)



Construct a blueprint for a new Spatial3DView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| background | Configuration for the background of the view.TYPE:Background\|Rgba32Like\|BackgroundKindLike\| NoneDEFAULT:None |
| line_grid | Configuration for the 3D line grid.TYPE:LineGrid3D\|BoolLike\| NoneDEFAULT:None |
| spatial_information | Configuration of debug drawing in the 3D view.TYPE:SpatialInformation\| NoneDEFAULT:None |
| eye_controls | Configuration for the 3D eyeTYPE:EyeControls3D\| NoneDEFAULT:None |
| time_ranges | Configures which range on each timeline is shown by this view (unless specified differently per entity).If not specified, the default is to show the latest state of each component. If a timeline is specified more than once, the first entry will be used.TYPE:VisibleTimeRanges\|VisibleTimeRangeLike\|Sequence[VisibleTimeRangeLike] \| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classTensorView



Bases: `View`



**View**: A view on a tensor of any dimensionality.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to create a TensorView.:



```
import numpy as np
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_tensor", spawn=True)

tensor = np.random.randint(0, 256, (32, 240, 320, 3), dtype=np.uint8)
rr.log("tensor", rr.Tensor(tensor, dim_names=("batch", "x", "y", "channel")))

blueprint = rrb.Blueprint(
    rrb.TensorView(
        origin="tensor",
        name="Tensor",
        # Explicitly pick which dimensions to show.
        slice_selection=rrb.TensorSliceSelection(
            # Use the first dimension as width.
            width=1,
            # Use the second dimension as height and invert it.
            height=rr.TensorDimensionSelection(dimension=2, invert=True),
            # Set which indices to show for the other dimensions.
            indices=[
                rr.TensorDimensionIndexSelection(dimension=2, index=4),
                rr.TensorDimensionIndexSelection(dimension=3, index=5),
            ],
            # Show a slider for dimension 2 only. If not specified, all dimensions in `indices` will have sliders.
            slider=[2],
        ),
        # Set a scalar mapping with a custom colormap, gamma and magnification filter.
        scalar_mapping=rrb.TensorScalarMapping(colormap="turbo", gamma=1.5, mag_filter="linear"),
        # Fill the view, ignoring aspect ratio.
        view_fit="fill",
    ),
    collapse_panels=True,
)
rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/tensor_view/04158807b970c16af7922698389b239b0575c436/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,slice_selection=None,scalar_mapping=None,view_fit=None)



Construct a blueprint for a new TensorView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| slice_selection | How to select the slice of the tensor to show.TYPE:TensorSliceSelection\| NoneDEFAULT:None |
| scalar_mapping | Configures how scalars are mapped to color.TYPE:TensorScalarMapping\| NoneDEFAULT:None |
| view_fit | Configures how the selected slice should fit into the view.TYPE:TensorViewFit\|ViewFitLike\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classTextDocumentView



Bases: `View`



**View**: A view of a single text document, for use with [archetypes.TextDocument](../archetypes/#rerun.archetypes.TextDocument).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to show a text document.:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_text_document", spawn=True)

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

# Create a text view that displays the markdown.
blueprint = rrb.Blueprint(rrb.TextDocumentView(origin="markdown", name="Markdown example"), collapse_panels=True)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/text_log/27f15235fe9639ff42b6ea0d2f0ce580685c021c/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None)



Construct a blueprint for a new TextDocumentView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classTextLogView



Bases: `View`



**View**: A view of a text log, for use with [archetypes.TextLog](../archetypes/#rerun.archetypes.TextLog).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to show a TextLogView.:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_text_log", spawn=True)

rr.set_time("time", sequence=0)
rr.log("log/status", rr.TextLog("Application started.", level=rr.TextLogLevel.INFO))
rr.set_time("time", sequence=5)
rr.log("log/other", rr.TextLog("A warning.", level=rr.TextLogLevel.WARN))
for i in range(10):
    rr.set_time("time", sequence=i)
    rr.log("log/status", rr.TextLog(f"Processing item {i}.", level=rr.TextLogLevel.INFO))

# Create a text view that displays all logs.
blueprint = rrb.Blueprint(
    rrb.TextLogView(
        origin="/log",
        name="Text Logs",
        columns=rrb.TextLogColumns(
            timeline_columns=["time"],
            text_log_columns=["loglevel", "entitypath", "body"],
        ),
        rows=rrb.TextLogRows(
            filter_by_log_level=["INFO", "WARN", "ERROR"],
        ),
        format_options=rrb.TextLogFormat(
            monospace_body=False,
        ),
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/text_log/457ab91ec42a481bacae4146c0fc01eee397bb86/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,columns=None,rows=None,format_options=None)



Construct a blueprint for a new TextLogView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| columns | The columns to display in the view.TYPE:TextLogColumns\| NoneDEFAULT:None |
| rows | Filter for rows to display in the view.TYPE:TextLogRows\| NoneDEFAULT:None |
| format_options | Formatting options for the text log view.TYPE:TextLogFormat\| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.



#### classTimeSeriesView



Bases: `View`



**View**: A time series view for scalars over time, for use with [archetypes.Scalars](../archetypes/#rerun.archetypes.Scalars).



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**

 Example

###### Use a blueprint to customize a TimeSeriesView.:



```
import math

import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_timeseries", spawn=True)

# Log some trigonometric functions
rr.log("trig/sin", rr.SeriesLines(colors=[255, 0, 0], names="sin(0.01t)"), static=True)
rr.log("trig/cos", rr.SeriesLines(colors=[0, 255, 0], names="cos(0.01t)"), static=True)
rr.log("trig/cos_scaled", rr.SeriesLines(colors=[0, 0, 255], names="cos(0.01t) scaled"), static=True)
for t in range(int(math.pi * 4 * 100.0)):
    rr.set_time("timeline0", sequence=t)
    rr.set_time("timeline1", duration=t)
    rr.log("trig/sin", rr.Scalars(math.sin(float(t) / 100.0)))
    rr.log("trig/cos", rr.Scalars(math.cos(float(t) / 100.0)))
    rr.log("trig/cos_scaled", rr.Scalars(math.cos(float(t) / 100.0) * 2.0))

# Create a TimeSeries View
blueprint = rrb.Blueprint(
    rrb.Vertical(
        contents=[
            rrb.TimeSeriesView(
                origin="/trig",
                # Set a custom Y axis.
                axis_y=rrb.ScalarAxis(range=(-1.0, 1.0), zoom_lock=True),
                # Configure the legend.
                plot_legend=rrb.PlotLegend(visible=False),
                # Set time different time ranges for different timelines.
                time_ranges=[
                    # Sliding window depending on the time cursor for the first timeline.
                    rrb.VisibleTimeRange(
                        "timeline0",
                        start=rrb.TimeRangeBoundary.cursor_relative(seq=-100),
                        end=rrb.TimeRangeBoundary.cursor_relative(),
                    ),
                    # Time range from some point to the end of the timeline for the second timeline.
                    rrb.VisibleTimeRange(
                        "timeline1",
                        start=rrb.TimeRangeBoundary.absolute(seconds=300.0),
                        end=rrb.TimeRangeBoundary.infinite(),
                    ),
                ],
            ),
            rrb.TimeSeriesView(
                origin="/trig",
                # Configure the legend.
                plot_legend=rrb.PlotLegend(visible=True),
                background=rrb.archetypes.PlotBackground(color=[128, 128, 128], show_grid=False),
            ),
        ]
    ),
    collapse_panels=True,
)

rr.send_blueprint(blueprint)
```

 ![](https://static.rerun.io/timeseries_view/c87150647feb413627fdb8563afe33b39d7dbf57/full.png)

##### def__init__(*,origin='/',contents='$origin/**',name=None,visible=None,defaults=None,overrides=None,axis_x=None,axis_y=None,plot_legend=None,background=None,time_ranges=None)



Construct a blueprint for a new TimeSeriesView view.



| PARAMETER | DESCRIPTION |
| --- | --- |
| origin | TheEntityPathto use as the origin of this view. All other entities will be transformed to be displayed relative to this origin.TYPE:EntityPathLikeDEFAULT:'/' |
| contents | The contents of the view specified as a query expression. This is either a single expression, or a list of multiple expressions. Seererun.blueprint.archetypes.ViewContents.TYPE:ViewContentsLikeDEFAULT:'$origin/**' |
| name | The display name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| defaults | List of archetypes or (described) component batches to add to the view. When an archetype in the view is missing a component included in this set, the value of default will be used instead of the normal fallback for the visualizer.Note that an archetype's required components typically don't have any effect. It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.TYPE:Iterable[AsComponents\|Iterable[DescribedComponentBatch]] \| NoneDEFAULT:None |
| overrides | Dictionary of overrides to apply to the view. The key is the path to the entity where the override should be applied. The value is a list of archetypes or (described) component batches to apply to the entity.It is recommended to use the archetype'sfrom_fieldsmethod instead and only specify the fields that you need.Important note: the path must be a fully qualified entity path starting at the root. The override paths do not yet support$originrelative paths or glob expressions. This will be addressed inhttps://github.com/rerun-io/rerun/issues/6673.TYPE:Mapping[EntityPathLike,AsComponents\|Iterable[DescribedComponentBatch\|AsComponents\|Iterable[DescribedComponentBatch]]] \| NoneDEFAULT:None |
| axis_x | Configures the horizontal axis of the plot.TYPE:TimeAxis\| NoneDEFAULT:None |
| axis_y | Configures the vertical axis of the plot.TYPE:ScalarAxis\| NoneDEFAULT:None |
| plot_legend | Configures the legend of the plot.TYPE:PlotLegend\|Corner2D\| NoneDEFAULT:None |
| background | Configures the background of the plot.TYPE:PlotBackground\| NoneDEFAULT:None |
| time_ranges | Configures which range on each timeline is shown by this view (unless specified differently per entity).If not specified, the default is to show the entire timeline. If a timeline is specified more than once, the first entry will be used.TYPE:VisibleTimeRanges\|VisibleTimeRangeLike\|Sequence[VisibleTimeRangeLike] \| NoneDEFAULT:None |



##### defblueprint_path()



The blueprint path where this view will be logged.



Note that although this is an `EntityPath`, is scoped to the blueprint tree and
not a part of the regular data hierarchy.



##### defto_blueprint()



Convert this view to a full blueprint.



##### defto_container()



Convert this view to a container.