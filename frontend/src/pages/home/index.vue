<template>
    <div class="flex h-screen w-screen">
        <header-bar :isShow="isShow" @showhome="show2"></header-bar>
        <Content :isShow1="isShow1" @onshow="show1"></Content>
    </div>
</template>

<script>
import HeaderBar from '@/components/HeaderBar/index.vue'
import Content from '@/components/Content/content.vue'

const Home = {
    data(){
        return {
            isShow: true,
            isShow1: true
        }
    },
    components: {
        HeaderBar,
        Content
    },
    methods:{
        show1(){
            this.isShow = !this.isShow
        },
        show2(){
            this.isShow1 = !this.isShow1
        }
    }
}
export default Home
</script>

<style></style>