<template>
    <div class="bg-white-600 w-full text-white">
        <div class="bg-gray-300 h-[50px] text-center flex justify-between items-center">
            <button class="px-[15px]" @click="showmenu">
                <svg class="mr-2 w-[24px] h-[24px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>menu</title><path d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" />
                </svg>
            </button>
            <input type="search" placeholder="Search..." class="leading-8 px-[10px] w-[300px] h-[30px] rounded-lg"/>
            <div class="flex px-[20px]">
                <button class="px-[10px]">
                    <img class="w-[36px] h-[36px] rounded-full" src="https://scontent.fhan2-4.fna.fbcdn.net/v/t39.30808-6/340786088_553659393505482_7823642108210577609_n.jpg?_nc_cat=100&cb=99be929b-59f725be&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=xnYxgF8bLAAAX-wRL9D&_nc_ht=scontent.fhan2-4.fna&oh=00_AfB_v17co9vNmxZXysDm5EPAxG_A3jMCy2BP5oNoWMifJg&oe=647CFC47"/>
                </button>
                <div>
                    <h1 class="text-sm text-black">Fullstack Developer</h1>
                    <h2 class="text-xs text-black text-left">Admin</h2>
                </div>
            </div>
        </div>
        <div>
            <router-view></router-view>
        </div>
    </div>
   
</template>

<script>
const Content = {
    methods:{
        showmenu(){
            this.$emit('showmenu')
        },
    },
    props: [],
}
export default Content
</script>

<style></style>