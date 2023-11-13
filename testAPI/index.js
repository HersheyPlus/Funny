const express = require('express')
const app = express()

app.use(express.json())


const users = [
    {
        name:"Bobby",
        age:42,
        country:"Thaliand"
    },
    {
        name:"Tommy",
        age:16,
        country:"Belgium"
    },
    {
        name:"Pattrick",
        age:26,
        country:"England"
    },
]
app.get('/api/test',(req,res)=>{
    res.json(users)
})

app.listen(5000,()=>{
    console.log("start running 5000")
})