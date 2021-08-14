
function getNodeEvaluations(nodeImage) {
    var uxNode = getNodeByImage(nodeImage);
    if(uxNode === undefined) return "";

    var evalInfo = "<table class=\"table table-striped\">";
    evalInfo += "<tr class=\"active\"><th colspan=\"4\"><h4>Metric Evaluations</h4></th></tr>"
    evalInfo += "<tr><th>Metric</th><th>Evaluation</th><th>Meaning</th></tr>";

    for (const [metric, eval] of Object.entries(uxNode.evaluations)) {
        if(eval.value === undefined) {
            for (const [subMetric, subEval] of Object.entries(eval)) {
                evalInfo += getMetricListEntry(nodeImage, metric+"_"+subMetric, subEval);
            }
        } else {
            evalInfo += getMetricListEntry(nodeImage, metric, eval);
        }
    }
    evalInfo += "</table>"

    return evalInfo;
}

function getMetricListEntry(nodeImage, metric, eval) {
    listEntry = "";
    listEntry += "<td style='vertical-align: middle;'><button class='metricTableButton' value='"+nodeImage+"|"+metric+"' onClick=showMetricDetails(this)>"+metric+"</button></td>";
    listEntry += "<td><div class=\"metricTableLabel\" style='background:"+getMetricColor(eval.evaluation)+";'>"+eval.evaluation+"</div></td>";
    listEntry += "<td style='vertical-align: middle;'>"+eval.meaning+"</td>";
    listEntry += "</tr>";
    return listEntry;
}

function getMetricColor(evaluation) {
    var color = "#FFFFFF";
    switch (evaluation) {
        case "good":
            color = "#2ca317";
            break;
        case "bad":
            color = "#e01f1f";            
            break;
        default:
            color = "#707070";
            break;
    }
    return color;
}

function getNodeByImage(nodeImage) {
    if(evaluations === undefined) return undefined;

    var nodeImage = nodeImage.split("states\\")[1];
    for (var i = 0; i < evaluations.length; i++) {
        if (evaluations[i].image == nodeImage) {
            return evaluations[i];
        }
    }
}

function showMetricDetails(btn) {
    var [nodeImage, metricName, subMetric] = btn.value.split("|");
    var utg_details = document.getElementById('utg_details');
    var uxNode = getNodeByImage(nodeImage);
    var metricDetails = uxNode.evaluations[metricName];
    var description = metricDescriptions[metricName]?.infoText;

    //Submetric
    if(metricDetails === undefined) {
        var splitName = metricName.split("_");
        var subMetric = splitName.pop();
        var mainMetric = splitName.join("_");
        metricDetails = uxNode.evaluations[mainMetric][subMetric];
        description = metricDescriptions[mainMetric][subMetric]?.infoText;
    }

    var detailsInfo = "<h2>"+prettyMetricName(metricName)+"</h2><hr/>";
    detailsInfo += "<div>";
    detailsInfo += "    <img class='col-md-5' src=\"" + nodeImage + "\">"
    detailsInfo += "    <h3 style='margin-top: 0px'>Description</h3>";
    detailsInfo += "    <p>"+description+"</p><hr/>";
    detailsInfo += "    <table class='table' style='display: block;'>";
    detailsInfo += "        <tr><th style='vertical-align: middle;'>evaluation</th>";
    detailsInfo += "            <td><div class=\"metricTableLabel\" style='background:"+getMetricColor(metricDetails.evaluation)+";'>"+metricDetails.evaluation+"</div></td></tr>";
    detailsInfo += "        <tr><th>meaning</th><td>"+metricDetails.meaning+"</td></tr>";
    detailsInfo += "        <tr><th>value</th><td>"+metricDetails.value+"</td></tr>";
    detailsInfo += "    </table>";
    detailsInfo += "</div>";
    detailsInfo += "<div class='metricDistribution'>";
    detailsInfo += "    <div class='recomContainer'>";
    detailsInfo +=          getRecommendationHTML(metricDetails);
    detailsInfo += "    </div>";
    detailsInfo += "    <div>";
    detailsInfo += "        <h3>Histogram</h3>";
    detailsInfo += "        <img style='padding-bottom: 10px;' src='diagrams\\metricDistribution\\"+metricName+"_value.png'>";
    detailsInfo += "        <p>The histogram shows the result of this metric for other app screenshots of the rico dataset.";
    detailsInfo += "        The dataset was retrieved from <a target='_blank' rel='noopener noreferrer' href='http://interactionmining.org/rico'>http://interactionmining.org/rico</a>"
    detailsInfo += "        on January 11, 2021 and partially analysed on Febuary 17, 2021.</p>";
    detailsInfo += "    </div>";
    detailsInfo += "</div>";
    detailsInfo += "";

    utg_details.innerHTML = detailsInfo;
}

function prettyMetricName(metricName) {
    var split = metricName.split("_");
    split = split.map(x => x.charAt(0).toUpperCase() + x.slice(1))
    return split.join(" ");
}

function getRecommendationHTML(metricDetails) {
    var recoms = metricDetails.recommendations;

    var recomHtml = "<h3>Recommendations</h3>";
    if (metricDetails.evaluation === "good" || metricDetails.evaluation === "normal") {
        recomHtml += "<p>This metric on your image has not been rated bad. Nothing to worry about.</p>";
        return recomHtml;
    }
    if (recoms === undefined || recoms.length <= 0) {
        recomHtml += "<p>Unfortunately we can not give you any recommendation for this metric on your current image.</p>";
        return recomHtml;
    }

    recomHtml += "<p>Take a look at the images below to get a feeling what you can do better.</p>";
    for (i = 0; i < recoms.length; i++) {
        if(i >= 3) break;
        recomHtml += "<img src='recommendations\\"+recoms[i]+"'>";
    }
    return recomHtml;
}