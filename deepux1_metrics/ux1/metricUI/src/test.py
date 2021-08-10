import metricscreator
import metricsevaluator
from core.utils import read_image
import pathlib


print(metricsevaluator.MetricsEvaluator.getEvaluations(metricscreator.MetricsCreator.getMetrics(read_image(pathlib.Path('TestScreen.png')))))

