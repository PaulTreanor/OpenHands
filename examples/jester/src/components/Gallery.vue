<template>
	<main>
		<b-container class="center-block text-center">		
			<h2 class="pt-4 pb-4" id="photoTitle">Photos</h2>
			<div v-if="this.photo.length === 0">
				<p id="noPhotos">No photos in gallery yet!</p>
			</div>
			<div  v-bind:key="photo" v-for="photo in photo">
				<Photo v-bind:photo="photo"/>
			</div>
			<h2 class="pt-4 pb-4" id="videoTitle">Videos</h2>
			<div v-if="this.video.length === 0">
				<p id="novideos">No Videos in gallery yet!</p>
			</div>
			<div v-bind:key="video" v-for="video in video">
				<Video v-bind:video="video"/>
			</div>
		</b-container>
	</main>
</template>

<script>

import Photo from './Photo';
import Video from './Video';

export default {
	name: "Gallery",
	components: {
		Photo,
		Video
	},
	props: ['photo', 'video'],	
}
</script>

<style scoped>

	h2 {
        color: purple;	
    }
</style>

