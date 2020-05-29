// IFetchDataListener.aidl
package com.example.weatherforecast;

// Declare any non-default types here with import statements

interface IFetchDataListener {
    /**
     * Demonstrates some basic types that you can use as parameters
     * and return values in AIDL.
     */
    void onWeatherDataRetrieved(String[] data);
}
