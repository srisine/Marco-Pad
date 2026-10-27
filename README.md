# Marco-Pad

<h1>A Macro Pad inspired by Marco Polo!</h1>

my first attempt at pcb and cad designing 


Not the most perfect pcb but still i managed to build smtn in KiCAD
<h1>PCB:</h1>
<img width="969" height="711" alt="image" src="https://github.com/user-attachments/assets/bc2843bf-90da-40ed-b23a-0d88293d67eb" />

<img width="493" height="495" alt="image" src="https://github.com/user-attachments/assets/eda0f4a7-9278-489c-b0af-1c58c0c585c7" />

<img width="704" height="541" alt="image" src="https://github.com/user-attachments/assets/69e7e9a4-96b7-430a-9fec-8708de1e6afa" />


Then i build an enclosure in Fusion 360 (First time ever)

<h1>CAD</h1>

<h2>V1</h2>
<img width="1015" height="729" alt="image" src="https://github.com/user-attachments/assets/a8c1e023-2be6-4375-987e-0d8f32f93c74" />

<img width="843" height="223" alt="image" src="https://github.com/user-attachments/assets/aa9bfba8-7d8f-43da-9735-c668819dc38d" />

<h2>V2</h2>

<img width="1920" height="722" alt="e6a9461e-dc8a-4ffe-8fda-f56303a07daf" src="https://github.com/user-attachments/assets/208cdf54-c4f0-4394-b9db-a8246425c438" />

<img width="1920" height="722" alt="49020a08-2915-4a54-be08-6de36561d586" src="https://github.com/user-attachments/assets/9cdd7e26-24fc-4860-8159-4dbbfd4b4868" />

<img width="1920" height="722" alt="Render_2026-Oct-26_10-58-21AM-000_CustomizedView20744086169" src="https://github.com/user-attachments/assets/6c15a1a2-cc40-4a64-8c65-551f02087174" />

<h2>V3(Added screw threads)</h2>

<img width="223" height="183" alt="a" src="https://github.com/user-attachments/assets/492cbb11-3f46-402b-b5c7-74c0a62f0569" />

<img width="1920" height="722" alt="re" src="https://github.com/user-attachments/assets/168d2d23-c970-4368-a8b9-34a3448fa563" />

<h1>Firmware overview</h1>
Then i used QMK to write a firmware

Rotary Encoder: for volume and mute/unmute
4 Buttons: for media control 
Oled: for status indicator

### 📦 Bill of Materials (BOM)

| Component | Quantity | Description |
| :--- | :---: | :--- |
| MX-Style Switches | 4x | Mechanical switches for the main keys |
| DSA Keycaps | 4x | White blank DSA profile keycaps |
| EC11 Rotary Encoder | 1x | Rotary encoder with integrated push switch |
| OLED Display | 1x | 0.91-inch I2C OLED display |
| M3 Screws | 4x | M3 x 16mm screws for the sandwich case |
| Microcontroller | 1x | Seeed Studio XIAO RP2040 (unsoldered) |
| Case | 1x | Custom 3D printed sandwich case (2 parts) |
