<!-- rivermap -->
<template>
  <div class="middlemiddlepart">
    <div ref="chart1" style="width: 60%; height: 50%;" class="chart1"></div>
    <div ref="chart2" style="width: 60%; height: 50%;" class="chart2"></div>
    <div ref="piechart1" style="width: 40%; height: 50%;" class="piechart1"></div>
    <div ref="piechart2" style="width: 40%; height: 50%;" class="piechart2"></div>
  </div>
</template>

<script>
import bus from '../utils/bus';
import * as echarts from 'echarts';
import * as d3 from 'd3';
import d3Tip from 'd3-tip';

export default {
  data () {
    return {
      gameid: -1,
      stylename: "unknown",
      myChart1: null,
      myChart2: null,
      mypieChart1: null,
      mypieChart2: null,
      time: '',
      start: '',
      end: '',
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      // console.log(gameid);
      this.gameid = gameid;
      
    });
    bus.on('stylename', (stylename) => {
      // console.log(stylename);
      this.stylename = stylename;
      this.initChart1();
      this.initChart2();
      this.initpieChart1();
      this.initpieChart2();
      this.updateChart1();
      this.$nextTick(() => {
        this.updateChart2();
        this.updatepieChart1();
        this.updatepieChart2();
      });
    });
    bus.on('timestamp', (timestamp) => {
      console.log("收到:"+timestamp);
      this.time = timestamp;
      console.log(this.time);
      this.initpieChart1();
      this.updatepieChart1();
      this.initpieChart2();
      this.updatepieChart2();
    });
  
    
  },
  methods: {
    initChart1() {
      this.myChart1 = echarts.init(this.$refs.chart1);
    },
    initChart2(){
      this.myChart2 = echarts.init(this.$refs.chart2);
    },
    initpieChart1(){
      this.mypieChart1 = echarts.init(this.$refs.piechart1);
    },
    initpieChart2(){
      this.mypieChart2 = echarts.init(this.$refs.piechart2);
    },
    updateChart1() {
      var that = this;
      const data = d3.csv(`../../assets/processed_output_emotion_by_gameid/processed_emotion_${this.gameid}.csv`);
      
      data.then(function(data) {
        // console.log(data)
        const date = data.map(row => row['date']);
        that.start = data[0].date;
        that.end = data[date.length - 1].date;
        bus.emit('timestamp', data[0].date);
        // console.log(that.start);
        // console.log(that.end);
        const compound1 = data.map(row => parseFloat(row['compound']));
        const neg1 = data.map(row => parseFloat(row['neg']));
        const neu1 = data.map(row => parseFloat(row['neu']));
        const pos1 = data.map(row => parseFloat(row['pos']));
        const option1 = {
          title: {
            text: 'Chosen',
            textStyle: {
                color: 'white', // 设置字体颜色为红色
                fontSize: 30 // 设置字体大小为12px
                // 可以添加其他字体样式属性
              }
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
            top: 10,
            left: '28%',
            data: ['positive', 'negative', 'neutral', 'praise'],
            textStyle: {
                color: 'white',
                fontSize: 12 // 设置字体大小为12px
                // 可以添加其他字体样式属性
              }
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
                          bus.emit('timestamp', params.value);
                          that.time = params.value;
                          console.log(that.time);
                          return 'time:' + params.value;
                      }
                  }
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
                  { offset: 0, color: 'rgb(128, 255, 165)' },
                  { offset: 1, color: 'rgb(1, 191, 236)' }
                ])
              },
              emphasis: {
                focus: 'series'
              },
              data: compound1
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
        data: neg1
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
        data: neu1
      },
      {
        name: 'praise',
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
        data: pos1
      },
            // Include other series data here...
          ]
        };
        that.myChart1.setOption(option1);
      })
    },
    updateChart2() {
      var that = this;
      var data1 = d3.json(`../../assets/average_processed_output_emotion/${this.stylename}.json`);
      
      data1.then(function(data) {
        // console.log(data)
        data = data.filter(row => row['date'] >= that.start && row['date'] <= that.end);
        // console.log(data)
        const date = data.map(row => row['date']);
        // console.log(that.start);
        // console.log(that.end);
        const compound = data.map(row => parseFloat(row['compound']));
        // console.log(compound);
        const neg = data.map(row => parseFloat(row['neg']));
        const neu = data.map(row => parseFloat(row['neu']));
        const pos = data.map(row => parseFloat(row['pos']));
        const option = {
        title: {
          text: 'Average',
          textStyle: {
                color: 'white', // 设置字体颜色为红色
                fontSize: 30 // 设置字体大小为12px
                // 可以添加其他字体样式属性
              }
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
          top: 10,
          left: '28%',
          data: ['positive', 'negative', 'neutral', 'praise'],
          textStyle: {
                color: 'white', // 设置字体颜色为红色
                fontSize: 12 // 设置字体大小为12px
                // 可以添加其他字体样式属性
              }
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
            data: date
          }
        ],
        yAxis: [
          {
            type: 'value',
            inverse: true // 将图表倒过来
          }
        ],
        series: [
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
      name: 'praise',
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
      that.myChart2.setOption(option);
    })
    

      
    },
    updatepieChart1(){
      var that = this;
      const data = d3.csv(`../../assets/processed_output_emotion_by_gameid/processed_emotion_${that.gameid}.csv`);
      
      data.then(function(data) {
        // console.log(that.time)
        // console.log(data)
        try{
          const timeData = data.find(row => row['date'] === that.time);
          // console.log(timeData);
          
          const date = timeData['date']
          const compound = timeData['compound'];
          const neg = timeData['neg'];
          const neu = timeData['neu'];
          const pos = timeData['pos'];
          const option = {
            tooltip: {
              trigger: 'item'
            },
            title: {  // 添加标题组件
              left: '40%',
              text: `${that.time}`,
              textStyle: {
                color: 'white',
                fontSize: 20,
                fontWeight: 'bold',
                textAlign: 'center'
              },
              top: 'bottom' // 设置标题在底部显示
            },
            series: [
              {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                  borderRadius: 10,
                  borderColor: '#fff',
                  borderWidth: 2
                },
                label: {
                  show: false,
                  position: 'center'
                },
                emphasis: {
                  label: {
                    show: true,
                    fontSize: 40,
                    fontWeight: 'bold'
                  }
                },
                labelLine: {
                  show: false
                },
                data: [
                  { value: compound, name: 'positive' },
                  { value: neg, name: 'negative' },
                  { value: neu, name: 'neutral' },
                  { value: pos, name: 'praise' }
                ]
              }
            ]
          };


          that.mypieChart1.setOption(option);


        } catch (error){
          //console.error(error);
          return;
        } 
      })
    },
    updatepieChart2(){
      var that = this;
      const data = d3.json(`../../assets/average_processed_output_emotion/${this.stylename}.json`);
      
      data.then(function(data) {
        // console.log(that.time)
        // console.log(data)
        try{
          const timeData = data.find(row => row['date'] === that.time);
          // console.log(timeData);
          if (!timeData) {
            throw new Error('Data not found');
          }
          const date = timeData['date']
          const compound = timeData['compound'];
          const neg = timeData['neg'];
          const neu = timeData['neu'];
          const pos = timeData['pos'];
          const option = {
            tooltip: {
              trigger: 'item'
            },
            legend: {
              top: '5%',
              left: 'center',
              textStyle: {
                color: 'white', // 设置字体颜色为红色
                fontSize: 12 // 设置字体大小为12px
                // 可以添加其他字体样式属性
              }
            },
            series: [
              {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                  borderRadius: 10,
                  borderColor: '#fff',
                  borderWidth: 2
                },
                label: {
                  show: false,
                  position: 'center'
                },
                emphasis: {
                  label: {
                    show: true,
                    fontSize: 40,
                    fontWeight: 'bold'
                  }
                },
                labelLine: {
                  show: false
                },
                data: [
                  { value: compound, name: 'positive' },
                  { value: neg, name: 'negative' },
                  { value: neu, name: 'neutral' },
                  { value: pos, name: 'praise' }
                ]
              }
            ]
          };


          that.mypieChart2.setOption(option);


        } catch (error){
          console.error(error);
          return;
        }
        
        
        
        

        
      })
    }
  }
};
</script>

<style>
.middlemiddlepart {
  position: relative;
  width: 100%;
  height: 100%;
}

.chart1 {
  position: absolute;
  top: 0;
  left: 10;
  width: 0%;
  height: 0%;
}

.chart2 {
  position: absolute;
  bottom: 0;
  left: 10;
  width: 50%;
  height: 50%;
}

.piechart1 {
  position: absolute;
  top: 0;
  right: 0;
  width: 0%;
  height: 0%;
}

.piechart2 {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 50%;
  height: 50%;
}

</style>
