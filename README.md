# ffmpeg-m2ts-to-mp4-auto-convertion
This python file uses ffmpeg and cmd to convert m2ts files (files used by camcorders) into mp4 without interlacing (other convertion programs create interlacing artifacts). Normally, when you use this method manually, you have to wait for a command to finish and input another convertion command. This script makes it so you just input the directory of the m2ts files and the number of them and then it automatically inputs the convertion commands.

This repository requires ffmpeg installed, which you can do following this WikiHow tutorial: https://www.wikihow.com/Install-FFmpeg-on-Windows

Obviously because of the usage of CMD commands, this repository only works on Windows.

Python version used: 3.7.9 (Thonny) 
