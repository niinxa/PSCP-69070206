1. ข้อมูล OJ
หมายเลข/ชื่อโจทย์ OJ:

2996 - สลับตัวอักษร

OJ submission ID ถ้ามีการส่งแล้ว:

543386

สถานะ OJ:

Pass

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

10-15 minutes

เลือกหนึ่งข้อ:

0-15 minutes


2. ความเข้าใจโจทย์ของฉัน
โจทย์ให้สลับตัวอักษรของข้อความ จากหลังมาหน้าและต้องเป็นตัวเล็กทั้งหมด

input : รับข้อความที่มีความยาว 5 ตัวอักษร มา 1 ข้อความ

Output : โปรแกรมแสดงข้อความที่ผ่านการแปลงจากหลังมาหน้าและเป็นตัวพิมพ์เล็กทั้งหมด

Constraints : หลังจากแปลงหลังมาหน้าแล้ว ต้องทำให้ตัวอักษรทุกตัวเป็นพิมพ์เล็กทั้งหมดด้วยฃ


3. แผนแรกของฉัน

step 1: รับinput เข้ามา

step 2: สร้างตัวแปรใหม่ขึ้นมารับค่าที่ผ่านการแปลงหลังมาหน้า โดยใช้[::1](เพื่อเเข้าถึงตำแหน่งข้อมูลจากหลังมาหน้า)

step 3: แสดงผลข้อความ และใช้.lower()ครอบ เพื่อให้เป็นพิมพ์เล็กทั้งหมด


4. วิธีสุดท้ายที่ใช้จริง

วิธีสุดท้ายของฉันเหมือนกับแผนแรก แต่เปลี่ยนการเข้าถึงตำแหน่งเเป็น[::-1] แทนเพราะ ถ้าไม่-1 จะไม่แสดงผลจาหลังมาหน้า


5. การทดสอบของฉัน

Test Case 1

ทำไมเลือก case นี้:

ตรวจการแปลงว่าเรียงจากหลังมาหน้าหรือไม่

Input:

hello

Expected output:

olleh

Actual output:

olleh

Result:

Pass


Test Case 2

ทำไมเลือก case นี้:

ตรวจว่าเป็นพิมพ์เล็กหรือไม่

Input:

Hello

Expected output:

olleh

Actual output:

olleh

Result:

Pass


Test Case 3

ทำไมเลือก case นี้:

ตรวจว่าเป็นพิมพ์เล็กทั้งหมดหรือไม่

Input:

HELLO

Expected output:

olleh

Actual output:

olleh

Result:

Pass


6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

No


7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

No


8. คำรับรองของนักศึกษา

เขียน Yes ในแต่ละ statement

Statement	Yes/No
I wrote this submission in my own words.	Yes

I understand my final code.	Yes

I recorded the real OJ status.	Yes

I did not copy AI-generated text directly into this file.	Yes

I did not copy code from another person.	Yes

If I received human help, I disclosed it in this file.	Yes

I submitted the final code to the OJ by myself.	Yes
