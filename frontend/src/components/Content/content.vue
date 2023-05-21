<template>
    <div class="bg-white-600 w-full text-white">
        <div class="bg-green-800 h-[50px] text-center flex justify-between items-center">
            <button class="px-[15px]" @click="show">
                <svg class="mr-2 w-[24px] h-[24px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><title>menu</title><path d="M3,6H21V8H3V6M3,11H21V13H3V11M3,16H21V18H3V16Z" />
                </svg>
            </button>
            <input type="search" placeholder="Search..." class="leading-8 px-[10px] w-[300px] h-[30px] rounded-lg"/>
            <div class="flex px-[20px]">
                <button class="px-[10px]">
                    <img class="w-[36px] h-[36px] rounded-full" src="https://scontent.fhan5-11.fna.fbcdn.net/v/t39.30808-6/340786088_553659393505482_7823642108210577609_n.jpg?_nc_cat=100&cb=99be929b-59f725be&ccb=1-7&_nc_sid=09cbfe&_nc_ohc=TK9JCwJ-8JUAX82a7Dw&_nc_ht=scontent.fhan5-11.fna&oh=00_AfC-5kI62i9fMJnQiLrHT4q3e3_z95dG1B14AE7S8FP5uQ&oe=646D2A47"/>
                </button>
                <div>
                    <h1 class="text-sm">Fullstack Developer</h1>
                    <h2 class="text-xs text-left">Admin</h2>
                </div>
            </div>
        </div>
        <div v-show="isShow1" class="m-[15px] border-solid border-2 rounded-lg w-[calc(100%-30px)] h-[calc(100vh-80px)] bg-green-300">
            <h1 class="text-black px-[15px] py-[20px] text-lg font-bold">Student List</h1>
            
            <div class="flex justify-center">
                <div class="flex flex-col px-[15px]">
                    <label class="text-black">Fullname</label>
                    <input class="w-[200px] h-[40px] rounded-lg leading-10 text-black" type="text" placeholder=" Mai Tien Dat" v-model="itemName"/>
                </div>
                <div class="flex flex-col px-[15px]">
                    <label class="text-black">Address</label>
                    <input class="w-[200px] h-[40px] rounded-lg leading-10 text-black" type="text" placeholder=" Nam Dinh" v-model="itemAddress"/>
                </div>
                <div class="flex flex-col px-[15px]">
                    <label class="text-black">Date</label>
                    <input class="w-[200px] h-[40px] rounded-lg leading-10 text-black" type="text" placeholder=" 28/02/2000" v-model="itemDate"/>
                </div>
                <div class="flex flex-col px-[15px]">
                    <label class="text-black">Email</label>
                    <input class="w-[200px] h-[40px] rounded-lg leading-10 text-black" type="text" placeholder=" Dat.mt@sis.hust.edu.vn" v-model="itemEmail"/>
                </div>
                <div class="py-[24px]">
                    <button @click="saveItems(haveID)" class="bg-green-800 w-[50px] h-[40px] rounded-lg">Save</button>
                </div>
            </div>

            <div class=" px-[30px]">
                <table class="text-black w-[100%] table-auto border-b-2 ">
                    <tr class="text-left border-b-2 h-[40px]">
                        <th>STT</th>
                        <th>Fullname</th>
                        <th>Address</th>
                        <th>Date</th>
                        <th>Email</th>
                        <th>Action</th>
                    </tr>
                    <tr class="table-auto border-b-2 h-[40px]" v-for="item in list" :key="item.id">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td> 
                        <td>{{ item.address }}</td> 
                        <td>{{ item.date }}</td> 
                        <td>{{ item.email }}</td> 
                        <td>
                            <button @click="editItem(item.id)" class="bg-green-600 rounded-lg px-[15px]">Edit</button>
                            <button @click="deleteItem(item.id)" class="bg-red-600 rounded-lg px-[15px]">Delete</button>
                        </td>
                    </tr>
                </table>
            </div>

        </div>
    </div>
</template>

<script>

const Content = {
    data(){
        return{
            // id:'',
            itemName:'',
            itemAddress:'',
            itemDate:'',
            itemEmail:'',
            haveID: null,
            id: '',
            list: [
                {
                    id:1,
                    name: 'Mai Tien Dat',
                    address: 'Nam Dinh',
                    date: '28/02/2000',
                    email: 'Dat.mt@sis.hust.edu.vn'
                },
                {
                    id:2,
                    name: 'Le Hoang Nam',
                    address: 'Nam Dinh',
                    date: '22/10/2000',
                    email: 'Nam.lh@sis.hust.edu.vn'
                }
            ]
        }
    },
    methods:{
        show(){
            this.$emit('onshow')
        },
        saveItems(haveID){
            if(haveID){
                var dataItem = this.list.filter((item) => (item.id == haveID))
                dataItem[0].name = this.itemName
                dataItem[0].address = this.itemAddress
                dataItem[0].date = this.itemDate
                dataItem[0].email = this.itemEmail
                this.itemName = null
                this.itemAddress = null
                this.itemDate = null
                this.itemEmail = null
            }else{
                const id = this.list.length +1
                const item ={
                    id: id,
                    name: this.itemName,
                    address: this.itemAddress,
                    date: this.itemDate,
                    email: this.itemEmail
                }
                this.list.push(item)
                this.itemName = null
                this.itemAddress = null
                this.itemDate = null
                this.itemEmail = null
            }
        },
        editItem(id){
            this.haveID = id
            var dataItem = this.list.filter((item) => (item.id == id))
            this.itemName = dataItem[0].name
            this.itemAddress = dataItem[0].address
            this.itemDate = dataItem[0].date
            this.itemEmail = dataItem[0].email
        },
        deleteItem(id){
            var index = this.list.findIndex((item) => (item.id == id))
            this.list.splice(index,1)
        }
    },
    props: ['isShow1']
}
export default Content
</script>

<style></style>