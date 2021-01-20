function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function plotpie(jstr){
  let boost = JSON.parse(jstr)
  let name = Object.keys(boost)
  let number = Object.values(boost)

  var data = [{
  values: number,
  labels: name,
  type: 'pie'
}];

var layout = {
  height: 400,
  width: 500
};


Plotly.newPlot('Pie', data, layout);
}


function plotline(jstr){
let boost = JSON.parse(jstr);
let xval = Object.keys(boost)
let yval = Object.values(boost)


var trace1 = {
  type: 'scatter',
  x: yval,
  y: xval,
  mode: 'markers',
  name: "Jason's by race",
  marker: {
    color: 'orange',
    line: {
      color: 'orange',
      width: 1,
    },
    symbol: 'star',
    size: 16
  }
};

var data = [trace1];

var layout = {
  title: '',
  xaxis: {
    showgrid: false,
    showline: true,
    linecolor: 'rgb(102, 102, 102)',
    titlefont: {
      font: {
        color: 'rgb(204, 204, 204)'
      }
    },
    tickfont: {
      font: {
        color: 'rgb(102, 102, 102)'
      }
    },
    autotick: false,
    dtick: 10,
    ticks: 'outside',
    tickcolor: 'rgb(102, 102, 102)'
  },
  margin: {
    l: 140,
    r: 40,
    b: 50,
    t: 80
  },
  legend: {
    font: {
      size: 10,
    },
    yanchor: 'middle',
    xanchor: 'right'
  },
  width: 600,
  height: 600,
  paper_bgcolor: 'white',
  plot_bgcolor: 'white',
  hovermode: 'closest'
};

Plotly.newPlot('Line', data, layout);
}


function greturn(){
  ajaxGetRequest('/piegraph', plotpie);
  ajaxGetRequest('/linegraph', plotline);
}