
bl_info = {
    "name": "Renaming Conventions",
    "author": "Th3R3ality",
    "version": (0, 0, 1),
    "blender": (3, 5, 1),
    "location": "3D Viewport > Sidebar > RealityTools",
    "description": "Add-on to rename bone prefix and suffix",
    "category": "Rigging",
}

import bpy
from rename import ARMATURE_PT_ArmatureRename





class RealityTools_panel:
    bl_category = 'RealityTools'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

class Renamings(RealityTools_panel, bpy.types.Panel):
    bl_idname = 'VIEW3D_PT_Renamings_panel'
    bl_label = 'Renaming Conventions'
    
    
    def draw(self, context):
        scene = context.scene
        layout = self.layout
        box = layout.box()

        #box.label(text=self.bl_label)
        box.prop(scene, "rename_Armature", text="Armature")
        box.label(text="Naming Convention")
        row = box.row()
        row.prop(scene, "rename_From", text="From")
        row.prop(scene, "rename_To", text="To")
        
        box.operator(ARMATURE_PT_ArmatureRename.bl_idname, text="Rename", icon="BONE_DATA")

class INFO_PT_syntax(RealityTools_panel, bpy.types.Panel):
    bl_parent_id  = 'VIEW3D_PT_Renamings_panel'
    bl_label = 'Syntax'
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="To indicate an identifier use \"\\?\"")
        layout.label(text="To indicate bone name use \"\\*\"")
        layout.label(text="To invert capitalisation prepend \"\\^\" to the identifier")
        
        box = layout.box()
        box.label(text="Add-on currently Doesn't support")
        box.label(text="naming conventions like \"left\" \"right\" etc.")

def register():
    bpy.types.Scene.rename_Armature = bpy.props.PointerProperty(type=bpy.types.Armature)
    bpy.types.Scene.rename_From = bpy.props.StringProperty()
    bpy.types.Scene.rename_To = bpy.props.StringProperty()
    
    bpy.utils.register_class(Renamings)
    bpy.utils.register_class(INFO_PT_syntax)
    bpy.utils.register_class(ARMATURE_PT_ArmatureRename)
    
def unregister():
    del bpy.types.Scene.rename_Armature
    del bpy.types.Scene.rename_From
    del bpy.types.Scene.rename_To
    
    bpy.utils.unregister_class(Renamings)
    bpy.utils.unregister_class(INFO_PT_syntax)
    bpy.utils.unregister_class(ARMATURE_PT_ArmatureRename)
    
if __name__ == '__main__':
    register()
