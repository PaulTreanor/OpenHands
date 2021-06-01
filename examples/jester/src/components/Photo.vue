<template>
    <div class="mb-5">
        <b-img class="pb-3" v-bind:src='image_src' id="image" fluid ></b-img>
        <br>
        <b-button class="mb-2 downloadPhoto" v-on:click='downloadPhoto'><b-icon class="mr-2" icon="file-earmark-arrow-down"></b-icon>Download</b-button>
    </div>
</template>

<script>
export default {
    name: "Photo", 
    props: ['photo'],
    data () {
		return {
			image_src : URL.createObjectURL(this.photo)
		}
	},
    methods: {
        downloadPhoto() {
            const blob = this.photo;
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = 'test.jpeg';
            document.body.appendChild(a);
            a.click();
            setTimeout(() => {
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            }, 100);
        }
    } 
}
</script>

<style scoped>
    .downloadPhoto {
        max-width: 640px;
        background-color: purple;
        border-color: purple;
    }
</style>>
    
