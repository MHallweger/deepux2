#############################
# Color Range - LAB Average #
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
#   This is a very similar implementation as CR4_HSV_avg. The main difference is the colour space that is used.
#
#############
# Technical #
#############
#
#   Inputs: JPG image (base64)
#   Returns: List of 6 items: Mean Lightness (float), Standard Deviation Lightness (float), Mean A (Green-Red Space) (float), Standard Deviation A (float), Mean B (Yellow-Blue Space) (float), Standard Deviation B (float)
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


def execute(b64):
    b64 = base64.b64decode(b64)
    b64 = BytesIO(b64)
    img = Image.open(b64).convert('RGB')
    img = np.array(img)
    img = util.img_as_ubyte(img)

    # Convert the LAB space
    lab = color.rgb2lab(img)

    L = lab[:, :, 0]
    A = lab[:, :, 1]
    B = lab[:, :, 2]

    # Get average and standard deviation for each value separately
    meanL = np.mean(L)
    stdL = np.std(L)
    # meanA = np.mean(A)
    # stdA = np.std(A)
    # meanB = np.mean(B)
    # stdB = np.std(B)

    result = [meanL, stdL]

    return result


def evaluate(labColours):
    meanL = labColours['meanL']
    stdL = labColours['stdL']

    # meanL
    if meanL >= 0.00 and meanL <= 40.00:
        meanLEvaluation = {'value': meanL, 'meaning': 'dark', 'evaluation': 'normal'}
    elif meanL >= 40.01 and meanL <= 75.00:
        meanLEvaluation = {'value': meanL, 'meaning': 'medium', 'evaluation': 'good'}
    else:
        meanLEvaluation = {'value': meanL, 'meaning': 'light', 'evaluation': 'normal'}

    # stdL
    if stdL >= 0.00 and stdL <= 15.00:
        stdLEvaluation = {'value': stdL, 'meaning': 'low', 'evaluation': 'bad'}
    elif stdL >= 15.01 and stdL <= 35.00:
        stdLEvaluation = {'value': stdL, 'meaning': 'medium', 'evaluation': 'good'}
    else:
        stdLEvaluation = {'value': stdL, 'meaning': 'high', 'evaluation': 'bad'}

    evaluation = {'meanLEvaluation': meanLEvaluation, 'stdLEvaluation': stdLEvaluation}

    return evaluation
