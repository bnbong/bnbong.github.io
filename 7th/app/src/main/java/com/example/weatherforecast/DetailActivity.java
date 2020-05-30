package com.example.weatherforecast;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        if(savedInstanceState == null){
            DetailFragment fragment = new DetailFragment();

            if(getIntent().hasExtra("data")) {
                Bundle arguments = new Bundle();
                arguments.putString("data", getIntent().getStringExtra("data"));

                fragment.setArguments(arguments);
            }

            getSupportFragmentManager().beginTransaction().add(R.id.detail_container, fragment)
                    .commit();
        }

    }

}
