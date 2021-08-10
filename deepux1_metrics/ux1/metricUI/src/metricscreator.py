import metrics.distinct_rgb_values as metric_distinct_rgb_values
import metrics.figure_ground_contrast as metric_figure_ground_contrast
import metrics.white_space as metric_white_space
import metrics.grid_quality as metric_grid_quality
import metrics.colourfulness as metric_colourfulness
import metrics.HSV_avg as metric_hsv_avg
import metrics.HSV_unique as metric_hsv_unique
import metrics.LAB_avg as metrics_lab_avg
import metrics.static_colour_clustering as metrics_static_colour_clustering
import metrics.dynamic_colour_clustering as metrics_dynamic_colour_clustering
import metrics.luminance_sd as metrics_luminance_sd
import metrics.wave as metrics_wave
import metrics.contour_density as metrics_contour_density
import metrics.contour_congestion as metrics_contour_congestion
import metrics.pixel_symmetry as metrics_pixel_symmetry
import metrics.quadtree_decomposition as metrics_quadtree_decomposition


class MetricsCreator:
    """
    Creates Metrics for a given base64 Input
    """

    @staticmethod
    def getMetrics(pictureAsBase64: str):
        # Anzahl der Farben im RGB Farbraum
        distinct_rgb_values = metric_distinct_rgb_values.Metric3.execute_metric(pictureAsBase64)

        # Unterscheidbarkeit des vordergrunds anhand des Kontrasts
        figure_ground_contrast = metric_figure_ground_contrast.Metric5.execute_metric(pictureAsBase64)

        # Weißer Raum
        white_space = metric_white_space.execute(pictureAsBase64)

        # Gitter Qualität
        grid_quality = metric_grid_quality.execute(pictureAsBase64)

        # Colourfulness
        colourfulness = metric_colourfulness.execute(pictureAsBase64)

        # hsv_colours
        hsv_avg = metric_hsv_avg.execute(pictureAsBase64)
        avgSaturation = hsv_avg[0]
        stdSaturation = hsv_avg[1]
        avgValue = hsv_avg[2]
        stdValue = hsv_avg[3]

        # hsv unique
        hsv_unique = metric_hsv_unique.execute(pictureAsBase64)

        # lab avg
        lab_avg = metrics_lab_avg.execute(pictureAsBase64)

        meanL = lab_avg[0]
        stdL = lab_avg[1]

        static_colour_clusters = metrics_static_colour_clustering.execute(pictureAsBase64)

        dynamic_colour_clusters = metrics_dynamic_colour_clustering.execute(pictureAsBase64)

        luminance_sd = metrics_luminance_sd.execute(pictureAsBase64)

        wave = metrics_wave.execute(pictureAsBase64)

        contour_density = metrics_contour_density.Metric4.execute(pictureAsBase64)

        contour_congestion = metrics_contour_congestion.Metric6.execute(pictureAsBase64)

        pixel_symmetry = metrics_pixel_symmetry.execute(pictureAsBase64)

        quadtree_decomposition = metrics_quadtree_decomposition.execute(pictureAsBase64)

        balance = quadtree_decomposition[0]
        symmetry = quadtree_decomposition[1]
        equilibrium = quadtree_decomposition[2]
        numberOfLeaves = quadtree_decomposition[3]

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

        return metricsValues
