package com.example.animation

import android.animation.ObjectAnimator

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.animation.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)



        binding.up.setOnClickListener{
            ObjectAnimator.ofFloat( binding.imageView, "alpha", 0f, 1f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
        }
        binding.bottom.setOnClickListener{
            ObjectAnimator.ofFloat( binding.imageView, "alpha", 1f, 0f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
        }
        binding.left.setOnClickListener{
            ObjectAnimator.ofFloat( binding.imageView, "scaleX", 2f, 1f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
        }
        binding.right.setOnClickListener{

        }
        binding.imageButton.setOnClickListener{
            ObjectAnimator.ofFloat( binding.imageView, "rotation", 0f, 180f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
            ObjectAnimator.ofFloat( binding.imageView, "scaleX", 1f, 2f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
            ObjectAnimator.ofFloat( binding.imageView, "scaleY", 1f, 2f).apply {
                duration = 500 // Animation duration: 2 seconds
                start() // Start the animation
            }
        }

    }
}