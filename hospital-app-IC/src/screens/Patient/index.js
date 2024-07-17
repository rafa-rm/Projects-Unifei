import React from "react";

import {SafeAreaView, TouchableOpacity, Text, TextInput, Alert, ScrollView} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

export const Patient = ({navigation}) => {
    const [name, onChangeName] = React.useState(null);
    const [weight, onChangeWeight] = React.useState(null);
    const [height, onChangeHeight] = React.useState(null);
    const [age, onChangeAge] = React.useState(null);
    const [local, onChangeLocal] = React.useState(null);

    function handleButtonPress(){ 
        if(name === null || weight === null || age === null || height === null
            || name === "" || weight === "" || age === "" || height === ""){
            Alert.alert("Preencha todos os campos corretamente!");
        }
        else{
            Database.createPatient({name, weight: parseFloat(weight), height: parseFloat(height), age: parseInt(age), local: local});
            onChangeName(null);
            onChangeWeight(null);
            onChangeHeight(null);
            onChangeAge(null);
            onChangeLocal(null);
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
                <Text style={styles.title}> Cadastro do paciente</Text>
                <Text style={styles.text}> Nome </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeName}
                    value={name}
                    placeholder="Ex.: José da Silva"
                />

                <Text style={styles.text}> Peso </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeWeight}
                    value={weight}
                    placeholder="Ex.: 70.65"
                    keyboardType="numeric"
                />

                <Text style={styles.text}> Altura </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeHeight}
                    value={height}
                    placeholder="Ex.: 1.85"
                    keyboardType="numeric"
                />

                <Text style={styles.text}> Idade </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeAge}
                    value={age}
                    placeholder="Ex.: 19"
                    keyboardType="number-pad"
                />

                <Text style={styles.text}> Localização </Text>
                <TextInput 
                    style={styles.input}
                    onChangeText={onChangeLocal}
                    value={local}
                    placeholder="Ex.: Quarto individual 3"
                />
                <TouchableOpacity style={styles.button} onPress={handleButtonPress}>
                    <Text style={styles.buttonText}> Cadastrar paciente </Text>
                </TouchableOpacity>
            </ScrollView>
        </SafeAreaView>
    )
}