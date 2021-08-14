import os
from deepux2.deepux1_metrics.ux1.src import metricscreator
from deepux2.deepux1_metrics.ux1.src import metricsevaluator
from deepux2.deepux1_metrics.ux1.src import recommendation
from deepux2.deepux1_metrics.ux1.src.core.utils import read_image
import pathlib


def process_single_image(image_name):
    # Move working dir if not in module directory
    if os.path.dirname(os.path.abspath(__file__)).lower() != os.path.abspath(os.getcwd()).lower():
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

    img = read_image(pathlib.Path(image_name))
    print("Processing image...")
    metrics, exec_times = metricscreator.MetricsCreator.getMetrics(img)
    evaluations = metricsevaluator.MetricsEvaluator.getEvaluations(metrics)
    recoms = recommendation.Recommendator().getRecommendations(evaluations)

    print(recoms)
    return recoms

