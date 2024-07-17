import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

export const PharmacyAuthorization = ({navigation}) => {

    const [medications, setMedications] = React.useState([]);

    React.useEffect(() => {
        Database.getMedications().then(medications => setMedications(medications));
    },[medications]);
    
    function handleButtonPress(medication) { 
        if(medication.status === "Aguardando Farmácia..."){
            Alert.alert(
                "Atenção",
                "Deseja Autorizar?",
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
                <Text style={styles.title}>Autorização dos medicamentos</Text>
                {medications.map ((medication, index) => {
                    return(
                        medication.status === "Aguardando Farmácia..." ?
                        <View style={styles.content}key={index}>
                            <Text style={styles.text}>Paciente: {medication.patient} </Text>
                            <Text style={styles.text}>Medicamento: {medication.medicine}</Text>
                            <Text style={styles.text}>Quantidade: {medication.quantity}</Text>
                            <TouchableOpacity style={styles.button} onPress={() => handleButtonPress(medication)}>
                                <Text style={styles.buttonText}>Confirmar Medicamento</Text>
                            </TouchableOpacity>
                        </View> : null
                    ) 
                })}
            </ScrollView>
        </SafeAreaView>
    )
}
