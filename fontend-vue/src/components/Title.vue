<template>
  <div class="container">
    <!-- 添加居中标题 -->
    <h1 class="centered-title">Discover Unique Games: <br> A Deep Dive into Steam Reviews</h1>
  </div>
</template>

<script>
export default {
  data () {
    return {
    }
  }
}
</script>

<style scoped>
/* 给容器设置一些基础样式 */
.container {
  display: flex; /* 使用 flex 布局 */
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
  height: 100%; /* 高度设置为视窗高度 */
  padding-bottom: 20px;
}

/* 标题的样式 */
.centered-title {
  text-align: center; /* 文本水平居中 */
  font-size: 28px; /* 字体大小 */
  color: #ffffff; /* 颜色 */
}
</style>
