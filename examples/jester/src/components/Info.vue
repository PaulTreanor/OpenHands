
<template>
    <main>
        <b-container class="info-col">
            <h4>What is Jester?</h4>
            <p >Jester is an app that allows you take photos and videos using hand gestures!</p>
            
            <h4>Taking Photos</h4>
            <div class="alert d-inline-flex">
                <i class="icon far fa-hand-peace fa-2x"></i>
                <p>A peace sign gesture takes a photo.</p>
            </div>
            
            <h4>Recording Videos</h4>
            <div class="alert d-inline-flex">
                <i class="icon far fa-thumbs-up fa-2x"></i>
                <p>A thumbs up gestures starts video recording.</p>
            </div>
            
            <div class="alert d-inline-flex">
                <i class="icon far fa-hand-paper fa-2x"></i>
                <p>A flat palm facing the camera stops the recording</p>
            </div>`
            
            <hr>

            <h4> Change Jester API address</h4>

            <form  v-on:submit.prevent="updateServerAddress">
                 <input type="text" size="45" v-model="tempAddress" :placeholder="currAddress" >
                  <br>
                  <button type="submit" class="btn btn-primary mt-3">Change Address</button>  
              </form>
        </b-container>
    </main>
</template>

<script>
export default {
    name: "Info",
    props: ["active_view", "server_address"],
    data () {
        return {
            currAddress: this.server_address,
            tempAddress: ""
        }
    },
    methods: {
        updateServerAddress() {
            console.log("Server address updating")
            this.$emit('change-address', this.tempAddress);
        }
    }
}
</script>

<style scoped>
    .info-col {
        max-width: 600px;
    }

    p {
        padding:0px;
        margin: 0px;
        padding-top: 5px;
    }

    h4 {
        padding-top: 25px;
        padding-bottom: 5px;
        color: purple;
    }

    .alert {
        margin-top: 5px;
        background: #FFFFFF;
        border: 1px solid rgba(214, 214, 214, 0.15);
        box-sizing: border-box;
        box-shadow: 0px 4px 8px rgba(56, 56, 56, 0.15);
        border-radius: 16px;
        color: #2c3e50;
        max-width: 500px;
    }

    .icon {
        margin-right: 20px;      
    }

    .btn-primary {
        background-color: purple;
        border-color: #730073;
    }

    .btn-primary:hover {
    color: #fff;
    background-color: #660066;
    border-color: #993299;
}
</style>
