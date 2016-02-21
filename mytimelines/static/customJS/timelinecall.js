var test = '{ "Timeline":[ {"Event":{ "Time":{ "Date":{ "Day": 23, "Month": 7, "Year": 2012 }, "TimeOfDay":{ "Hour": 16, "Minutes": 30, "Seconds": 40 } }, "Data":{ "Message": "Today was a good damn day", "Name": "My Birthday", "Icon": "76924374uh2l3r7hq23bnr4pd9q78e38g2w3jinr2p" } }}, {"Event":{ "Time":{ "Date":{ "Day": 2, "Month": 9, "Year": 2013 } }, "Data":{ "Message": "Today was a shit day", "Name": "Gym Day", "Icon": "76924374uh2l3r7hq23bnr4pd9q78e38g2w3jinr2p" } }}, {"Event":{ "Time":{ "Date":{ "Day": 2, "Month": 9, "Year": 2016 } }, "Data":{ "Message": "Today was a shit day", "Name": "Gym Day", "Icon": "76924374uh2l3r7hq23bnr4pd9q78e38g2w3jinr2p" } }} ] }'


/**
 * Created by Sparksmith on 2/21/2016.
 */
function initOptions(start, end) {
    var options = {
        "width": "100%",
        "height": "auto",
        "style": "box",
        "zoomMin": 10000,
        "min": new Date(start.Year - 1, start.Month - 1, start.Day),
        "max": new Date(end.Year + 1, end.Month - 1, end.Day)
    };
    return options
}

// init the data set
function initDataSet() {
    var data = new google.visualization.DataTable();
    data.addColumn('datetime', 'start');
    data.addColumn('datetime', 'end');
    data.addColumn('string', 'content');

    return data
}

function makeAJAXcall(){
    var id = document.URL.split("/")[4];
    $.get("/timelines/"+id+"/?"+Math.random(), function(data) {
        console.log(data);
        if (data.Timeline.length > 0) {
            drawTimeline(data, 'timeline');
        }
    });
}

// draw the thing!
function drawTimeline(json, divTarget) {
    object = json;

    data = initDataSet();
    options = initOptions(object.Timeline[0].Event.Time.Date, object.Timeline[object.Timeline.length - 1].Event.Time.Date);

    data = populateTimeline(data, object);

    var timeline = new links.Timeline(document.getElementById(divTarget));
    timeline.setOptions(options);
    timeline.draw(data);
}

function generateRow(obj) {
    //[new Date(obj.Timeline[i].Event.Time.Date.Year, obj.Timeline[i].Event.Time.Date.Month-1, obj.Timeline[i].Event.Time.Date.Day), , obj.Timeline[i].Event.Data.Name + '<br><br>' + obj.Timeline[i].Event.Data.Message]
    if (obj.Time.hasOwnProperty('TimeOfDay')) {
        if (obj.Data.hasOwnProperty('Icon')) {
            return [new Date(obj.Time.Date.Year, obj.Time.Date.Month - 1, obj.Time.Date.Day, obj.Time.TimeOfDay.Hour, obj.Time.TimeOfDay.Minutes, obj.Time.TimeOfDay.Seconds), , '<img src="' + obj.Data.Icon + '" style="width:32px; height:32px;">' + obj.Data.Name + '<br><br>' + obj.Data.Message + '<br>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Edit-50.png" style="width:28px;height:28px;margin-right:5px;"></a>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Link-50.png" style="width:28px;height:28px;margin-left: 5px;;"></a>']
        } else {
            return [new Date(obj.Time.Date.Year, obj.Time.Date.Month - 1, obj.Time.Date.Day, obj.Time.TimeOfDay.Hour, obj.Time.TimeOfDay.Minutes, obj.Time.TimeOfDay.Seconds), , obj.Data.Name + '<br><br>' + obj.Data.Message + '<br>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Edit-50.png" style="width:28px;height:28px;margin-right:5px;"></a>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Link-50.png" style="width:28px;height:28px;margin-left: 5px;;"></a>'];
        }
    } else {
        if (obj.Data.hasOwnProperty('Icon')) {
            return [new Date(obj.Time.Date.Year, obj.Time.Date.Month - 1, obj.Time.Date.Day), , '<img src="' + obj.Data.Icon + '" style="width:32px; height:32px;">' + obj.Data.Name + '<br><br>' + obj.Data.Message + '<br>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Edit-50.png" style="width:28px;height:28px;margin-right:5px;"></a>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Link-50.png" style="width:28px;height:28px;margin-left: 5px;;"></a>'];
        } else {
            return [new Date(obj.Time.Date.Year, obj.Time.Date.Month - 1, obj.Time.Date.Day), , obj.Data.Name + '<br><br>' + obj.Data.Message + '<br>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Edit-50.png" style="width:28px;height:28px;margin-right:5px;"></a>' + '<a href='+obj.Data.Url+'><img src="/static/icons/Link-50.png" style="width:28px;height:28px;margin-left: 5px;;"></a>'];
        }
    }
}

function populateTimeline(data, obj) {
    for (i = 0; i < obj.Timeline.length; i++) {
        data.addRow(generateRow(obj.Timeline[i].Event));
    }
    return data
}
