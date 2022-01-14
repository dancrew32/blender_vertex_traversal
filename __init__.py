import bpy


bl_info = {
    "name": "Vertex Traversal",
    "blender": (3, 0, 0),
    "category": "3D View",
}


def set_object_mode():
    bpy.ops.object.mode_set(mode='OBJECT')


def set_edit_mode():
    bpy.ops.object.mode_set(mode='EDIT')


def deselect():
    bpy.ops.mesh.select_all(action='DESELECT')


def get_active_object():
    return bpy.context.active_object


def get_vertex_data():
    set_object_mode()
    obj = get_active_object()
    set_edit_mode()
    bpy.ops.mesh.select_mode(type='VERT')
    current_vertex_index = 0
    vertices_length = len(obj.data.vertices)
    for key, value in obj.data.vertices.items():
        if value.select:
            current_vertex_index = key   
    return {'current_vertex_index': current_vertex_index,
            'vertices_length': vertices_length}


def get_next_vertex():
    data = get_vertex_data()
    return 0 if data['current_vertex_index'] + 1 >= data['vertices_length'] else data['current_vertex_index'] + 1


def get_prev_vertex():
    data = get_vertex_data()
    return data['vertices_length'] - 1 if data['current_vertex_index'] - 1 < 0 else data['current_vertex_index'] - 1


def select_next_vertex():
    obj = get_active_object()
    deselect()
    set_object_mode()
    next_vertex_index = get_next_vertex()
    obj.data.vertices[next_vertex_index].select = True
    set_edit_mode()
  

def select_prev_vertex():
    obj = get_active_object()
    deselect()
    set_object_mode()
    prev_vertex_index = get_prev_vertex()
    obj.data.vertices[prev_vertex_index].select = True
    set_edit_mode()


class Panel(bpy.types.Panel):
    """Show Vertex Traversal side panel in 3D View"""

    bl_idname = "VERTEX_TRAVERSAL_PT_PANEL"
    bl_label = "Vertex Traversal"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vertex Traversal"

    @classmethod
    def poll(cls, context):
        return context.mode in {'EDIT'}

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.row()
        row.operator("vertex.prev")
        row.operator("vertex.next")



class OpNextVertex(bpy.types.Operator):
    bl_idname = 'vertex.next'
    bl_label = 'Next Vertex'

    def execute(self, context):
        select_next_vertex()
        return {'FINISHED'}


class OpPrevVertex(bpy.types.Operator):
    bl_idname = 'vertex.prev'
    bl_label = 'Prev Vertex'

    def execute(self, context):
        select_prev_vertex()
        return {'FINISHED'}


def register():
    bpy.utils.register_class(OpNextVertex)
    bpy.utils.register_class(OpPrevVertex)
    bpy.utils.register_class(Panel)


def unregister():
    bpy.utils.unregister_class(OpNextVertex)
    bpy.utils.unregister_class(OpPrevVertex)
    bpy.utils.unregister_class(Panel)


if __name__ == "__main__":
    register()

