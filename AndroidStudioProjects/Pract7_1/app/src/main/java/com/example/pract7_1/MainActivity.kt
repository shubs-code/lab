package com.example.pract7_1

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.pract7_1.databinding.ActivityMainBinding
import com.google.android.material.datepicker.DayViewDecorator
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale



class MainActivity : AppCompatActivity() {
    final  lateinit var binding:ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)

        setContentView(binding.root)

        val sdf = SimpleDateFormat("dd/MM/yyyy", Locale.getDefault())

        binding.textView123.text = "Today is : "+ sdf.format(Date())

        binding.calendarView.setOnDateChangeListener{ _, year, month, dayOfMonth->
            val selectedDate = "$dayOfMonth/${month + 1}/$year"
            binding.textView123.text = "Selected Date : "+selectedDate
        }

    }

}