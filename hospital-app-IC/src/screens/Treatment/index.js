import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

export const Treatment = ({navigation}) => {

    const [medications, setMedications] = React.useState([]);

    React.useEffect(() => {
        Database.getMedications().then(medications => setMedications(medications));
    },[medications]);
    
    function handleButtonPress(medication) { 
        if(medication.status === "Aguardando Farmácia..."){
            Alert.alert(
                "Atenção",
                "É necessário a autorização da farmácia",
                [{
                    text: "Ok",
                    style: "cancel"
                }],
                {cancelable: false}
            );
        }
        if(medication.status === "Autorizado"){
            Alert.alert(
                "Atenção",
                "Deseja iniciar a preparação da medicação?",
                [
                    {
                        text: "Não",
                        style: "cancel"
                    },
                    {
                        text: "Sim",
                        onPress: () => {
                            Database.updateMedication(medication.id);
                        }
                    }
                ],
                {cancelable: false}
            );
        }
        if(medication.status === "Encaminhado"){
            Alert.alert(
                "Você está concluindo a medicação do paciente",
                "Deseja continuar?",
                [
                    {
                        text: "Não",
                        style: "cancel"
                    },
                    {
                        text: "Sim",
                        onPress: () => {
                            Database.updateMedication(medication.id);
                        }
                    }
                ],
                {cancelable: false}
            );
        }
        if(medication.status === "Preparado"){
            Alert.alert(
                "Você está encaminhando o medicamento ao paciente",
                "Deseja continuar?",
                [
                    {
                        text: "Não",
                        style: "cancel"
                    },
                    {
                        text: "Sim",
                        onPress: () => {
                            Database.updateMedication(medication.id);
                        }
                    }
                ],
                {cancelable: false}
            );
        }
    }

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll}>
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}>Acompanhamento dos pacientes</Text>
                {medications.map ((medication, index) => {
                    return(
                        medication.status !== 'Administrado' ?
                        <View style={styles.content}key={index}>
                            <Text style={styles.text}>Paciente: {medication.patient} </Text>
                            <Text style={styles.text}>Medicamento: {medication.medicine}</Text>
                            <Text style={styles.text}>Quantidade: {medication.quantity}</Text>
                            <Text style={styles.text}>Dia e Hora: {new Date(medication.dateMedicine).toUTCString()}</Text>
                            <Text style={styles.text}>Dose {medication.dose}</Text>
                            <Text style={styles.text}>Status: {medication.status}</Text>
                            <TouchableOpacity style={styles.button} onPress={() => handleButtonPress(medication)}>
                                <Text style={styles.buttonText}>Atualizar Status</Text>
                            </TouchableOpacity>
                        </View> : null
                    ) 
                })}
            </ScrollView>
        </SafeAreaView>
    )
}