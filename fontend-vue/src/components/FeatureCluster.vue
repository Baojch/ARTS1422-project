<template>
  <div ref="d3Container"></div>
</template>

<script>
import * as d3 from 'd3';
import d3Tip from 'd3-tip';
import bus from '../utils/bus';
import gameCategories from '../../assets/gameinfo.json';
export default {
  data() {
    return {
      gameid: -1,
      stylename: "unknown",
      prevStylename: "",
      prevCentroidsData: null,
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      this.gameid = gameid;
    });
    bus.on('stylename', (stylename) => {
      this.stylename = stylename;
      this.drawChart();
    });
  },
  methods: {
    drawChart() {
        console.log(this.stylename);
        console.log(this.gameid);
        if (!this.stylename || this.gameid === -1) return; // 确保stylename和gameid都已设置

        const list = [];
        const highlight_id = [];
        const highlight_name = [];
        for (let game in gameCategories[this.stylename]) {
            if (gameCategories[this.stylename][game]['appid'] === this.gameid) {
                for (let category of gameCategories[this.stylename][game]['categories']) {
                    highlight_id.push(category['id']);
                    highlight_name.push(category['description']);
                }
            } else {
                for (let category of gameCategories[this.stylename][game]['categories']) {
                    list.push(category['id']);
                }
            }

        }
        console.log("highlight_id:" + highlight_id);
        console.log("highlight_name:" + highlight_name);
        console.log("list:" + list);

        // 去除重复数字得到类别数
        var categories = Array.from(new Set(list.concat(highlight_id)));

        // 定义颜色比例尺
        var colorScale = d3.scaleOrdinal()
            .domain(categories)
            .range(d3.schemeCategory10); // 使用 D3 提供的 schemeCategory10 颜色方案

        // 随机生成聚类中心的坐标
        var centroidsData = this.prevStylename === this.stylename ? this.prevCentroidsData : categories.map(function(category) {
            return {
                category: category,
                x: Math.random() * 370 + 10,
                y: Math.random() * 285 + 32,
            };
        });
        this.prevStylename = this.stylename;
        this.prevCentroidsData = centroidsData;



        const width = 390;
        const height = 328;
        const svg = d3.select(this.$refs.d3Container)
            .html('') // 清空之前的内容
            .append('svg')
            .attr('width', width)
            .attr('height', height);

        var titleText = 'Feature cluster for ' + this.stylename + ' Games'

        // 添加标题
        svg.append('text')
            .attr('x', width / 2)
            .attr('y', 20) // 标题的y位置，可以根据需要调整
            .attr('text-anchor', 'middle') // 使标题居中
            .style('font-size', '20px') // 设置字体大小
            .style('fill', 'white') // Set text color to white
            .text(titleText);

        // 添加圆点(list中的点)
        svg.selectAll(".list-circle")
            .data(list)
            .enter().append("circle")
            .attr("class", "list-circle")
            .attr("cx", function(d, i) {
                // 获取相应聚类中心的坐标
                var centroid = centroidsData.find(function(c) { return c.category === d; });
                // 在聚类中心的周围随机分布
                return centroid.x + Math.random() * 20 - 10;
            })
            .attr("cy", function(d) {
                var centroid = centroidsData.find(function(c) { return c.category === d; });
                return centroid.y + Math.random() * 20 - 10;
            })
            .attr("r", 4) // 固定点的半径
            .attr("fill", function(d) {
                return highlight_id.includes(d) ? colorScale(d) : "#ccc";
            }); // 设置颜色，高亮点为多样色，非高亮点为灰色

        // 创建一个提示框
        const tip = d3Tip()
            .attr('class', 'd3-tip')
            .offset([-10, 0])
            .html(function(d) {
                // 获取当前圆圈的数据值
                var currentData = d3.select(this).datum();
                console.log(currentData);
                // 获取当前数据在 highlight_id 数组中的索引
                var index = highlight_id.indexOf(currentData);
                // 返回对应的 highlight_name 值
                return "<div style='background-color: rgba(255, 255, 255, 0.9); padding: 5px; border-radius: 5px;'>" + highlight_name[index] + "</div>";
            });

        // 将提示框与 SVG 元素关联
        svg.call(tip);

        // 添加高亮圆点
        svg.selectAll(".highlighted-circle")
            .data(highlight_id)
            .enter().append("circle")
            .attr("class", "highlighted-circle")
            .attr("cx", function(d, i) {
                var centroid = centroidsData.find(function(c) { return c.category === d; });
                return centroid.x + Math.random() * 20 - 10;
            })
            .attr("cy", function(d) {
                var centroid = centroidsData.find(function(c) { return c.category === d; });
                return centroid.y + Math.random() * 20 - 10;
            })
            .attr("r", 4)
            .attr("fill", function(d) {
                return colorScale(d);
            })
            .attr("stroke", "#FFFDD0")
            .attr("stroke-width", 2)
            // 鼠标悬停时显示提示框
            .on('mouseover', tip.show)
            // 鼠标移出时隐藏提示框
            .on('mouseout', tip.hide);

    }
  }
}
</script>

<style scoped>
</style>