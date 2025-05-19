import rospy
from intera_interface import Limb

def move_sawyer_to_90_degrees():
    rospy.init_node('sawyer_90_degree_position')

    limb = Limb('right')

    # 90° = 1.57 rad für jedes Gelenk, das dies unterstützt
    target_angles = {
        'right_j0': 1.57,
        'right_j1': 1.39,
        'right_j2': 1.57,
        'right_j3': 1.57,
        'right_j4': 1.57,
        'right_j5': 1.57,
        'right_j6': 1.57
    }

    rospy.loginfo("Bewege Sawyer in die 90°-Position...")
    limb.move_to_joint_positions(target_angles)
    rospy.loginfo("Position erreicht!")

if __name__ == '__main__':
    try:
        move_sawyer_to_90_degrees()
    except rospy.ROSInterruptException:
        pass
