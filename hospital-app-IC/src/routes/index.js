import React from 'react'

import { NavigationContainer } from '@react-navigation/native'

import { createNativeStackNavigator } from '@react-navigation/native-stack'

import { Home } from '../screens/Home'

import { Patient } from '../screens/Patient'

import { Stock } from '../screens/Stock'

import {Medication} from '../screens/Medication'

import {Treatment} from '../screens/Treatment'

import {UpdateStock} from '../screens/UpdateStock'

import {TrackStock} from '../screens/TrackStock'

import {Doctor} from '../screens/Doctor'

import {Nurse} from '../screens/Nurse'

import { Secretary } from '../screens/Secretary'

import {HospitalPharmacy} from '../screens/HospitalPharmacy'

import {Historic} from '../screens/Historic'

import {PharmacyAuthorization} from '../screens/PharmacyAuthorization'

const Stack = createNativeStackNavigator()

export const Routes = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerShown: false
        }}
      >
        <Stack.Screen
          name="Home"
          component={Home} />
        <Stack.Screen
          name="Patient"
          component={Patient}
        />
        <Stack.Screen
          name="Stock"
          component={Stock}
        />
        <Stack.Screen
          name="Medication"
          component={Medication}
        />
        <Stack.Screen
          name="Treatment"
          component={Treatment}
        />
        <Stack.Screen
          name="UpdateStock"
          component={UpdateStock}
        />
        <Stack.Screen
          name="TrackStock"
          component={TrackStock}
        />
        <Stack.Screen
          name="Doctor"
          component={Doctor}
        />
        <Stack.Screen
          name="Nurse"
          component={Nurse}
        />
        <Stack.Screen
          name="Secretary"
          component={Secretary}
        />
        <Stack.Screen
          name="HospitalPharmacy"
          component={HospitalPharmacy}
        />
        <Stack.Screen
          name="Historic"
          component={Historic}
        />
        <Stack.Screen
          name="PharmacyAuthorization"
          component={PharmacyAuthorization}
        />
      </Stack.Navigator>
    </NavigationContainer>
  )
}