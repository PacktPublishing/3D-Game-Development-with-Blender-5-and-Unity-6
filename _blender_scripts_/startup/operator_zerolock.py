import bpy


def main(context):
    for ob in context.selected_objects:
        ob.location.zero()
        
        for i in range(3):
            ob.lock_location[i] = True
            ob.lock_rotation[i] = True
            ob.lock_scale[i] = True
        ob.lock_rotation_w = True


class ZeroLockOperator(bpy.types.Operator):
    """Clear objects location and lock transforms"""
    bl_idname = "object.b2u_zerolock_operator"
    bl_label = "Lock at Origin"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(ZeroLockOperator.bl_idname, text=ZeroLockOperator.bl_label)


# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access).
def register():
    bpy.utils.register_class(ZeroLockOperator)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)


def unregister():
    bpy.utils.unregister_class(ZeroLockOperator)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)


if __name__ == "__main__":
    register()

    # Test call.
    #bpy.ops.object.simple_operator()
