import React from "react";

import {SafeAreaView, TouchableOpacity, Text, TextInput, Alert, ScrollView} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

import DropDownPicker from 'react-native-dropdown-picker';

import DateTimePickerModal from "react-native-modal-datetime-picker";


export const Medication = ({navigation}) => {
    const [selectedPatient, setSelectedPatient] = React.useState(null);
    const [selectedMedicine, setSelectedMedicine] = React.useState(null);
    const [dateFirstMedicine, setDateFirstMedicine] = React.useState(null);
    const [patients, setPatients] = React.useState([]);
    const [medicines, setMedicines] = React.useState([]);
    const [intervalMedicine, setIntervalMedicine] = React.useState(null);
    const [dosesMedicine, setDosesMedicine] = React.useState(null);
    const [quantityMedicine, setQuantityMedicine] = React.useState(null);

    const [patientOpen, setPatientOpen] = React.useState(false);
    const [medicineOpen, setMedicineOpen] = React.useState(false);

    const [isDatePickerVisible, setDatePickerVisibility] = React.useState(false);

    function resetHooks(){
        setSelectedPatient(null);
        setSelectedMedicine(null);
        setDateFirstMedicine(null);
        setPatients([]);
        setMedicines([]);
        setIntervalMedicine(null);
        setDosesMedicine(null);
        setQuantityMedicine(null);
        setDatePickerVisibility(false);
    }

    const showDatePicker = () => {
        setDatePickerVisibility(true);
    };
    
    const hideDatePicker = () => {
        setDatePickerVisibility(false);
    };
    
    const handleConfirm = (date) => {
        setDateFirstMedicine(new Date(date-10800000))
        hideDatePicker();
    };

    React.useEffect(() => {
        Database.getPatients().then(patients => setPatients(patients));
        Database.getStock().then(medicines => setMedicines(medicines));
    },[]);

    async function handleButtonPress(){ 
        if(intervalMedicine === null || dosesMedicine === null || quantityMedicine === null || 
            intervalMedicine === "" || dosesMedicine === "" || quantityMedicine === ""){
            Alert.alert("Preencha todos os campos corretamente! ");
        }
        else if(dateFirstMedicine === null || selectedPatient === null || selectedMedicine === null){
            Alert.alert("Selecione os campos corretamente! ");
        }
        else{
            let miliDateFirst = Date.parse(new Date(dateFirstMedicine).toString());
            Database.createMedication({patient: selectedPatient.name, medicine: selectedMedicine.name, quantity: quantityMedicine, status: "Aguardando Farmácia..."},
            miliDateFirst, dosesMedicine ,3600000*intervalMedicine);
            Database.updateStock(selectedMedicine.name,selectedMedicine.quantity - (parseFloat(quantityMedicine) * parseFloat(dosesMedicine)));
            Database.createHistoric(selectedPatient.name,selectedMedicine.name,miliDateFirst, dosesMedicine ,3600000*intervalMedicine);
            resetHooks();
        }
    }

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll} showsVerticalScrollIndicator= {false} >
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}> Cadastro de Medicação</Text>
                <Text style={styles.text}> Paciente</Text>
                <DropDownPicker styles = {styles.picker}
                    items={patients.map((patient) => {
                        return  ({
                            label: patient.name,
                            value: patient,
                        })
                    })}
                    open={patientOpen}
                    value={selectedPatient}
                    setOpen={setPatientOpen}
                    setValue={setSelectedPatient}
                    setItems={setPatients}
                    searchable={true}
                    placeholder="Selecione um paciente"
                    listMode="MODAL"
                />
                <Text style={styles.text}> Medicamento</Text>
                <DropDownPicker styles = {styles.picker}
                    items={medicines.map((medicine) => {
                        return  ({
                            label: medicine.name,
                            value: medicine,
                        })
                    })}
                    open={medicineOpen}
                    value={selectedMedicine}
                    setOpen={setMedicineOpen}
                    setValue={setSelectedMedicine}
                    setItems={setMedicines}
                    searchable={true}
                    placeholder="Selecione um medicamento"
                    listMode="MODAL"
                />
                {/*<Picker
                    style={styles.picker}
                    selectedValue={selectedPatient}
                    onValueChange={(patientValue, patientIndex) =>
                    setSelectedPatient(patientValue)
                }>
                    <Picker.Item key = {-5} label = {"Selecione"} value = {null} />
                    {patients.map((patient,index) => {
                        return <Picker.Item key = {index} label = {patient.name} value = {patient.name}/>
                    })}
                </Picker>
                <Text style={styles.text}>Selecione o Medicamento</Text>
                <Picker
                    style={styles.picker}
                    selectedValue={selectedMedicine}
                    onValueChange={(medicineValue, medicineIndex) =>
                    setSelectedMedicine(medicineValue)
                }>
                    <Picker.Item key = {-3} label = {"Selecione"} value = {{}} />
                    {medicines.map((medicine,index) => {
                        return <Picker.Item key = {index} label = {medicine.name} value = {medicine}/>
                    })}
                </Picker>*/}

                <Text style={styles.text}>Selecione a data e horário para medicação</Text>
                <TouchableOpacity style={styles.button} onPress={showDatePicker}>
                    <Text style={styles.buttonText}>Clique para selecionar</Text>
                </TouchableOpacity>
                <DateTimePickerModal
                    isVisible={isDatePickerVisible}
                    mode="datetime"
                    onConfirm={handleConfirm}
                    onCancel={hideDatePicker}
                />
                {dateFirstMedicine ? 
                    <Text style = {styles.dateText}>
                        Dia selecionado: 
                        {' '}{dateFirstMedicine.getDate()} / {dateFirstMedicine.getMonth() + 1} / {dateFirstMedicine.getFullYear()}
                        {"\n"}Horário selecionado:
                        {' '}{dateFirstMedicine.getUTCHours()}:{dateFirstMedicine.getMinutes()}
                    </Text>
                : null}

                <Text style={styles.text}>Quantidade de medicamento a ser aplicado em cada dose</Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={setQuantityMedicine}
                    value={quantityMedicine}
                    placeholder="Ex.: 1"
                    keyboardType="numeric"
                />
                <Text style={styles.text}>Numero de doses </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={setDosesMedicine}
                    value={dosesMedicine}
                    placeholder="Ex.: 2"
                    keyboardType="numeric"
                />
                <Text style={styles.text}>Tempo entre as doses (em horas)</Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={setIntervalMedicine}
                    value={intervalMedicine}
                    placeholder="Ex.: 6"
                    keyboardType="numeric"
                />
                <TouchableOpacity style={styles.button} onPress={handleButtonPress}>
                    <Text style={styles.buttonText}> Medicar o paciente </Text>
                </TouchableOpacity>
            </ScrollView>
        </SafeAreaView>    
    )
}