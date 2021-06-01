<template>
    <div>
        <b-navbar toggleable="lg" type="dark" variant="success">
            <b-navbar-brand href="#" v-on:click="$emit('active-view', 1)">
                <h4 class="brand">Jester</h4>
            </b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            
            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav class="ml-auto">
                    <b-nav-item v-on:click="$emit('active-view', 1)">
                        <div class="d-flex" v-bind:class="{'is-active':activeView ===1}" id="cameraButton"> 
                            <b-icon class="h3 mr-2" icon="camera" shift-v="-4"></b-icon>  
                            <p class="mt-1">Camera</p>                    
                        </div>
                    </b-nav-item>
                    <b-nav-item v-on:click="$emit('active-view', 3)">
                        <div class="d-flex" v-bind:class="{'is-active':activeView ===3}" id="galleryButton">
                             <b-icon class="h3 mr-2" icon="card-image" shift-v="-4"></b-icon> 
                             <p class="mt-1">Gallery</p>
                        </div>
                    </b-nav-item>
                    <b-nav-item v-on:click="$emit('active-view', 2)">
                        <div class="d-flex" v-bind:class="{'is-active':activeView ===2}" id="infoButton">
                             <b-icon class="h6 mr-2" icon="info-square" shift-v="-4"></b-icon> 
                             <p class="mt-1">Information</p> 
                            </div>
                    </b-nav-item>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </div>   
</template>

<script>
export default {
    name: "Nav",
    props: ["active-view"], 
}
</script>

<style scoped>
    * {
        margin-bottom: 0px;
    }

    .is-active {
        color: white;
    }
    
    .brand {
        color:white;
    }

    h4 {
        margin:0px;
    }

    .bg-success {
    background-color: purple !important;
    }

    .navbar {
        padding: 0.2rem 1rem;
    }
</style>