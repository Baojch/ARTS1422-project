<!-- rivermap -->
<template>
  <div class="middlemiddlepart">
    {{ gameid }}
    <div ref="chart1" style="width: 500px; height: 250px;" class="chart1"></div>
    <div ref="chart2" style="width: 500px; height: 250px;" class="chart2"></div>
  </div>
</template>

<script>
import bus from '../utils/bus';
import * as echarts from 'echarts';
import * as d3 from 'd3';

export default {
  data () {
    return {
      gameid: -1,
      myChart1: null,
      myChart2: null,
      start: '',
      end: '',
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      console.log(gameid);
      this.gameid = gameid;
    });
    bus.on('stylename', (stylename) => {
      console.log(stylename);
      this.stylename = stylename;
      this.initChart1();
      this.initChart2();
      this.updateChart1();
      this.updateChart2();
    });
  },
  methods: {
    initChart1() {
      this.myChart1 = echarts.init(this.$refs.chart1);
    },
    initChart2(){
      this.myChart2 = echarts.init(this.$refs.chart2);
    },
    updateChart1() {
      var that = this;
      const data = d3.csv(`../../assets/processed_output_emotion_by_gameid/processed_emotion_${this.gameid}.csv`);
      
      data.then(function(data) {
        console.log(data)
        const date = data.map(row => row['date']);
        that.start = data[0];
        that.end = data[-1];
        console.log(this.start);
        const compound = data.map(row => parseFloat(row['compound']));
        const neg = data.map(row => parseFloat(row['neg']));
        const neu = data.map(row => parseFloat(row['neu']));
        const pos = data.map(row => parseFloat(row['pos']));
        const option = {
        title: {
          text: 'Chosen'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['compound', 'negative', 'neutral', 'positive']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: date,
            axisPointer: {
              label: {
                formatter: function (params) {
                  // 在这里可以获取鼠标在时间轴上的时间值
                  bus.emit('timestamp', params.value);
                  return 'time:' + params.value;
                }
              }
            },
            onclick: function(params) {
              var clickedTime = params.value; // 获取点击的时间值
              return 'Clicked time:', clickedTime;
              // 在这里可以将点击的时间值记录下来或进行其他操作
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'compound',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgb(128, 255, 165)' },
                { offset: 1, color: 'rgb(1, 191, 236)' }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: compound
          },

    {
      name: 'negative',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(0, 221, 255)'
          },
          {
            offset: 1,
            color: 'rgb(77, 119, 255)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: neg
    },
    {
      name: 'neutral',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(55, 162, 255)'
          },
          {
            offset: 1,
            color: 'rgb(116, 21, 219)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: neu
    },
    {
      name: 'positive',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        {
            offset: 0,
            color: 'rgb(255, 191, 0)'
          },
          {
            offset: 1,
            color: 'rgb(224, 62, 76)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: pos
    },
          // Include other series data here...
        ]
      };
      that.myChart1.setOption(option);
    })
    

      
    },
    updateChart2() {
      var that = this;
      const data = d3.csv(`../../assets/processed_output_emotion_by_gameid/processed_emotion_${this.gameid}.csv`);
      
      data.then(function(data) {
        console.log(data)
        const date = data.map(row => row['date']);
        this.start = data[0];
        this.end = data[-1];
        console.log(this.start);
        const compound = data.map(row => parseFloat(row['compound']));
        const neg = data.map(row => parseFloat(row['neg']));
        const neu = data.map(row => parseFloat(row['neu']));
        const pos = data.map(row => parseFloat(row['pos']));
        const option = {
        title: {
          text: 'Chosen'
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'cross',
            label: {
              backgroundColor: '#6a7985'
            }
          }
        },
        legend: {
          data: ['compound', 'negative', 'neutral', 'positive']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            boundaryGap: false,
            data: date,
            axisPointer: {
              label: {
                formatter: function (params) {
                  // 在这里可以获取鼠标在时间轴上的时间值
                  bus.emit('timestamp', params.value);
                  return 'time:' + params.value;
                }
              }
            },
            onclick: function(params) {
              var clickedTime = params.value; // 获取点击的时间值
              return 'Clicked time:', clickedTime;
              // 在这里可以将点击的时间值记录下来或进行其他操作
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'compound',
            type: 'line',
            stack: 'Total',
            smooth: true,
            lineStyle: {
              width: 0
            },
            showSymbol: false,
            areaStyle: {
              opacity: 0.8,
              color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                { offset: 0, color: 'rgb(128, 255, 165)' },
                { offset: 1, color: 'rgb(1, 191, 236)' }
              ])
            },
            emphasis: {
              focus: 'series'
            },
            data: compound
          },

    {
      name: 'negative',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(0, 221, 255)'
          },
          {
            offset: 1,
            color: 'rgb(77, 119, 255)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: neg
    },
    {
      name: 'neutral',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
          {
            offset: 0,
            color: 'rgb(55, 162, 255)'
          },
          {
            offset: 1,
            color: 'rgb(116, 21, 219)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: neu
    },
    {
      name: 'positive',
      type: 'line',
      stack: 'Total',
      smooth: true,
      lineStyle: {
        width: 0
      },
      showSymbol: false,
      areaStyle: {
        opacity: 0.8,
        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
        {
            offset: 0,
            color: 'rgb(255, 191, 0)'
          },
          {
            offset: 1,
            color: 'rgb(224, 62, 76)'
          }
        ])
      },
      emphasis: {
        focus: 'series'
      },
      data: pos
    },
          // Include other series data here...
        ]
      };
      that.myChart1.setOption(option);
    })
    

      
    }

  }
};
</script>

<style>
.container {
  position: relative;
  top: 0;
  right: 0;
  width: 50%;
  height: 50%;
}

/* .chart {
  position: absolute;
  top: 0;
  right: 0;
  width: 50%;
  height: 50%;
} */

</style>
