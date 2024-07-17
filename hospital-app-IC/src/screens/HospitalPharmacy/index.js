import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View} from "react-native"

import styles from "../../global/styles"

export const HospitalPharmacy = ({navigation}) => {

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    function stockButtonPress(){
        navigation.navigate('Stock');
    }

    function updateStockButtonPress(){
        navigation.navigate('UpdateStock');
    }

    function trackStockButtonPress(){
        navigation.navigate('TrackStock');
    }

    function AuthorizationButtonPress(){
        navigation.navigate('PharmacyAuthorization');
    }
    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll}>
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}>Selecione a função que deseja realizar</Text>

                <TouchableOpacity style={styles.button} onPress={stockButtonPress}>
                    <Text style={styles.buttonText}>Cadastrar no estoque</Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.button} onPress={updateStockButtonPress}>
                    <Text style={styles.buttonText}>Atualizar do estoque</Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.button} onPress={trackStockButtonPress}>
                    <Text style={styles.buttonText}>Acompanhar o estoque</Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.button} onPress={AuthorizationButtonPress}>
                    <Text style={styles.buttonText}>Autorizar os medicamentos</Text>
                </TouchableOpacity>

            </ScrollView>
        </SafeAreaView>
    )
}