from tkinter import *
import tkinter.filedialog as fd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import metricscreator
import metricsevaluator
from core.utils import read_image
import matplotlib.pyplot as plt


def selectPictureAndEvaluate():
    path = fd.askopenfilename(filetypes=[("Image File", '.jpg')])
    metrics = metricsevaluator.MetricsEvaluator.getEvaluations(
        metricscreator.MetricsCreator.getMetrics(read_image(path)))
    print(metrics)
    makeDistinctRGBvaluesPlot(metrics)


def makeConclusionPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'distinct_rgb_values': metrics['distinct_rgb_values']['value'], 'figure_ground_contrast': metrics['figure_ground_contrast']['value'], 'white_space': metrics['white_space']['value'], 'grid_quality':  metrics['grid_quality']['value'],
            'colourfulness': metrics['colourfulness']['value'], 'avgSaturation': metrics['hsv_colours']['avgSaturation']['value'], 'stdSaturation': metrics['hsv_colours']['stdSaturation']['value'], 'avgValue': metrics['hsv_colours']['avgValue']['value'],
            'stdValue': metrics['hsv_colours']['stdValue']['value'], 'hsv_unique': metrics['hsv_unique']['value'], 'meanLEvaluation': metrics['lab_avg']['meanLEvaluation']['value'], 'stdLEvaluation': metrics['lab_avg']['stdLEvaluation']['value'],
            'static_colour_clusters': metrics['static_colour_clusters']['value'], 'dynamic_colour_clusters': metrics['dynamic_colour_clusters']['value'], 'luminance_sd': metrics['luminance_sd']['value'], 'wave': metrics['wave']['value'],
            'contour_density': metrics['contour_density']['value'], 'contour_congestion': metrics['contour_congestion']['value'], 'pixel_symmetry': metrics['pixel_symmetry']['value'], 'balance': metrics['quadtree_decomposition']['balance']['value'],
            'symmetry': metrics['quadtree_decomposition']['symmetry']['value'], 'equilibrium': metrics['quadtree_decomposition']['equilibrium']['value'], 'numberOfLeaves': metrics['quadtree_decomposition']['numberOfLeaves']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("")
    plt.title("Zusammenfassung")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeConclusionPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeenumberOfLeavesPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Good (bad)': 1500.00, 'Fair (normal)': 3200.00, 'Poor (bad)': 3201.00,
            'Your score: ' + metrics['quadtree_decomposition']['numberOfLeaves']['meaning'] + " (" + metrics['quadtree_decomposition']['numberOfLeaves'][
                'evaluation'] + ')': metrics['quadtree_decomposition']['numberOfLeaves']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.00 - 1500.00, Fair range = 1500 - 3200.00, Poor range = > 3200.00")
    plt.title("quadtree_decomposition: numberOfLeaves")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeConclusionPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeequilibriumPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Not centralized (bad)': 0.65, 'Centralized (good)': 00.66,
            'Your score: ' + metrics['quadtree_decomposition']['equilibrium']['meaning'] + " (" + metrics['quadtree_decomposition']['equilibrium'][
                'evaluation'] + ')': metrics['quadtree_decomposition']['equilibrium']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 0.65, Medium range = > 0.65")
    plt.title("quadtree_decomposition: equilibrium")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeenumberOfLeavesPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makesymmetryPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Poor (bad)': 00.50, 'Acceptable (good)': 00.51,
            'Your score: ' + metrics['quadtree_decomposition']['symmetry']['meaning'] + " (" + metrics['quadtree_decomposition']['symmetry'][
                'evaluation'] + ')': metrics['quadtree_decomposition']['symmetry']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 0.50, Medium range = > 0.50")
    plt.title("quadtree_decomposition: symmetry")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeequilibriumPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makebalancePlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Potential unbalanced (bad)': 00.65, 'Balanced (good)': 00.66,
            'Your score: ' + metrics['quadtree_decomposition']['balance']['meaning'] + " (" + metrics['quadtree_decomposition']['balance'][
                'evaluation'] + ')': metrics['quadtree_decomposition']['balance']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 0.65, Medium range = > 0.65")
    plt.title("quadtree_decomposition: balance")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makesymmetryPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makestdLPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Dark (normal)': 15.00, 'Medium (good)': 35.00, 'Light (normal)': 36.00,
            'Your score: ' + metrics['lab_avg']['stdLEvaluation']['meaning'] + " (" + metrics['lab_avg']['stdLEvaluation'][
                'evaluation'] + ')': metrics['lab_avg']['stdLEvaluation']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 15.00, Medium range = 15.01 - 35.00, High range = > 35.00")
    plt.title("Lab_avg: stdL")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makebalancePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makemeanLPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Dark (normal)': 40.00, 'Medium (good)': 75.00, 'Light (normal)': 76.00,
            'Your score: ' + metrics['lab_avg']['meanLEvaluation']['meaning'] + " (" + metrics['lab_avg']['meanLEvaluation'][
                'evaluation'] + ')': metrics['lab_avg']['meanLEvaluation']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 40.00, Medium range = 40.01 - 75.00, High range = > 75.00")
    plt.title("Lab_avg: meanL")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makestdLPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makestdValuePlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Low (bad)': 0.15, 'Medium (good)': 0.35, 'High (bad)': 0.36,
            'Your score: ' + metrics['hsv_colours']['stdValue']['meaning'] + " (" + metrics['hsv_colours']['stdValue'][
                'evaluation'] + ')': metrics['hsv_colours']['stdValue']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.00 - 0.15, Medium range = 0.16 - 0.35, High range = > 0.35")
    plt.title("HSV_avg: stdValue")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makemeanLPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeavgValuePlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Dark (bad)': 0.40, 'Medium (good)': 0.80, 'Light (bad)': 0.81,
            'Your score: ' + metrics['hsv_colours']['avgValue']['meaning'] + " (" + metrics['hsv_colours']['avgValue'][
                'evaluation'] + ')': metrics['hsv_colours']['avgValue']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Dark range = 0.0 - 0.40, Medium range = 0.41 - 0.80, Light range = > 0.80")
    plt.title("HSV_avg: avgValue")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makestdValuePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makestdSaturationPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Low (bad)': 0.20, 'Medium (good)': 0.40, 'High (bad)': 0.41,
            'Your score: ' + metrics['hsv_colours']['stdSaturation']['meaning'] + " (" +
            metrics['hsv_colours']['stdSaturation'][
                'evaluation'] + ')': metrics['hsv_colours']['stdSaturation']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.0 - 0.20, Medium range = 0.21 - 0.40, High range = > 0.40")
    plt.title("HSV_avg: stdSaturation")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeavgValuePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeavgSaturationPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Low (bad)': 0.10, 'Medium (good)': 0.60, 'High (bad)': 0.61,
            'Your score: ' + metrics['hsv_colours']['avgSaturation']['meaning'] + " (" +
            metrics['hsv_colours']['avgSaturation'][
                'evaluation'] + ')': metrics['hsv_colours']['avgSaturation']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.0 - 0.10, Medium range = 0.11 - 0.60, High range = > 0.60")
    plt.title("HSV_avg: avgSaturation")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makestdSaturationPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makepixel_symmetryPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Good (good)': 1.00, 'Poor (bad)': 1.01,
            'Your score: ' + metrics['pixel_symmetry']['meaning'] + " (" + metrics['pixel_symmetry'][
                'evaluation'] + ')': metrics['pixel_symmetry']['value']}

    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.0 - 1.00, Poor range = > 1.00")
    plt.title("Pixel_symmetry")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeavgSaturationPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makecontour_congestionPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Good (good)': 0.25, 'Fair (normal)': 0.50, 'Poor (bad)': 0.51,
            'Your score: ' + metrics['contour_congestion']['meaning'] + " (" + metrics['contour_congestion'][
                'evaluation'] + ')': metrics['contour_congestion']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.0 - 0.25, Fair range = 0.26 - 0.50, Poor range = > 0.50")
    plt.title("Contour_congestion")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makepixel_symmetryPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeContour_densityPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Good (good)': 0.12, 'Fair (normal)': 0.22, 'Poor (bad)': 0.23,
            'Your score: ' + metrics['contour_density']['meaning'] + " (" + metrics['contour_density'][
                'evaluation'] + ')': metrics['contour_density']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.0 - 0.12, Fair range = 0.13 - 0.22, Poor range = > 0.22")
    plt.title("Contour_density")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makecontour_congestionPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makewavePlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Low (bad)': 0.54, 'Good (good)': 0.55,
            'Your score: ' + metrics['wave']['meaning'] + " (" + metrics['wave'][
                'evaluation'] + ')': metrics['wave']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.0 - 0.54, Good range = > 0.54")
    plt.title("Wave")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeContour_densityPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeluminance_sdPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Less colourful (normal)': 60, 'Fair (normal)': 90, 'Colourful (normal)': 91,
            'Your score: ' + metrics['luminance_sd']['meaning'] + " (" + metrics['luminance_sd'][
                'evaluation'] + ')': metrics['luminance_sd']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.0 - 60, Acceptable range = 60.01 - 90, Potential varied range = > 90")
    plt.title("luminance_sd")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makewavePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeDynamic_colour_clustersPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Less colourful (normal)': 500, 'Fair (normal)': 1000, 'Colourful (normal)': 1001,
            'Your score: ' + metrics['dynamic_colour_clusters']['meaning'] + " (" + metrics['dynamic_colour_clusters'][
                'evaluation'] + ')': metrics['dynamic_colour_clusters']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Less colourful range = 0.0 - 500, Fair range = 501 - 1000, Colourful range = > 1000")
    plt.title("DynamicColourClusters")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeluminance_sdPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeStaticColourClustersPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Less colourful (normal)': 50, 'Fair (normal)': 100, 'Colourful (normal)': 101,
            'Your score: ' + metrics['static_colour_clusters']['meaning'] + " (" + metrics['static_colour_clusters'][
                'evaluation'] + ')': metrics['static_colour_clusters']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Less colourful range = 0.0 - 4000, Fair range = 40001 - 8000, Colourful range = > 80001")
    plt.title("StaticColourClusters")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeDynamic_colour_clustersPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makehsv_uniquePlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Good (good)': 2000, 'Potential varied (normal)': 20001,
            'Your score: ' + metrics['hsv_unique']['meaning'] + " (" + metrics['hsv_unique'][
                'evaluation'] + ')': metrics['hsv_unique']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Good range = 0.0 - 20000, Potential varied range = > 2000")
    plt.title("hsv_unique")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeStaticColourClustersPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makecolourfulnessPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Less colourful (normal)': 50, 'Fair (normal)': 100, 'Colourful (normal)': 101,
            'Your score: ' + metrics['colourfulness']['meaning'] + " (" + metrics['colourfulness'][
                'evaluation'] + ')': metrics['colourfulness']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Less colourful range = 0.0 - 50, Fair range = 50.01 - 100, Colourful range = >100")
    plt.title("Colourfulness")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makehsv_uniquePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makegrid_qualityPlot(metrics, plotWindow):
    plotWindow.destroy()

    data = {'Low (bad)': 100, 'Medium (good)': 220, 'High (bad)': 221,
            'Your score: ' + metrics['grid_quality']['meaning'] + " (" + metrics['grid_quality'][
                'evaluation'] + ')': metrics['grid_quality']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.0 - 100, Medium range = 101 - 220, High range = else")
    plt.title("Grid_quality")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makecolourfulnessPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeWhite_spacePlot(metrics, plotWindow):
    plotWindow.destroy()
    data = {'Low (bad)': 0.3, 'High (bad)': 0.81, 'Good (good)': 0.31,
            'Your score: ' + metrics['white_space']['meaning'] + " (" + metrics['white_space'][
                'evaluation'] + ')': metrics['white_space']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Low range = 0.0 - 0.3, High range = 0.31 - 0.8, Good range = else")
    plt.title("white_space")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makegrid_qualityPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeFigure_ground_contrastPlot(metrics, plotWindow):
    plotWindow.destroy()
    data = {'High Contrast (bad)': 0.71, 'Low Contrast (bad)': 0.29, 'Fair (good)': 0.5,
            'Your score: ' + metrics['figure_ground_contrast']['meaning'] + " (" + metrics['figure_ground_contrast'][
                'evaluation'] + ')': metrics['figure_ground_contrast']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("High Contrast range = > 0.7, Low Contrast range = <= 0.3, Fair (good) range = > 0.3 and < 0.7")
    plt.title("figure_ground_contrast")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeWhite_spacePlot(metrics, plotWindow))
    btnNext.pack(side="bottom")

    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


def makeDistinctRGBvaluesPlot(metrics):
    data = {'Less colourful (normal)': 5000, 'colourful (normal)': 15001, 'Fair (good)': 15002,
            'Your score: ' + metrics['distinct_rgb_values']['meaning'] + " (" + metrics['distinct_rgb_values'][
                'evaluation'] + ')': metrics['distinct_rgb_values']['value']}
    keys = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(keys, values, color='maroon',
            width=0.4)

    plt.xlabel("Less colourful range = 0-5000, colourful range = 5001-15001, Fair (good) range = <15001")
    plt.title("Distinct RGB values")

    plotWindow = Toplevel(mainWindow)
    btnNext = Button(plotWindow, text="Next", height=7, width=40,
                     command=lambda: makeFigure_ground_contrastPlot(metrics, plotWindow))
    btnNext.pack(side="bottom")
    canvas = FigureCanvasTkAgg(fig, master=plotWindow)
    canvas.get_tk_widget().pack()
    canvas.draw()


mainWindow = Tk()
btnSelectPicture = Button(mainWindow, text="Bild auswählen", height=15, width=40,
                          command=lambda: selectPictureAndEvaluate())
btnEvaluateFromEmulator = Button(mainWindow, text="Von Emulator screenshotten", height=15, width=40,
                                 command=lambda: selectPictureAndEvaluate)
btnSelectPicture.pack(side="top", fill="x")
btnEvaluateFromEmulator.pack(side="bottom", fill="both", expand=True)
mainWindow.mainloop()
