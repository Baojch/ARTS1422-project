<!-- game categories -->
<template>
  <div class="scrollable" ref="scrollable" v-scroll="onScroll">
    <section id="sec-3"></section>
    <div class="l-title">Game Styles</div>
    <div class="l-level1" v-for="style in gamestylesWithId" @click="unfold(style.id)">
        &nbsp;<span v-html="signal[style.id]"></span>{{style.name}}
      <div class="l-level2" v-for="game in gameCategories[style.name]" v-if="whether_unfold[style.id]">
        <div :class="{ 'selected': isSelected(game.appid) }" @click="Innerclick($event,game,style.name)">
          &nbsp;<span v-if="!isSelected(game.appid)" style="color: #ffffff;">•&nbsp;</span>{{ game.name }}
          <span class="metacritic-score" :style="{ width: getMetacriticScoreWidth(game.metacritic_score), height: getMetacriticScoreWidth(game.metacritic_score)}">
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import gameCategories from '../../assets/gameinfo.json';
import bus from '../utils/bus';

export default {
  data() {
    return {
      sellect_game: "",
      signal:['<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>','<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>'],
      metacritic_score: "",
      whether_unfold:[0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0,0,0],
      selectedIndex: -1,
    }
  },
  setup() {
    console.log("created");
    console.log(gameCategories);
    //get gamestyles
    let gamestyles = [];
    for (let key in gameCategories) {
      gamestyles.push(key);
      if (typeof gameCategories[key] === 'object' && !Array.isArray(gameCategories[key])) {
        gamestyles = gamestyles.concat(getKeys(gameCategories[key], fullKey));
      }
    }
    console.log("All gamestyles:", gamestyles);
    // change  to gamestylesWithId(dict {"id": 0, "name": "RPG"},)
    const gamestylesWithId = gamestyles.map((genre, index) => ({
      id: index,
      name: genre
    }));
    console.log(gamestylesWithId);

    return {gamestylesWithId, gameCategories}
  },
  methods: {
    unfold(db){
      // console.log("func: unfold"+db);
      if(this.signal[db]=='<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>'){
        this.signal[db] = '<span v-html class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span>';
        this.whether_unfold[db] = 1;
      }else{
        this.signal[db]='<span v-html class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>';
        this.whether_unfold[db] = 0;
      }
    },
    onScroll(event) {
      console.log('Scrolling', event.target.scrollTop);
    },
    Innerclick(event, game, stylename) {
      event.stopPropagation();
      this.sellect_game = game.name;
      this.metacritic_score = game.metacritic_score;
      this.selectedIndex = game.appid;
      bus.emit('gameid', game.appid); // 触发事件并传递appid
      bus.emit('stylename', stylename);
      bus.emit('gamename',game.name);
    },
    isSelected(appid) {
      return this.selectedIndex === appid;
    },
    // 计算 Metacritic 分数对应的正方形宽度
    getMetacriticScoreWidth(score) {
      if (score === "N/A") return '0px';
      // 这里假设最大宽度为 100px，对应最高分数
      const maxWidth = 15;
      const maxScore = 50;
      const numericScore = parseInt(score);
      const width = ((numericScore-50) / maxScore) * maxWidth;
      return `${width}px`;
    }
  }
}
</script>

<style scoped>
  .l-title {
    margin-top: 0%;
    font-size: 24px;
    color: white;
    letter-spacing: 3px;
    text-align: center;
    font-weight: bold;
}
  .l-level1{
    margin-top: 1%;
    margin-left: 0%;
    font-size:23px;
    color: white;
    letter-spacing:3px;
    text-align: left;
  }
  .l-level2{
    margin-top: 1%;
    margin-left: 3%;
    font-size: 15px;
    color: white;
    letter-spacing:2px;
    text-align: left;
  }
  .l-level2 div {
    margin-bottom: 5px; /* 这里可以根据需要调整间距大小 */
  }
  .scrollable {
    overflow-y: scroll;
    padding: 5px;
    scrollbar-color: #888 #e0e0e0;
  }
  .selected {
    display: inline-block;
    background-color: #ffffff;
    border-radius: 20px;
    border: 2px solid #ffffff;
    padding: 5px 10px;
    color: #000000;
    text-align: center;
  }
  /* 样式 Metacritic 分数的正方形 */
  .metacritic-score {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    background-color: #ffcc00; /* 默认背景颜色，可以根据需要调整 */
    margin-left: 3px; /* 调整与游戏名称的间距 */
  }
</style>

