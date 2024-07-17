import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View} from "react-native"

import styles from "../../global/styles"

export const Nurse = ({navigation}) => {

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    function patientButtonPress(){
        navigation.navigate('Patient');
    }

    function treatmentButtonPress(){
        navigation.navigate('Treatment');
    }

    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll}>
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}>Selecione a função que deseja realizar</Text>

                <TouchableOpacity style={styles.button} onPress={patientButtonPress}>
                    <Text style={styles.buttonText}>Cadastrar o paciente</Text>
                </TouchableOpacity>
                
                <TouchableOpacity style={styles.button} onPress={treatmentButtonPress}>
                    <Text style={styles.buttonText}>Ministrar medicação</Text>
                </TouchableOpacity>

            </ScrollView>
        </SafeAreaView>
    )
}