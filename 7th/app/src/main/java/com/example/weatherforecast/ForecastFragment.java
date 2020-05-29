package com.example.weatherforecast;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import android.os.IBinder;
import android.os.RemoteException;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ForecastFragment extends Fragment {

    public static final String ACTION_RETRIEVE_WEATHER_DATA = "com.example.WeatherForecast.RETRIEVE_DATA";

    private IFetchWeatherService mService;
    private ServiceConnection mServiceConnection = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            mServiceConnection = (ServiceConnection) IFetchWeatherService.Stub.asInterface(service);

            try {
                mService.registerFetchDataListener(mFetchDataListener);
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void onServiceDisconnected(ComponentName name) {
            mService = null;
        }
    };

    private IFetchDataListener.Stub mFetchDataListener = new IFetchDataListener.Stub() {
        @Override
        public void onWeatherDataRetrieved(String[] data) throws RemoteException {
            mForecastAdapter.clear();
            for(String forecasteddata : data) {
                mForecastAdapter.add(forecasteddata);
            }
        }
    };

    private BroadcastReceiver mBroadcastReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if(action.equals(FetchWeatherService.ACTION_RETREVE_WEATHER_DATA)) {
                String[] data = intent.getStringArrayExtra(FetchWeatherService.EXTRA_WEATHER_DATA);
                mForecastAdapter.clear();
                for(String dayForecastStr : data) {
                    mForecastAdapter.add(dayForecastStr);
                }
            }
        }
    };
    private ArrayAdapter<String> mForecastAdapter;



    public static ForecastFragment newInstance() {
        return new ForecastFragment();
    }

    @Override
    public void onDestroy(){
        if(mService != null){
            try{
                mService.unregisterFetchDataListener(mFetchDataListener);
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }
        getActivity().unbindService(mServiceConnection);
        super.onDestroy();
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setHasOptionsMenu(true);
    }


    private void refreshWeatherData() {
        if(mService != null){
            try{
                mService.retrieveWeatherData();
            } catch (RemoteException e) {
                e.printStackTrace();
            }
        }
    }

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        String[] data = {
                "Mon 6/23 - Sunny 31/17",
                "Tue 6/24 - Foggy - 21/8",
                "Wed 6/25 - Cloudy - 22/17",
                "Thurs 6/26 - Rainy - 18/11",
                "Fri 6/27 - Foggy - 21/10",
                "Sat 6/28 - TRAPPED IN WEATHERSTATION - 23/18",
                "Sun 6/29 - Sunny - 20/7"
        };

        List<String> weekForecast = new ArrayList<String>(Arrays.asList(data));

        mForecastAdapter = new ArrayAdapter<String>(getActivity(),
                R.layout.list_view_item,
                R.id.list_item_forecast_textview,
                weekForecast);

        View rootView = inflater.inflate(R.layout.main_fragment, container, false);

        ListView listView = (ListView) rootView.findViewById(R.id.listview_forecast);
        listView.setAdapter(mForecastAdapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                String forecast = mForecastAdapter.getItem(position);
                Toast.makeText(getActivity(), forecast, Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(getActivity(), DetailActivity.class);
                intent.putExtra("data", forecast);
            }
        });

        IntentFilter intentFilter = new IntentFilter(FetchWeatherService.ACTION_RETREVE_WEATHER_DATA);
        getActivity().registerReceiver(mBroadcastReceiver, intentFilter);
        return rootView;
    }


}
