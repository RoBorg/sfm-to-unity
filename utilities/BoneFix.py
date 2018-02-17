# BoneFix
# Fix bones from SFM -> Unity Conversion
# Adapted from https://smutba.se/project/59/

import bpy
import pprint


class ExitOK(Exception):
    pass


bpy.ops.object.mode_set(mode='EDIT')
edit_bones = bpy.context.object.data.edit_bones

Allbones = {
    # Bones divided into sections

    # "NPC Spine [Spn0]", Causes leg movement with IK
    "NPC Spine1 [Spn1]", "ValveBiped.Bip01_Spine1", "bip_spine_0",
    "NPC Spine2 [Spn2]", "ValveBiped.Bip01_Spine2", "bip_spine_1",
    "ValveBiped.Bip01_Spine4", "bip_spine_2",
    "NPC Neck [Neck]", "ValveBiped.Bip01_Neck1", "bip_neck",
    "NPC Head [Head]", "ValveBiped.Bip01_Head1", "bip_head",
    # 1. Spine Section

    "NPC L Hand [LHnd]", "ValveBiped.Bip01_L_Hand", "bip_hand_L", "lHand",
    "NPC L Finger01 [LF01]", "ValveBiped.Bip01_L_Finger01", "bip_thumb_1_L", "lThumb2",
    "NPC L Finger02 [LF02]", "ValveBiped.Bip01_L_Finger02", "bip_thumb_2_L", "lThumb3",
    "NPC L Finger11 [LF11]", "ValveBiped.Bip01_L_Finger11", "bip_index_1_L", "lIndex2",
    "NPC L Finger12 [LF12]", "ValveBiped.Bip01_L_Finger12", "bip_index_2_L", "lIndex3",
    "NPC L Finger21 [LF21]", "ValveBiped.Bip01_L_Finger21", "bip_middle_1_L", "lMid2",
    "NPC L Finger22 [LF22]", "ValveBiped.Bip01_L_Finger22", "bip_middle_2_L", "lMid3",
    "NPC L Finger31 [LF31]", "ValveBiped.Bip01_L_Finger31", "bip_ring_1_L", "lRing2",
    "NPC L Finger32 [LF32]", "ValveBiped.Bip01_L_Finger32", "bip_ring_2_L", "lRing3",
    "NPC L Finger41 [LF41]", "ValveBiped.Bip01_L_Finger41", "bip_pinky_1_L", "lPinky2",
    "NPC L Finger42 [LF42]", "ValveBiped.Bip01_L_Finger42", "bip_pinky_2_L", "LPinky3",

    "NPC L Forearm [LLar] Chain", "NPC L Forearm [LLar]", "ValveBiped.Bip01_L_Forearm", "bip_lowerArm_L", "lForearmBend",
    "lShldrBend",
    # 2. Left Arm Section

    "NPC R Hand [RHnd]", "ValveBiped.Bip01_R_Hand", "bip_hand_R", "rHand",
    "NPC R Finger01 [RF01]", "ValveBiped.Bip01_R_Finger01", "bip_thumb_1_R", "rThumb2",
    "NPC R Finger02 [RF02]", "ValveBiped.Bip01_R_Finger02", "bip_thumb_2_R", "rThumb3",
    "NPC R Finger11 [RF11]", "ValveBiped.Bip01_R_Finger11", "bip_index_1_R", "rIndex2",
    "NPC R Finger12 [RF12]", "ValveBiped.Bip01_R_Finger12", "bip_index_2_R", "rIndex3",
    "NPC R Finger21 [RF21]", "ValveBiped.Bip01_R_Finger21", "bip_middle_1_R", "rMid2",
    "NPC R Finger22 [RF22]", "ValveBiped.Bip01_R_Finger22", "bip_middle_2_R", "rMid3",
    "NPC R Finger31 [RF31]", "ValveBiped.Bip01_R_Finger31", "bip_ring_1_R", "rRing2",
    "NPC R Finger32 [RF32]", "ValveBiped.Bip01_R_Finger32", "bip_ring_2_R", "rRing3",
    "NPC R Finger41 [RF41]", "ValveBiped.Bip01_R_Finger41", "bip_pinky_1_R", "rPinky2",
    "NPC R Finger42 [RF42]", "ValveBiped.Bip01_R_Finger42", "bip_pinky_2_R", "rPinky3",

    "NPC R Forearm [RLar] Chain", "NPC R Forearm [RLar]", "ValveBiped.Bip01_R_Forearm", "bip_lowerArm_R", "rForearmBend",
    "rShldrBend",
    # 3. Right Arm Section

    "NPC L Foot [LFt ]", "ValveBiped.Bip01_L_Foot", "bip_foot_L", "lFoot",
    "NPC L Calf [LClf] Chain", "NPC L Calf [LClf]", "ValveBiped.Bip01_L_Calf", "bip_knee_L", "lShin",
    "NPC L Toe0 [LToe]", "ValveBiped.Bip01_L_Toe0", "bip_toe_L",
    # 4. Left Foot Section

    "NPC R Foot [RFt ]", "ValveBiped.Bip01_R_Foot", "bip_foot_R", "rFoot",
    "NPC R Calf [RClf] Chain", "NPC R Calf [RClf]", "ValveBiped.Bip01_R_Calf", "bip_knee_R", "rShin",
    "NPC R Toe0 [RToe]", "ValveBiped.Bip01_R_Toe0", "bip_toe_R",
    # 5. Right Foot Section
}

# Update skeleton
for bone in edit_bones:
    try:
        actualbone = bone.name

        if bone.name == "lHand":
            edit_bones["lHand"].parent = edit_bones["lForearmBend"]
            edit_bones["lHand"].tail = (edit_bones["lHand"].tail + edit_bones["lIndex1"].head +
                                        edit_bones["lMid1"].head + edit_bones["lRing1"].head + edit_bones["lPinky1"].head)/5

        if bone.name == "rHand":
            edit_bones["rHand"].parent = edit_bones["rForearmBend"]
            edit_bones["rHand"].tail = (edit_bones["rHand"].tail + edit_bones["rIndex1"].head +
                                        edit_bones["rMid1"].head + edit_bones["rRing1"].head + edit_bones["rPinky1"].head)/5

        if bone.name == "lForearmBend":
            edit_bones["lForearmBend"].parent = edit_bones["lShldrBend"]

        if bone.name == "rForearmBend":
            edit_bones["rForearmBend"].parent = edit_bones["rShldrBend"]

        if bone.name == "lShin":
            edit_bones["lShin"].parent = edit_bones["lThighBend"]

        if bone.name == "rShin":
            edit_bones["rShin"].parent = edit_bones["rThighBend"]

        if edit_bones[actualbone].parent:
            print("!!!!!!!!!!!! 2b : PARENT BONES PRESENT !!!!!!!!!")
            parentbone = edit_bones[actualbone].parent
            print("!!!!!!!!!!!! 3b : Parentbone: " +
                  edit_bones[actualbone].parent.name)
            if actualbone in Allbones:
                print("!!!!!!!!!!!! 4b : No multiple child bones detected")
                EditBone = bpy.context.object.data.edit_bones[bone.name]
                parentbone.tail = edit_bones[actualbone].head
                EditBone.use_connect = True

        if bone.name == "NPC L Hand [LHnd]":
            edit_bones["NPC L Hand [LHnd]"].tail = (edit_bones["NPC L Hand [LHnd]"].tail + edit_bones["NPC L Finger40 [LF40]"].head +
                                                    edit_bones["NPC L Finger30 [LF30]"].head + edit_bones["NPC L Finger20 [LF20]"].head + edit_bones["NPC L Finger10 [LF10]"].head)/5

        if bone.name == "NPC R Hand [RHnd]":
            edit_bones["NPC R Hand [RHnd]"].tail = (edit_bones["NPC R Hand [RHnd]"].tail + edit_bones["NPC R Finger40 [RF40]"].head +
                                                    edit_bones["NPC R Finger30 [RF30]"].head + edit_bones["NPC R Finger20 [RF20]"].head + edit_bones["NPC R Finger10 [RF10]"].head)/5

        if bone.name == "ValveBiped.Bip01_L_Hand":
            edit_bones["ValveBiped.Bip01_L_Hand"].tail = (edit_bones["ValveBiped.Bip01_L_Hand"].tail + edit_bones["ValveBiped.Bip01_L_Finger4"].head +
                                                          edit_bones["ValveBiped.Bip01_L_Finger3"].head + edit_bones["ValveBiped.Bip01_L_Finger2"].head + edit_bones["ValveBiped.Bip01_L_Finger1"].head)/5

        if bone.name == "ValveBiped.Bip01_R_Hand":
            edit_bones["ValveBiped.Bip01_R_Hand"].tail = (edit_bones["ValveBiped.Bip01_R_Hand"].tail + edit_bones["ValveBiped.Bip01_R_Finger4"].head +
                                                          edit_bones["ValveBiped.Bip01_R_Finger3"].head + edit_bones["ValveBiped.Bip01_R_Finger2"].head + edit_bones["ValveBiped.Bip01_R_Finger1"].head)/5

    except ExitOK:
        print("OK")

    bpy.context.scene.update()

# Update bone tail positions
edit_bones = bpy.context.object.data.edit_bones

for bone in edit_bones:
    parentbone = bone.parent

    if parentbone == None:
        continue

    parentbone.tail = bone.head
    bone.use_connect = True

    bpy.context.scene.update()

# Finish off
bpy.ops.object.posemode_toggle()
bpy.context.object.data.show_bone_custom_shapes = False
bpy.context.object.data.use_auto_ik = True
