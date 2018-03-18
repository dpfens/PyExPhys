"""
Anthropometry formulas
Winter, David A. Biomechanics and Motor Control of Human Movement. New York, N.Y.: Wiley, 2009. Print.
"""
cpdef double height_from_height_eyes(double segment_length):
    """
    Calculates body height based on the height of the eyes from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.936

cpdef double height_from_height_head(double segment_length):
    """
    Calculates body height based on the height of the head (up to the bottom of the chin) from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.870

cpdef double height_from_height_shoulders(double segment_length):
    """
    Calculates body height based on the height of the shoulders from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.818

cpdef double height_from_height_chest(double segment_length):
    """
    Calculates body height based on the height of the chest (equal to the nipples) from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.720

cpdef double height_from_height_elbow(double segment_length):
    """
    Calculates body height based on the height of the elbows from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.630

cpdef double height_from_height_wrist(double segment_length):
    """
    Calculates body height based on the height of the elbows from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.485

cpdef double height_from_height_fingertip(double segment_length):
    """
    Calculates body height based on the height of the fingertips from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.377

cpdef double height_from_height_hips(double segment_length):
    """
    Calculates body height based on the height of the hips from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.530

cpdef double height_from_height_buttocks(double segment_length):
    """
    Calculates body height based on the height of the buttocks from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.485

cpdef double height_from_height_knee(double segment_length):
    """
    Calculates body height based on the height of the knees from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.285

cpdef double height_from_height_ankle(double segment_length):
    """
    Calculates body height based on the height of the ankles from the ground
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.039

cpdef double height_from_head_height(double segment_length):
    """
    Calculates body height based on the height of the head
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.130

cpdef double height_from_shoulder_distance(double segment_length):
    """
    Calculates body height based on the horizontal distance from the center of the chest to the shoulder
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.129

cpdef double height_from_shoulder_width(double segment_length):
    """
    Calculates body height based on the width of the shoulders
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.259

cpdef double height_from_hips_width(double segment_length):
    """
    Calculates body height based on the horizontal width of the hips
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.191

cpdef double height_from_nipple_width(double segment_length):
    """
    Calculates body height based on the horizontal distance between nipples
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.174

cpdef double height_from_foot_width(double segment_length):
    """
    Calculates body height based on the foot breadth
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.055

cpdef double height_from_foot_length(double segment_length):
    """
    Calculates body height based on the foot length
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.152

cpdef double height_from_humerus_length(double segment_length):
    """
    Calculates body height based on the humerus (shoulder to elbow) length
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.186

cpdef double height_from_forearm_length(double segment_length):
    """
    Calculates body height based on the forearm length (elbow to wrist)
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.146

cpdef double height_from_hand_length(double segment_length):
    """
    Calculates body height based on the hand length (wrist to fingertips)
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.108

cpdef double height_from_upperbody_length(double segment_length):
    """
    Calculates body height based on the upper body length (top of head to bottom of torso)
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.520


cdef class Segment(object):

    def __cinit__(self, double body_height):
        if body_height <= 0:
            raise ValueError('body_height must be > 0')
        self.body_height = body_height

    cpdef double height_eyes(self):
        """
        Calculates the height of the eyes from the ground based on the body height
        """
        return 0.936 * self.body_height

    cpdef double height_head(self):
        """
        Calculates the height of the head (up to the bottom of the chin) from the ground based on the body height
        """
        return 0.870 * self.body_height

    cpdef double height_shoulders(self):
        """
        Calculates the height of the shoulders from the ground based on the body height
        """
        return 0.818 * self.body_height

    cpdef double height_chest(self):
        """
        Calculates the height of the chest (equal to the nipples) from the ground based on the body height
        """
        return 0.720 * self.body_height

    cpdef double height_elbow(self):
        """
        Calculates the height of the elbows from the ground based on the body height
        """
        return 0.630 * self.body_height

    cpdef double height_wrist(self):
        """
        Calculates the height of the elbows from the ground based on the body height
        """
        return 0.485 * self.body_height

    cpdef double height_fingertip(self):
        """
        Calculates the height of the fingertips from the ground based on the body height
        """
        return 0.377 * self.body_height

    cpdef double height_hips(self):
        """
        Calculates the height of the hips from the ground based on the body height
        """
        return 0.530 * self.body_height

    cpdef double height_buttocks(self):
        """
        Calculates the height of the buttocks from the ground based on the body height
        """
        return 0.485 * self.body_height

    cpdef double height_knee(self):
        """
        Calculates the height of the knees from the ground based on the body height
        """
        return 0.285 * self.body_height

    cpdef double height_ankle(self):
        """
        Calculates the height of the ankles from the ground based on the body height
        """
        return 0.039 * self.body_height

    cpdef double head_height(self):
        """
        Calculates the height of the head based on the body height
        """
        return 0.130 * self.body_height

    cpdef double shoulder_distance(self):
        """
        Calculates the horizontal distance from the center of the chest to the shoulder based on the body height
        """
        return 0.129 * self.body_height

    cpdef double shoulder_width(self):
        """
        Calculates the width of the shoulders based on the body height
        """
        return 0.259 * self.body_height

    cpdef double hips_width(self):
        """
        Calculates the horizontal width of the hips based on the body height
        """
        return 0.191 * self.body_height

    cpdef double nipple_width(self):
        """
        Calculates the horizontal distance between nipples based on the body height
        """
        return 0.174 * self.body_height

    cpdef double foot_width(self):
        """
        Calculates the foot breadth based on the body height
        """
        return 0.055 * self.body_height

    cpdef double foot_length(self):
        """
        Calculates the foot length based on the body height
        """
        return 0.152 * self.body_height

    cpdef double humerus_length(self):
        """
        Calculates the humerus (shoulder to elbow) length based on the body height
        """
        return 0.186 * self.body_height

    cpdef double forearm_length(self):
        """
        Calculates the forearm length (elbow to wrist) based on the body height
        """
        return 0.146 * self.body_height

    cpdef double hand_length(self):
        """
        Calculates the hand length (wrist to fingertips) based on the body height
        """
        return 0.108 * self.body_height

    cpdef double upperbody_length(self):
        """
        Calculates the upper body length (top of head to bottom of torso) based on the body height
        """
        return 0.520 * self.body_height
