package com.example.myapplication

import android.os.Bundle
import android.widget.Toast
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat
import com.example.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    final lateinit var binding: ActivityMainBinding
    final lateinit var  dbHelper: DBHelper
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        dbHelper = DBHelper(this)
        binding.button2.setOnClickListener{
            val name = binding.editTextText.text.toString()
            val age = binding.editTextNumber.text.toString().toIntOrNull()

            if (name.isNotEmpty() && age != null) {
                val id = dbHelper.insertUser(name, age)
            }

        }
    }
}