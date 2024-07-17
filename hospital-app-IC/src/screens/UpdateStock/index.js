import React from "react";

import {SafeAreaView, TouchableOpacity, Text, ScrollView, Alert, View, TextInput} from "react-native"

import styles from "../../global/styles"

import Database from '../../Database'

import DropDownPicker from 'react-native-dropdown-picker';

export const UpdateStock = ({navigation}) => {

    const [medicines, setMedicines] = React.useState([]);

    const [selectedMedicine, setSelectedMedicine] = React.useState(null);

    const [medicineOpen, setMedicineOpen] = React.useState(false);

    const [quantity, onChangeQuantity] = React.useState(null);

    React.useEffect(() => {
        Database.getStock().then(medicines => setMedicines(medicines));
    }, [selectedMedicine]);
    
    function handleButtonPress(medicine) { 
        Alert.alert(
            "Atenção",
            "Deseja alterar a quantidade deste medicamento no estoque?",
            [
                {
                    text: "Não",
                    style: "cancel"
                },
                {
                    text: "Sim",
                    onPress: () => {
                        Database.updateStock(selectedMedicine.name, quantity);
                        setSelectedMedicine(null);
                    }
                }
            ],
            {cancelable: false}
        );
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
                <Text style={styles.title}>Atualização do estoque</Text>
                {<DropDownPicker styles = {styles.picker}
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
                />}

                {selectedMedicine ? 
                    <View style={styles.content}>
                        <Text style={styles.text}>Nova quantidade de {selectedMedicine.name}:</Text>
                        <TextInput 
                        style={styles.input}
                        onChangeText={onChangeQuantity}
                        value={quantity}
                        placeholder="Ex.: 25"
                        keyboardType="numeric"
                        />
                        <TouchableOpacity style={styles.button} onPress={() => handleButtonPress()}>
                            <Text style={styles.buttonText}>Alterar Quantidade</Text>
                        </TouchableOpacity>
                    </View> : null
                }
            </ScrollView>
        </SafeAreaView>
    )
}