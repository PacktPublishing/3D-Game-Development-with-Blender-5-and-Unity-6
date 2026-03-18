# import the required modules
import bpy
from bpy_extras import object_utils
from bpy_extras.object_utils import AddObjectHelper

# declare a new command
class AddEmpty(bpy.types.Operator, AddObjectHelper):
    """Add rotated empty"""
    bl_idname = "object.y_up_add"
    bl_label = "Y-Up axis"
    def execute(self, context):
        # create a new object
        selected_objects  = list(context.selected_objects)
        ob = object_utils.object_data_add(context,
                                          None,
                                          operator=self,
                                          name='Empty')
        # change display and rotation
        # 90 degrees equals pi/2, i.e. 1.5708...
        ob.empty_display_type = 'ARROWS'
        ob.rotation_euler.x = 1.5708
        # lock transforms
        for i in range(3):
            ob.lock_location[i] = True
            ob.lock_rotation[i] = True
            ob.lock_scale[i] = True
        ob.lock_rotation_w = True
        
        for sel_ob in selected_objects:
            sel_ob.parent = ob
        
        # exit with success
        return {'FINISHED'}
# declare menu entry
def menu_func(self, context):
    self.layout.operator(AddEmpty.bl_idname,
                         icon='EMPTY_ARROWS')

# that’s it, declare load procedure
def register():
    bpy.utils.register_class(AddEmpty)
    bpy.types.VIEW3D_MT_empty_add.append(menu_func)
# and unload procedure
def unregister():
    bpy.types.VIEW3D_MT_empty_add.remove(menu_func)
    bpy.utils.unregister_class(AddEmpty)
# actually load
if __name__ == "__main__":
    register()
