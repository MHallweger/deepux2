import deepux1_metrics.ux1.src.metrics.distinct_rgb_values as metric_distinct_rgb_values
import deepux1_metrics.ux1.src.metrics.figure_ground_contrast as metric_figure_ground_contrast
import deepux1_metrics.ux1.src.metrics.grid_quality as metric_grid_quality
import deepux1_metrics.ux1.src.metrics.white_space as metric_white_space
import deepux1_metrics.ux1.src.metrics.colourfulness as metric_colourfulness
import deepux1_metrics.ux1.src.metrics.HSV_avg as metric_hsv_avg
import deepux1_metrics.ux1.src.metrics.HSV_unique as metric_hsv_unique
import deepux1_metrics.ux1.src.metrics.LAB_avg as metrics_lab_avg
import deepux1_metrics.ux1.src.metrics.static_colour_clustering as metrics_static_colour_clustering
import deepux1_metrics.ux1.src.metrics.dynamic_colour_clustering as metrics_dynamic_colour_clustering
import deepux1_metrics.ux1.src.metrics.luminance_sd as metrics_luminance_sd
import deepux1_metrics.ux1.src.metrics.wave as metrics_wave
import deepux1_metrics.ux1.src.metrics.contour_density as metrics_contour_density
import deepux1_metrics.ux1.src.metrics.contour_congestion as metrics_contour_congestion
import deepux1_metrics.ux1.src.metrics.pixel_symmetry as metrics_pixel_symmetry
import deepux1_metrics.ux1.src.metrics.quadtree_decomposition as metrics_quadtree_decomposition


class MetricsEvaluator:
    """
    Creates Evaluator for given Metrics
    """

    @staticmethod
    def getEvaluations(metricAsJsonObject):
        rgbEvaluation = metric_distinct_rgb_values.Metric3.evaluate(metricAsJsonObject['distinct_rgb_values'])

        fgcEvaluation = metric_figure_ground_contrast.Metric5.evaluate(metricAsJsonObject['figure_ground_contrast'])

        gridEvaluation = metric_grid_quality.evaluate(metricAsJsonObject['grid_quality'])

        whiteSpaceEvaluation = metric_white_space.evaluate(metricAsJsonObject['white_space'])

        colourfulnessEvaluation = metric_colourfulness.evaluate(metricAsJsonObject['colourfulness'])

        # hsv_colours
        hsv_coloursEvaluation = metric_hsv_avg.evaluate(metricAsJsonObject['hsv_colours'])

        # hsv unique
        hsv_uniqueEvaluation = metric_hsv_unique.evaluate(metricAsJsonObject['hsv_unique'])

        # lab avg
        lab_avgEvaluation = metrics_lab_avg.evaluate(metricAsJsonObject['lab_avg'])

        static_colour_clustersEvaluation = metrics_static_colour_clustering.evaluate(
            metricAsJsonObject['static_colour_clusters'])

        dynamic_colour_clustersEvaluation = metrics_dynamic_colour_clustering.evaluate(
            metricAsJsonObject['dynamic_colour_clusters'])

        luminance_sdEvaluation = metrics_luminance_sd.evaluate(metricAsJsonObject['luminance_sd'])

        waveEvaluation = metrics_wave.evaluate(metricAsJsonObject['wave'])

        contour_densityEvaluation = metrics_contour_density.evaluate(metricAsJsonObject['contour_density'])

        metrics_contour_congestionEvaluation = metrics_contour_congestion.evaluate(
            metricAsJsonObject['contour_congestion'])

        pixel_symmetryEvaluation = metrics_pixel_symmetry.evaluate(metricAsJsonObject['pixel_symmetry'])

        quadtree_decomposition = metrics_quadtree_decomposition.evaluate(metricAsJsonObject['quadtree_decomposition'])

        evaluatorsValues = {'distinct_rgb_values': rgbEvaluation,
                            'figure_ground_contrast': fgcEvaluation,
                            'white_space': whiteSpaceEvaluation,
                            'grid_quality': gridEvaluation,
                            'colourfulness': colourfulnessEvaluation,
                            'hsv_colours': hsv_coloursEvaluation,
                            'hsv_unique': hsv_uniqueEvaluation,
                            'lab_avg': lab_avgEvaluation,
                            'static_colour_clusters': static_colour_clustersEvaluation,
                            'dynamic_colour_clusters': dynamic_colour_clustersEvaluation,
                            'luminance_sd': luminance_sdEvaluation,
                            'wave': waveEvaluation,
                            'contour_density': contour_densityEvaluation,
                            'contour_congestion': metrics_contour_congestionEvaluation,
                            'pixel_symmetry': pixel_symmetryEvaluation,
                            'quadtree_decomposition': quadtree_decomposition}

        return evaluatorsValues
