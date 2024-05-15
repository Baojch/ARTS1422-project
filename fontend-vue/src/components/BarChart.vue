<!-- barchart -->
<template>
  <div class="container">
    <h1 class="centered-title">Current VS Average</h1>
      <div style="height: 10px;"></div>
      <div v-for="(item, index) in scaled_left" :key="index" class="comparison-bar">
      <div :style="{ width: item * 35 + '%' }" class="current-bar">
        <span class="bar-value">{{ selected[index] }}</span>
      </div>
      <div :style="{backgroundImage:'url('+icons[index]+')'}"class="icon"></div>
      <div :style="{ width: scaled_right[index] * 35 + '%' }" class="average-bar">
        <span class="bar-value">{{ average[index] }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '../utils/bus';
import compare from '../../assets/compareinfo.json';

export default {
  data () {
    return {
      gameid: -1,
      stylename: "",
      icons:[],
      scaled_left:[],
      scaled_right:[],
      selected:[],
      average:[],
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      //console.log(gameid);
      this.icons=[
        '../../assets/images/评论小.png',
        '../../assets/images/点赞.png',
        '../../assets/images/时间.png',
        '../../assets/images/差评.png',
        '../../assets/images/comment_comment.png'
      ]
      this.gameid = gameid;
      var sum=[0,0,0,0,0];
      var cnt=0
      for (let game in compare[this.stylename]) {
        cnt+=1;

        sum[0]+=parseInt(compare[this.stylename][game]["num_comment"]);
        sum[1]+=parseInt(compare[this.stylename][game]["voted_up"]);
        sum[2]+=parseInt(compare[this.stylename][game]["playtime"]);
        sum[3]+=parseInt(compare[this.stylename][game]["negative"]);
        sum[4]+=parseInt(compare[this.stylename][game]["comment_comment"]);

        if(compare[this.stylename][game]['appid']===this.gameid){
          this.selected[0]=compare[this.stylename][game]["num_comment"];
          this.selected[1]=compare[this.stylename][game]["voted_up"];
          this.selected[2]=compare[this.stylename][game]["playtime"];
          this.selected[3]=compare[this.stylename][game]["negative"];
          this.selected[4]=compare[this.stylename][game]["comment_comment"];
        }
      }
      for(var i=0;i<=4;i++){
        sum[i]=parseInt(sum[i]/cnt);
        this.average[i]=sum[i];
      }
      sum[2]=parseInt(sum[2]/1440);
      this.average[2]=parseInt(this.average[2]/1440);
      this.selected[2]=parseInt(this.selected[2]/1440);
      console.log(this.selected);
      console.log(sum);
      for(var i=0;i<=4;i++){
        if(this.selected[i]>sum[i]){
          this.scaled_left[i]=1
          this.scaled_right[i]=sum[i]/this.selected[i]
        }
        else{
          this.scaled_left[i]=this.selected[i]/sum[i]
          this.scaled_right[i]=1
        }
      }
      console.log(this.scaled_left);
      console.log(this.scaled_right);
  })
    bus.on('stylename', (stylename) => {
      console.log(stylename);
      this.stylename = stylename;
    })
  }
}
</script>

<style  scoped>
.current-bar,
.average-bar {
  height: 16px;
  background-color: #cccccc;
}

.centered-title {
  text-align: center; /* 文本水平居中 */
  font-size: 26px; /* 字体大小 */
  color: #ffffff; /* 颜色 */
}
.comparison-bar {
  position: relative;
  display: flex;
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  margin-top: 15px; /* 顶部外边距 */
  margin-bottom: 25px; /* 增加底部外边距 */
}

.icon {
  width: 20px;
  height: 20px;

  left: 50%; /* Move the icon to the center horizontally */
  /* Adjust to center the icon precisely */
  margin-top: -10px; /* Center vertically */
  margin: 0 10px;
  background-size: cover;
}

.bar-value {

  top: -20px; /* 距离条形图顶部的距离 */
  left: 0; /* 距离条形图左侧的距离 */
  font-size: 12px; /* 数值的字体大小 */
  color: #000; /* 数值的颜色 */
  background-color: #fff; /* 数值的背景颜色 */
  padding: 2px 5px; /* 数值周围的内边距 */
  border-radius: 5px; /* 数值的边框圆角 */
  z-index: 1; /* 确保数值位于条形图上方 */
  opacity: 0; /* 初始状态下数值不可见 */
  transition: opacity 0.3s ease; /* 添加过渡效果 */
}

.comparison-bar:hover .bar-value {
  opacity: 1; /* 悬停时数值可见 */
}

.comparison-bar:hover .current-bar,
.comparison-bar:hover .average-bar {
  opacity: 0.7; /* 降低当前和平均条形图的不透明度 */
}

</style>
