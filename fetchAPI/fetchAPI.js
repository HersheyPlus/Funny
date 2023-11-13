const url = 'https://jsonplaceholder.typicode.com/comments'
/*
https://jsonplaceholder.typicode.com/photos
https://jsonplaceholder.typicode.com/todos
https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/posts
*/
const fetchData = fetch(url).then(res => res.json()) // convert to json
.then(data=>{
    let count = 0
    data.forEach(element => {
        console.log(element)
        count++
    })
    console.log(`\n\x1b[32m----- Fetch successfully! -----\x1b[0m`)
    console.log(`\x1b[33m>>>>> Data(s): ${count} elements,\x1b[0m`)
    console.log(`\x1b[31m>>>>> Source:\x1b[0m ${url}\n`)
})
.catch(err=>{
    console.log("Error fetch data...",err)
    console.log(`Are you sure this link: ${url} is right ?`)
})

fetchData

/**
    \x1b[31m set color to red
    \x1b[0m resets the text color to  default.
 */