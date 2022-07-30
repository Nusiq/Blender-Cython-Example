import bpy

from .hello import hello_cython
from .hello2 import hello_cython2

bl_info = {
    "name" : "Cython Test",
    "author" : "Artur D.",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

# Model exporter
class CYTHON_TEST_OT_MyOperator(bpy.types.Operator):
    bl_idname = "cython_test.my_operator"
    bl_label = "Cython Test: My Operator"
    bl_options = {'REGISTER'}
    bl_description = "This is just a test Cython operator"

    def execute(self, context):
        hello_cython()
        hello_cython2()
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(
        CYTHON_TEST_OT_MyOperator.bl_idname,
        text=CYTHON_TEST_OT_MyOperator.bl_label)

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.utils.register_class(CYTHON_TEST_OT_MyOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(CYTHON_TEST_OT_MyOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
