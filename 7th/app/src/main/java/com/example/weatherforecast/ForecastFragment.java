package com.example.weatherforecast;

import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.content.ServiceConnection;
import android.content.SharedPreferences;
import android.database.Cursor;
import android.os.Bundle;

import com.example.weatherforecast.FetchWeatherService;
import com.example.weatherforecast.FetchWeatherService.FetchWeatherTask;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.loader.app.LoaderManager;
import androidx.loader.content.CursorLoader;
import androidx.loader.content.Loader;

import android.os.IBinder;
import android.os.RemoteException;
import android.preference.PreferenceManager;
import android.text.format.Time;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.CursorAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ForecastFragment extends Fragment implements LoaderManager.LoaderCallbacks<Cursor> {

    static final int COL_WEATHER_ID = 0;
    static final int COL_WEATHER_DATE = 1;
    static final int COL_WEATHER_DESC = 2;
    static final int COL_WEATHER_MAX_TEMP = 3;
    static final int COL_WEATHER_MIN_TEMP = 4;

    public ForecastFragment(){

    }

    public static long normalizeDate(long startDate) {
        // normalize the start date to the beginning of the (UTC) day
        Time time = new Time();
        time.set(startDate);
        int julianDay = Time.getJulianDay(startDate, time.gmtoff);
        return time.setJulianDay(julianDay);
    }

    private static final String[] FORECAST_COLUMNS = {
            // In this case the id needs to be fully qualified with a table name, since
            // the content provider joins the location & weather tables in the background
            // (both have an _id column)
            // On the one hand, that's annoying.  On the other, you can search the weather table
            // using the location set by the user, which is only in the Location table.
            // So the convenience is worth it.
            WeatherContract.WeatherColumns._ID,
            WeatherContract.WeatherColumns.COLUMN_DATE,
            WeatherContract.WeatherColumns.COLUMN_SHORT_DESC,
            WeatherContract.WeatherColumns.COLUMN_MAX_TEMP,
            WeatherContract.WeatherColumns.COLUMN_MIN_TEMP,
    };



    public static final String ACTION_RETRIEVE_WEATHER_DATA = "com.example.WeatherForecast.RETRIEVE_DATA";

    private static final int FORECAST_LOADER = 0;
    private WeatherForecastAdapter mForecastAdapter;
    private IFetchWeatherService mService;

    private class WeatherForecastAdapter extends CursorAdapter {
        public class ViewHolder {
            public final TextView mTextView;

            public ViewHolder(View view) {
                mTextView = (TextView)view.findViewById(R.id.list_item_forecast_textview);
            }
        }

        public WeatherForecastAdapter(Context context, Cursor cursor, int flags) {
            super(context, cursor, flags);
        }

        @Override
        public View newView(Context context, Cursor cursor, ViewGroup parent) {
            View view = LayoutInflater.from(context).inflate(R.layout.list_view_item, parent, false);

            ViewHolder viewHolder = new ViewHolder(view);
            view.setTag(viewHolder);

            return view;
        }

        @Override
        public void bindView(View view, Context context, Cursor cursor) {
            ViewHolder holder = (ViewHolder)view.getTag();

            StringBuilder sb = new StringBuilder();
            long dateInMillis = cursor.getLong(COL_WEATHER_DATE);
            sb.append(getReadableDateString(dateInMillis));

            String description = cursor.getString(COL_WEATHER_DESC);
            sb.append(" - " + description);

            double high = cursor.getDouble(COL_WEATHER_MAX_TEMP);

            double low = cursor.getDouble(COL_WEATHER_MIN_TEMP);

            String highAndLow = formatHighLows(high, low);
            sb.append(" - " + highAndLow);

            holder.mTextView.setText(sb.toString());
        }
    }

    private String getReadableDateString(long time){
        // Because the API returns a unix timestamp (measured in seconds),
        // it must be converted to milliseconds in order to be converted to valid date.
        SimpleDateFormat shortenedDateFormat = new SimpleDateFormat("EEE MMM dd");
        return shortenedDateFormat.format(time);
    }

    private String formatHighLows(double high, double low) {
        // For presentation, assume the user doesn't care about tenths of a degree.
        long roundedHigh = Math.round(high);
        long roundedLow = Math.round(low);

        String highLowStr = roundedHigh + "/" + roundedLow;
        return highLowStr;
    }

    private ServiceConnection mServiceConnection = new ServiceConnection() {
        @Override
        public void onServiceConnected(ComponentName name, IBinder service) {
            mService = IFetchWeatherService.Stub.asInterface(service);

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
        }
    };

    private BroadcastReceiver mBroadcastReceiver = new BroadcastReceiver() {
        @Override
        public void onReceive(Context context, Intent intent) {
            String action = intent.getAction();
            if(action.equals(FetchWeatherService.ACTION_RETRIEVE_WEATHER_DATA)) {

            }
        }
    };


    public static ForecastFragment newInstance() {
        return new ForecastFragment();
    }

    @Override
    public void onActivityCreated(@Nullable Bundle savedInstanceState) {
        getLoaderManager().initLoader(FORECAST_LOADER, null, this);
        super.onActivityCreated(savedInstanceState);
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


    private void refreshWeatherData(){
        Intent intent = new Intent(getActivity(),FetchWeatherService.class);
        intent.setAction(FetchWeatherService.ACTION_RETRIEVE_WEATHER_DATA);
        getActivity().startService(intent);
//        if(mService != null){
//            try {
//                mService.retrieveWeatherData();
//            } catch (RemoteException e) {
//                e.printStackTrace();
//            }
//        }
    }

    @Override
    public void onCreateOptionsMenu(Menu menu, MenuInflater inflater) {
        inflater.inflate(R.menu.menu_fragment_main, menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_refresh) {
            refreshWeatherData();
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setHasOptionsMenu(true);

        getActivity().bindService(new Intent(getActivity(), FetchWeatherService.class), mServiceConnection, Context.BIND_AUTO_CREATE);
    }


    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {

        mForecastAdapter = new WeatherForecastAdapter(getActivity(), null, 0);

        View rootView = inflater.inflate(R.layout.main_fragment, container, false);

        ListView listView = (ListView) rootView.findViewById(R.id.listview_forecast);
        listView.setAdapter(mForecastAdapter);
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
//                String forecast = String.valueOf(mForecastAdapter.getItem(position));
//                Toast.makeText(getActivity(), forecast, Toast.LENGTH_SHORT).show();
//                Intent intent = new Intent(getActivity(), DetailActivity.class);
//                intent.putExtra("data", forecast);
//                startActivity(intent);
            }
        });

        IntentFilter intentFilter = new IntentFilter(FetchWeatherService.ACTION_RETRIEVE_WEATHER_DATA);
        getActivity().registerReceiver(mBroadcastReceiver, intentFilter);
        return rootView;
    }


    @NonNull
    @Override
    public Loader<Cursor> onCreateLoader(int id, @Nullable Bundle args) {
        // This is called when a new Loader needs to be created.  This
        // fragment only uses one loader, so we don't care about checking the id.

        // To only show current and future dates, filter the query to return weather only for
        // dates after or including today.

        // Sort order:  Ascending, by date.
        String sortOrder = WeatherContract.WeatherColumns.COLUMN_DATE + " ASC";

        long now = System.currentTimeMillis();
        long normalizedDate = normalizeDate(now);

        return new CursorLoader(getActivity(),
                WeatherContract.WeatherColumns.CONTENT_URI,
                FORECAST_COLUMNS,
                WeatherContract.WeatherColumns.COLUMN_DATE + " >= ?",
                new String[] {Long.toString(now)},
                sortOrder);
    }

    @Override
    public void onLoadFinished(@NonNull Loader<Cursor> loader, Cursor data) {
        mForecastAdapter.swapCursor(data);
    }

    @Override
    public void onLoaderReset(@NonNull Loader<Cursor> loader) {
        mForecastAdapter.swapCursor(null);
    }
}
