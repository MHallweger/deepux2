import pandas as pd
import json

class Recommendator:

    def __init__(self):
        self.mass_csv = self.readMassCSV()


    def readMassCSV(self):
        df_mass_csv = pd.read_csv("../data/mass_evaluations.csv", usecols=[
            'image', 'package_name',
            'distinct_rgb_values_value', 'distinct_rgb_values_meaning', 'distinct_rgb_values_evaluation',
            'figure_ground_contrast_value',
            'figure_ground_contrast_meaning', 'figure_ground_contrast_evaluation', 'white_space_value',
            'white_space_meaning', 'white_space_evaluation',
            'grid_quality_value', 'grid_quality_meaning', 'grid_quality_evaluation', 'colourfulness_value',
            'colourfulness_meaning', 'colourfulness_evaluation',
            'hsv_colours_avgSaturation_value', 'hsv_colours_avgSaturation_meaning', 'hsv_colours_avgSaturation_evaluation',
            'hsv_colours_stdSaturation_value',
            'hsv_colours_stdSaturation_meaning', 'hsv_colours_stdSaturation_evaluation', 'hsv_colours_avgValue_value',
            'hsv_colours_avgValue_meaning',
            'hsv_colours_avgValue_evaluation', 'hsv_colours_stdValue_value', 'hsv_colours_stdValue_meaning',
            'hsv_colours_stdValue_evaluation',
            'hsv_unique_value', 'hsv_unique_meaning', 'hsv_unique_evaluation', 'lab_avg_meanLEvaluation_value',
            'lab_avg_meanLEvaluation_meaning',
            'lab_avg_meanLEvaluation_evaluation', 'lab_avg_stdLEvaluation_value', 'lab_avg_stdLEvaluation_meaning',
            'lab_avg_stdLEvaluation_evaluation', 'static_colour_clusters_value',
            'static_colour_clusters_meaning', 'static_colour_clusters_evaluation', 'dynamic_colour_clusters_value',
            'dynamic_colour_clusters_meaning',
            'dynamic_colour_clusters_evaluation', 'luminance_sd_value', 'luminance_sd_meaning', 'luminance_sd_evaluation',
            'wave_value', 'wave_meaning', 'wave_evaluation', 'contour_density_value', 'contour_density_meaning',
            'contour_density_evaluation',
            'contour_congestion_value', 'contour_congestion_meaning', 'contour_congestion_evaluation',
            'pixel_symmetry_value',
            'pixel_symmetry_meaning', 'pixel_symmetry_evaluation', 'quadtree_decomposition_balance_value',
            'quadtree_decomposition_balance_meaning',
            'quadtree_decomposition_balance_evaluation', 'quadtree_decomposition_symmetry_value',
            'quadtree_decomposition_symmetry_meaning',
            'quadtree_decomposition_symmetry_evaluation', 'quadtree_decomposition_equilibrium_value',
            'quadtree_decomposition_equilibrium_meaning',
            'quadtree_decomposition_equilibrium_evaluation', 'quadtree_decomposition_numberOfLeaves_value',
            'quadtree_decomposition_numberOfLeaves_meaning',
            'quadtree_decomposition_numberOfLeaves_evaluation'
        ])

        return df_mass_csv
        
        #append_bad_metrics(df_mass_csv, dictMetricsEvaluation)

    def get_bad_metrics(self, metricsEvaluation):
        badMetrics = {}

        if metricsEvaluation['figure_ground_contrast']['evaluation'] == "bad":
            badMetrics["figure_ground_contrast_evaluation"] = "good"

        if metricsEvaluation['white_space']['evaluation'] == "bad":
            badMetrics["white_space_evaluation"] = "good"

        if metricsEvaluation['grid_quality']['evaluation'] == "bad":
            badMetrics["grid_quality_evaluation"] = "good"

        if metricsEvaluation['quadtree_decomposition']['symmetry']['evaluation'] == "bad":
            badMetrics["quadtree_decomposition_symmetry_evaluation"] = "good"

        if metricsEvaluation['quadtree_decomposition']['balance']['evaluation'] == "bad":
            badMetrics["quadtree_decomposition_balance_evaluation"] = "good"

        if metricsEvaluation['quadtree_decomposition']['equilibrium']['evaluation'] == "bad":
            badMetrics["quadtree_decomposition_equilibrium_evaluation"] = "good"

        if metricsEvaluation['quadtree_decomposition']['numberOfLeaves']['evaluation'] == "bad":
            badMetrics["quadtree_decomposition_numberOfLeaves_evaluation"] = "good"

        if metricsEvaluation['hsv_colours']['avgSaturation']['evaluation'] == "bad":
            badMetrics["hsv_colours_avgSaturation_evaluation"] = "good"

        if metricsEvaluation['hsv_colours']['stdSaturation']['evaluation'] == "bad":
            badMetrics["hsv_colours_stdSaturation_evaluation"] = "good"

        if metricsEvaluation['hsv_colours']['avgValue']['evaluation'] == "bad":
            badMetrics["hsv_colours_avgValue_evaluation"] = "good"

        if metricsEvaluation['hsv_colours']['stdValue']['evaluation'] == "bad":
            badMetrics["hsv_colours_stdValue_evaluation"] = "good"

        if metricsEvaluation['lab_avg']['stdLEvaluation']['evaluation'] == "bad":
            badMetrics["lab_avg_stdLEvaluation_evaluation"] = "good"

        if metricsEvaluation['luminance_sd']['evaluation'] == "bad":
            badMetrics["luminance_sd_evaluation"] = "good"

        if metricsEvaluation['wave']['evaluation'] == "bad":
            badMetrics["wave_evaluation"] = "good"

        if metricsEvaluation['contour_density']['evaluation'] == "bad":
            badMetrics["contour_density_evaluation"] = "good"

        if metricsEvaluation['contour_congestion']['evaluation'] == "bad":
            badMetrics["contour_congestion_evaluation"] = "good"

        if metricsEvaluation['pixel_symmetry']['evaluation'] == "bad":
            badMetrics["pixel_symmetry_evaluation"] = "good"

        return badMetrics
        #queryMetrics(mass_df, metricsEvaluation, badMetrics)

    def queryMetrics(self, mass_df, metricsEvaluation, badMetrics):
        queryString = ' distinct_rgb_values_evaluation == "' + metricsEvaluation['distinct_rgb_values']['evaluation'] + '"' \
                    + ' and figure_ground_contrast_evaluation == "' + metricsEvaluation['figure_ground_contrast'][
                        'evaluation'] + '"' \
                    + ' and white_space_evaluation == "' + metricsEvaluation['white_space']['evaluation'] + '"' \
                    + ' and grid_quality_evaluation == "' + metricsEvaluation['grid_quality']['evaluation'] + '"' \
                    + ' and colourfulness_evaluation == "' + metricsEvaluation['colourfulness']['evaluation'] + '"' \
                    + ' and hsv_colours_avgSaturation_evaluation == "' + \
                    metricsEvaluation['hsv_colours']['avgSaturation']['evaluation'] + '"' \
                    + ' and hsv_colours_stdSaturation_evaluation == "' + \
                    metricsEvaluation['hsv_colours']['stdSaturation']['evaluation'] + '"' \
                    + ' and hsv_colours_avgValue_evaluation == "' + metricsEvaluation['hsv_colours']['avgValue'][
                        'evaluation'] + '"' \
                    + ' and hsv_colours_stdValue_evaluation == "' + metricsEvaluation['hsv_colours']['stdValue'][
                        'evaluation'] + '"' \
                    + ' and hsv_unique_evaluation == "' + metricsEvaluation['hsv_unique']['evaluation'] + '"' \
                    + ' and lab_avg_meanLEvaluation_evaluation == "' + metricsEvaluation['lab_avg']['meanLEvaluation'][
                        'evaluation'] + '"' \
                    + ' and lab_avg_stdLEvaluation_evaluation == "' + metricsEvaluation['lab_avg']['stdLEvaluation'][
                        'evaluation'] + '"' \
                    + ' and static_colour_clusters_evaluation == "' + metricsEvaluation['static_colour_clusters'][
                        'evaluation'] + '"' \
                    + ' and dynamic_colour_clusters_evaluation == "' + metricsEvaluation['dynamic_colour_clusters'][
                        'evaluation'] + '"' \
                    + ' and luminance_sd_evaluation == "' + metricsEvaluation['luminance_sd']['evaluation'] + '"' \
                    + ' and wave_evaluation == "' + metricsEvaluation['wave']['evaluation'] + '"' \
                    + ' and contour_density_evaluation == "' + metricsEvaluation['contour_density']['evaluation'] + '"' \
                    + ' and contour_congestion_evaluation == "' + metricsEvaluation['contour_congestion'][
                        'evaluation'] + '"' \
                    + ' and pixel_symmetry_evaluation == "' + metricsEvaluation['pixel_symmetry']['evaluation'] + '"' \
                    + ' and quadtree_decomposition_balance_evaluation == "' + \
                    metricsEvaluation['quadtree_decomposition']['balance']['evaluation'] + '"' \
                    + ' and quadtree_decomposition_symmetry_evaluation == "' + \
                    metricsEvaluation['quadtree_decomposition']['symmetry']['evaluation'] + '"' \
                    + ' and quadtree_decomposition_equilibrium_evaluation == "' + \
                    metricsEvaluation['quadtree_decomposition']['equilibrium']['evaluation'] + '"' \
                    + ' and quadtree_decomposition_numberOfLeaves_evaluation == "' + \
                    metricsEvaluation['quadtree_decomposition']['numberOfLeaves']['evaluation'] + '"' \

        for keyFromBadMetrics in badMetrics:
            replacedQueryString = queryString.replace(keyFromBadMetrics + ' == \"bad\" ', keyFromBadMetrics + ' == \"good\" ')
            tmp_query_mass_df = mass_df.query(replacedQueryString)
            if not tmp_query_mass_df.empty:
                replacedKeyStringForMetricsEvaluation = keyFromBadMetrics.replace("_evaluation", "")

                imageValuesAsString = tmp_query_mass_df["image"].to_string(header=False, index=False).split('\n')
                commaSeperatedImageValuesAsString = [','.join(ele.split()) for ele in imageValuesAsString]

                if "quadtree_decomposition" not in replacedKeyStringForMetricsEvaluation \
                        and "hsv_colours" not in replacedKeyStringForMetricsEvaluation\
                        and "lav_avg" not in replacedKeyStringForMetricsEvaluation:
                    metricsEvaluation[replacedKeyStringForMetricsEvaluation].update(recommendations=commaSeperatedImageValuesAsString)
                else:
                    splittedKeyValue = replacedKeyStringForMetricsEvaluation.split('_')
                    metricsEvaluation[splittedKeyValue[0] + "_" + splittedKeyValue[1]][splittedKeyValue[2]].update(recommendations=commaSeperatedImageValuesAsString)

        return metricsEvaluation
        # with open('recommandation.json', 'w') as fp:
        #     json.dump(metricsEvaluation, fp)



    def getRecommendations(self, metricsEvaluation):
        bad_metrics = self.get_bad_metrics(metricsEvaluation)
        evals_with_recom = self.queryMetrics(self.mass_csv, metricsEvaluation, bad_metrics)
        return evals_with_recom

