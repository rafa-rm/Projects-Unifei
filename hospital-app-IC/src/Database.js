import AsyncStorage from '@react-native-async-storage/async-storage';

async function createPatient(patient){ 
    try{
        const listItem = patient;
        let savedItems = [];
        const response = await AsyncStorage.getItem('patients');

        if(response) savedItems = JSON.parse(response);
        savedItems.push(listItem);
        savedItems.sort((a,b) => (a.name < b.name) ? -1 : ((a.name > b.name) ? 1 : 0));

        await AsyncStorage.setItem('patients', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}


async function createStock(medicine){ 
    try{
        const listItem = medicine;
        let savedItems = [];
        const response = await AsyncStorage.getItem('stock');
        
        if(response) savedItems = JSON.parse(response);
        savedItems.push(listItem);
        savedItems.sort((a,b) => (a.name < b.name) ? -1 : ((a.name > b.name) ? 1 : 0));

        await AsyncStorage.setItem('stock', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}

async function removeStock(name){
    try{
        let savedItems = [];
        const response = await AsyncStorage.getItem('stock');

        if(response) savedItems = JSON.parse(response);
        const index = await savedItems.findIndex(item => item.name === name);
        savedItems.splice(index, 1);
        await AsyncStorage.setItem('stock', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}

async function updateStock(name, quantity){
    try{
        const listItem = {name,quantity};
        let savedItems = [];
        const response = await AsyncStorage.getItem('stock');

        if(response) savedItems = JSON.parse(response);
        const index = await savedItems.findIndex(item => item.name === name);
        savedItems.splice(index, 1);

        savedItems.push(listItem);
        savedItems.sort((a,b) => (a.name < b.name) ? -1 : ((a.name > b.name) ? 1 : 0));

        await AsyncStorage.setItem('stock', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}

async function createMedication(medicine, miliDateFirst, dosesMedicine, intervalMedicine){ 
    try{
        for(let i = 0; i < dosesMedicine; i++){
            const listItem = medicine;
            listItem ['id'] = new Date().getTime();
            listItem ['dateMedicine'] = new Date(miliDateFirst + intervalMedicine*i);
            listItem ['dose'] = i+1;
            let savedItems = [];
            const response = await AsyncStorage.getItem('medicines');

            if(response) savedItems = JSON.parse(response);
            savedItems.push(listItem);
            savedItems.sort((a,b) => (a.dateMedicine < b.dateMedicine) ? -1 : ((a.dateMedicine > b.dateMedicine) ? 1 : 0));

            await AsyncStorage.setItem('medicines', JSON.stringify(savedItems));
        }
    }
    catch(e){
        console.log(e);
    }
}

async function createHistoric(patient, medicine, miliDateFirst, dosesMedicine, intervalMedicine){ 
    try{
        const listItem = {patient, medicine,dosesMedicine};
        listItem ['id'] = new Date().getTime();
        listItem ['firstDate'] = new Date(miliDateFirst);
        listItem ['lastDate'] = new Date(miliDateFirst + intervalMedicine*dosesMedicine);
        let savedItems = [];
        const response = await AsyncStorage.getItem('historic');

        if(response) savedItems = JSON.parse(response);
        savedItems.push(listItem);
        savedItems.sort((a,b) => (a.patient < b.patient) ? -1 : ((a.patient > b.patient) ? 1 : 0));

        await AsyncStorage.setItem('historic', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}

async function updateMedication(id){ 
    try{
        let savedItems = [];
        const response = await AsyncStorage.getItem('medicines');
        if(response) savedItems = JSON.parse(response);

        const index = await savedItems.findIndex(item => item.id === id);
        if(savedItems[index].status === "Encaminhado") {
            savedItems[index].status = "Administrado";
        }
        if(savedItems[index].status === "Preparado") {
            savedItems[index].status = "Encaminhado";
        }
        if(savedItems[index].status === "Autorizado") {
            savedItems[index].status = "Preparado";
        }
        if(savedItems[index].status === "Aguardando Farmácia...") {
            savedItems[index].status = "Autorizado";
        }

        await AsyncStorage.setItem('medicines', JSON.stringify(savedItems));
    }
    catch(e){
        console.log(e);
    }
}


async function getPatients(){
    try{
        return AsyncStorage.getItem('patients')
            .then(response => {
                if (response)
                    return Promise.resolve(JSON.parse(response));
                else
                    return Promise.resolve([]);
            })
    }
    catch(e){
        console.log(e);
    }
}

async function getStock(){
    try{
        return AsyncStorage.getItem('stock')
            .then(response => {
                if (response)
                    return Promise.resolve(JSON.parse(response));
                else
                    return Promise.resolve([]);
            })
    }
    catch(e){
        console.log(e);
    }
}


async function getMedications(){
    try{
        return AsyncStorage.getItem('medicines')
            .then(response => {
                if (response)
                    return Promise.resolve(JSON.parse(response));
                else
                    return Promise.resolve([]);
            })
    }
    catch(e){
        console.log(e);
    }
}

async function getHistoric(){
    try{
        return AsyncStorage.getItem('historic')
            .then(response => {
                if (response)
                    return Promise.resolve(JSON.parse(response));
                else
                    return Promise.resolve([]);
            })
    }
    catch(e){
        console.log(e);
    }
}

module.exports = {
    createPatient,
    createStock,
    updateStock,
    removeStock,
    createMedication,
    updateMedication,
    getMedications,
    getPatients,
    getStock,
    createHistoric,
    getHistoric
}