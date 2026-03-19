import bpy


def exclude_collection(name, exclude_it):
    """Set exlude status of a first level collection of
    given `name` to `exclude_it`.
    IMPORTANT: Doesn’t check sublevel collections"""
    layer = bpy.context.view_layer.layer_collection
    try:
        coll = layer.children[name]
    except KeyError:
        # collection not found, exit
        return
    # set the exclude flag
    coll.exclude = exclude_it
