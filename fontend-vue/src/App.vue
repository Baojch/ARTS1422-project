<script setup>
import TitleComponent from './components/Title.vue';
import GameCategoriesComponent from './components/GameCategories.vue';
import PicturesComponent from './components/Pictures.vue';
import BarChartComponent from './components/BarChart.vue';
import RivermapComponent from './components/Rivermap.vue';
import FeatureClusterComponent from './components/FeatureCluster.vue';
import WordCloudComponent from './components/WordCloud.vue';
import FunCommentsComponent from './components/FunComments.vue';
import SaveComponent from './components/Save.vue';
import { ref } from 'vue';
const selectedAppId = ref(null);

const handleSelectGame = (appid) => {
  selectedAppId.value = appid;
}
</script>

<template>
  <div id="app">
    <div class="flex-row toppart">
        <TitleComponent style="width: 37.5%;height: 100%;" class="borderpink"/>
        <div style="width: 4.5%;"></div>
        <FunCommentsComponent style="width: 58%;height: 100%;" class="borderpink"/>
    </div>
    <div style="height: 3%;"></div>
    <div class="flex-row middlepart" >
      <div class="leftpart">
        <div style="width: 100%;height: 58%;" class="borderpink">
          <GameCategoriesComponent style="width: 100%;height: 100%;"/>
        </div>
        <div style="height: 3%;"></div>
        <FeatureClusterComponent style="width: 100%;height: 39%;" class="borderpink"/>
      </div>
      <div style="width: 2%;"></div>
      <div class="middlemiddlepart">
        <PicturesComponent style="width: 100%;height: 20%;" class="borderpink"/>
        <div style="height: 3%;"></div>
        <RivermapComponent style="width: 100%;height: 77%;" class="borderpink"/>
      </div>
      <div style="width: 2%;"></div>
      <div class="rightpart">
        <BarChartComponent style="width: 100%;height: 33%;" class="borderpink"/>
        <div style="height: 3%;"></div>
        <WordCloudComponent style="width: 100%;height: 31%;" class="borderpink"/>
        <div style="height: 3%;"></div>
        <SaveComponent style="width: 100%;height: 30%;" class="borderpink"/>
      </div>
    </div>
  </div>
</template>

<style>
.borderpink {
  border: 2px solid #F7CAC9; /* 设置边框宽度和颜色 */
  border-radius: 20px;      /* 设置圆角半径 */
  padding: 10px;            /* 内边距，确保内容不贴近边框 */
  box-sizing: border-box;   /* 确保填充不影响组件大小 */
}

.flex-row {
  display: flex;          /* 使用flexbox */
  flex-direction: row;    /* 组件在一行显示 */
}

.flex-column {
  display: flex;       
  flex-direction: column;
}

.toppart {
  width: 100%;
  height: 9%;
}

.middlepart {
  width: 100%;
  height: 88%;
}
.leftpart {
  width: 23.8%;
  height: 100%;
}
.middlemiddlepart{
  width: 54%;
  height: 100%;
}
.rightpart {
  width: 18.2%;
  height: 100%;
}
</style>
