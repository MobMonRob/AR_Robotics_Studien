#!/usr/bin/env python
import rospy
import tf
from geometry_msgs.msg import Point

class MoveToAxisPositions:
    def __init__(self):
        rospy.init_node('move_to_axis_positions', anonymous=True)
        self.pub = rospy.Publisher('/current_position', Point, queue_size=10)
        self.tf_listener = tf.TransformListener()
        self.rate = rospy.Rate(10)  # 10 Hz

        # Neutrale Positionen entlang der Achsen (x, y, z)
        self.axis_positions = [
            Point(1.0, 0.0, 0.0),  # X-Achse
            Point(0.0, 1.0, 0.0),  # Y-Achse
            Point(0.0, 0.0, 1.0)   # Z-Achse
        ]

    def move_to_positions(self):
        
        for target_position in self.axis_positions:
            rospy.loginfo(f"Bewege zu neutraler Position: {target_position}")
            while not rospy.is_shutdown():
                try:
                    # Hole aktuelle Position des Endeffektors
                    (trans, _) = self.tf_listener.lookupTransform('base_link', 'tool0', rospy.Time(0))
                    current_position = Point(*trans)

                    # Aktuelle Position veröffentlichen
                    self.pub.publish(current_position)
                    rospy.loginfo(f"Aktuelle Position: x={current_position.x}, y={current_position.y}, z={current_position.z}")

                    # Prüfen, ob die Zielposition erreicht wurde
                    if self.is_target_position_reached(current_position, target_position):
                        rospy.loginfo(f"Zielposition erreicht: {target_position}")
                        break

                    # Bewege den Roboter in Richtung der Zielposition
                    self.update_position_towards_target(current_position, target_position)
                    self.rate.sleep()

                except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                    rospy.logwarn("Fehler bei der TF-Abfrage.")
                    continue

    def update_position_towards_target(self, current_position, target_position):

        rospy.loginfo(f"Bewege von {current_position} zu {target_position}.")

    def is_target_position_reached(self, current_position, target_position):
        tolerance = 0.01  # Toleranz für das Erreichen der Zielposition
        return (abs(current_position.x - target_position.x) < tolerance and
                abs(current_position.y - target_position.y) < tolerance and
                abs(current_position.z - target_position.z) < tolerance)

if __name__ == '__main__':
    try:
        mover = MoveToAxisPositions()
        mover.move_to_positions()
    except rospy.ROSInterruptException:
        pass
