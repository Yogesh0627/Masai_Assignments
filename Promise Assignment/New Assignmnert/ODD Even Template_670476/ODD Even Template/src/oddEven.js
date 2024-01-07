function getData(data) {
    return  promise1 = new Promise(function(resolve,reject){
        if (data % 2 == 0){
            setTimeout(function(){
                resolve("Even")
            },4000)
        }
        else if (data % 2 == 1){
            setTimeout(function(){
                resolve("Odd")
            },2000)
        }
        else{reject("Error")}
    })
    // return promise1
}
getData(10).then(function(data1){
    console.log(data1)}).catch(function(data2){
    console.log(data2)})


// export default getData


