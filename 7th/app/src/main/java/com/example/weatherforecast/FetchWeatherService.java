package com.example.weatherforecast;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.util.Log;

import androidx.annotation.Nullable;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import static android.app.PendingIntent.getActivity;

public class FetchWeatherService extends Service {
    public static final String ACTION_RETREVE_WEATHER_DATA = "com.XXX.weatherforecast.DATA_RETRIEVED";
    public static final String EXTRA_WEATHER_DATA = "weather-data";
    public FetchWeatherService(){
    }

    public int onStartCommand(Intent intent, int flags, int startId) {
        String action = intent.getAction();
        if(action.equals(ACTION_RETREVE_WEATHER_DATA)) {
            retrieveWeatherData(startId);
        }

        return super.onStartCommand(intent, flags, startId);
    }

    private void retrieveWeatherData(int startId) {
        FetchWeatherTask weatherTask = new FetchWeatherTask(startId);
        SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
        String cityId = preferences.getString("city", String.valueOf(1835847));
        weatherTask.execute(cityId);
    }

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    private void notifyWeatherDataRetrieved(String[] result) {
        Intent intent = new Intent(ACTION_RETREVE_WEATHER_DATA);
        intent.putExtra(EXTRA_WEATHER_DATA, result);
        sendBroadcast(intent);
    }


    public class FetchWeatherTask extends AsyncTask<String, Void, String[]> {

        private final String LOG_TAG = FetchWeatherTask.class.getSimpleName();
        private int mStartId = -1;

        public FetchWeatherTask(int startId) {
            Log.d(LOG_TAG, "abcdef", new RuntimeException());
            mStartId = startId;
        }

        @Override
        protected String[] doInBackground(String... params) {
            // These two need to be declared outside the try/catch
            // so that they can be closed in the finally block.
            HttpURLConnection urlConnection = null;
            BufferedReader reader = null;

            // Will contain the raw JSON response as a string.
            String forecastJsonStr = null;

            try {
                // Construct the URL for the OpenWeatherMap query
                // Possible parameters are avaiable at OWM's forecast API page, at
                // http://openweathermap.org/API#forecast
                String baseUrl = "http://api.openweathermap.org/data/2.5/forecast/daily?id=1835847&mode=json&units=metric&cnt=7";
                String apiKey = "&APPID=5fd2f2cde90c1533efb95b19c048a528";
                URL url = new URL(baseUrl.concat(apiKey));

                // Create the request to OpenWeatherMap, and open the connection
                urlConnection = (HttpURLConnection) url.openConnection();
                urlConnection.setRequestMethod("GET");
                urlConnection.connect();

                // Read the input stream into a String
                InputStream inputStream = urlConnection.getInputStream();
                StringBuffer buffer = new StringBuffer();
                if (inputStream == null) {
                    // Nothing to do.
                    return null;
                }
                reader = new BufferedReader(new InputStreamReader(inputStream));

                String line;
                while ((line = reader.readLine()) != null) {
                    // Since it's JSON, adding a newline isn't necessary (it won't affect parsing)
                    // But it does make debugging a *lot* easier if you print out the completed
                    // buffer for debugging.
                    buffer.append(line + "\n");
                }

                if (buffer.length() == 0) {
                    // Stream was empty.  No point in parsing.
                    return null;
                }
                forecastJsonStr = buffer.toString();
            } catch (IOException e) {
                Log.e(LOG_TAG, "Error ", e);
                // If the code didn't successfully get the weather data, there's no point in attemping
                // to parse it.
                return null;
            } finally {
                if (urlConnection != null) {
                    urlConnection.disconnect();
                }
                if (reader != null) {
                    try {
                        reader.close();
                    } catch (final IOException e) {
                        Log.e(LOG_TAG, "Error closing stream", e);
                    }
                }
            }
            return null;
        }

        @Override
        protected void onPostExecute(String[] result) {
            if (result != null) {
                notifyWeatherDataRetrieved(result);
                }
                // New data is back from the server.  Hooray!
            }
        }
    }

