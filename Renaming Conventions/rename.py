import bpy

############################
####       RENAME      #####
############################
indicator_chars = [
    "r",
    "l",
    "R",
    "L",
    ]

def has_indicator(_from, name):
    indicator = _from.replace("\\*", '').replace("\\^", '')
    #print(indicator)
    for c in indicator_chars:
        if indicator.replace("\\?", c) in name:
            #print("+++indicator: " + c + "+++")
            return c
        
    #print("---no indicator---")
    return False

class ARMATURE_PT_ArmatureRename(bpy.types.Operator):
    """Rename Armature"""
    bl_idname = "armature.rename_bones"
    bl_label = "Rename Armature"
    bl_options = {'REGISTER', 'UNDO'}
    

    def execute(self, context):
        scene = context.scene
        _from = scene.rename_From
        _to = scene.rename_To
        _arm = scene.rename_Armature
        
        #print("from: " + _from)
        #print("to: " + _to)
        #print("armature: ",end='')
        #print(_arm)
        
        if (_arm == 'None'):
            return {"CANCELLED"}
        
        
        for bone in _arm.bones:
            indicator_char = has_indicator(_from, bone.name)
            if indicator_char == False:
                continue
            if "\\^" in _from:
                _from = _from.replace("\\^", '')
                
            indicator = _from.replace('\\*', '').replace("\\?", indicator_char)
            
            if "\\^" in _to:
                if indicator_char.isupper():
                    indicator_char = indicator_char.lower()
                else:
                    indicator_char = indicator_char.upper()
            
            stripped_name = bone.name.replace(indicator, '')
            
            new_name = _to.replace("\\?", indicator_char).replace("\\*", stripped_name).replace("\\^", '')
            
            bone.name = new_name
        
        return {"FINISHED"}
##############################