---
source: https://ref.rerun.io/docs/python/stable/common/blueprint_archetypes
title: Archetypes
---

# Archetypes



### rerun.blueprint.archetypes



#### classBackground



Bases: `BackgroundExt`, `Archetype`



**Archetype**: Configuration for the background of a spatial view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(color_or_kind=None,*,color=None,kind=None)



Create a new instance of the Background archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| color_or_kind | Either a color for solid background color or kind of the background (seeBackgroundKind). If set,colorandkindmust not be set.TYPE:Rgba32Like\|BackgroundKindLike\| NoneDEFAULT:None |
| kind | The type of the background. Defaults to BackgroundKind.GradientDark.TYPE:BackgroundKindLike\| NoneDEFAULT:None |
| color | Color used for BackgroundKind.SolidColor.Defaults to White.TYPE:Rgba32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `Background`.



##### deffrom_fields(*,clear_unset=False,kind=None,color=None)classmethod



Update only some specific fields of a `Background`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| kind | The type of the background.TYPE:BackgroundKindLike\| NoneDEFAULT:None |
| color | Color used for the solid background type.TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classContainerBlueprint



Bases: `Archetype`



**Archetype**: The description of a container.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(container_kind,*,display_name=None,contents=None,col_shares=None,row_shares=None,active_tab=None,visible=None,grid_columns=None)



Create a new instance of the ContainerBlueprint archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| container_kind | The class of the view.TYPE:ContainerKindLike |
| display_name | The name of the container.TYPE:Utf8Like\| NoneDEFAULT:None |
| contents | ContainerIds orViewIds that are children of this container.TYPE:EntityPathArrayLike\| NoneDEFAULT:None |
| col_shares | The layout shares of each column in the container.Forcomponents.ContainerKind.Horizontalcontainers, the length of this list should always match the number of contents.Ignored forcomponents.ContainerKind.Verticalcontainers.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| row_shares | The layout shares of each row of the container.Forcomponents.ContainerKind.Verticalcontainers, the length of this list should always match the number of contents.Ignored forcomponents.ContainerKind.Horizontalcontainers.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| active_tab | Which tab is active.Only applies toTabscontainers.TYPE:EntityPathLike\| NoneDEFAULT:None |
| visible | Whether this container is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| grid_columns | How many columns this grid should have.If unset, the grid layout will be auto.Ignored forcomponents.ContainerKind.Horizontal/components.ContainerKind.Verticalcontainers.TYPE:UInt32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ContainerBlueprint`.



##### deffrom_fields(*,clear_unset=False,container_kind=None,display_name=None,contents=None,col_shares=None,row_shares=None,active_tab=None,visible=None,grid_columns=None)classmethod



Update only some specific fields of a `ContainerBlueprint`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| container_kind | The class of the view.TYPE:ContainerKindLike\| NoneDEFAULT:None |
| display_name | The name of the container.TYPE:Utf8Like\| NoneDEFAULT:None |
| contents | ContainerIds orViewIds that are children of this container.TYPE:EntityPathArrayLike\| NoneDEFAULT:None |
| col_shares | The layout shares of each column in the container.Forcomponents.ContainerKind.Horizontalcontainers, the length of this list should always match the number of contents.Ignored forcomponents.ContainerKind.Verticalcontainers.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| row_shares | The layout shares of each row of the container.Forcomponents.ContainerKind.Verticalcontainers, the length of this list should always match the number of contents.Ignored forcomponents.ContainerKind.Horizontalcontainers.TYPE:Float32ArrayLike\| NoneDEFAULT:None |
| active_tab | Which tab is active.Only applies toTabscontainers.TYPE:EntityPathLike\| NoneDEFAULT:None |
| visible | Whether this container is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |
| grid_columns | How many columns this grid should have.If unset, the grid layout will be auto.Ignored forcomponents.ContainerKind.Horizontal/components.ContainerKind.Verticalcontainers.TYPE:UInt32Like\| NoneDEFAULT:None |



#### classDataframeQuery



Bases: `DataframeQueryExt`, `Archetype`



**Archetype**: The query for the dataframe view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,timeline=None,filter_by_range=None,filter_is_not_null=None,apply_latest_at=False,select=None)



Create a new instance of the DataframeQuery archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline | The timeline for this query.TYPE:Utf8Like\| NoneDEFAULT:None |
| filter_by_range | If set, a range filter is applied.TYPE:tuple[TimeInt,TimeInt] \|FilterByRangeLike\| NoneDEFAULT:None |
| filter_is_not_null | If provided, the dataframe will only contain rows corresponding to timestamps at which an event was logged for the provided column.TYPE:ComponentColumnSelectorLike\| NoneDEFAULT:None |
| apply_latest_at | Should empty cells be filled with latest-at queries?TYPE:boolDEFAULT:False |
| select | Selected columns. If unset, all columns are selected.TYPE:list[ComponentColumnSelectorLike\|Utf8Like\|str] \| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `DataframeQuery`.



##### deffrom_fields(*,clear_unset=False,timeline=None,filter_by_range=None,filter_is_not_null=None,apply_latest_at=None,select=None)classmethod



Update only some specific fields of a `DataframeQuery`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| timeline | The timeline for this query.If unset, the timeline currently active on the time panel is used.TYPE:Utf8Like\| NoneDEFAULT:None |
| filter_by_range | If provided, only rows whose timestamp is within this range will be shown.Note: will be unset as soon astimelineis changed.TYPE:FilterByRangeLike\| NoneDEFAULT:None |
| filter_is_not_null | If provided, only show rows which contains a logged event for the specified component.TYPE:FilterIsNotNullLike\| NoneDEFAULT:None |
| apply_latest_at | Should empty cells be filled with latest-at queries?TYPE:BoolLike\| NoneDEFAULT:None |
| select | Selected columns. If unset, all columns are selected.TYPE:SelectedColumnsLike\| NoneDEFAULT:None |



#### classEntityBehavior



Bases: `Archetype`



**Archetype**: General visualization behavior of an entity.



TODO(#6541): Fields of this archetype currently only have an effect when logged in the blueprint store.

 Example

###### entity_behavior:



```
import rerun as rr
import rerun.blueprint as rrb

rr.init("rerun_example_entity_behavior", spawn=True)

# Use `EntityBehavior` to override visibility & interactivity of entities in the blueprint.
rr.send_blueprint(
    rrb.Spatial2DView(
        overrides={
            "hidden_subtree": rrb.EntityBehavior(visible=False),
            "hidden_subtree/not_hidden": rrb.EntityBehavior(visible=True),
            "non_interactive_subtree": rrb.EntityBehavior(interactive=False),
        }
    )
)

rr.log("hidden_subtree", rr.Points2D(positions=(0, 0), radii=0.5))
rr.log("hidden_subtree/also_hidden", rr.LineStrips2D(strips=[(-1, 1), (1, -1)]))
rr.log("hidden_subtree/not_hidden", rr.LineStrips2D(strips=[(1, 1), (-1, -1)]))
rr.log("non_interactive_subtree", rr.Boxes2D(centers=(0, 0), half_sizes=(1, 1)))
rr.log("non_interactive_subtree/also_non_interactive", rr.Boxes2D(centers=(0, 0), half_sizes=(0.5, 0.5)))
```

 ![](https://static.rerun.io/entity_behavior/831ccdaba769608408edb5edbfaaecf604b53d69/full.png)

##### def__init__(*,interactive=None,visible=None)



Create a new instance of the EntityBehavior archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| interactive | Whether the entity can be interacted with.This property is propagated down the entity hierarchy until another child entity setsinteractiveto a different value at which point propagation continues with that value instead.Defaults to parent'sinteractivevalue or true if there is no parent.TYPE:BoolLike\| NoneDEFAULT:None |
| visible | Whether the entity is visible.This property is propagated down the entity hierarchy until another child entity setsvisibleto a different value at which point propagation continues with that value instead.Defaults to parent'svisiblevalue or true if there is no parent.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `EntityBehavior`.



##### deffrom_fields(*,clear_unset=False,interactive=None,visible=None)classmethod



Update only some specific fields of a `EntityBehavior`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| interactive | Whether the entity can be interacted with.This property is propagated down the entity hierarchy until another child entity setsinteractiveto a different value at which point propagation continues with that value instead.Defaults to parent'sinteractivevalue or true if there is no parent.TYPE:BoolLike\| NoneDEFAULT:None |
| visible | Whether the entity is visible.This property is propagated down the entity hierarchy until another child entity setsvisibleto a different value at which point propagation continues with that value instead.Defaults to parent'svisiblevalue or true if there is no parent.TYPE:BoolLike\| NoneDEFAULT:None |



#### classEyeControls3D



Bases: `Archetype`



**Archetype**: The controls for the 3D eye in a spatial 3D view.



This configures the camera through which the 3D scene is viewed.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,kind=None,position=None,look_target=None,eye_up=None,speed=None,tracking_entity=None,spin_speed=None)



Create a new instance of the EyeControls3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| kind | The kind of the eye for the spatial 3D view.This controls how the eye movement behaves when the user interact with the view. Defaults to orbital.TYPE:Eye3DKindLike\| NoneDEFAULT:None |
| position | The cameras current position.TYPE:Vec3DLike\| NoneDEFAULT:None |
| look_target | The position the camera is currently looking at.If this is an orbital camera, this also is the center it orbits around.By default this is the center of the scene bounds.TYPE:Vec3DLike\| NoneDEFAULT:None |
| eye_up | The up-axis of the eye itself, in world-space.Initially, the up-axis of the eye will be the same as the up-axis of the scene (or +Z if the scene has no up axis defined).TYPE:Vec3DLike\| NoneDEFAULT:None |
| speed | Translation speed of the eye in the view (when using WASDQE keys to move in the 3D scene).The default depends on the control kind. For orbit cameras it is derived from the distance to the orbit center. For first person cameras it is derived from the scene size.TYPE:Float64Like\| NoneDEFAULT:None |
| tracking_entity | Currently tracked entity.If this is a camera, it takes over the camera pose, otherwise follows the entity.TYPE:EntityPathLike\| NoneDEFAULT:None |
| spin_speed | What speed, if any, the camera should spin around the eye-up axis.Defaults to zero, meaning no spinning.TYPE:Float64Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `EyeControls3D`.



##### deffrom_fields(*,clear_unset=False,kind=None,position=None,look_target=None,eye_up=None,speed=None,tracking_entity=None,spin_speed=None)classmethod



Update only some specific fields of a `EyeControls3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| kind | The kind of the eye for the spatial 3D view.This controls how the eye movement behaves when the user interact with the view. Defaults to orbital.TYPE:Eye3DKindLike\| NoneDEFAULT:None |
| position | The cameras current position.TYPE:Vec3DLike\| NoneDEFAULT:None |
| look_target | The position the camera is currently looking at.If this is an orbital camera, this also is the center it orbits around.By default this is the center of the scene bounds.TYPE:Vec3DLike\| NoneDEFAULT:None |
| eye_up | The up-axis of the eye itself, in world-space.Initially, the up-axis of the eye will be the same as the up-axis of the scene (or +Z if the scene has no up axis defined).TYPE:Vec3DLike\| NoneDEFAULT:None |
| speed | Translation speed of the eye in the view (when using WASDQE keys to move in the 3D scene).The default depends on the control kind. For orbit cameras it is derived from the distance to the orbit center. For first person cameras it is derived from the scene size.TYPE:Float64Like\| NoneDEFAULT:None |
| tracking_entity | Currently tracked entity.If this is a camera, it takes over the camera pose, otherwise follows the entity.TYPE:EntityPathLike\| NoneDEFAULT:None |
| spin_speed | What speed, if any, the camera should spin around the eye-up axis.Defaults to zero, meaning no spinning.TYPE:Float64Like\| NoneDEFAULT:None |



#### classForceCenter



Bases: `Archetype`



**Archetype**: Tries to move the center of mass of the graph to the origin.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,enabled=None,strength=None)



Create a new instance of the ForceCenter archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| enabled | Whether the center force is enabled.The center force tries to move the center of mass of the graph towards the origin.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ForceCenter`.



##### deffrom_fields(*,clear_unset=False,enabled=None,strength=None)classmethod



Update only some specific fields of a `ForceCenter`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| enabled | Whether the center force is enabled.The center force tries to move the center of mass of the graph towards the origin.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |



#### classForceCollisionRadius



Bases: `Archetype`



**Archetype**: Resolves collisions between the bounding circles, according to the radius of the nodes.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,enabled=None,strength=None,iterations=None)



Create a new instance of the ForceCollisionRadius archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| enabled | Whether the collision force is enabled.The collision force resolves collisions between nodes based on the bounding circle defined by their radius.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |
| iterations | Specifies how often this force should be applied per iteration.Increasing this parameter can lead to better results at the cost of longer computation time.TYPE:UInt64Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ForceCollisionRadius`.



##### deffrom_fields(*,clear_unset=False,enabled=None,strength=None,iterations=None)classmethod



Update only some specific fields of a `ForceCollisionRadius`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| enabled | Whether the collision force is enabled.The collision force resolves collisions between nodes based on the bounding circle defined by their radius.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |
| iterations | Specifies how often this force should be applied per iteration.Increasing this parameter can lead to better results at the cost of longer computation time.TYPE:UInt64Like\| NoneDEFAULT:None |



#### classForceLink



Bases: `Archetype`



**Archetype**: Aims to achieve a target distance between two nodes that are connected by an edge.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,enabled=None,distance=None,iterations=None)



Create a new instance of the ForceLink archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| enabled | Whether the link force is enabled.The link force aims to achieve a target distance between two nodes that are connected by one ore more edges.TYPE:BoolLike\| NoneDEFAULT:None |
| distance | The target distance between two nodes.TYPE:Float64Like\| NoneDEFAULT:None |
| iterations | Specifies how often this force should be applied per iteration.Increasing this parameter can lead to better results at the cost of longer computation time.TYPE:UInt64Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ForceLink`.



##### deffrom_fields(*,clear_unset=False,enabled=None,distance=None,iterations=None)classmethod



Update only some specific fields of a `ForceLink`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| enabled | Whether the link force is enabled.The link force aims to achieve a target distance between two nodes that are connected by one ore more edges.TYPE:BoolLike\| NoneDEFAULT:None |
| distance | The target distance between two nodes.TYPE:Float64Like\| NoneDEFAULT:None |
| iterations | Specifies how often this force should be applied per iteration.Increasing this parameter can lead to better results at the cost of longer computation time.TYPE:UInt64Like\| NoneDEFAULT:None |



#### classForceManyBody



Bases: `Archetype`



**Archetype**: A force between each pair of nodes that ressembles an electrical charge.



If `strength` is smaller than 0, it pushes nodes apart, if it is larger than 0 it pulls them together.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,enabled=None,strength=None)



Create a new instance of the ForceManyBody archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| enabled | Whether the many body force is enabled.The many body force is applied on each pair of nodes in a way that ressembles an electrical charge. If the strength is smaller than 0, it pushes nodes apart; if it is larger than 0, it pulls them together.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.Ifstrengthis smaller than 0, it pushes nodes apart, if it is larger than 0 it pulls them together.TYPE:Float64Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ForceManyBody`.



##### deffrom_fields(*,clear_unset=False,enabled=None,strength=None)classmethod



Update only some specific fields of a `ForceManyBody`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| enabled | Whether the many body force is enabled.The many body force is applied on each pair of nodes in a way that ressembles an electrical charge. If the strength is smaller than 0, it pushes nodes apart; if it is larger than 0, it pulls them together.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.Ifstrengthis smaller than 0, it pushes nodes apart, if it is larger than 0 it pulls them together.TYPE:Float64Like\| NoneDEFAULT:None |



#### classForcePosition



Bases: `Archetype`



**Archetype**: Similar to gravity, this force pulls nodes towards a specific position.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,enabled=None,strength=None,position=None)



Create a new instance of the ForcePosition archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| enabled | Whether the position force is enabled.The position force pulls nodes towards a specific position, similar to gravity.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |
| position | The position where the nodes should be pulled towards.TYPE:Vec2DLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ForcePosition`.



##### deffrom_fields(*,clear_unset=False,enabled=None,strength=None,position=None)classmethod



Update only some specific fields of a `ForcePosition`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| enabled | Whether the position force is enabled.The position force pulls nodes towards a specific position, similar to gravity.TYPE:BoolLike\| NoneDEFAULT:None |
| strength | The strength of the force.TYPE:Float64Like\| NoneDEFAULT:None |
| position | The position where the nodes should be pulled towards.TYPE:Vec2DLike\| NoneDEFAULT:None |



#### classGraphBackground



Bases: `Archetype`



**Archetype**: Configuration of a background in a graph view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,color=None)



Create a new instance of the GraphBackground archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| color | Color used for the background.TYPE:Rgba32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `GraphBackground`.



##### deffrom_fields(*,clear_unset=False,color=None)classmethod



Update only some specific fields of a `GraphBackground`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| color | Color used for the background.TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classLineGrid3D



Bases: `LineGrid3DExt`, `Archetype`



**Archetype**: Configuration for the 3D line grid.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(visible=None,*,spacing=None,plane=None,stroke_width=None,color=None)



Create a new instance of the LineGrid3D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| visible | Whether the grid is visible.Defaults to true.TYPE:BoolLike\| NoneDEFAULT:None |
| spacing | Space between grid lines spacing of one line to the next in scene units.As you zoom out, successively only every tenth line is shown. This controls the closest zoom level.TYPE:Float32Like\| NoneDEFAULT:None |
| plane | In what plane the grid is drawn.Defaults to whatever plane is determined as the plane at zero units up/down as defined bycomponents.ViewCoordinatesif present.TYPE:Plane3DLike\| NoneDEFAULT:None |
| stroke_width | How thick the lines should be in ui units.Default is 1.0 ui unit.TYPE:Float32Like\| NoneDEFAULT:None |
| color | Color used for the grid.Transparency via alpha channel is supported. Defaults to a slightly transparent light gray.TYPE:Rgba32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `LineGrid3D`.



##### deffrom_fields(*,clear_unset=False,visible=None,spacing=None,plane=None,stroke_width=None,color=None)classmethod



Update only some specific fields of a `LineGrid3D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| visible | Whether the grid is visible.Defaults to true.TYPE:BoolLike\| NoneDEFAULT:None |
| spacing | Space between grid lines spacing of one line to the next in scene units.As you zoom out, successively only every tenth line is shown. This controls the closest zoom level.TYPE:Float32Like\| NoneDEFAULT:None |
| plane | In what plane the grid is drawn.Defaults to whatever plane is determined as the plane at zero units up/down as defined bycomponents.ViewCoordinatesif present.TYPE:Plane3DLike\| NoneDEFAULT:None |
| stroke_width | How thick the lines should be in ui units.Default is 1.0 ui unit.TYPE:Float32Like\| NoneDEFAULT:None |
| color | Color used for the grid.Transparency via alpha channel is supported. Defaults to a slightly transparent light gray.TYPE:Rgba32Like\| NoneDEFAULT:None |



#### classMapBackground



Bases: `Archetype`



**Archetype**: Configuration for the background map of the map view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(provider)



Create a new instance of the MapBackground archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| provider | Map provider and style to use.Note: Requires a Mapbox API key in theRERUN_MAPBOX_ACCESS_TOKENenvironment variable.TYPE:MapProviderLike |



##### defcleared()classmethod



Clear all the fields of a `MapBackground`.



##### deffrom_fields(*,clear_unset=False,provider=None)classmethod



Update only some specific fields of a `MapBackground`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| provider | Map provider and style to use.Note: Requires a Mapbox API key in theRERUN_MAPBOX_ACCESS_TOKENenvironment variable.TYPE:MapProviderLike\| NoneDEFAULT:None |



#### classMapZoom



Bases: `Archetype`



**Archetype**: Configuration of the map view zoom level.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(zoom)



Create a new instance of the MapZoom archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| zoom | Zoom level for the map.Zoom level follow theOpenStreetMapdefinition.TYPE:Float64Like |



##### defcleared()classmethod



Clear all the fields of a `MapZoom`.



##### deffrom_fields(*,clear_unset=False,zoom=None)classmethod



Update only some specific fields of a `MapZoom`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| zoom | Zoom level for the map.Zoom level follow theOpenStreetMapdefinition.TYPE:Float64Like\| NoneDEFAULT:None |



#### classNearClipPlane



Bases: `Archetype`



**Archetype**: Controls the distance to the near clip plane in 3D scene units.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(near_clip_plane)



Create a new instance of the NearClipPlane archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| near_clip_plane | Controls the distance to the near clip plane in 3D scene units.Content closer than this distance will not be visible.TYPE:Float32Like |



##### defcleared()classmethod



Clear all the fields of a `NearClipPlane`.



##### deffrom_fields(*,clear_unset=False,near_clip_plane=None)classmethod



Update only some specific fields of a `NearClipPlane`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| near_clip_plane | Controls the distance to the near clip plane in 3D scene units.Content closer than this distance will not be visible.TYPE:Float32Like\| NoneDEFAULT:None |



#### classPanelBlueprint



Bases: `Archetype`



**Archetype**: Shared state for the 3 collapsible panels.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,state=None)



Create a new instance of the PanelBlueprint archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| state | Current state of the panel.TYPE:PanelStateLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `PanelBlueprint`.



##### deffrom_fields(*,clear_unset=False,state=None)classmethod



Update only some specific fields of a `PanelBlueprint`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| state | Current state of the panel.TYPE:PanelStateLike\| NoneDEFAULT:None |



#### classPlotBackground



Bases: `Archetype`



**Archetype**: Configuration of a background in a plot view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,color=None,show_grid=None)



Create a new instance of the PlotBackground archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| color | Color used for the background.TYPE:Rgba32Like\| NoneDEFAULT:None |
| show_grid | Should the grid be drawn?TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `PlotBackground`.



##### deffrom_fields(*,clear_unset=False,color=None,show_grid=None)classmethod



Update only some specific fields of a `PlotBackground`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| color | Color used for the background.TYPE:Rgba32Like\| NoneDEFAULT:None |
| show_grid | Should the grid be drawn?TYPE:BoolLike\| NoneDEFAULT:None |



#### classPlotLegend



Bases: `PlotLegendExt`, `Archetype`



**Archetype**: Configuration for the legend of a plot.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(corner=None,*,visible=None)



Create a new instance of the PlotLegend archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| corner | To what corner the legend is aligned.Defaults to the right bottom corner.TYPE:Corner2DLike\| NoneDEFAULT:None |
| visible | Whether the legend is shown at all.True by default.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `PlotLegend`.



##### deffrom_fields(*,clear_unset=False,corner=None,visible=None)classmethod



Update only some specific fields of a `PlotLegend`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| corner | To what corner the legend is aligned.Defaults to the right bottom corner.TYPE:Corner2DLike\| NoneDEFAULT:None |
| visible | Whether the legend is shown at all.True by default.TYPE:BoolLike\| NoneDEFAULT:None |



#### classScalarAxis



Bases: `Archetype`



**Archetype**: Configuration for the scalar (Y) axis of a plot.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,range=None,zoom_lock=None)



Create a new instance of the ScalarAxis archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| range | The range of the axis.If unset, the range well be automatically determined based on the queried data.TYPE:Range1DLike\| NoneDEFAULT:None |
| zoom_lock | If enabled, the Y axis range will remain locked to the specified range when zooming.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ScalarAxis`.



##### deffrom_fields(*,clear_unset=False,range=None,zoom_lock=None)classmethod



Update only some specific fields of a `ScalarAxis`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| range | The range of the axis.If unset, the range well be automatically determined based on the queried data.TYPE:Range1DLike\| NoneDEFAULT:None |
| zoom_lock | If enabled, the Y axis range will remain locked to the specified range when zooming.TYPE:BoolLike\| NoneDEFAULT:None |



#### classSpatialInformation



Bases: `Archetype`



**Archetype**: This configures extra drawing config for the 3D view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(target_frame,*,show_axes=None,show_bounding_box=None)



Create a new instance of the SpatialInformation archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| target_frame | The target reference frame for all transformations.Defaults to the coordinate frame used by the space origin entity.TYPE:Utf8Like |
| show_axes | Whether axes should be shown at the origin.TYPE:BoolLike\| NoneDEFAULT:None |
| show_bounding_box | Whether the bounding box should be shown.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `SpatialInformation`.



##### deffrom_fields(*,clear_unset=False,target_frame=None,show_axes=None,show_bounding_box=None)classmethod



Update only some specific fields of a `SpatialInformation`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| target_frame | The target reference frame for all transformations.Defaults to the coordinate frame used by the space origin entity.TYPE:Utf8Like\| NoneDEFAULT:None |
| show_axes | Whether axes should be shown at the origin.TYPE:BoolLike\| NoneDEFAULT:None |
| show_bounding_box | Whether the bounding box should be shown.TYPE:BoolLike\| NoneDEFAULT:None |



#### classTensorScalarMapping



Bases: `Archetype`



**Archetype**: Configures how tensor scalars are mapped to color.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,mag_filter=None,colormap=None,gamma=None)



Create a new instance of the TensorScalarMapping archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| mag_filter | Filter used when zooming in on the tensor.Note that the filter is applied to the scalar valuesbeforethey are mapped to color.TYPE:MagnificationFilterLike\| NoneDEFAULT:None |
| colormap | How scalar values map to colors.TYPE:ColormapLike\| NoneDEFAULT:None |
| gamma | Gamma exponent applied to normalized values before mapping to color.Raises the normalized values to the power of this value before mapping to color. Acts like an inverse brightness. Defaults to 1.0.The final value for display is set as:colormap( ((value - data_display_range.min) / (data_display_range.max - data_display_range.min)) ** gamma )TYPE:Float32Like\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TensorScalarMapping`.



##### deffrom_fields(*,clear_unset=False,mag_filter=None,colormap=None,gamma=None)classmethod



Update only some specific fields of a `TensorScalarMapping`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| mag_filter | Filter used when zooming in on the tensor.Note that the filter is applied to the scalar valuesbeforethey are mapped to color.TYPE:MagnificationFilterLike\| NoneDEFAULT:None |
| colormap | How scalar values map to colors.TYPE:ColormapLike\| NoneDEFAULT:None |
| gamma | Gamma exponent applied to normalized values before mapping to color.Raises the normalized values to the power of this value before mapping to color. Acts like an inverse brightness. Defaults to 1.0.The final value for display is set as:colormap( ((value - data_display_range.min) / (data_display_range.max - data_display_range.min)) ** gamma )TYPE:Float32Like\| NoneDEFAULT:None |



#### classTensorSliceSelection



Bases: `Archetype`



**Archetype**: Specifies a 2D slice of a tensor.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,width=None,height=None,indices=None,slider=None)



Create a new instance of the TensorSliceSelection archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| width | Which dimension to map to width.If not specified, the height will be determined automatically based on the name and index of the dimension.TYPE:TensorDimensionSelectionLike\| NoneDEFAULT:None |
| height | Which dimension to map to height.If not specified, the height will be determined automatically based on the name and index of the dimension.TYPE:TensorDimensionSelectionLike\| NoneDEFAULT:None |
| indices | Selected indices for all other dimensions.If any of the here listed dimensions is equal towidthorheight, it will be ignored.TYPE:TensorDimensionIndexSelectionArrayLike\| NoneDEFAULT:None |
| slider | Any dimension listed here will have a slider for the index.Edits to the sliders will directly manipulate dimensions on theindiceslist. If any of the here listed dimensions is equal towidthorheight, it will be ignored. If not specified, adds slides for any dimension inindices.TYPE:TensorDimensionIndexSliderArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TensorSliceSelection`.



##### deffrom_fields(*,clear_unset=False,width=None,height=None,indices=None,slider=None)classmethod



Update only some specific fields of a `TensorSliceSelection`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| width | Which dimension to map to width.If not specified, the height will be determined automatically based on the name and index of the dimension.TYPE:TensorDimensionSelectionLike\| NoneDEFAULT:None |
| height | Which dimension to map to height.If not specified, the height will be determined automatically based on the name and index of the dimension.TYPE:TensorDimensionSelectionLike\| NoneDEFAULT:None |
| indices | Selected indices for all other dimensions.If any of the here listed dimensions is equal towidthorheight, it will be ignored.TYPE:TensorDimensionIndexSelectionArrayLike\| NoneDEFAULT:None |
| slider | Any dimension listed here will have a slider for the index.Edits to the sliders will directly manipulate dimensions on theindiceslist. If any of the here listed dimensions is equal towidthorheight, it will be ignored. If not specified, adds slides for any dimension inindices.TYPE:TensorDimensionIndexSliderArrayLike\| NoneDEFAULT:None |



#### classTensorViewFit



Bases: `TensorViewFitExt`, `Archetype`



**Archetype**: Configures how a selected tensor slice is shown on screen.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(scaling=None)



Create a new instance of the TensorViewFit archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| scaling | How the image is scaled to fit the view.TYPE:ViewFitLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TensorViewFit`.



##### deffrom_fields(*,clear_unset=False,scaling=None)classmethod



Update only some specific fields of a `TensorViewFit`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| scaling | How the image is scaled to fit the view.TYPE:ViewFitLike\| NoneDEFAULT:None |



#### classTextLogColumns



Bases: `Archetype`



**Archetype**: Configuration of the text log columns.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,timeline_columns=None,text_log_columns=None)



Create a new instance of the TextLogColumns archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| timeline_columns | What timeline columns to show.Defaults to displaying all timelines.TYPE:TimelineColumnArrayLike\| NoneDEFAULT:None |
| text_log_columns | All columns to be displayed.Defaults to showing all text log column kinds in the order of the enum.TYPE:TextLogColumnArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TextLogColumns`.



##### deffrom_fields(*,clear_unset=False,timeline_columns=None,text_log_columns=None)classmethod



Update only some specific fields of a `TextLogColumns`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| timeline_columns | What timeline columns to show.Defaults to displaying all timelines.TYPE:TimelineColumnArrayLike\| NoneDEFAULT:None |
| text_log_columns | All columns to be displayed.Defaults to showing all text log column kinds in the order of the enum.TYPE:TextLogColumnArrayLike\| NoneDEFAULT:None |



#### classTextLogFormat



Bases: `Archetype`



**Archetype**: Configuration of the text log rows.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,monospace_body=None)



Create a new instance of the TextLogFormat archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| monospace_body | Whether to use a monospace font for the log message body.Defaults to not being enabled.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TextLogFormat`.



##### deffrom_fields(*,clear_unset=False,monospace_body=None)classmethod



Update only some specific fields of a `TextLogFormat`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| monospace_body | Whether to use a monospace font for the log message body.Defaults to not being enabled.TYPE:BoolLike\| NoneDEFAULT:None |



#### classTextLogRows



Bases: `Archetype`



**Archetype**: Configuration of the text log rows.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,filter_by_log_level=None)



Create a new instance of the TextLogRows archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| filter_by_log_level | Log levels to display.Defaults to showing all logged levels.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TextLogRows`.



##### deffrom_fields(*,clear_unset=False,filter_by_log_level=None)classmethod



Update only some specific fields of a `TextLogRows`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| filter_by_log_level | Log levels to display.Defaults to showing all logged levels.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



#### classTimeAxis



Bases: `Archetype`



**Archetype**: Configuration for the time (X) axis of a plot.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,link=None,view_range=None,zoom_lock=None)



Create a new instance of the TimeAxis archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| link | How should the horizontal/X/time axis be linked across multiple plots?Linking with global will ignoreview_range.TYPE:LinkAxisLike\| NoneDEFAULT:None |
| view_range | The view range of the horizontal/X/time axis.TYPE:TimeRangeLike\| NoneDEFAULT:None |
| zoom_lock | If enabled, the X axis range will remain locked to the specified range when zooming.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TimeAxis`.



##### deffrom_fields(*,clear_unset=False,link=None,view_range=None,zoom_lock=None)classmethod



Update only some specific fields of a `TimeAxis`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| link | How should the horizontal/X/time axis be linked across multiple plots?Linking with global will ignoreview_range.TYPE:LinkAxisLike\| NoneDEFAULT:None |
| view_range | The view range of the horizontal/X/time axis.TYPE:TimeRangeLike\| NoneDEFAULT:None |
| zoom_lock | If enabled, the X axis range will remain locked to the specified range when zooming.TYPE:BoolLike\| NoneDEFAULT:None |



#### classTimePanelBlueprint



Bases: `Archetype`



**Archetype**: Time panel specific state.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,state=None,timeline=None,playback_speed=None,fps=None,play_state=None,loop_mode=None,time_selection=None)



Create a new instance of the TimePanelBlueprint archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| state | Current state of the panel.TYPE:PanelStateLike\| NoneDEFAULT:None |
| timeline | What timeline the panel is on.TYPE:Utf8Like\| NoneDEFAULT:None |
| playback_speed | A time playback speed multiplier.TYPE:Float64Like\| NoneDEFAULT:None |
| fps | Frames per second. Only applicable for sequence timelines.TYPE:Float64Like\| NoneDEFAULT:None |
| play_state | If the time is currently paused, playing, or following.Defaults to either playing or following, depending on the data source.TYPE:PlayStateLike\| NoneDEFAULT:None |
| loop_mode | How the time should loop. A selection loop only works if there is also atime_selectionpassed.Defaults to off.TYPE:LoopModeLike\| NoneDEFAULT:None |
| time_selection | Selects a range of time on the time panel.TYPE:AbsoluteTimeRangeLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `TimePanelBlueprint`.



##### deffrom_fields(*,clear_unset=False,state=None,timeline=None,playback_speed=None,fps=None,play_state=None,loop_mode=None,time_selection=None)classmethod



Update only some specific fields of a `TimePanelBlueprint`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| state | Current state of the panel.TYPE:PanelStateLike\| NoneDEFAULT:None |
| timeline | What timeline the panel is on.TYPE:Utf8Like\| NoneDEFAULT:None |
| playback_speed | A time playback speed multiplier.TYPE:Float64Like\| NoneDEFAULT:None |
| fps | Frames per second. Only applicable for sequence timelines.TYPE:Float64Like\| NoneDEFAULT:None |
| play_state | If the time is currently paused, playing, or following.Defaults to either playing or following, depending on the data source.TYPE:PlayStateLike\| NoneDEFAULT:None |
| loop_mode | How the time should loop. A selection loop only works if there is also atime_selectionpassed.Defaults to off.TYPE:LoopModeLike\| NoneDEFAULT:None |
| time_selection | Selects a range of time on the time panel.TYPE:AbsoluteTimeRangeLike\| NoneDEFAULT:None |



#### classViewBlueprint



Bases: `Archetype`



**Archetype**: The description of a single view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(class_identifier,*,display_name=None,space_origin=None,visible=None)



Create a new instance of the ViewBlueprint archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| class_identifier | The class of the view.TYPE:Utf8Like |
| display_name | The name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| space_origin | The "anchor point" of this view.In other words, the coordinate frame at this entity becomes the reference frame of the view.Defaults to the root path '/' if not specified.The transform at this path forms the reference point for all scene->world transforms in this view. I.e. the position of this entity path in space forms the origin of the coordinate system in this view. Furthermore, this is the primary indicator for heuristics on what entities we show in this view.TYPE:EntityPathLike\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ViewBlueprint`.



##### deffrom_fields(*,clear_unset=False,class_identifier=None,display_name=None,space_origin=None,visible=None)classmethod



Update only some specific fields of a `ViewBlueprint`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| class_identifier | The class of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| display_name | The name of the view.TYPE:Utf8Like\| NoneDEFAULT:None |
| space_origin | The "anchor point" of this view.In other words, the coordinate frame at this entity becomes the reference frame of the view.Defaults to the root path '/' if not specified.The transform at this path forms the reference point for all scene->world transforms in this view. I.e. the position of this entity path in space forms the origin of the coordinate system in this view. Furthermore, this is the primary indicator for heuristics on what entities we show in this view.TYPE:EntityPathLike\| NoneDEFAULT:None |
| visible | Whether this view is visible.Defaults to true if not specified.TYPE:BoolLike\| NoneDEFAULT:None |



#### classViewContents



Bases: `Archetype`



**Archetype**: The contents of a `View`.



The contents are found by combining a collection of `QueryExpression`s.



```
+ /world/**           # add everythingâ¦
- /world/roads/**     # â¦but remove all roadsâ¦
+ /world/roads/main   # â¦but show main road
```



If there is multiple matching rules, the most specific rule wins.
If there are multiple rules of the same specificity, the last one wins.
If no rules match, the path is excluded.



Specifying a path without a `+` or `-` prefix is equivalent to `+`:

```
/world/**           # add everythingâ¦
- /world/roads/**   # â¦but remove all roadsâ¦
/world/roads/main   # â¦but show main road
```



The `/**` suffix matches the whole subtree, i.e. self and any child, recursively
(`/world/**` matches both `/world` and `/world/car/driver`).
Other uses of `*` are not (yet) supported.



Internally, `EntityPathFilter` sorts the rule by entity path, with recursive coming before non-recursive.
This means the last matching rule is also the most specific one. For instance:

```
+ /world/**
- /world
- /world/car/**
+ /world/car/driver
```



The last rule matching `/world/car/driver` is `+ /world/car/driver`, so it is included.
The last rule matching `/world/car/hood` is `- /world/car/**`, so it is excluded.
The last rule matching `/world` is `- /world`, so it is excluded.
The last rule matching `/world/house` is `+ /world/**`, so it is included.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(query)



Create a new instance of the ViewContents archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| query | TheQueryExpressionthat populates the contents for the view.They determine which entities are part of the view.TYPE:Utf8ArrayLike |



##### defcleared()classmethod



Clear all the fields of a `ViewContents`.



##### deffrom_fields(*,clear_unset=False,query=None)classmethod



Update only some specific fields of a `ViewContents`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| query | TheQueryExpressionthat populates the contents for the view.They determine which entities are part of the view.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |



#### classViewportBlueprint



Bases: `Archetype`



**Archetype**: The top-level description of the viewport.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,root_container=None,maximized=None,auto_layout=None,auto_views=None,past_viewer_recommendations=None)



Create a new instance of the ViewportBlueprint archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| root_container | The layout of the viewsTYPE:UuidLike\| NoneDEFAULT:None |
| maximized | Show one tab as maximized?TYPE:UuidLike\| NoneDEFAULT:None |
| auto_layout | Whether the viewport layout is determined automatically.Iftrue, the container layout will be reset whenever a new view is added or removed. This defaults tofalseand is automatically set tofalsewhen there is user determined layout.TYPE:BoolLike\| NoneDEFAULT:None |
| auto_views | Whether or not views should be created automatically.Iftrue, the viewer will only add views that it hasn't considered previously (as identified bypast_viewer_recommendations) and which aren't deemed redundant to existing views. This defaults tofalseand is automatically set tofalsewhen the user adds views manually in the viewer.TYPE:BoolLike\| NoneDEFAULT:None |
| past_viewer_recommendations | Hashes of all recommended views the viewer has already added and that should not be added again.This is an internal field and should not be set usually. If you want the viewer from stopping to add views, you should setauto_viewstofalse.The viewer uses this to determine whether it should keep adding views.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `ViewportBlueprint`.



##### deffrom_fields(*,clear_unset=False,root_container=None,maximized=None,auto_layout=None,auto_views=None,past_viewer_recommendations=None)classmethod



Update only some specific fields of a `ViewportBlueprint`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| root_container | The layout of the viewsTYPE:UuidLike\| NoneDEFAULT:None |
| maximized | Show one tab as maximized?TYPE:UuidLike\| NoneDEFAULT:None |
| auto_layout | Whether the viewport layout is determined automatically.Iftrue, the container layout will be reset whenever a new view is added or removed. This defaults tofalseand is automatically set tofalsewhen there is user determined layout.TYPE:BoolLike\| NoneDEFAULT:None |
| auto_views | Whether or not views should be created automatically.Iftrue, the viewer will only add views that it hasn't considered previously (as identified bypast_viewer_recommendations) and which aren't deemed redundant to existing views. This defaults tofalseand is automatically set tofalsewhen the user adds views manually in the viewer.TYPE:BoolLike\| NoneDEFAULT:None |
| past_viewer_recommendations | Hashes of all recommended views the viewer has already added and that should not be added again.This is an internal field and should not be set usually. If you want the viewer from stopping to add views, you should setauto_viewstofalse.The viewer uses this to determine whether it should keep adding views.TYPE:UInt64ArrayLike\| NoneDEFAULT:None |



#### classVisibleTimeRanges



Bases: `VisibleTimeRangesExt`, `Archetype`



**Archetype**: Configures what range of each timeline is shown on a view.



Whenever no visual time range applies, queries are done with "latest-at" semantics.
This means that the view will, starting from the time cursor position,
query the latest data available for each component type.



The default visual time range depends on the type of view this property applies to:
- For time series views, the default is to show the entire timeline.
- For any other view, the default is to apply latest-at semantics.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(ranges=None,*,timeline=None,range=None,start=None,end=None)



Create a new instance of the VisibleTimeRanges archetype.



Either from a list of `VisibleTimeRange` objects, or from a single `timeline`-name plus either `range` or `start` & `end`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| ranges | The time ranges to show for each timeline unless specified otherwise on a per-entity basis.If a timeline is listed twice, a warning will be issued and the first entry will be used.TYPE:VisibleTimeRangeArrayLike\| NoneDEFAULT:None |
| timeline | The name of the timeline to show. Mutually exclusive withranges.TYPE:Utf8Like\| NoneDEFAULT:None |
| range | The range of the timeline to show. Requirestimelineto be set. Mutually exclusive withstart&end.TYPE:TimeRangeLike\| NoneDEFAULT:None |
| start | The start of the timeline to show. Requirestimelineto be set. Mutually exclusive withrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |
| end | The end of the timeline to show. Requirestimelineto be set. Mutually exclusive withrange.TYPE:TimeRangeBoundary\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `VisibleTimeRanges`.



##### deffrom_fields(*,clear_unset=False,ranges=None)classmethod



Update only some specific fields of a `VisibleTimeRanges`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| ranges | The time ranges to show for each timeline unless specified otherwise on a per-entity basis.If a timeline is specified more than once, the first entry will be used.TYPE:VisibleTimeRangeArrayLike\| NoneDEFAULT:None |



#### classVisualBounds2D



Bases: `VisualBounds2DExt`, `Archetype`



**Archetype**: Controls the visual bounds of a 2D view.



Everything within these bounds are guaranteed to be visible.
Somethings outside of these bounds may also be visible due to letterboxing.



If no visual bounds are set, it will be determined automatically,
based on the bounding-box of the data or other camera information present in the view.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(*,x_range=None,y_range=None)



Create a new instance of the VisualBounds2D archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| x_range | The minimum visible range of the X-axis (usually left and right bounds).TYPE:Range1DLike\| NoneDEFAULT:None |
| y_range | The minimum visible range of the Y-axis (usually left and right bounds).TYPE:Range1DLike\| NoneDEFAULT:None |



##### defcleared()classmethod



Clear all the fields of a `VisualBounds2D`.



##### deffrom_fields(*,clear_unset=False,range=None)classmethod



Update only some specific fields of a `VisualBounds2D`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| range | Controls the visible range of a 2D view.Use this to control pan & zoom of the view.TYPE:Range2DLike\| NoneDEFAULT:None |



#### classVisualizerOverrides



Bases: `Archetype`



**Archetype**: Override the visualizers for an entity.



This archetype is a stop-gap mechanism based on the current implementation details
of the visualizer system. It is not intended to be a long-term solution, but provides
enough utility to be useful in the short term.



**NOTE**: Rerun `v0.24` changed the behavior of archetypes.VisualizerOverrides, so that currently they only
work with time series views. We plan to bring this feature for all views in future versions.



This can only be used as part of blueprints. It will have no effect if used
in a regular entity.



â ï¸ **This type isunstableand may change significantly in a way that the data won't be backwards compatible.**



##### def__init__(ranges)



Create a new instance of the VisualizerOverrides archetype.



| PARAMETER | DESCRIPTION |
| --- | --- |
| ranges | Names of the visualizers that should be active.TYPE:Utf8ArrayLike |



##### defcleared()classmethod



Clear all the fields of a `VisualizerOverrides`.



##### deffrom_fields(*,clear_unset=False,ranges=None)classmethod



Update only some specific fields of a `VisualizerOverrides`.



| PARAMETER | DESCRIPTION |
| --- | --- |
| clear_unset | If true, all unspecified fields will be explicitly cleared.TYPE:boolDEFAULT:False |
| ranges | Names of the visualizers that should be active.TYPE:Utf8ArrayLike\| NoneDEFAULT:None |