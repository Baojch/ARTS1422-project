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
  }

}
</script>

<style  scoped>

</style>
