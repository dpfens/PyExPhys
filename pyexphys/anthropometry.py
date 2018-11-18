"""
Anthropometry formulas for determining heights of the body and its parts

Winter, David A. Biomechanics and Motor Control of Human Movement. New York, N.Y.: Wiley, 2009. Print.
"""


def height_from_height_eyes(segment_length):
    """
    Calculates body height based on the height of the eyes from the ground

    args:
        segment_length (float): height of the eyes from the ground

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.936


def height_from_height_head(segment_length):
    """
    Calculates body height based on the height of the head (up to the bottom of the chin) from the ground

    args:
        segment_length (float): height of the head (up to the bottom of the chin)

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.870


def height_from_height_shoulders(segment_length):
    """
    Calculates body height based on the height of the shoulders from the ground

    args:
        segment_length (float): height of the shoulders

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.818


def height_from_height_chest(segment_length):
    """
    Calculates body height based on the height of the chest (equal to the nipples) from the ground

    args:
        segment_length (float): height of the chest (equal to the nipples)

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.720


def height_from_height_elbow(segment_length):
    """
    Calculates body height based on the height of the elbows from the ground

    args:
        segment_length (float): height of the elbows

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.630


def height_from_height_wrist(segment_length):
    """
    Calculates body height based on the height of the elbows from the ground

    args:
        segment_length (float): height of the wrists

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.485


def height_from_height_fingertip(segment_length):
    """
    Calculates body height based on the height of the fingertips from the ground

    args:
        segment_length (float): height of the fingertips

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.377


def height_from_height_hips(segment_length):
    """
    Calculates body height based on the height of the hips from the ground

    args:
        segment_length (float): height of the hips

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.530


def height_from_height_buttocks(segment_length):
    """
    Calculates body height based on the height of the buttocks from the ground

    args:
        segment_length (float): height of the buttocks

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.485


def height_from_height_knee(segment_length):
    """
    Calculates body height based on the height of the knees from the ground

    args:
        segment_length (float): height of the knees

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.285


def height_from_height_ankle(segment_length):
    """
    Calculates body height based on the height of the ankles from the ground

    args:
        segment_length (float): height of the ankles

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.039


def height_from_head_length(segment_length):
    """
    Calculates body height based on the height of the head

    args:
        segment_length (float): vertical length of head

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.130


def height_from_shoulder_distance(segment_length):
    """
    Calculates body height based on the horizontal distance from the center of the chest to the shoulder

    args:
        segment_length (float): horizontal distance from the center of the chest to the shoulder

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.129


def height_from_shoulder_width(segment_length):
    """
    Calculates body height based on the width of the shoulders

    args:
        segment_length (float): width of the shoulders

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.259


def height_from_hips_width(segment_length):
    """
    Calculates body height based on the horizontal width of the hips

    args:
        segment_length (float): width of the hips

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.191


def height_from_nipple_width(segment_length):
    """
    Calculates body height based on the horizontal distance between nipples

    args:
        segment_length (float): horizontal distance between nipples

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.174


def height_from_foot_width(segment_length):
    """
    Calculates body height based on the foot breadth

    args:
        segment_length (float): breadth of the foot

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.055


def height_from_foot_length(segment_length):
    """
    Calculates body height based on the foot length

    args:
        segment_length (float): length of foot

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.152


def height_from_humerus_length(segment_length):
    """
    Calculates body height based on the humerus (shoulder to elbow) length

    args:
        segment_length (float): length of humerus (shoulder to end of elbow)

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.186


def height_from_forearm_length(segment_length):
    """
    Calculates body height based on the forearm length (elbow to wrist)

    args:
        segment_length (float): length of forearm

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.146


def height_from_hand_length(segment_length):
    """
    Calculates body height based on the hand length (wrist to fingertips)

    args:
        segment_length (float): length of length of hand

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.108


def height_from_upperbody_length(segment_length):
    """
    Calculates body height based on the upper body length (top of head to bottom of torso)

    args:
        segment_length (float): length of upper body

    Returns:
        float: total body height
    """
    if segment_length <= 0:
        raise ValueError('segment_length must be > 0')
    return segment_length / 0.520


class Segment(object):

    def __init__(self, body_height):
        if body_height <= 0:
            raise ValueError('body_height must be > 0')
        self.body_height = body_height

    def height_eyes(self):
        """
        Calculates the height of the eyes from the ground based on the body height

        Returns:
            float: height of the eyes from the ground
        """
        return 0.936 * self.body_height

    def height_head(self):
        """
        Calculates the height of the head (up to the bottom of the chin) from the ground based on the body height

        Returns:
            float: height of the head (bottom of chin) from the ground
        """
        return 0.870 * self.body_height

    def height_shoulders(self):
        """
        Calculates the height of the shoulders from the ground based on the body height

        Returns:
            float: height of the shoulders from the ground
        """
        return 0.818 * self.body_height

    def height_chest(self):
        """
        Calculates the height of the chest (equal to the nipples) from the ground based on the body height

        Returns:
            float: height of the chest (equal to nipples) from the ground
        """
        return 0.720 * self.body_height

    def height_elbow(self):
        """
        Calculates the height of the elbows from the ground based on the body height

        Returns:
            float: height of the elbow from the ground
        """
        return 0.630 * self.body_height

    def height_wrist(self):
        """
        Calculates the height of the wrists from the ground based on the body height

        Returns:
            float: height of the wrists from the ground
        """
        return 0.485 * self.body_height

    def height_fingertip(self):
        """
        Calculates the height of the fingertips from the ground based on the body height

        Returns:
            float: height of the fingertips from the ground
        """
        return 0.377 * self.body_height

    def height_hips(self):
        """
        Calculates the height of the hips from the ground based on the body height

        Returns:
            float: height of the hips from the ground
        """
        return 0.530 * self.body_height

    def height_buttocks(self):
        """
        Calculates the height of the buttocks from the ground based on the body height

        Returns:
            float: height of the buttocks from the ground
        """
        return 0.485 * self.body_height

    def height_knee(self):
        """
        Calculates the height of the knees from the ground based on the body height

        Returns:
            float: height of the knees from the ground
        """
        return 0.285 * self.body_height

    def height_ankle(self):
        """
        Calculates the height of the ankles from the ground based on the body height

        Returns:
            float: height of theankles from the ground
        """
        return 0.039 * self.body_height

    def head_height(self):
        """
        Calculates the height of the head based on the body height

        Returns:
            float: vertical height of the head
        """
        return 0.130 * self.body_height

    def shoulder_distance(self):
        """
        Calculates the horizontal distance from the center of the chest to the shoulder based on the body height

        Returns:
            float: horizontal distance from the center of the chest to the shoulder
        """
        return 0.129 * self.body_height

    def shoulder_width(self):
        """
        Calculates the width of the shoulders based on the body height

        Returns:
            float: shoulder width
        """
        return 0.259 * self.body_height

    def hips_width(self):
        """
        Calculates the horizontal width of the hips based on the body height

        Returns:
            float: width of the hips
        """
        return 0.191 * self.body_height

    def nipple_width(self):
        """
        Calculates the horizontal distance between nipples based on the body height

        Returns:
            float: horizontal distance between nipples
        """
        return 0.174 * self.body_height

    def foot_width(self):
        """
        Calculates the foot breadth based on the body height

        Returns:
            float: width of the foot
        """
        return 0.055 * self.body_height

    def foot_length(self):
        """
        Calculates the foot length based on the body height

        Returns:
            float: length of the foot
        """
        return 0.152 * self.body_height

    def humerus_length(self):
        """
        Calculates the humerus (shoulder to elbow) length based on the body height

        Returns:
            float: length of the humerus
        """
        return 0.186 * self.body_height

    def forearm_length(self):
        """
        Calculates the forearm length (elbow to wrist) based on the body height

        Returns:
            float: length of the forearm
        """
        return 0.146 * self.body_height

    def hand_length(self):
        """
        Calculates the hand length (wrist to fingertips) based on the body height

        Returns:
            float: length of the hand
        """
        return 0.108 * self.body_height

    def upperbody_length(self):
        """
        Calculates the upper body length (top of head to bottom of torso) based on the body height

        Returns:
            float: length of the upper body
        """
        return 0.520 * self.body_height
