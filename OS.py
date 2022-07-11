#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  OS.py
#  
#  NoCopyright 2022  <mirrorbyte@outlook.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Thanks to Cyber Coding for the Terminal script.


import os
import time

print("""


████████ ██████   ██████  ██████  ██  ██████      ██████  ███████      ██     ██████  
   ██    ██   ██ ██    ██ ██   ██ ██ ██          ██    ██ ██          ███    ██  ████ 
   ██    ██████  ██    ██ ██████  ██ ██          ██    ██ ███████      ██    ██ ██ ██ 
   ██    ██   ██ ██    ██ ██      ██ ██          ██    ██      ██      ██    ████  ██ 
   ██    ██   ██  ██████  ██      ██  ██████      ██████  ███████      ██ ██  ██████  
                                                                                      
                                                                                      
                                                                     Beta Edition
""")                                                         
print("| NoCopyright Mirrobyte Technologies | Licence: GNU General Public License 2.0 ") 
print("Website: http://tropicos.rf.gd | Email: mirrorbyte@outlook.com")
print("Welcome User!")
print("The Date Is: " + time.strftime("%m/%d/%y"))
print("")
while True:
    command = input("USER@TropicOS>")
    os.system(command)  

