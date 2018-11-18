"""
The Enums module contains two classes of identifiers for Gender and Physical Activity Levels (PAL). Developers can use these classes to provide input parameters in creating class instances, and in executing methods. These class attributes can be used to identify that the individual is of a specified gender, or that the individual is of a specified physical activity level.

The values of the attributes in these classes have no meaning in regards to calculations. These values are merely used for identifying the relevant equation to be executed.
"""


class Gender(object):
    Male = 1
    Female = 2


class PAL(object):
    """
    Physical Activity Levels (PAL) are categories for expressing a person's physical activity in a daily basis. PALs are often used to estimate total energy expenditure. PALs are calculated as the ratio of TEE to BMR. The categories used are as follows:

    - Sedentary (1.0 < PAL < 1.40)
    - Low (1.40 < PAL < 1.60)
    - Active (1.6 < PAL < 1.90)
    - VeryActive (1.9 < PAL < 2.5)"""
    Sedentary = 1
    Low = 2
    Active = 3
    VeryActive = 4


class Race(object):
    """
    Race categories
    """
    Black = 1
    White = 0
