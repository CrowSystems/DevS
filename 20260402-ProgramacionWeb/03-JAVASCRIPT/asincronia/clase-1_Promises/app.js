const Promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        let operationSuccessfull = true;
        if(operationSuccessfull){
            resolve("La operacion fue exitosa")
        } else {
            reject("Fallo la operacion");
        }
    }, 2000);   
});

promise
    .then((successMessage)=> {
        console.log(successMessage)
    })
    .catch((errorMessage) => {
        console.log(errorMessage)
    });