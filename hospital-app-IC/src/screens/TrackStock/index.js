import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

export const TrackStock = ({navigation}) => {

    const [medicines, setMedicines] = React.useState([]);

    React.useEffect(() => {
        Database.getStock().then(medicines => setMedicines(medicines));
    }, []);

    function logoutButtonPress(){
        navigation.navigate('Home');
    }

    medicines.sort((a,b) => (a.quantity < b.quantity) ? -1 : ((a.quantity > b.quantity) ? 1 : 0));

    return( 
        <SafeAreaView style={styles.container}>
            <ScrollView style={styles.scroll}>
                <TouchableOpacity style={styles.buttonLogout} onPress={logoutButtonPress}>
                    <Text style={styles.logoutText}> Sair </Text>
                </TouchableOpacity>
                <Text style={styles.title}>Acompanhar estoque dos medicamentos</Text>
                {medicines.map ((medicine, index) => {
                    return(
                        <View style={styles.content}key={index}>
                            <Text style={styles.text}>Medicamento: {medicine.name} </Text>
                            <Text style={styles.text}>Quantidade: {medicine.quantity}</Text>
                        </View> 
                    ) 
                })}
            </ScrollView>
        </SafeAreaView>
    )
}