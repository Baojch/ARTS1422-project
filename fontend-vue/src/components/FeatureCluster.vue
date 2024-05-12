<!-- feature cluster -->
<template>
  <div>
    {{ gameid }}
  </div>
</template>

<script>
import bus from '../utils/bus';

export default {
  data () {
    return {
      gameid: -1,
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
    })
  }

}
</script>

<style  scoped>

</style>
