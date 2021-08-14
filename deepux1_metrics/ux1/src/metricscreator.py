import datetime
import time

import deepux1_metrics.ux1.src.metrics.distinct_rgb_values as metric_distinct_rgb_values
import deepux1_metrics.ux1.src.metrics.figure_ground_contrast as metric_figure_ground_contrast
import deepux1_metrics.ux1.src.metrics.white_space as metric_white_space
import deepux1_metrics.ux1.src.metrics.grid_quality as metric_grid_quality
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


class MetricsCreator:
    """
    Creates Metrics for a given base64 Input
    """

    @staticmethod
    def getMetrics(pictureAsBase64: str):
        execution_times = {}

        # Anzahl der Farben im RGB Farbraum
        start_time = time.time()
        distinct_rgb_values = metric_distinct_rgb_values.Metric3.execute_metric(pictureAsBase64)
        execution_times["distinct_rgb_values_time"] = time.time() - start_time

        # Unterscheidbarkeit des vordergrunds anhand des Kontrasts
        start_time = time.time()
        figure_ground_contrast = metric_figure_ground_contrast.Metric5.execute_metric(pictureAsBase64)
        execution_times["figure_ground_contrast_time"] = time.time() - start_time

        # Weißer Raum
        start_time = time.time()
        white_space = metric_white_space.execute(pictureAsBase64)
        execution_times["white_space_time"] = time.time() - start_time

        # Gitter Qualität
        start_time = time.time()
        grid_quality = metric_grid_quality.execute(pictureAsBase64)
        execution_times["grid_quality_time"] = time.time() - start_time

        # Colourfulness
        start_time = time.time()
        colourfulness = metric_colourfulness.execute(pictureAsBase64)
        execution_times["colourfulness_time"] = time.time() - start_time

        # hsv_colours
        start_time = time.time()
        hsv_avg = metric_hsv_avg.execute(pictureAsBase64)
        avgSaturation = hsv_avg[0]
        stdSaturation = hsv_avg[1]
        avgValue = hsv_avg[2]
        stdValue = hsv_avg[3]
        execution_times["hsv_avg_time"] = time.time() - start_time

        # hsv unique
        start_time = time.time()
        hsv_unique = metric_hsv_unique.execute(pictureAsBase64)
        execution_times["hsv_unique_time"] = time.time() - start_time

        # lab avg
        start_time = time.time()
        lab_avg = metrics_lab_avg.execute(pictureAsBase64)
        meanL = lab_avg[0]
        stdL = lab_avg[1]
        execution_times["lab_avg_time"] = time.time() - start_time

        # static colors
        start_time = time.time()
        static_colour_clusters = metrics_static_colour_clustering.execute(pictureAsBase64)
        execution_times["static_colour_clusters_time"] = time.time() - start_time

        #dynamic color clusters
        start_time = time.time()
        dynamic_colour_clusters = metrics_dynamic_colour_clustering.execute(pictureAsBase64)
        execution_times["dynamic_colour_clusters_time"] = time.time() - start_time

        #luminace
        start_time = time.time()
        luminance_sd = metrics_luminance_sd.execute(pictureAsBase64)
        execution_times["luminance_sd_time"] = time.time() - start_time

        #wave
        start_time = time.time()
        wave = metrics_wave.execute(pictureAsBase64)
        execution_times["wave_time"] = time.time() - start_time

        #contour density
        start_time = time.time()
        contour_density = metrics_contour_density.Metric4.execute(pictureAsBase64)
        execution_times["wave_time"] = time.time() - start_time

        #contour congestion
        start_time = time.time()
        contour_congestion = metrics_contour_congestion.Metric6.execute(pictureAsBase64)
        execution_times["contour_congestion_time"] = time.time() - start_time

        #pixel symmetry
        start_time = time.time()
        pixel_symmetry = metrics_pixel_symmetry.execute(pictureAsBase64)
        execution_times["pixel_symmetry_time"] = time.time() - start_time

        #quadtree decomposition
        start_time = time.time()
        quadtree_decomposition = metrics_quadtree_decomposition.execute(pictureAsBase64)

        balance = quadtree_decomposition[0]
        symmetry = quadtree_decomposition[1]
        equilibrium = quadtree_decomposition[2]
        numberOfLeaves = quadtree_decomposition[3]
        execution_times["quadtree_decomposition_time"] = time.time() - start_time

        metricsValues = {'distinct_rgb_values': distinct_rgb_values,
                         'figure_ground_contrast': figure_ground_contrast,
                         'white_space': white_space,
                         'grid_quality': grid_quality,
                         'colourfulness': colourfulness,
                         'hsv_colours':
                             {
                                 'avgSaturation': avgSaturation,
                                 'stdSaturation': stdSaturation,
                                 'avgValue': avgValue,
                                 'stdValue': stdValue
                             },
                         'hsv_unique': hsv_unique,
                         'lab_avg':
                             {
                                 'meanL': meanL,
                                 'stdL': stdL
                             },
                         'static_colour_clusters': static_colour_clusters,
                         'dynamic_colour_clusters': dynamic_colour_clusters,
                         'luminance_sd': luminance_sd,
                         'wave': wave,
                         'contour_density': contour_density,
                         'contour_congestion': contour_congestion,
                         'pixel_symmetry': pixel_symmetry,
                         'quadtree_decomposition':
                             {
                                 'balance': balance,
                                 'symmetry': symmetry,
                                 'equilibrium': equilibrium,
                                 'numberOfLeaves': numberOfLeaves
                             }
                         }

        return (metricsValues, execution_times)
