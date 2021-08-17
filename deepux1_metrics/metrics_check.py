import json
from deepux1_metrics.ux1.src.test import process_single_image

# Bools for UI
distinct_rgb_values = True
figure_ground_contrast = True
white_space = True
grid_quality = True
colourfulness = True
hsv_colours = True
hsv_unique = True
lab_avg = True
static_colour_clusters = True
dynamic_colour_clusters = True
luminance_sd = True
wave = True
contour_density = True
contour_congestion = True
pixel_symmetry = True
quadtree_decomposition = True

choosen_percentage = 50  # Accuracy

using_metrics_list = []  # Contains all choosen metrics
evaluation_list = []  # Contains all evaluation-values


def check_metrics(image_name, firstStart):

    if(firstStart):
        __init__()

    start_string = str(process_single_image(image_name))

    singleToDoubleQuote = start_string.replace("'", "\"")
    json_object = json.loads(singleToDoubleQuote)

    evaluation_amount = 0  # Real evaluation Amount
    evaluation_percentage = 0  # Real evaluation percentage Amount
    best_possible_evaluation_amount = 0  # Use case: All evaluation values are "Good"
    pairs = json_object.items()

    for key, value in pairs:
        if key != "hsv_colours" and key != "lab_avg" and key != "quadtree_decomposition":
            if key in using_metrics_list:
                evaluation_list.append(value["evaluation"])
        else:
            if key in using_metrics_list:
                if key == "hsv_colours":
                    evaluation_list.append(value["avgSaturation"]["evaluation"])
                    evaluation_list.append(value["stdSaturation"]["evaluation"])
                    evaluation_list.append(value["avgValue"]["evaluation"])
                    evaluation_list.append(value["stdValue"]["evaluation"])
                elif key == "lab_avg":
                    evaluation_list.append(value["meanLEvaluation"]["evaluation"])
                    evaluation_list.append(value["stdLEvaluation"]["evaluation"])
                elif key == "quadtree_decomposition":
                    evaluation_list.append(value["balance"]["evaluation"])
                    evaluation_list.append(value["symmetry"]["evaluation"])
                    evaluation_list.append(value["equilibrium"]["evaluation"])
                    evaluation_list.append(value["numberOfLeaves"]["evaluation"])

    for eval in evaluation_list:
        if eval == "good":
            evaluation_amount += 2
        if eval == "normal":
            evaluation_amount += 1

    best_possible_evaluation_amount = len(evaluation_list) * 2
    evaluation_percentage = (100 / best_possible_evaluation_amount) * evaluation_amount

    if evaluation_percentage >= choosen_percentage:
        print("Ausgewählter Prozentsatz: " + str(choosen_percentage) + str("%"))
        print("Best möglicher zu erreichender Wert: " + str(best_possible_evaluation_amount))
        print("Erreichter Wert: " + str(evaluation_amount))
        print("Ergebnis: Dieses Bild ist gut!" + str(" (") + str("{:.2f}".format(evaluation_percentage)) + str("%)"))
        evaluation_amount = 0  # Real evaluation Amount
        best_possible_evaluation_amount = 0  # Use case: All evaluation values are "Good"
        return evaluation_percentage
    else:
        print("Ausgewählter Prozentsatz: " + str(choosen_percentage))
        print("Best möglicher zu erreichender Wert: " + str(best_possible_evaluation_amount))
        print("Erreichter Wert: " + str(evaluation_amount))
        print("Ergebnis: Dieses Bild ist schlecht!" + str(" (") + str("{:.2f}".format(evaluation_percentage)) + str("%)"))
        evaluation_amount = 0  # Real evaluation Amount
        best_possible_evaluation_amount = 0  # Use case: All evaluation values are "Good"
        return evaluation_percentage


def __init__():
    if distinct_rgb_values:
        using_metrics_list.append("distinct_rgb_values")
    if figure_ground_contrast:
        using_metrics_list.append("figure_ground_contrast")
    if white_space:
        using_metrics_list.append("white_space")
    if grid_quality:
        using_metrics_list.append("grid_quality")
    if colourfulness:
        using_metrics_list.append("colourfulness")
    if hsv_colours:
        using_metrics_list.append("hsv_colours")
    if hsv_unique:
        using_metrics_list.append("hsv_unique")
    if lab_avg:
        using_metrics_list.append("lab_avg")
    if static_colour_clusters:
        using_metrics_list.append("static_colour_clusters")
    if dynamic_colour_clusters:
        using_metrics_list.append("dynamic_colour_clusters")
    if luminance_sd:
        using_metrics_list.append("luminance_sd")
    if wave:
        using_metrics_list.append("wave")
    if contour_density:
        using_metrics_list.append("contour_density")
    if contour_congestion:
        using_metrics_list.append("contour_congestion")
    if pixel_symmetry:
        using_metrics_list.append("pixel_symmetry")
    if quadtree_decomposition:
        using_metrics_list.append("quadtree_decomposition")

    print(str("Ausgewählte Metriken: " + str(len(using_metrics_list)) + str(" (") + str(using_metrics_list) + str(")")))


if __name__ == '__main__':
    __init__()