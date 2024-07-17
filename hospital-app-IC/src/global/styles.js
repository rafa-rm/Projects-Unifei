import { StyleSheet} from "react-native";

export default StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'flex-start',
        backgroundColor: '#e2f5f2',
    },
    scroll: {
        marginLeft: 10,
        marginRight: 10
    },
    title: {
        margin: 40,
        textAlign: 'center',
        fontSize: 26,
    },
    text: {
        marginLeft: 14,
        marginTop: 5,
        marginBottom: 5,
        fontSize: 20,
        textAlign: 'left',
    },
    dateText: {
        marginLeft: 20,
        marginRight: 20,
        marginBottom: 5,
        marginTop: 5,
        fontSize: 20,
        borderRadius: 20,
        textAlign: 'center',
        backgroundColor: '#c1d6d3'
    },
    content: {
        backgroundColor: '#c1d6d3',
        margin: 10,
        borderRadius: 20
    },
    button: {
        backgroundColor: '#fff',
        justifyContent: 'center',
        alignItems: 'center',
        height: 60,
        marginTop: 10,
        marginBottom: 10,
        width: '85%',
        left: '7.5%',
        borderRadius: 20
    },
    buttonText: {
        textAlign: 'center',
        justifyContent: 'center',
        fontSize: 20,
        padding: '5%',
    },
    buttonLogout: {
        backgroundColor: '#ddd',
        top: 40,
        left: '80%',
        width: '15%',
        borderRadius: 20,
    },
    logoutText: {
        fontSize: 16,
        padding: 8,
    },
    input: {
        backgroundColor: '#FFF',
        height: 50,
        margin: 12,
        padding: 10,
        borderRadius: 10,
    },
    picker: {
        backgroundColor: '#FFF',
        marginLeft: 20,
        marginRight: 20
    }
})