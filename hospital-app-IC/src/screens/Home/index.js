import React from "react";

import {SafeAreaView, TouchableOpacity, Text, TextInput} from "react-native"

import styles from "../../global/styles"

export const Home = ( {navigation} ) => {
    const [username, onChangeUsername] = React.useState(null);
    const [password, onChangePassword] = React.useState(null);

    function resetHooks(){
        onChangeUsername(null);
        onChangePassword(null);
    }
    function handleButtonPress(){
        if((username == "Doc") && (password == "Doc")){
            navigation.navigate('Doctor');
            resetHooks();
        }
        if((username == "Nurse") && (password == "Nurse")){
            navigation.navigate('Nurse');
            resetHooks();
        }
        if((username == "Sec") && (password == "Sec")){
            navigation.navigate('Secretary');
            resetHooks();
        }
        if((username == "Phar") && (password == "Phar")){
            navigation.navigate('HospitalPharmacy');
            resetHooks();
        }
    }

    return( 
        <SafeAreaView style={styles.container}>
            <Text style={styles.title}> Login no sistema</Text>
            <TextInput 
                style={styles.input}
                onChangeText={onChangeUsername}
                value={username}
                placeholder="Username"
            />
            <TextInput 
                style={styles.input}
                onChangeText={onChangePassword}
                value={password}
                placeholder="Password"
                secureTextEntry={true}
            />
            
            <TouchableOpacity style={styles.button} onPress={handleButtonPress}>
                <Text style={styles.buttonText}>  Login no sistema </Text>
            </TouchableOpacity>
        </SafeAreaView>
    )
}