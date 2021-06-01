<template>
  <div id="app">
    <Nav v-bind:active-view="active_view" v-on:active-view='setActiveView'/>
    <Camera v-bind:server_address="serverAddress" v-on:caputure-image='storeImage' v-on:recorded-video='storeVideo' v-if="active_view === 1"/>
    <Info  v-bind:server_address="serverAddress" v-on:change-address='changeAddress' v-if="active_view === 2"/>
    <Gallery v-bind:photo="photos" v-bind:video="recordedVideos" v-if="active_view === 3"/>
  </div>
</template>

<script>
import Nav from './components/Nav';
import Camera from './components/Camera';
import Info from './components/Info';
import Gallery from './components/Gallery';

export default {
  name: 'App',
  components: {
    Nav,
    Camera,
    Info,
    Gallery
  },
  data() {
    return {
      active_view: 1,
      photos: [],
      recordedVideos: [], 
      serverAddress: "http://192.168.43.105:5000/",
    };
  },
  
  methods: { 
    changeAddress(address) {
      console.log(address)
      this.serverAddress = address;
    },

    setActiveView(num) {
      this.active_view = num;
    },
    storeImage(blob) {
      this.photos.push(blob); 
      if (this.photos.length > 5){
        //drop first element in array
        this.photos.shift()
      }
    },
    storeVideo(blob) {
      this.recordedVideos.push(blob);
      if (this.recordedVideos.length > 1){
        this.recordedVideos.shift()
      }
    }
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif; 
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  main {
    margin:0;
    padding:0;
	}
</style>
