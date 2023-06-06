<template>
    <div class="m-[15px] border-solid border-2 rounded-lg w-[calc(100%-30px)] h-[calc(100vh-80px)] bg-white">
        <h1 class="text-black px-[15px] py-[12px] text-lg font-bold">Student List</h1>
        
        <div class="flex justify-center">
            <div class="flex flex-col px-[15px]">
                <label class="text-black">Fullname</label>
                <input class="w-[200px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Mai Tien Dat" v-model="itemName"/>
            </div>
            <div class="flex flex-col px-[15px]">
                <label class="text-black">Address</label>
                <input class="w-[200px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Nam Dinh" v-model="itemAddress"/>
            </div>
            <div class="flex flex-col px-[15px]">
                <label class="text-black">Date</label>
                <input class="w-[200px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" 28/02/2000" v-model="itemDate"/>
            </div>
            <div class="flex flex-col px-[15px]">
                <label class="text-black">Email</label>
                <input class="w-[200px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Dat.mt@sis.hust.edu.vn" v-model="itemEmail"/>
            </div>
            <div class="py-[24px]">
                <button @click="createItems()" class="bg-green-800 w-[50px] h-[40px] rounded-lg">Add</button>
            </div>
        </div>

        <div class=" px-[30px]">
            <table class="text-black w-[100%] table-auto border-b-2 ">
                <tr class="text-left border-b-2 h-[40px]">
                    <th>Id</th>
                    <th>Fullname</th>
                    <th>Address</th>
                    <th>Date</th>
                    <th>Email</th>
                    <th>Action</th>
                </tr>
                <tr class="table-auto border-b-2 h-[40px]" v-for="(item, index) in data" :key="item.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ item.name }}</td> 
                    <td>{{ item.address }}</td> 
                    <td>{{ item.date }}</td> 
                    <td>{{ item.email }}</td> 
                    <td class="inline-flex relative items-center gap-4 py-[10px] w-full">
                        <svg @click="editItem(item.id)" class="w-[24px] h-[24px] mr-2 fill-green-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M362.7 19.3L314.3 67.7 444.3 197.7l48.4-48.4c25-25 25-65.5 0-90.5L453.3 19.3c-25-25-65.5-25-90.5 0zm-71 71L58.6 323.5c-10.4 10.4-18 23.3-22.2 37.4L1 481.2C-1.5 489.7 .8 498.8 7 505s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L421.7 220.3 291.7 90.3z"/></svg>
                        <svg @click="deleteItem(item.id)" class="w-[24px] h-[24px] fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M135.2 17.7C140.6 6.8 151.7 0 163.8 0H284.2c12.1 0 23.2 6.8 28.6 17.7L320 32h96c17.7 0 32 14.3 32 32s-14.3 32-32 32H32C14.3 96 0 81.7 0 64S14.3 32 32 32h96l7.2-14.3zM32 128H416V448c0 35.3-28.7 64-64 64H96c-35.3 0-64-28.7-64-64V128zm96 64c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16zm96 0c-8.8 0-16 7.2-16 16V432c0 8.8 7.2 16 16 16s16-7.2 16-16V208c0-8.8-7.2-16-16-16z"/></svg>
                    </td>
                </tr>
            </table>
        </div>
        <!-- <div class="flex justify-center absolute bottom-4 right-[600px]">
            <div class="text-black">
                <button class="px-[10px] hover:text-green-500"> < </button>
                <button class="px-[10px] hover:text-green-500">1</button>
                <button class="px-[10px] hover:text-green-500">2</button>
                <button class="px-[10px] hover:text-green-500">3</button>
                <button class="px-[10px] hover:text-green-500"> > </button>
            </div>
        </div> -->
        <div v-show="formModal" class="flex justify-center items-center h-full w-full bg-[#808080ab] absolute top-0 left-0">
            <div class="bg-white-600 custom-shadow h-[500px] w-[600px] rounded-3xl bg-white ">
                <h1 class="text-black text-center py-[20px] text-xl font-semibold">Student List</h1>
                <div class="flex flex-row justify-evenly py-[20px]">
                    <label class="text-black leading-10 px-[15px]">Fullname</label>
                    <input class="w-[300px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Mai Tien Dat" v-model="itemName"/>
                </div>
                <div class="flex flex-row justify-evenly py-[20px]">
                    <label class="text-black leading-10  px-[15px]">Address</label>
                    <input class="w-[300px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Nam Dinh" v-model="itemAddress"/>
                </div>
                <div class="flex flex-row justify-evenly py-[20px]">
                    <label class="text-black leading-10  px-[15px]">Date</label>
                    <input class="w-[300px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" 28/02/2000" v-model="itemDate"/>
                </div>
                <div class="flex flex-row justify-evenly py-[20px]">
                    <label class="text-black leading-10  px-[15px]">Email</label>
                    <input class="w-[300px] h-[40px] border-stone-400 border-2 rounded-lg leading-10 text-black" type="text" placeholder=" Dat.mt@sis.hust.edu.vn" v-model="itemEmail"/>
                </div>
                <div class="py-[24px] flex justify-center gap-4">
                    <button @click="save()" class="bg-green-500 text-white w-[100px] py-2 rounded-lg">Save</button>
                    <button @click="close()" class="bg-red-400 text-white w-[100px] py-2 rounded-lg">Cancel</button>
                </div>
            </div>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios'
import API_URL from '@/links/index.js'
const Homes = {
    data(){
        return{
            formModal: false,
            data: [],
            itemName:null,
            itemAddress:null,
            itemDate:null,
            itemEmail:null,
            id: null,
            list: []
        }
    },
    methods:{
        async getStudentList(){
            try{
               const {data} =await axios.get(`${API_URL}`)
               this.data = data.filter(item => item.active !==false )
                
            }catch(error){
                console.log(error)
            }
        },
        showmenu(){
            this.$emit('showmenu')
        },
        createItems(){
            axios.post(`${API_URL}`, {
                "name": this.itemName,
                "address": this.itemAddress,
                "date": this.itemDate,
                "email": this.itemEmail,
                "active": true
            })
            .then((response) => {
                this.getStudentList()
                this.itemName = null
                this.itemAddress = null
                this.itemDate = null
                this.itemEmail = null
            })
        },
        editItem(item){
            this.formModal = true
            this.item = item
            var items = this.data.filter((data) => (data.id == item))
            this.itemName = items[0].name 
            this.itemAddress = items[0].address
            this.itemDate = items[0].date
            this.itemEmail = items[0].email
        },
        close(){
            this.formModal = false
            this.itemName = null
            this.itemAddress = null
            this.itemDate = null
            this.itemEmail = null
        },
        save(){
            axios.patch(`${API_URL}${this.item}`, {
                "name": this.itemName,
                "address": this.itemAddress,
                "date": this.itemDate,
                "email": this.itemEmail,
                "active": true
            })
            .then((response) => {
                this.getStudentList()
                this.itemName = null
                this.itemAddress = null
                this.itemDate = null
                this.itemEmail = null
            })
            this.formModal = false
        },
        async deleteItem(item){
            console.log(item)
            try{
               const {data} =await axios.delete(`${API_URL}${item}`)
               this.data = data.filter(a => a.id == item)
                
            }catch(error){
                console.log('lỗi: ', error)
            }
            this.getStudentList()
        }
    },
    props: [],
    mounted(){
      this.getStudentList()
    }
}
export default Homes
</script>

<style></style>