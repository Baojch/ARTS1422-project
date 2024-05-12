<!-- wordcloud -->
<template>
  <div>
    <img v-if="gameid !== -1"  :src="imagePath" alt="Game Image" class="image-container"/>
  </div>
</template>

<script>
import bus from '../utils/bus';
import gameCategories from '../../assets/gameinfo.json';

export default {
  data () {
    return {
      gameid: -1,
      stylename: '',
      imagePath: ''
    }
  },
  mounted() {
    bus.on('gameid', this.handleGameIdChange);
    
  },
  methods: {
    handleGameIdChange(gameid) {
      this.gameid = gameid;
      this.updateImagePath();
    },
    updateImagePath() {
      // 假设你有一个函数或对象来根据 gameid 和 stylename 获取图像路径
      this.imagePath = `../../assets/wordcloud/wordcloud_${this.gameid}.png`;
    }
  }
}
</script>

<style scoped>
.image-container {
  max-width: 100%; /* 设置图片最大宽度为父元素宽度 */
  max-height: 100%; /* 设置图片最大高度为父元素高度 */
  object-fit: contain; /* 保持图片比例并填充整个容器 */
}

</style>
