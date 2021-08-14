###############
# White Space #
###############
#
#   V1.0
#   29/05/2017
#
#   Implemented by:
#   Thomas Langerak
#   (hello@thomaslangerak.nl)
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
#############
# Technical #
#############
#
#   Inputs: PNG image (base64), segmentation elements (list)
#   Returns: List of 1 item: White Space (float)
#
##############
# References #
##############
#
#   1.  Miniukovich, A. and De Angeli, A. Computation of Interface Aesthetics.
#       Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems - CHI '15, (2015).
#
##############
# Change Log #
##############
#
###############
# Bugs/Issues #
###############
#
import base64
from io import BytesIO
from PIL import Image
import deepux1_metrics.ux1.src.segmentation as segmentation

def execute(b64):
    elements = segmentation.get_elements(b64)['elements']
    b64 = base64.b64decode(b64)
    b64 = BytesIO(b64)
    img = Image.open(b64)

    width, height = img.size

    imsize = width * height

    non_white_space = 0
    for ele in elements:
        non_white_space += ele['width'] * ele['height']

    return (imsize - non_white_space) / float(imsize)

def evaluate(whiteSpaceValue):
    if whiteSpaceValue >= 0.00 and whiteSpaceValue <= 0.30:
        evaluation = {'value': whiteSpaceValue, 'meaning': 'Low', 'evaluation': 'bad'}
    elif whiteSpaceValue >= 0.31 and whiteSpaceValue <= 0.80:
        evaluation = {'value': whiteSpaceValue, 'meaning': 'Good', 'evaluation': 'good'}
    else:
        evaluation = {'value': whiteSpaceValue, 'meaning': 'High', 'evaluation': 'bad'}

    return evaluation
