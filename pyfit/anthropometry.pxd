"""
Anthropometry formulas
Winter, David A. Biomechanics and Motor Control of Human Movement. New York, N.Y.: Wiley, 2009. Print.
"""

cpdef double height_from_height_eyes(double segment_length)

cpdef double height_from_height_head(double segment_length)

cpdef double height_from_height_shoulders(double segment_length)

cpdef double height_from_height_chest(double segment_length)

cpdef double height_from_height_elbow(double segment_length)

cpdef double height_from_height_wrist(double segment_length)

cpdef double height_from_height_fingertip(double segment_length)

cpdef double height_from_height_hips(double segment_length)

cpdef double height_from_height_buttocks(double segment_length)

cpdef double height_from_height_knee(double segment_length)

cpdef double height_from_height_ankle(double segment_length)

cpdef double height_from_head_height(double segment_length)

cpdef double height_from_shoulder_distance(double segment_length)

cpdef double height_from_shoulder_width(double segment_length)

cpdef double height_from_hips_width(double segment_length)

cpdef double height_from_nipple_width(double segment_length)

cpdef double height_from_foot_width(double segment_length)

cpdef double height_from_foot_length(double segment_length)

cpdef double height_from_humerus_length(double segment_length)

cpdef double height_from_forearm_length(double segment_length)

cpdef double height_from_hand_length(double segment_length)

cpdef double height_from_upperbody_length(double segment_length)


cdef class Segment(object):
    cdef double body_height

    cpdef double height_eyes(self)

    cpdef double height_head(self)

    cpdef double height_shoulders(self)

    cpdef double height_chest(self)

    cpdef double height_elbow(self)

    cpdef double height_wrist(self)

    cpdef double height_fingertip(self)

    cpdef double height_hips(self)

    cpdef double height_buttocks(self)

    cpdef double height_knee(self)

    cpdef double height_ankle(self)

    cpdef double head_height(self)

    cpdef double shoulder_distance(self)

    cpdef double shoulder_width(self)

    cpdef double hips_width(self)

    cpdef double nipple_width(self)

    cpdef double foot_width(self)

    cpdef double foot_length(self)

    cpdef double humerus_length(self)

    cpdef double forearm_length(self)

    cpdef double hand_length(self)
    cpdef double upperbody_length(self)
