#############################
# Color Range - HSV Average #
#############################
#
#   V1.0
#   29/05/2017
#
#   Implemented by:
#   Yuxi Zhu (matlab) & Thomas Langerak (converted to python)
#   (zhuyuxi1990@gmail.com) & (hello@thomaslangerak.nl)
#
#   Supervisor:
#   Antti Oulasvirta
#
#   This work was funded by Technology Industries of Finland in a three-year
#   project grant on self-optimizing web services. The principal investigator
#   is Antti Oulasvirta of Aalto University (antti.oulasvirta@aalto.fi)
#
###########
# Summary #
###########
#
#   Hasler & Susstrunk validated this metric in their paper. It looks at the average value and standard deviation for
#   every value in the HSV colour space.
#
#############
# Technical #
#############
#
#   Inputs: JPG image (base64)
#   Returns: List of 5 items: Average Hue (float), Average Saturation (float), Standard Deviation of Saturation (float), Average Value (float), Standard Deviation of Value (float)
#
##############
# References #
##############
#
#   1.  Hasler, D. and Susstrunk, S. Measuring Colourfuness in Natural Images. (2003).
#
##############
# Change Log #
##############
#
###############
# Bugs/Issues #
###############
#
from skimage import color, util
import numpy as np
import base64
from PIL import Image
from io import BytesIO


# Functions for easy use of radials in sin,cos and tan. based on:
# https://stackoverflow.com/questions/43100286/python-trigonometric-calculations-in-degrees
def sind(x):
    y = np.sin(np.deg2rad(x))
    y = np.rad2deg(y)

    return y


def cosd(x):
    y = np.cos(np.deg2rad(x))
    y = np.rad2deg(y)

    return y


def atan2d(x, y):
    z = np.arctan2(np.deg2rad(x), np.deg2rad(y))
    z = np.rad2deg(z)

    return z


def execute(b64):
    b64 = base64.b64decode(b64)
    b64 = BytesIO(b64)
    img = Image.open(b64).convert('RGB')
    img = np.array(img)
    img = util.img_as_ubyte(img)
    img = img / 255.  # this division is needed to get proper values. for hue, saturation and value (0 to 360, 0 to 1,0 to 1)
    img = color.rgb2hsv(img)
    img = img.reshape(-1, 3)
    img = [tuple(l) for l in img]

    h = []
    s = []
    v = []

    # Give each channel its own list
    for items in img:
        [hue, sat, val] = [items[0], items[1], items[2]]
        h.append(hue * 360)
        s.append(sat)
        v.append(val)

    # Hue is an angle, so cannot simple add and average it
    sumsin = sum(sind(h[:]))
    sumcos = sum(cosd(h[:]))

    # Get the average value and standard deviation over H,S and V
    avgHue = atan2d(sumsin, sumcos) % 360
    avgSaturation = np.mean(s)
    stdSaturation = np.std(s)
    avgValue = np.mean(v)
    stdValue = np.std(v)
    result = [avgSaturation, stdSaturation, avgValue, stdValue]

    return result


def evaluate(hsvColours):
    avgSaturation = hsvColours['avgSaturation']
    stdSaturation = hsvColours['stdSaturation']
    avgValue = hsvColours['avgValue']
    stdValue = hsvColours['stdValue']

    # avg saturation
    if avgSaturation >= 0.00 and avgSaturation <= 0.10:
        avgSaturationEvaluation = {'value': avgSaturation, 'meaning': 'low', 'evaluation': 'bad'}
    elif avgSaturation >= 0.11 and avgSaturation <= 0.60:
        avgSaturationEvaluation = {'value': avgSaturation, 'meaning': 'medium', 'evaluation': 'good'}
    else:
        avgSaturationEvaluation = {'value': avgSaturation, 'meaning': 'high', 'evaluation': 'bad'}

    # std Saturation
    if stdSaturation >= 0.00 and stdSaturation <= 0.20:
        stdSaturationEvaluation = {'value': stdSaturation, 'meaning': 'low', 'evaluation': 'bad'}
    elif stdSaturation >= 0.21 and stdSaturation <= 0.40:
        stdSaturationEvaluation = {'value': stdSaturation, 'meaning': 'medium', 'evaluation': 'good'}
    else:
        stdSaturationEvaluation = {'value': stdSaturation, 'meaning': 'high', 'evaluation': 'bad'}

    # avg Value
    if avgValue >= 0.00 and avgValue <= 0.40:
        avgValueEvaluation = {'value': avgValue, 'meaning': 'dark', 'evaluation': 'normal'}
    elif avgValue >= 0.41 and avgValue <= 0.80:
        avgValueEvaluation = {'value': avgValue, 'meaning': 'medium', 'evaluation': 'normal'}
    else:
        avgValueEvaluation = {'value': avgValue, 'meaning': 'light', 'evaluation': 'bad'}

    # std Value
    if stdValue >= 0.00 and stdValue <= 0.15:
        stdValueEvaluation = {'value': stdValue, 'meaning': 'low', 'evaluation': 'bad'}
    elif stdValue >= 0.16 and stdValue <= 0.35:
        stdValueEvaluation = {'value': stdValue, 'meaning': 'medium', 'evaluation': 'good'}
    else:
        stdValueEvaluation = {'value': stdValue, 'meaning': 'high', 'evaluation': 'bad'}

    evaluation = {'avgSaturation': avgSaturationEvaluation, 'stdSaturation': stdSaturationEvaluation,
                  'avgValue': avgValueEvaluation, 'stdValue': stdValueEvaluation}

    return evaluation
