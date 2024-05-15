<template>
  <div>
    <div class="input-container">
      <div class="textbox-wrapper">
        <textarea class="textbox" v-model="note" placeholder="please type your note here"></textarea>
        <button @click="sendMessage" class="send-button">
          <img src="../../assets/images/上传.png" alt="发送">
        </button>
      </div>
      <div style="height: 10px;"></div>
      <div class="entries-container">
        <ul class="list-group">
          <li v-for="entry in entries" :key="entry.timestamp" class="list-group-item custom-list-item">
            <div>{{ entry.gamename }}</div>
            <div>Time: {{ entry.timestamp }}</div>
            <div>notes: {{ entry.note }}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import bus from '../utils/bus';

export default {
  data() {
    return {
      gamename: "None",
      timestamp: "None",
      note: "",
      entries: []
    }
  },
  mounted() {
    bus.on('gamename', (gamename) => {
      console.log(gamename);
      this.gamename = gamename;
    });
    bus.on('timestamp', (timestamp) => {
      console.log(timestamp);
      this.timestamp = timestamp;
    });
  },
  methods: {
    sendMessage() {
      console.log("send message");
      const entry = {
        gamename: this.gamename,
        timestamp: this.timestamp,
        note: this.note
      };
      this.entries.push(entry);
      this.note = "";
    }
  }
}
</script>

<style scoped>
.input-container {
  position: relative;
  height: 100%;
  width: 90%; /* 设置宽度为90% */
  margin: 0 auto; /* 水平居中 */
}

.textbox-wrapper {
  position: relative;
}

.textbox {
  width: 100%;
  border: 2px solid #ADACAC;
  background-color: black;
  color: white;
  padding: 8px;
  resize: none;
  overflow: auto;
  height: 90px; /* Adjusted height */
}

.textbox::placeholder {
  color: #707070;
}

.send-button {
  position: absolute;
  right: 5px;
  bottom: 11px;
  width: 30px; /* Set width and height to make the button smaller */
  height: 30px;
  border-radius: 50%; /* Make the button round */
  background-color: #E0E0E0; /* Gray-white background */
  border: none;
  cursor: pointer;
  padding: 5px; /* Adjust padding for image */
}

.send-button img {
  max-width: 100%; /* Ensure the image fits inside the button */
  max-height: 100%;
}

.entries-container {
  max-height: 165px; /* 设置最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.custom-list-item {
  background-color: #1c1c1c; /* 深灰色背景 */
  color: #fff; /* 白色文字 */
}

/* 自定义滚动条样式 */
.entries-container::-webkit-scrollbar {
  width: 8px; /* 滚动条宽度 */
}

.entries-container::-webkit-scrollbar-track {
  background-color: #333; /* 滚动条轨道颜色 */
}

.entries-container::-webkit-scrollbar-thumb {
  background-color: #666; /* 滚动条滑块颜色 */
  border-radius: 4px; /* 滚动条滑块圆角 */
}

.entries-container::-webkit-scrollbar-thumb:hover {
  background-color: #999; /* 鼠标悬停时滚动条滑块颜色 */
}
</style>