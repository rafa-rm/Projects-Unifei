import React from "react";

import {SafeAreaView, TouchableOpacity, Text, TextInput, ScrollView, Alert} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

export const Stock = ({navigation}) => {
    const [unity,onChangeUnity] = React.useState(null);
    const [name, onChangeName] = React.useState(null);
    const [quantity, onChangeQuantity] = React.useState(null);

    
    function handleButtonPress(){ 
        if(name === null || quantity === null
            || name === "" || quantity === ""){
            Alert.alert("Preencha todos os campos corretamente!");
        }
        else{
            Database.createStock({name,unity,quantity: parseFloat(quantity)})  
            onChangeName(null);
            onChangeQuantity(null);  
        }
    }

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView>
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}> Cadastro no estoque de medicamentos</Text>
                <Text style={styles.text}> Nome </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeName}
                    value={name}
                    placeholder="Ex.: Tylenol"
                />

                <Text style={styles.text}> Unidade do medicamento </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeUnity}
                    value={unity}
                    placeholder="Ex.: 750 mg"
                />

                <Text style={styles.text}> Quantidade </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeQuantity}
                    value={quantity}
                    placeholder="Ex.: 25"
                    keyboardType="numeric"
                />
                
                <TouchableOpacity style={styles.button} onPress={handleButtonPress}>
                    <Text style={styles.buttonText}> Cadastrar no estoque </Text>
                </TouchableOpacity>
            </ScrollView>
        </SafeAreaView>
    )
}