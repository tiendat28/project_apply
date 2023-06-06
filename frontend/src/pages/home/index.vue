<template>
    <div class="flex h-screen w-screen relative">
        <header-bar :isShow="isShow" ></header-bar>
        <Content @showmenu="show"></Content>
    </div>
</template>

<script>
import HeaderBar from '@/components/HeaderBar/index.vue'
import Content from '@/components/Content/content.vue'

const Home = {
    data(){
        return {
            isShow: true,
        }
    },
    components: {
        HeaderBar,
        Content,
    },
    methods:{
        show(){
            this.isShow = !this.isShow
        },
    }
}
export default Home
</script>

<style></style>