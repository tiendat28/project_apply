<template>
   <div class=" m-[15px] border-solid border-2 rounded-lg w-[calc(100%-30px)] h-[calc(100vh-80px)] bg-white">
        <select @change="choise($event)" class="m-[20px] bg-green-800 w-[200px] h-[40px] rounded-lg">
            <option>Select a student</option>
            <option v-for="item in data" :key="item.id" :value="item.id">{{ item.name }}</option>
        </select>
        <div class="text-black" v-for="item in list" :key="item.id">
            <h1>Name:<b>{{ item.name }}</b></h1>
            <h1>Address:<b>{{ item.address }}</b></h1>
        </div>
        <div class=" px-[30px]">
            <table class="text-black w-[100%] table-auto border-b-2 ">
                <tr class="text-left border-b-2 h-[40px]">
                    <th>Course</th>
                    <th>15'</th>
                    <th>30'</th>
                    <th>45'</th>
                    <th>60'</th>
                    <th>90'</th>
                    <th>GPA</th>
                    <th>Feedback</th>
                </tr>
                <tr class="table-auto border-b-2 h-[40px]" v-for="item in point" :key="item.id">
                    <td>{{ item.course }}</td>
                    <td>{{ item.a }}</td> 
                    <td>{{ item.b }}</td> 
                    <td>{{ item.c }}</td> 
                    <td>{{ item.d }}</td> 
                    <td>{{ item.e }}</td> 
                    <td>{{ (item.a + item.b + item.c + item.d + item.e)/5}}</td> 
                    <td>
                        <span style="color: green;" v-if="item.gpa > 8.5">Good</span>
                        <span style="color: red;" v-else>Bad</span>
                    </td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import API_URL from '@/links/index.js'
import API_URL_1 from '@/links/link1.js'
const Project = {
    data(){
        return{
            id:'',
            data: [],
            point: [],
            list:[],
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
        getPoint(){
           axios.get(`${API_URL_1}`)
           .then(response => {
            this.point = response.data
           })    
        },
        choise(e){
            axios.get(`${API_URL}`)
            .then(response => {
            const list = response.data.filter(item => item.id == e.target.value)
            console.log("list:",list)
            })
            .catch(error => {
            console.error(error);
            })
        }
        
    },
    mounted(){
      this.getStudentList()
      this.getPoint()
    }   
}
export default Project

</script>

<style></style>