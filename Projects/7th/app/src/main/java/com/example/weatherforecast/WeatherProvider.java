package com.example.weatherforecast;

import android.content.ContentProvider;
import android.content.ContentValues;
import android.content.UriMatcher;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.net.Uri;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import static com.example.weatherforecast.WeatherContract.normalizeDate;

public class WeatherProvider extends ContentProvider {
    private WeatherDbHelper mDbHelper = null;
    private static final UriMatcher sUriMatcher = buildUriMatcher();

    static final int WEATHER = 100;
    static final int WEATHER_DIR = 101;
    static final int WEATHER_ITEM = 102;

    public WeatherProvider(){

    }

    private static UriMatcher buildUriMatcher() {
        final UriMatcher matcher = new UriMatcher(UriMatcher.NO_MATCH);
        final String authority = WeatherContract.CONTENT_AUTHORITY;

        // For each type of URI you want to add, create a corresponding code.
        matcher.addURI(authority, WeatherContract.PATH_WEATHER, WEATHER);
        matcher.addURI(authority, WeatherContract.PATH_WEATHER + "/*", WEATHER_DIR);
        matcher.addURI(authority, WeatherContract.PATH_WEATHER + "/*/#", WEATHER_ITEM);
        return matcher;

    }


    @Override
    public boolean onCreate() {
        mDbHelper = new WeatherDbHelper(getContext());
        return true;
    }

    @Nullable
    @Override
    public Cursor query(@NonNull Uri uri, @Nullable String[] projection, @Nullable String selection, @Nullable String[] selectionArgs, @Nullable String sortOrder) {
        Cursor retCursor;
        switch (sUriMatcher.match(uri)) {
            case WEATHER:
            case WEATHER_DIR:
                break;
            case WEATHER_ITEM:
                String weatherId = uri.getPathSegments().get(1);
                if (selection != null) {
                    selection += " AND " + WeatherContract.WeatherColumns._ID + " = " + weatherId;
                }
                break;
            default:
                throw new UnsupportedOperationException("Unknown uri = " + uri);
        }

        retCursor = mDbHelper.getReadableDatabase().query(
                WeatherContract.WeatherColumns.TABLE_NAME,
                projection,
                selection,
                selectionArgs,
                null,
                null,
                sortOrder
        );

        retCursor.setNotificationUri(getContext().getContentResolver(), uri);

        return retCursor;
    }

    @Nullable
    @Override
    public String getType(@NonNull Uri uri) {
        final int match = sUriMatcher.match(uri);

        switch (match) {
            case WEATHER:
            case WEATHER_DIR:
                return WeatherContract.WeatherColumns.CONTENT_TYPE;
            case WEATHER_ITEM:
                return WeatherContract.WeatherColumns.CONTENT_ITEM_TYPE;
            default:
                throw new UnsupportedOperationException("Unknown uri = " + uri);
        }
    }

    @Nullable
    @Override
    public Uri insert(@NonNull Uri uri, @Nullable ContentValues values) {
        final SQLiteDatabase db = mDbHelper.getWritableDatabase();
        Uri retUri;

        switch (sUriMatcher.match(uri)) {
            case WEATHER:
                long id = db.insert(WeatherContract.WeatherColumns.TABLE_NAME, null, values);
                if (id > 0) {
                    retUri = WeatherContract.WeatherColumns.buildWeatherUri(id);
                } else {
                    throw new android.database.SQLException("Failed to insert row into " + uri);
                }
                break;
            default:
                throw new UnsupportedOperationException("Unknown uri = " + uri);
        }

        getContext().getContentResolver().notifyChange(uri, null);
        return retUri;
    }

    @Override
    public int delete(@NonNull Uri uri, @Nullable String selection, @Nullable String[] selectionArgs) {
        final SQLiteDatabase db = mDbHelper.getWritableDatabase();
        int rowsDeleted;

        switch (sUriMatcher.match(uri)) {
            case WEATHER:
                break;
            case WEATHER_ITEM:
                String weatherId = uri.getPathSegments().get(1);
                if (selection != null) {
                    selection += " AND " + WeatherContract.WeatherColumns._ID + " = " + weatherId;
                }

            default:
                throw new UnsupportedOperationException("Unknown uri = " + uri);
        }

        rowsDeleted = db.delete(WeatherContract.WeatherColumns.TABLE_NAME, selection, selectionArgs);

        return rowsDeleted;
    }

    @Override
    public int update(@NonNull Uri uri, @Nullable ContentValues values, @Nullable String selection, @Nullable String[] selectionArgs) {
        final SQLiteDatabase db = mDbHelper.getWritableDatabase();
        int rowUpdated;

        switch (sUriMatcher.match(uri)) {
            case WEATHER:
            case WEATHER_DIR:
                break;
            case WEATHER_ITEM:
                String weatherId = uri.getPathSegments().get(1);
                if (selection != null) {
                    selection += " AND " + WeatherContract.WeatherColumns._ID + " = " + weatherId;
                }
                break;
            default:
                throw new UnsupportedOperationException("Unknown uri = " + uri);
        }

        normalizeDate(values);
        rowUpdated = db.update(WeatherContract.WeatherColumns.TABLE_NAME, values, selection, selectionArgs);

        if (rowUpdated != 0) {
            getContext().getContentResolver().notifyChange(uri, null);
        }

        return rowUpdated;
    }

    private void normalizeDate(ContentValues values) {
        if (values.containsKey(WeatherContract.WeatherColumns.COLUMN_DATE)) {
            long dateValue = values.getAsLong(WeatherContract.WeatherColumns.COLUMN_DATE);
            values.put(WeatherContract.WeatherColumns.COLUMN_DATE, WeatherContract.normalizeDate(dateValue));
        }
    }
}
