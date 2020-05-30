package com.example.weatherforecast;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.view.Menu;
import android.view.MenuItem;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu){
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item){
        int id = item.getItemId();

        if(id == R.string.action_settings) { //why can't R.id.action_settings?
            startActivity(new Intent(this, SettingsActivity.class));
            return true;
        }

//        if(id == R.id.action_refresh) {
//            startActivity(new Intent(this, ForecastFragment.class));
//            return true;
//        }

        return super.onOptionsItemSelected(item);
    }
}
