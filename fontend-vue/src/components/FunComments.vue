<template>
  <div class="scrolling">
    <div v-if="gameid !== -1" class="comment-wrapper">
      <marquee direction="left" :style="{ color: randomColor(), fontSize: fontSize }">{{ comments[0]+comments[1] }}</marquee>
      <marquee direction="left" :style="{ color: randomColor(), fontSize: fontSize }">{{ comments[2]+comments[3] }}</marquee>
    </div>
  </div>
</template>

<script>
import bus from '../utils/bus';
import fun_comments from '../../assets/fun_comment.json';

export default {
  data() {
    return {
      gameid: -1,
      comments: [],
      colors: ['#C8A2C8', '#89CFF0', '#FFFDD0', '#FF7F50', "#DCAE96"],
      fontSize: '20px' // 设置字号为20px
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      console.log(gameid);
      this.gameid = gameid;
      for (var i = 0; i <= 4; i++) {
        this.comments[i] = fun_comments[gameid][i].replace(/\n/g, '').replace("10/10", '').replace("11/10", '');
      }
      console.log(this.comments);
    })
  },
  methods: {
    randomColor() {
      // 从颜色数组中随机选择一个颜色
      var color = this.colors[Math.floor(Math.random() * this.colors.length)];
      console.log(color);
      return color;
    }
  }
}
</script>

<style scoped>
</style>
