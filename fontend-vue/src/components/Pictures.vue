<!-- pictures -->
<template>
  <div class="image-container">
    <div v-if="gameid !== -1" class="image-wrapper">
      <img :src="imgpath[0]" alt="Game Header Image" class="game-image game-image--large">
      <div class="square-images">
        <img :src="imgpath[1]" alt="Game Thumbnail 1" class="game-image game-image--square">
        <div style="width: 50px;"></div>
        <img :src="imgpath[2]" alt="Game Thumbnail 2" class="game-image game-image--square">
      </div>
    </div>
    <div v-else style="text-align: center; font-size: 28px; color: white;">Please select a game</div>
  </div>
</template>

<script>
import bus from '../utils/bus';
import gameCategories from '../../assets/gameinfo.json';

export default {
  data () {
    return {
      gameid: -1,
      stylename: "",
      imgpath:[],
    }
  },
  mounted() {
    bus.on('gameid', (gameid) => {
      console.log(gameid);
      this.gameid = gameid;
    })
    bus.on('stylename', (stylename) => {
      console.log(stylename);
      this.stylename = stylename;
      // console.log("test:" + gameCategories[this.stylename]);
      for (let game in gameCategories[this.stylename]) {
        if(gameCategories[this.stylename][game]['appid']===this.gameid) {
          this.imgpath[0] = gameCategories[this.stylename][game]['header_image'];
          this.imgpath[1] = gameCategories[this.stylename][game]['thumbnails'][0];
          this.imgpath[2] = gameCategories[this.stylename][game]['thumbnails'][1];
          // console.log(this.imgpath)
        }
      }

    })
  }

}
</script>

<style scoped>
.image-container {
  width: 100%;
  max-width: 100%;
  height: 100%;
  margin: 0 auto;
}

.image-wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.game-image {
  max-width: 40%;
  height: auto;
  object-fit: contain;
}

.game-image--large {
  max-width: 33%;
  margin-top: 4px;
  margin-left: 30px;
  border: 2px solid #FFFDD0;
}

.game-image--square {
  max-width: 41%;
  object-fit: cover;
  margin-top: 4px;
  aspect-ratio: 1.5 / 1;
  border: 2px solid #FFFDD0;
}

.square-images {
  display: flex;
  margin-left: 65px;
  width: 100%;
}
</style>
