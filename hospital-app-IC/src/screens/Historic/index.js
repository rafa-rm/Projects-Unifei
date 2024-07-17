import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, TextInput, View} from "react-native"

import styles from "../../global/styles"

import DropDownPicker from 'react-native-dropdown-picker';

import Database from '../../Database'

export const Historic = ({navigation}) => {

    const [patients, setPatients] = React.useState([]);

    const [patientsStatus, setPatientsStatus] = React.useState([]);

    const [selectedPatient, setSelectedPatient] = React.useState(null);

    const [discharged, setDischarged] = React.useState(true);

    const [open, setOpen] = React.useState(false);

    React.useEffect(() => {
        Database.getHistoric().then(patients => setPatients(patients));
        Database.getMedications().then(patientsStatus => setPatientsStatus(patientsStatus));
        isDischarged(patientsStatus);
    },[selectedPatient]);

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    function noRepeat(patients){
        return(
            patients.map((patient, index) => {
                if(index > 0){
                    if(patients[index].patient !== patients[index - 1].patient ){
                        return(
                        {
                            label: patient.patient,
                            value: patient
                        })
                    }
                    else{
                        return 
                    }
                }
                else{
                    return(
                        {
                            label: patient.patient,
                            value: patient
                        })
                }
        }))
    }

    function isDischarged(patientsStatus){
        setDischarged(true);
        patientsStatus.map((patientStatus) => {
            if(patientStatus.status !== "Administrado"){
                console.log(patientStatus)
                setDischarged(false);
                return false;
            }
        })
        return true;
    }

    return(
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll} showsVerticalScrollIndicator= {false} >
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}>Histórico do paciente</Text>
                <DropDownPicker styles = {styles.picker}
                    items=
                    {noRepeat(patients).filter(function( element ) {
                        return element !== undefined;
                     })}
                    open={open}
                    value={selectedPatient}
                    setOpen={setOpen}
                    setValue={setSelectedPatient}
                    setItems={setPatients}
                    searchable={true}
                    placeholder="Selecione um paciente"
                    listMode="MODAL"
                />
                {   selectedPatient ? 
                    <View style={styles.content}>
                        <Text style={styles.text}>{selectedPatient.patient} {discharged ? 'já teve alta' : 'ainda não teve alta'} </Text>
                    </View>
                    /*discharged ? 
                        <Text styles = {styles.text}>{selectedPatient.patient} já teve alta</Text> : 
                        <Text styles = {styles.text}>{selectedPatient.patient} ainda não teve alta</Text> :*/
                    : null
                } 
                {patients.map((patient) => {
                    if(selectedPatient){
                        if(patient.patient === selectedPatient.patient){
                            return(
                                <View style={styles.content}>
                                    <Text style={styles.text}> Remédio utilizado: {patient.medicine}</Text>
                                    <Text style={styles.text}> Primeira dose: {patient.firstDate.substr(0,10)} {patient.firstDate.substr(11,5)}</Text>
                                    <Text style={styles.text}> Número de doses: {patient.dosesMedicine}</Text>
                                </View>
                            )
                        }
                    }
                })}
            </ScrollView>
        </SafeAreaView>
    )
}